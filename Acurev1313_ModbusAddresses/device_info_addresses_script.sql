
CREATE TABLE readings_addresses (
    id SERIAL PRIMARY KEY,
    modbus_address JSONB,
    parameter_description TEXT,
    standard CHARACTER(10),
    data_type CHARACTER(10),
    rw CHARACTER(3),
    data_range JSONB,
    measurement_units CHARACTER(5),
    default_value NUMERIC,
    model JSONB,
    register_number INTEGER
);


INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4096, 4097]', 'sunspec_id', 'sunspec', 'Uint16', 'R', '0x53756e53', '', '1', '[1, 4]', 2);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4098', 'id', 'Acurev 1300', 'Uint16', 'R', '1', '', '1', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4099', 'lenth', 'Acurev 1300', 'Uint16', 'R', '65', '', '65', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4100, 4101, 4102, 4103, 4104, 4105, 4106, 4107]', 'manufacturer', 'Acurev 1300', 'string', 'R', 'Well known value registered with SunSpec for compliance', '', 'Accuenergy', '[1, 4]', 16);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4116, 4117, 4118, 4119, 4120, 4121, 4122, 4123]', 'model', 'Acurev 1300', 'string', 'R', 'Manufacturer specific value (32 chars)', '', 'AcuRev1300', '[1, 4]', 16);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4132, 4133, 4134, 4135, 4136, 4137, 4138, 4139]', 'options', 'Acurev 1300', 'string', 'R', 'Manufacturer specific value (16 chars)', '', 'AcuRev130X', '[1, 4]', 8);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4140, 4141, 4142, 4143, 4144, 4145, 4146, 4147]', 'version', 'Acurev 1300', 'string', 'R', 'Manufacturer specific value (16 chars)', '', 'H:1.10 S:1.01', '[1, 4]', 8);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4148, 4149, 4150, 4151, 4152, 4153, 4154, 4155]', 'serial_number', 'Acurev 1300', 'string', 'R', 'Manufacturer specific value (32 chars)', '', 'nan', '[1, 4]', 16);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4164', 'device_address', 'Acurev 1300', 'uint16', 'R/W', 'Modbus device address', '', 'nan', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4165', 'id', 'Acurev 1300', 'Uint16', 'R', 'Meter (Single Phase) single phase (AN or AB) meter --201 split single phase (ABN) meter â€“202 wye-connect three phase (abcn) meterâ€”203 delta-connect three phase (abc) meter --204', '', 'nan', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4166', 'lenth', 'Acurev 1300', 'Uint16', 'R', '105', '', 'nan', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4171', 'current_scale_factor', 'sunspec', 'sunssf', 'R', '-3~+5 (used as exponent of a power of 10)', '', 'nan', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4180', 'voltage_scale_factor', 'sunspec', 'sunssf', 'R', '-2~2', '', 'nan', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4182', 'frequency_scale_factor', 'Acurev 1300', 'sunssf', 'R', '-2', '', 'nan', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4187', 'real_power_scale_factor', 'sunspec', 'sunssf', 'R', '0 ~ 4', '', 'nan', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4192', 'apparent_power_scale_factor', 'sunspec', 'sunssf', 'R', '0 ~ 4', '', 'nan', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4197', 'reactive_power_scale_factor', 'sunspec', 'sunssf', 'R', '0 ~ 4', '', 'nan', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4202', 'power_factor_scale_factor', 'sunspec', 'sunssf', 'R', '-3', '', 'nan', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4219', 'totwh_sf', 'sunspec', 'acc32', 'R', '-3 ~ 0', '', 'nan', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4236', 'totvah_sf_sunspec', 'sunspec', 'sunssf', 'R', '-3 ~ 0', '', 'nan', '[2, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4269', 'totvarh_sf', 'sunspec', 'nan', 'R', 'nan', '', 'nan', '[2, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('[4270, 4271]', 'meter_event_flags', 'nan', 'bitfield32', 'R', '0', '', '0', '[1, 4]', 2);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4272', 'sunspec_end_id_sunspec', 'sunspec', 'uint16', 'nan', '0xFFFF', '', 'nan', '[1, 4]', 1);
INSERT INTO device_info_addresses 
    (modbus_address, parameter_description, standard, data_type, rw, data_range, measurement_units, default_value, model, register_number) 
    VALUES 
    ('4273', 'sunspec_end_lenth_sunspec', 'sunspec', 'uint16', 'nan', '0x0000', '', 'nan', '[1, 4]', 1);