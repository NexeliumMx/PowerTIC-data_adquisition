var admin = require("firebase-admin");
var serviceAccount = require("/home/guillermo/MICO/PowerTIc/PowerTIC/Rapberry-Js/power-tic-firebase-adminsdk-9u1tt-190471deb9.json");
const childProcess = require('child_process');

// Initialize the app with a service account, granting admin privileges
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  // The database URL depends on the location of the database
  databaseURL: "https://power-tic-default-rtdb.firebaseio.com/"
});

// As an admin, the app has access to read and write all data, regardless of Security Rules
var db = admin.database();
var ref = db.ref("/Meters/E3T15060693/Firmware");
ref.on('child_changed', (snapshot) => {
    const changedPost = snapshot.val();
    console.log('The updated post title is ' + changedPost);
    sh('bash /home/guillermo/MICO/PowerTIc/PowerTIC/try.sh')
  });
ref.onDisconnect().update({"Status":false})
async function sh(cmd_to_execute) {
    return new Promise(function (resolve, reject) {
        childProcess.exec(cmd_to_execute, (err, stdout, stderr) => {
            if (err) {
              reject(err);
              } else {
                resolve({stdout, stderr});
              }
          });
      });
  }
  