function trend = get_alc_trend(system,trendname,sTime,eTime)
% Load trend data from ALC system
% input 1 - structure with type, url, user and pwd of the ALC system
% input 2 - name of trend, such as: '#etc_oa_terminal_-_sample_equipment/oat'
% input 3 - start time as date vector, datenum, or date string
% input 4 - end time as date vector, datenum, or date string
% output - timeseries object containing trend data vs time
%
% example: to get outside ambient temperatures for the past day,
%    system = struct('type','soap','url','http://192.168.1.103','user','MPCLABSOAP','pwd','mpclabsoap');
%    trend = get_alc_trend(system,'#etc_oa_terminal_-_sample_equipment/oat',now-1,now)

LIMIT = 100000;

if strcmp(system.type,'mysql') || strcmp(system.type,'mysqlMPC')
    % convert start and end times to the string format MySQL wants
    sTime = datestr(sTime,'yyyy-mm-dd HH:MM:SS');
    eTime = datestr(eTime,'yyyy-mm-dd HH:MM:SS');

    if strcmp(system.type,'mysql')
        % BANCROFT
        url = sprintf('jdbc:mysql://%s:3306/bancroft_trends', system.url);
        conn = database('bancroft_trends',system.user,system.pwd,'com.mysql.jdbc.Driver',url);
    else
        % MPC LAB
        url = sprintf('jdbc:mysql://%s:3306/mpclab_trends', system.url);
        conn = database('mpclab_trends',system.user,system.pwd,'com.mysql.jdbc.Driver',url);
    end
    
    query = sprintf('SELECT DATE_STAMP_,DATA_VALUE_ FROM trenddata t WHERE t.TID_=(SELECT TID_ FROM metadata WHERE SOURCEPATH_="%s") AND t.DATE_STAMP_>="%s" AND t.DATE_STAMP_<"%s" limit 0,%d',trendname,sTime,eTime,LIMIT);
    curs = exec(conn, query);
    res = fetch(curs);
    datacell = res.Data;
    if isempty(datacell) || isscalar(datacell)
        trend = timeseries([],[],'Name',trendname);
    else
        time = datenum(datacell(:,1),'yyyy-mm-dd HH:MM:SS');
        data = str2double(datacell(:,2));
        if all(diff(time))
            trend = timeseries(data,time,'Name',trendname);
            trend.TimeInfo.Units = 'days';
        else
            warning('Duplicate time values detected, need to improve discrete signal handling');
            trend.Time = time;
            trend.Data = data;
        end
    end
    close(curs);
    close(conn);
%elseif strcmp(system.type,'soap')
else
    % decrease start time by one second to include initial point
    sTime = datenum(sTime) - 1/86400;
    % convert start and end times to the string format ALC wants
    sTime = datestr(sTime,'mm/dd/yyyy HH:MM:SS AM');
    eTime = datestr(eTime,'mm/dd/yyyy HH:MM:SS AM');
    
    if exist('TrendServiceService','file')~=2
        createClassFromWsdl(strcat(system.url,'/_common/services/TrendService?wsdl'));
    end
    obj = TrendServiceService;

    datacell = getTrendData(obj,system.user,system.pwd,trendname,sTime,eTime,0,LIMIT);
    if isempty(datacell)
        trend = timeseries([],[],'Name',trendname);
    else
        time = datenum(datacell(1:2:end),'mm/dd/yyyy HH:MM:SS AM');
        data = str2double(datacell(2:2:end));
        if all(diff(time))
            trend = timeseries(data,time,'Name',trendname);
            trend.TimeInfo.Units = 'days';
        else
            warning('Duplicate time values detected, need to improve discrete signal handling')
            trend.Time = time;
            trend.Data = data;
            %trend.DataInfo.Interpolation.Name = 'zoh';
        end
    end
end

if(length(trend.Data)>=LIMIT)
    warning('Data dimension reach the limit of %d entries.', LIMIT);
end
