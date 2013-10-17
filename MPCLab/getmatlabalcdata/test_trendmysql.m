% TEST MATLAB-ALC CONNECTION VIA MYSQL (BANCROFT LIBRARY)
% 
% Plot the outside air temperature trend of the last 10 days.

% clc

% % Bancroft and Weather DB
% % USE MPC MPC username/pwd
% system = struct('type', 'mysql','url','192.168.1.102','user','MPC','pwd','MPC')
% % % % system = struct('type', 'mysql','url','192.168.1.102','user','MPC_DATABASES','pwd','MPC171274Jr')
% % trendname = '/#doe_ah-a_and_dh-1/oat';
% trendname = '/#doe_vav_b-3-11/lstat/zone_temp';
% trend = get_alc_trend(system,trendname,datenum(2012,8,16,0,0,0),datenum(2012,8,17,0,0,0));

% MPC DB
system = struct('type','mysqlMPC','url','192.168.1.103','user','root','pwd','MPCserver')
% system = struct('type','mpclab_trends','url','192.168.1.103','user','root','pwd','MPCserver');
trendname = '/#etc_fcu_-_sample_equipment/static';
% trendname = '/#etc_fcu_-_sample_equipment/sa_temp';
trend = get_alc_trend(system,trendname, datenum(2012,9,1,0,0,0),datenum(2012,9,10,0,0,0));


close all
figure;plot(trend);
