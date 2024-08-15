SET CONSTRAINTS ALL DEFERRED;

CREATE SCHEMA IF NOT EXISTS PowerTIC;
SET search_path TO PowerTIC;

CREATE TABLE IF NOT EXISTS Locations (
  LocationID SMALLINT PRIMARY KEY,
  NumbMeters INT,
  Name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Meters (
  MetersID SERIAL PRIMARY KEY,
  SerialNumb TEXT NOT NULL,
  identif TEXT NOT NULL,
  RegisterYear SMALLINT NOT NULL,
  Model TEXT NOT NULL,
  Vers TEXT NOT NULL,
  Locations_LocationID SMALLINT NOT NULL,
  Manufacturer TEXT NOT NULL,
  FOREIGN KEY (Locations_LocationID)
    REFERENCES Locations (LocationID)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  UNIQUE (SerialNumb, Locations_LocationID)
);

CREATE TABLE IF NOT EXISTS ModbusQueries (
  Serial INT PRIMARY KEY,
  Modbus_Address JSONB NOT NULL,
  Parameter_description TEXT NOT NULL,
  Standard TEXT NOT NULL,
  data_type TEXT NOT NULL,
  data_range TEXT NOT NULL,
  Model TEXT NOT NULL,
  Mod_default TEXT NOT NULL,
  Register_number SMALLINT NOT NULL,
  MetersID INT NOT NULL,
  FOREIGN KEY (MetersID)
    REFERENCES Meters (MetersID)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  UNIQUE (Serial),
  UNIQUE (Modbus_Address)
);

CREATE TABLE IF NOT EXISTS Measurements (
  idMeasurements SERIAL PRIMARY KEY,
  "Timestamp" TEXT NOT NULL,
  amps_total SMALLINT NOT NULL,
  amps_phase_a SMALLINT NOT NULL,
  amps_phase_b SMALLINT NOT NULL,
  amps_phase_c SMALLINT NOT NULL,
  volatge_ln_average SMALLINT NOT NULL,
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
  total_real_energy_exported INT NOT NULL,
  total_watt_hours_exported_in_phase_a INT NOT NULL,
  total_watt_hours_exported_in_phase_b INT NOT NULL,
  total_watt_hours_exported_in_phase_c INT NOT NULL,
  total_real_energy_imported INT NOT NULL,
  total_watt_hours_imported_in_phase_a INT NOT NULL,
  total_watt_hours_imported_in_phase_b INT NOT NULL,
  total_watt_hours_imported_in_phase_c INT NOT NULL,
  total_va_hours_exported INT NOT NULL,
  total_va_hours_exported_phase_b INT NOT NULL,
  total_va_hours_exported_phase_c INT NOT NULL,
  total_va_hours_imported INT NOT NULL,
  total_va_hours_imported_phase_a INT NOT NULL,
  total_va_hours_imported_phase_b INT NOT NULL,
  total_va_hours_imported_phase_c INT NOT NULL,
  total_var_hours_imported_q1 INT NOT NULL,
  total_var_hours_imported_q1_phase_a INT NOT NULL,
  total_var_hours_imported_q1_phase_b INT NOT NULL,
  total_var_hours_imported_q1_phase_c INT NOT NULL,
  total_var_hours_imported_q2 INT NOT NULL,
  total_var_hours_imported_q2_phase_a INT NOT NULL,
  total_var_hours_imported_q2_phase_b INT NOT NULL,
  total_var_hours_imported_q2_phase_c INT NOT NULL,
  total_var_hours_imported_q3 INT NOT NULL,
  total_var_hours_imported_q3_phase_a INT NOT NULL,
  total_var_hours_imported_q3_phase_b INT NOT NULL,
  total_var_hours_imported_q3_phase_c INT NOT NULL,
  total_var_hours_imported_q4 INT NOT NULL,
  total_var_hours_imported_q4_phase_a INT NOT NULL,
  total_var_hours_imported_q4_phase_b INT NOT NULL,
  total_var_hours_imported_q4_phase_c INT NOT NULL,
  MetersID INT NOT NULL,
  FOREIGN KEY (MetersID)
    REFERENCES Meters (MetersID)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);

SET CONSTRAINTS ALL IMMEDIATE;