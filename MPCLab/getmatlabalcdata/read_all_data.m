% Read all MPCLab data out and write to csv files
% Kaifei Chen - kaifei@berkeley.edu

fid = fopen('mpclab_trends.csv');
format = '%s %s %s %s %s %s %s %s %s';
colnames = textscan(fid, format, 1, 'delimiter', ',');
data = textscan(fid, format, 'delimiter', ',');
fclose(fid);

system = struct('type', 'mysqlMPC', 'url', '192.168.1.103', 'user', 'root', 'pwd', 'MPCserver');
tnames = data{9}; % trend names
for i = 1:length(tnames)
	mkdir(sprintf('data/%d', i));

	tname = tnames{i};
	stime = datenum(2012,8,1,0,0,0); % start time
	for month = 1:2
		trend = get_alc_trend(system,trendname, stime, stime+30*month);
		save sprintf('data/%d/%d', i, month) trend;

		stime = stime+30*month;
	end
end