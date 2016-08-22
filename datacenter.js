//http://www.sohamkamani.com/blog/2015/08/21/python-nodejs-comm/

var Blynk = require('blynk-library');

var AUTH = '87a44ef01d6e48dda71868341d85cc36';

var blynk = new Blynk.Blynk(AUTH, options = {
        connector : new Blynk.TcpClient()
});

var v2 = new blynk.VirtualPin(2);
var v3 = new blynk.VirtualPin(3);

v2.on('read', function() {
        var spawn = require('child_process').spawn,
        py    = spawn('python3', ['eon_blynk.py']),
        dataString = '';

        py.stdout.on('data', function(data){
		a = data
		console.log(a)
                dataString += data.toString();
                n = parseInt(dataString);
        });

        py.stdout.on('end', function(){
                console.log('Temperatura: ',n);
                v2.write(n);
        });
});

v3.on('read', function() {
        var spawn = require('child_process').spawn,
        py    = spawn('python3', ['eon_blynk.py']),
        dataString = '';

        py.stdout.on('data', function(data){
                dataString += data.toString();
                n = parseInt(dataString);
        });

        py.stdout.on('end', function(){
                console.log('Humedad: ',n);
                v3.write(n);
        });
});
