
CREATE TABLE measurements_address (
    modbus_address_hex TEXT,
    modbus_address_dec TEXT,
    parameter_description TEXT,
    standard TEXT,
    data_type TEXT,
    rw TEXT,
    data_range TEXT,
    measurement_units TEXT,
    default_value TEXT,
    model TEXT,
    register_number TEXT
);

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1000H, 1001H', '4096, 4097', 'sunspec_id', 
        'sunspec', 'Uint16', 'R', '0x53756e53', '', 
        '1', '1~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1002H', '4098', 'id', 
        'Acurev 1300', 'Uint16', 'R', '1', '', 
        '1', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1003H', '4099', 'lenth', 
        'Acurev 1300', 'Uint16', 'R', '65', '', 
        '65', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1004H, 1005H, 1006H, 1007H, 1008H, 1009H, 1010H, 1011H, 1012H, 1013H', '4100, 4101, 4102, 4103, 4104, 4105, 4106, 4107, 4108, 4109', 'manufacturer', 
        'Acurev 1300', 'string', 'R', 'Well known value registered with SunSpec for compliance', '', 
        'Accuenergy', '1~4', '16.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1014H, 1015H, 1016H, 1017H, 1018H, 1019H, 101AH, 101BH, 101CH, 101DH, 101EH, 101FH, 1020H, 1021H, 1022H, 1023H', '4116, 4117, 4118, 4119, 4120, 4121, 4122, 4123, 4124, 4125, 4126, 4127, 4128, 4129, 4130, 4131', 'model', 
        'Acurev 1300', 'string', 'R', 'Manufacturer specific value (32 chars)', '', 
        'AcuRev1300', '1~4', '16.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1024H, 1025H, 1026H, 1027H, 1028H, 1029H, 102AH, 102BH', '4132, 4133, 4134, 4135, 4136, 4137, 4138, 4139', 'options', 
        'Acurev 1300', 'string', 'R', 'Manufacturer specific value (16 chars)', '', 
        'AcuRev130X', '1~4', '8.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '102CH, 102DH, 102EH, 102FH, 1030H, 1031H, 1032H, 1033H', '4140, 4141, 4142, 4143, 4144, 4145, 4146, 4147', 'version', 
        'Acurev 1300', 'string', 'R', 'Manufacturer specific value (16 chars)', '', 
        'H:1.10 S:1.01', '1~4', '8.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1034H, 1035H, 1036H, 1037H, 1038H, 1039H, 103AH, 103BH, 103CH, 103DH, 103EH, 103FH, 1040H, 1041H, 1042H, 1043H', '4148, 4149, 4150, 4151, 4152, 4153, 4154, 4155, 4156, 4157, 4158, 4159, 4160, 4161, 4162, 4163', 'serial_number', 
        'Acurev 1300', 'string', 'R', 'Manufacturer specific value (32 chars)', '', 
        '', '1~4', '16.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1044H', '4164', 'device_address', 
        'Acurev 1300', 'uint16', 'R/W', 'Modbus device address', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1045H', '4165', 'id', 
        'Acurev 1300', 'Uint16', 'R', 'Meter (Single Phase) single phase (AN or AB) meter --201 split single phase (ABN) meter â€“202 wye-connect three phase (abcn) meterâ€”203 delta-connect three phase (abc) meter --204', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1046H', '4166', 'lenth', 
        'Acurev 1300', 'Uint16', 'R', '105', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1047H', '4167', 'amps_total', 
        'sunspec', 'int16', 'R', '0~9999', 'A', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1048H', '4168', 'amps_phase_a', 
        'sunspec', 'int16', 'R', '0~9999', 'A', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1049H', '4169', 'amps_phase_b', 
        'sunspec', 'int16', 'R', '0~9999', 'A', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '104AH', '4170', 'amps_phase_c', 
        'sunspec', 'int16', 'R', '0~9999', 'A', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '104BH', '4171', 'current_scale_factor', 
        'sunspec', 'sunssf', 'R', '-3~+5 (used as exponent of a power of 10)', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '104CH', '4172', 'voltage_ln_average', 
        'sunspec', 'int16', 'R', '0~9999', 'V', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '104DH', '4173', 'phase_voltage_an', 
        'sunspec', 'int16', 'R', '0~9999', 'V', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '104EH', '4174', 'phase_voltage_bn', 
        'sunspec', 'int16', 'R', '0~9999', 'V', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '104FH', '4175', 'phase_voltage_cn', 
        'sunspec', 'int16', 'R', '0~9999', 'V', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1050H', '4176', 'voltage_ll_average', 
        'sunspec', 'int16', 'R', '0~9999', 'V', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1051H', '4177', 'phase_voltage_ab', 
        'sunspec', 'int16', 'R', '0~9999', 'V', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1052H', '4178', 'phase_voltage_bc', 
        'sunspec', 'int16', 'R', '0~9999', 'V', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1053H', '4179', 'phase_voltage_ca', 
        'sunspec', 'int16', 'R', '0~9999', 'V', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1054H', '4180', 'voltage_scale_factor', 
        'sunspec', 'sunssf', 'R', '-2~2', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1055H', '4181', 'frequency', 
        'Acurev 1300', 'int16', 'R', '45 - 65', 'Hz', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1056H', '4182', 'frequency_scale_factor', 
        'Acurev 1300', 'sunssf', 'R', '-2', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1057H', '4183', 'total_real_power', 
        'sunspec', 'int16', 'R', '0~9999', 'W', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1058H', '4184', 'watts_phase_a', 
        'sunspec', 'int16', 'R', '0~9999', 'W', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1059H', '4185', 'watts_phase_b', 
        'sunspec', 'int16', 'R', '0~9999', 'W', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '105AH', '4186', 'watts_phase_c', 
        'sunspec', 'int16', 'R', '0~9999', 'W', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '105BH', '4187', 'real_power_scale_factor', 
        'sunspec', 'sunssf', 'R', '0 ~ 4', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '105CH', '4188', 'ac_apparent_power_va', 
        'sunspec', 'int16', 'R', '0~9999', 'VA', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '105DH', '4189', 'va_phase_a', 
        'sunspec', 'int16', 'R', '0~9999', 'VA', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '105EH', '4190', 'va_phase_b', 
        'sunspec', 'int16', 'R', '0~9999', 'VA', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '105FH', '4191', 'va_phase_c', 
        'sunspec', 'int16', 'R', '0~9999', 'VA', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1060H', '4192', 'apparent_power_scale_factor', 
        'sunspec', 'sunssf', 'R', '0 ~ 4', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1061H', '4193', 'reactive_power_var', 
        'sunspec', 'int16', 'R', '0~9999', 'var', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1062H', '4194', 'var_phase_a', 
        'sunspec', 'int16', 'R', '0~9999', 'var', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1063H', '4195', 'var_phase_b', 
        'sunspec', 'int16', 'R', '0~9999', 'var', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1064H', '4196', 'var_phase_c', 
        'sunspec', 'int16', 'R', '0~9999', 'var', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1065H', '4197', 'reactive_power_scale_factor', 
        'sunspec', 'sunssf', 'R', '0 ~ 4', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1066H', '4198', 'power_factor', 
        'sunspec', 'int16', 'R', '-1000 ~ 1000', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1067H', '4199', 'pf_phase_a', 
        'sunspec', 'int16', 'R', '-1000 ~ 1000', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1068H', '4200', 'pf_phase_b', 
        'sunspec', 'int16', 'R', '-1000 ~ 1000', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1069H', '4201', 'pf_phase_c', 
        'sunspec', 'int16', 'R', '-1000 ~ 1000', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '106AH', '4202', 'power_factor_scale_factor', 
        'sunspec', 'sunssf', 'R', '-3', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '106BH, 106CH', '4203, 4204', 'total_real_energy_exported', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'Wh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '106DH, 106EH', '4205, 4206', 'total_watt_hours_exported_in_phase_a', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'Wh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '106FH, 1070H', '4207, 4208', 'total_watt_hours_exported_in_phase_b', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'Wh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1071H, 1072H', '4209, 4210', 'total_watt_hours_exported_in_phase_c', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'Wh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1073H, 1074H', '4211, 4212', 'total_real_energy_imported', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'Wh', 
        '', '1~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1075H, 1076H', '4213, 4214', 'total_watt_hours_imported_phase_a', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'Wh', 
        '', '1~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1077H, 1078H', '4215, 4216', 'total_watt_hours_imported_phase_b', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'Wh', 
        '', '1~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1079H, 107AH', '4217, 4218', 'total_watt_hours_imported_phase_c', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'Wh', 
        '', '1~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '107B', '4219', 'totwh_sf', 
        'sunspec', 'acc32', 'R', '-3 ~ 0', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '107CH, 107DH', '4220, 4221', 'total_va_hours_exported', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'VAh', 
        '', '3~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '107EH, 107FH', '4222, 4223', 'total_va_hours_exported_phase_a', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'VAh', 
        '', '3~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1080H, 1081H', '4224, 4225', 'total_va_hours_exported_phase_b', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'VAh', 
        '', '3~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1082H, 1083H', '4226, 4227', 'total_va_hours_exported_phase_c', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'VAh', 
        '', '3~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1084H, 1085H', '4228, 4229', 'total_va_hours_imported', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'VAh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1086H, 1087H', '4230, 4231', 'total_va_hours_imported_phase_a', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'VAh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1088H, 1089H', '4232, 4233', 'total_va_hours_imported_phase_b', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'VAh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '108AH, 108BH', '4234, 4235', 'total_va_hours_imported_phase_c', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'VAh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '108CH', '4236', 'totvah_sf_sunspec', 
        'sunspec', 'sunssf', 'R', '-3 ~ 0', '', 
        '', '2~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '108DH, 108EH', '4237, 4238', 'total_var_hours_imported_q1', 
        'sunspec', 'bitfield32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '108FH, 1090H', '4239, 4240', 'total_var_hours_imported_q1_phase_a', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1091H, 1092H', '4241, 4242', 'total_var_hours_imported_q1_phase_b', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1093H, 1094H', '4243, 4244', 'total_var_hours_imported_q1_phase_c', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1095H, 1096H', '4245, 4246', 'total_var_hours_imported_q2', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1097H, 1098H', '4247, 4248', 'total_var_hours_imported_q2_phase_a', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '1099H, 109AH', '4249, 4250', 'total_var_hours_imported_q2_phase_b', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '109BH, 109CH', '4251, 4252', 'total_var_hours_imported_q2_phase_c', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '109DH, 109EH', '4253, 4254', 'total_var_hours_exported_q3', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '109FH, 10A0H', '4255, 4256', 'total_var_hours_exported_q3_phase_a', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '10A1H, 10A2H', '4257, 4258', 'total_var_hours_exported_q3_phase_b', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '10A3H, 10A4H', '4259, 4260', 'total_var_hours_exported_q3_phase_c', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '10A5H, 10A6H', '4261, 4262', 'total_var_hours_exported_q4', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '10A7H, 10A8H', '4263, 4264', 'total_var_hours_exported_q4_phase_a', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '10A9H, 10AAH', '4265, 4266', 'total_var_hours_exported_q4_phase_b', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '10ABH, 10ACH', '4267, 4268', 'total_var_hours_exported_q4_phase_c', 
        'sunspec', 'acc32', 'R/W', '0-999999999', 'varh', 
        '', '2~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '10ADH', '4269', 'totvarh_sf', 
        'sunspec', '', 'R', '', '', 
        '', '2~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '10AEH, 10AFH', '4270, 4271', 'meter_event_flags', 
        '', 'bitfield32', 'R', '0', '', 
        '0', '1~4', '2.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '10B0H', '4272', 'sunspec_end_id_sunspec', 
        'sunspec', 'uint16', '', '0xFFFF', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '10B1H', '4273', 'sunspec_end_lenth_sunspec', 
        'sunspec', 'uint16', '', '0x0000', '', 
        '', '1~4', '1.0'
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    

    INSERT INTO measurements_address (
        modbus_address_hex, modbus_address_dec, parameter_description, 
        standard, data_type, rw, data_range, measurement_units, 
        default_value, model, register_number
    ) VALUES (
        '', '', '', 
        '', '', '', '', '', 
        '', '', ''
    );
    