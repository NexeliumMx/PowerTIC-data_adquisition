CREATE TABLE power_meter_readings (
    reading_id SERIAL PRIMARY KEY,
    reading_time TIMESTAMP WITH TIME ZONE NOT NULL,
    amps_total SMALLINT NOT NULL,
    amps_phase_a SMALLINT NOT NULL,
    amps_phase_b SMALLINT NOT NULL,
    amps_phase_c SMALLINT NOT NULL,
    voltage_ln_average SMALLINT NOT NULL,
    phase_voltage_an SMALLINT NOT NULL,
    phase_voltage_bn SMALLINT NOT NULL,
    phase_voltage_cn SMALLINT NOT NULL,
    voltage_ll_average SMALLINT NOT NULL,
    phase_voltage_ab SMALLINT NOT NULL,
    phase_voltage_bc SMALLINT NOT NULL,
    phase_voltage_ca SMALLINT NOT NULL,
    frequency SMALLINT NOT NULL,
    total_real_power SMALLINT NOT NULL,
    watts_phase_a SMALLINT NOT NULL,
    watts_phase_b SMALLINT NOT NULL,
    watts_phase_c SMALLINT NOT NULL,
    ac_apparent_power_va SMALLINT NOT NULL,
    va_phase_a SMALLINT NOT NULL,
    va_phase_b SMALLINT NOT NULL,
    va_phase_c SMALLINT NOT NULL,
    reactive_power_var SMALLINT NOT NULL,
    var_phase_a SMALLINT NOT NULL,
    var_phase_b SMALLINT NOT NULL,
    var_phase_c SMALLINT NOT NULL,
    power_factor SMALLINT NOT NULL,
    pf_phase_a SMALLINT NOT NULL,
    pf_phase_b SMALLINT NOT NULL,
    pf_phase_c SMALLINT NOT NULL,
    total_real_energy_exported INTEGER NOT NULL,
    total_watt_hours_exported_in_phase_a INTEGER NOT NULL,
    total_watt_hours_exported_in_phase_b INTEGER NOT NULL,
    total_watt_hours_exported_in_phase_c INTEGER NOT NULL,
    total_real_energy_imported INTEGER NOT NULL,
    total_watt_hours_imported_phase_a INTEGER NOT NULL,
    total_watt_hours_imported_phase_b INTEGER NOT NULL,
    total_watt_hours_imported_phase_c INTEGER NOT NULL,
    total_va_hours_exported INTEGER NOT NULL,
    total_va_hours_exported_phase_a INTEGER NOT NULL,
    total_va_hours_exported_phase_b INTEGER NOT NULL,
    total_va_hours_exported_phase_c INTEGER NOT NULL,
    total_va_hours_imported INTEGER NOT NULL,
    total_va_hours_imported_phase_a INTEGER NOT NULL,
    total_va_hours_imported_phase_b INTEGER NOT NULL,
    total_va_hours_imported_phase_c INTEGER NOT NULL,
    total_var_hours_imported_q1 INTEGER NOT NULL,
    total_var_hours_imported_q1_phase_a INTEGER NOT NULL,
    total_var_hours_imported_q1_phase_b INTEGER NOT NULL,
    total_var_hours_imported_q1_phase_c INTEGER NOT NULL,
    total_var_hours_imported_q2 INTEGER NOT NULL,
    total_var_hours_imported_q2_phase_a INTEGER NOT NULL,
    total_var_hours_imported_q2_phase_b INTEGER NOT NULL,
    total_var_hours_imported_q2_phase_c INTEGER NOT NULL,
    total_var_hours_exported_q3 INTEGER NOT NULL,
    total_var_hours_exported_q3_phase_a INTEGER NOT NULL,
    total_var_hours_exported_q3_phase_b INTEGER NOT NULL,
    total_var_hours_exported_q3_phase_c INTEGER NOT NULL,
    total_var_hours_exported_q4 INTEGER NOT NULL,
    total_var_hours_exported_q4_phase_a INTEGER NOT NULL,
    total_var_hours_exported_q4_phase_b INTEGER NOT NULL,
    total_var_hours_exported_q4_phase_c INTEGER NOT NULL,
CONSTRAINT chk_reading_values CHECK (
    amps_total BETWEEN 0 AND 9999 AND
    amps_phase_a BETWEEN 0 AND 9999 AND
    amps_phase_b BETWEEN 0 AND 9999 AND
    amps_phase_c BETWEEN 0 AND 9999 AND
    voltage_ln_average BETWEEN 0 AND 9999 AND
    phase_voltage_an BETWEEN 0 AND 9999 AND
    phase_voltage_bn BETWEEN 0 AND 9999 AND
    phase_voltage_cn BETWEEN 0 AND 9999 AND
    voltage_ll_average BETWEEN 0 AND 9999 AND
    phase_voltage_ab BETWEEN 0 AND 9999 AND
    phase_voltage_bc BETWEEN 0 AND 9999 AND
    phase_voltage_ca BETWEEN 0 AND 9999 AND
    frequency BETWEEN 45  AND 65 AND
    total_real_power BETWEEN 0 AND 9999 AND
    watts_phase_a BETWEEN 0 AND 9999 AND
    watts_phase_b BETWEEN 0 AND 9999 AND
    watts_phase_c BETWEEN 0 AND 9999 AND
    ac_apparent_power_va BETWEEN 0 AND 9999 AND
    va_phase_a BETWEEN 0 AND 9999 AND
    va_phase_b BETWEEN 0 AND 9999 AND
    va_phase_c BETWEEN 0 AND 9999 AND
    reactive_power_var BETWEEN 0 AND 9999 AND
    var_phase_a BETWEEN 0 AND 9999 AND
    var_phase_b BETWEEN 0 AND 9999 AND
    var_phase_c BETWEEN 0 AND 9999 AND
    power_factor BETWEEN -1000 AND 1000 AND
    pf_phase_a BETWEEN -1000 AND 1000 AND
    pf_phase_b BETWEEN -1000 AND 1000 AND
    pf_phase_c BETWEEN -1000 AND 1000 AND
    total_real_energy_exported BETWEEN 0 AND 999999999 AND
    total_watt_hours_exported_in_phase_a BETWEEN 0 AND 999999999 AND
    total_watt_hours_exported_in_phase_b BETWEEN 0 AND 999999999 AND
    total_watt_hours_exported_in_phase_c BETWEEN 0 AND 999999999 AND
    total_real_energy_imported BETWEEN 0 AND 999999999 AND
    total_watt_hours_imported_phase_a BETWEEN 0 AND 999999999 AND
    total_watt_hours_imported_phase_b BETWEEN 0 AND 999999999 AND
    total_watt_hours_imported_phase_c BETWEEN 0 AND 999999999 AND
    total_va_hours_exported BETWEEN 0 AND 999999999 AND
    total_va_hours_exported_phase_a BETWEEN 0 AND 999999999 AND
    total_va_hours_exported_phase_b BETWEEN 0 AND 999999999 AND
    total_va_hours_exported_phase_c BETWEEN 0 AND 999999999 AND
    total_va_hours_imported BETWEEN 0 AND 999999999 AND
    total_va_hours_imported_phase_a BETWEEN 0 AND 999999999 AND
    total_va_hours_imported_phase_b BETWEEN 0 AND 999999999 AND
    total_va_hours_imported_phase_c BETWEEN 0 AND 999999999 AND
    total_var_hours_imported_q1 BETWEEN 0 AND 999999999 AND
    total_var_hours_imported_q1_phase_a BETWEEN 0 AND 999999999 AND
    total_var_hours_imported_q1_phase_b BETWEEN 0 AND 999999999 AND
    total_var_hours_imported_q1_phase_c BETWEEN 0 AND 999999999 AND
    total_var_hours_imported_q2 BETWEEN 0 AND 999999999 AND
    total_var_hours_imported_q2_phase_a BETWEEN 0 AND 999999999 AND
    total_var_hours_imported_q2_phase_b BETWEEN 0 AND 999999999 AND
    total_var_hours_imported_q2_phase_c BETWEEN 0 AND 999999999 AND
    total_var_hours_exported_q3 BETWEEN 0 AND 999999999 AND
    total_var_hours_exported_q3_phase_a BETWEEN 0 AND 999999999 AND
    total_var_hours_exported_q3_phase_b BETWEEN 0 AND 999999999 AND
    total_var_hours_exported_q3_phase_c BETWEEN 0 AND 999999999 AND
    total_var_hours_exported_q4 BETWEEN 0 AND 999999999 AND
    total_var_hours_exported_q4_phase_a BETWEEN 0 AND 999999999 AND
    total_var_hours_exported_q4_phase_b BETWEEN 0 AND 999999999 AND
    total_var_hours_exported_q4_phase_c BETWEEN 0 AND 999999999
)
);