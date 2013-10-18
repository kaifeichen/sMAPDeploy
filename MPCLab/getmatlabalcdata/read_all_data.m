% Read all MPCLab data out and write to mat files
% Kaifei Chen - kaifei@berkeley.edu

fid = fopen('MPCtrends.csv');
format = '%s %s %s %s %s %s';
colnames = textscan(fid, format, 1, 'delimiter', ',');
data = textscan(fid, format, 'delimiter', ',');
fclose(fid);

system = struct('type', 'mysqlMPC', 'url', '192.168.1.103', 'user', 'root', 'pwd', 'MPCserver');
tnames = data{5}; % trend names
for i = 1:length(tnames)
	if ~exist(sprintf('data/%d', i), 'dir')
		mkdir(sprintf('data/%d', i));
	end

	tname = tnames{i};
	stime = datenum(2012,7,1,0,0,0); % start time
	for month = 1:18
		trend = get_alc_trend(system, tname, stime, stime+30);
		save(sprintf('data/%d/%d.mat', i, month), 'trend');

		stime = stime + 30;
	end
end