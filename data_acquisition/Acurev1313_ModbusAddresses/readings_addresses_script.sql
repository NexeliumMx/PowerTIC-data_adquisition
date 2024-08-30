CREATE TABLE readings_addresses (
    id SERIAL PRIMARY KEY,
    modbus_address JSONB,
    parameter_description TEXT,
    standard VARCHAR(50),
    data_type VARCHAR(20),
    rw VARCHAR(3),
    data_range JSONB,
    measurement_units VARCHAR(10),
    default_value VARCHAR(100),
    model JSONB,
    register_number INTEGER
);


INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4167', 'amps_total', 'sunspec', 'int16', 'R', '[0, 9999]', 'A', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4168', 'amps_phase_a', 'sunspec', 'int16', 'R', '[0, 9999]', 'A', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4169', 'amps_phase_b', 'sunspec', 'int16', 'R', '[0, 9999]', 'A', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4170', 'amps_phase_c', 'sunspec', 'int16', 'R', '[0, 9999]', 'A', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4172', 'voltage_ln_average', 'sunspec', 'int16', 'R', '[0, 9999]', 'V', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4173', 'phase_voltage_an', 'sunspec', 'int16', 'R', '[0, 9999]', 'V', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4174', 'phase_voltage_bn', 'sunspec', 'int16', 'R', '[0, 9999]', 'V', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4175', 'phase_voltage_cn', 'sunspec', 'int16', 'R', '[0, 9999]', 'V', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4176', 'voltage_ll_average', 'sunspec', 'int16', 'R', '[0, 9999]', 'V', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4177', 'phase_voltage_ab', 'sunspec', 'int16', 'R', '[0, 9999]', 'V', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4178', 'phase_voltage_bc', 'sunspec', 'int16', 'R', '[0, 9999]', 'V', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4179', 'phase_voltage_ca', 'sunspec', 'int16', 'R', '[0, 9999]', 'V', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4181', 'frequency', 'Acurev 1300', 'int16', 'R', '[45 , 65]', 'Hz', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4183', 'total_real_power', 'sunspec', 'int16', 'R', '[0, 9999]', 'W', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4184', 'watts_phase_a', 'sunspec', 'int16', 'R', '[0, 9999]', 'W', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4185', 'watts_phase_b', 'sunspec', 'int16', 'R', '[0, 9999]', 'W', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4186', 'watts_phase_c', 'sunspec', 'int16', 'R', '[0, 9999]', 'W', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4188', 'ac_apparent_power_va', 'sunspec', 'int16', 'R', '[0, 9999]', 'VA', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4189', 'va_phase_a', 'sunspec', 'int16', 'R', '[0, 9999]', 'VA', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4190', 'va_phase_b', 'sunspec', 'int16', 'R', '[0, 9999]', 'VA', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4191', 'va_phase_c', 'sunspec', 'int16', 'R', '[0, 9999]', 'VA', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4193', 'reactive_power_var', 'sunspec', 'int16', 'R', '[0, 9999]', 'var', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4194', 'var_phase_a', 'sunspec', 'int16', 'R', '[0, 9999]', 'var', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4195', 'var_phase_b', 'sunspec', 'int16', 'R', '[0, 9999]', 'var', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4196', 'var_phase_c', 'sunspec', 'int16', 'R', '[0, 9999]', 'var', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4198', 'power_factor', 'sunspec', 'int16', 'R', '[-1000, 1000]', 'nan', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4199', 'pf_phase_a', 'sunspec', 'int16', 'R', '[-1000, 1000]', 'nan', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4200', 'pf_phase_b', 'sunspec', 'int16', 'R', '[-1000, 1000]', 'nan', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4201', 'pf_phase_c', 'sunspec', 'int16', 'R', '[-1000, 1000]', 'nan', NULL, '[1, 4]', 1);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4203, 4204]', 'total_real_energy_exported', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'Wh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4205, 4206]', 'total_watt_hours_exported_in_phase_a', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'Wh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4207, 4208]', 'total_watt_hours_exported_in_phase_b', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'Wh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4209, 4210]', 'total_watt_hours_exported_in_phase_c', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'Wh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4211, 4212]', 'total_real_energy_imported', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'Wh', NULL, '[1, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4213, 4214]', 'total_watt_hours_imported_phase_a', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'Wh', NULL, '[1, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4215, 4216]', 'total_watt_hours_imported_phase_b', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'Wh', NULL, '[1, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4217, 4218]', 'total_watt_hours_imported_phase_c', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'Wh', NULL, '[1, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4220, 4221]', 'total_va_hours_exported', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'VAh', NULL, '[3, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4222, 4223]', 'total_va_hours_exported_phase_a', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'VAh', NULL, '[3, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4224, 4225]', 'total_va_hours_exported_phase_b', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'VAh', NULL, '[3, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4226, 4227]', 'total_va_hours_exported_phase_c', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'VAh', NULL, '[3, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4228, 4229]', 'total_va_hours_imported', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'VAh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4230, 4231]', 'total_va_hours_imported_phase_a', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'VAh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4232, 4233]', 'total_va_hours_imported_phase_b', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'VAh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4234, 4235]', 'total_va_hours_imported_phase_c', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'VAh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4237, 4238]', 'total_var_hours_imported_q1', 'sunspec', 'bitfield32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4239, 4240]', 'total_var_hours_imported_q1_phase_a', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4241, 4242]', 'total_var_hours_imported_q1_phase_b', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4243, 4244]', 'total_var_hours_imported_q1_phase_c', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4245, 4246]', 'total_var_hours_imported_q2', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4247, 4248]', 'total_var_hours_imported_q2_phase_a', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4249, 4250]', 'total_var_hours_imported_q2_phase_b', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4251, 4252]', 'total_var_hours_imported_q2_phase_c', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4253, 4254]', 'total_var_hours_exported_q3', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4255, 4256]', 'total_var_hours_exported_q3_phase_a', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4257, 4258]', 'total_var_hours_exported_q3_phase_b', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4259, 4260]', 'total_var_hours_exported_q3_phase_c', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4261, 4262]', 'total_var_hours_exported_q4', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4263, 4264]', 'total_var_hours_exported_q4_phase_a', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4265, 4266]', 'total_var_hours_exported_q4_phase_b', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);
INSERT INTO readings_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4267, 4268]', 'total_var_hours_exported_q4_phase_c', 'sunspec', 'acc32', 'R/W', '[0, 999999999]', 'varh', NULL, '[2, 4]', 2);