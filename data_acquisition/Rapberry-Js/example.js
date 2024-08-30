var admin = require("firebase-admin");
var serviceAccount = require("Rapberry-Js/power-tic-firebase-adminsdk-9u1tt-190471deb9.json");
const childProcess = require('child_process');

// Initialize the app with a service account, granting admin privileges
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  // The database URL depends on the location of the database
  databaseURL: "https://power-tic-default-rtdb.firebaseio.com/"
});
sh('python /home/power-tic/MICO/PowerTIC/Rapberry/initialize.py & echo "initialized"')
// As an admin, the app has access to read and write all data, regardless of Security Rules
var db = admin.database();
var ref = db.ref("/Meters/E3T15060693/Firmware");
ref.update({"Status":true})
ref.on('child_changed', (snapshot) => {
    const changedPost = snapshot.val();
    console.log('The updated post title is ' + changedPost);
    sh('bash try.sh & echo "running"')
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
  function keepAlive() {
    ref.get('/status')
      .then(response => {
        console.log('Keep-alive successful');
      })
      .catch(error => {
        console.error('Keep-alive failed:', error);
      });
  }
  function read() {
    sh('python Rapberry/deploy.py & echo "reading"')
  }
  setInterval(read, 300000); 
  setInterval(keepAlive, 60000); // Send a request every minute
  