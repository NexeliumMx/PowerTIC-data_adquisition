import { serverTimestamp } from 'firebase/firestore';

const examplePowerMeterReading = {
  //amps_total: 0,
  //amps_phase_A: 0,
  //amps_phase_B: 0,
  //amps_phase_C: 0,
  //voltage_average_LN: 0,
  //phase_voltage_AN: 0,
  //phase_voltage_BN: 0,
  //phase_voltage_CN: 0,
  //voltage_average_LL: 0,
  //phase_voltage_AB: 0,
  //phase_voltage_BC: 0,
  //phase_voltage_CA: 0,
  //frequency: 0,
  //total_real_power: 0,
  //watts_phase_A: 0,
  //watts_phase_B: 0,
  //watts_phase_C: 0,
  //AC_apparent: 0,
  //VA_phase_A: 0,
  //VA_phase_B: 0,
  //VA_phase_C: 0,
  //reactive_power_VAR: 0,
  //VAR_phase_A: 0,
  //VAR_phase_B: 0,
  //VAR_phase_C: 0,
  //power_factor: 0,
  //pf_phase_A: 0,
  //pf_phase_B: 0,
  //pf_phase_C: 0,
  //total_real_energy_exported: 0,
  //total_watt_hour_exported_phase_A: 0,
  //total_watt_hour_exported_phase_B: 0,
  //total_watt_hour_exported_phase_C: 0,
  //total_real_energy_imported: 0,
  //total_watt_hours_imported_phase_A: 0,
  //total_watt_hours_imported_phase_B: 0,
  //total_watt_hours_imported_phase_C: 0,
  //total_VA_hours_exported: 0,
  //total_VA_hours_exported_phase_A: 0,
  //total_VA_hours_exported_phase_B: 0,
  //total_VA_hours_exported_phase_C: 0,
  //total_VA_hours_imported: 0,
  //total_VA_hours_imported_phase_A: 0,
  //total_VA_hours_imported_phase_B: 0,
  //total_VA_hours_imported_phase_C: 0,
  //total_VAR_hours_imported_Q1: 0,
  //total_VAR_hours_imported_Q1_phase_A: 0,
  //total_VAR_hours_imported_Q1_phase_B: 0,
  //total_VAR_hours_imported_Q1_phase_C: 0,
  timestamp_server: serverTimestamp(),
  timestamp_power_meter: "2024-07-26T14:23:03Z"
};

export default examplePowerMeterReading;