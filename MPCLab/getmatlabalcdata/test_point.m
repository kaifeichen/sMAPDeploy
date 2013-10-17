clc

% system = struct('type', 'soap', 'url','http://192.168.1.103','user','MPCLABSOAP','pwd','mpclabsoap');
system = struct('type', 'soap', 'url','http://192.168.1.103','user','MPC','pwd','MPCserver');


pointname = '/#etc_fcu_-_sample_equipment/sf_vfd_output'; %fan speed
pointname1 = '/#etc_fcu_-_sample_equipment/sd1'; % supply damper 1 position
pointname2 = '/#etc_fcu_-_sample_equipment/sd2'; % supply damper 2 position
pointname3 = '/#etc_fcu_-_sample_equipment/chw_valve'; %hot water valve % open
pointname4 = '/#etc_fcu_-_sample_equipment/hw_valve'; %cold water valve % open
pointname6 = '/#etc_fcu_-_sample_equipment/rd1'; % return damper 1 position
pointname7 = '/#etc_fcu_-_sample_equipment/rd2'; % return damper 2 position

% Gets Current Data
get_alc_value(system,pointname)
% get_alc_value(system,pointname1)
% get_alc_value(system,pointname2)
% get_alc_value(system,pointname3)
% get_alc_value(system,pointname4)

% Set dampers to 40% open
% set_alc_value(system,pointname1,40)
% set_alc_value(system,pointname2,40)

% Set Cooling valve to 5% open
% set_alc_value(system,pointname3,10)

% Turn fan on with dampers all open
set_alc_value(system,pointname,60)
% damp = 100;
% set_alc_value(system,pointname1,damp)
% set_alc_value(system,pointname2,damp)
% set_alc_value(system,pointname6,damp)
% set_alc_value(system,pointname7,damp)
% 
% 
% % Go back to original control
% % This is important!!
unset_alc_value(system,pointname)
% unset_alc_value(system,pointname1)
% unset_alc_value(system,pointname2)
% unset_alc_value(system,pointname6)
% unset_alc_value(system,pointname7)