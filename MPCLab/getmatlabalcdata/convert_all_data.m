% Convert all MPCLab data to csv files
% Kaifei Chen - kaifei@berkeley.edu


for tnum = 1:30
    for month = 1:18
        tnum, month
        fname = sprintf('data/%d/%d', tnum, month);
        load(fname);
        data = horzcat(trend.Time, trend.Data);
        fid = fopen([fname, '.csv'], 'w');
        for rec = 1:size(data, 1)
            fprintf(fid,'%s, ', datestr(data(rec,1), 'mm/dd/yy HH:MM:SS'));
            fprintf(fid,'%20.10f\n', data(rec,2));
        end
        fclose(fid);
    end
end