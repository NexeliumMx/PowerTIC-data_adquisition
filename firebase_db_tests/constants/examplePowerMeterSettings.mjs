import { serverTimestamp } from 'firebase/firestore';

const examplePowerMeterSettings = {
  ID: 'JHHJ87621',
  manufacturer: 'acuRev',
  model: 'acuRev13003P4WEnergyMeter',
  version: 'v283.02',
  SN: 'E3T150600001',
  timestamp_server: serverTimestamp(),
  location: "San Angel",
};

export default examplePowerMeterSettings;