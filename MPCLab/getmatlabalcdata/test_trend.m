% RUN THIS FILE to test accessing a few trends and plotting them.

clc
clear all
close all

% This is for MPC LAB data
system = struct('type', 'soap', 'url','http://192.168.1.103','user','MPC','pwd','MPCserver');

% Trend names are in mpclab_trends.csv
trendname1 = '#etc_oa_terminal_-_sample_equipment/oat';
% trendname = '#etc_fcu_-_sample_equipment/sf_vfd_output'
% trendname = '#etc_fcu_-_sample_equipment/sup_dmpr_1_fdbk'
% trendname = '/#etc_fcu_-_sample_equipment/avg_zn_tmp'
trendname2 = '#etc_fcu_-_sample_equipment/lstat/zone_temp';
% trendname = '/#etc_fcu_-_sample_equipment/static';
% trendname = '#etc_fcu_-_sample_equipment/static';
trendname3 = '#etc_fcu_-_sample_equipment/sa_temp';

% Command to get trends
OAT = get_alc_trend(system,trendname1,now-15,now-13);
zoneTemp = get_alc_trend(system,trendname2,now-15,now-13);
supplyTemp = get_alc_trend(system,trendname3,now-15,now-13);

% Plot trends for sanity check
figure;plot(OAT);datetick('x');
figure;plot(zoneTemp);datetick('x');
figure;plot(supplyTemp);datetick('x');

% save LabHVACdata OAT zoneTemp supplyTemp