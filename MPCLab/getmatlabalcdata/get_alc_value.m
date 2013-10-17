function value = get_alc_value(system, pointname)
% Get the current value of an ALC system point
% input 1 - structure with url, user and pwd of the ALC system
% input 2 - name of point, such as: '#etc_fcu_-_sample_equipment/sf_vfd_output'
% output - current value (double)

if exist('EvalExpServiceService','file')~=2
    createClassFromWsdl(strcat(system.url,'/_common/services/EvalService?wsdl'));
end
obj = EvalExpServiceService;

value = getValue(obj, system.user, system.pwd, pointname);
value = str2double(value);
