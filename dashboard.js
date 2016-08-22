//http://www.sohamkamani.com/blog/2015/08/21/python-nodejs-comm/

var Blynk = require('blynk-library');

var AUTH = '87a44ef01d6e48dda71868341d85cc36';

var blynk = new Blynk.Blynk(AUTH, options = {
	connector : new Blynk.TcpClient()
});

var v1 = new blynk.VirtualPin(1);
var v2 = new blynk.VirtualPin(2);
var v3 = new blynk.VirtualPin(3);

v1.on('write', function(param) {
	console.log('V1:', param[0]);
});

v2.on('read', function() {
	var spawn = require('child_process').spawn,
	py    = spawn('python3', ['R2AandPub.py']),
    	dataString = '';
	
	py.stdout.on('data', function(data){
		dataString += data.toString();
		n = parseInt(dataString);
	});

	py.stdout.on('end', function(){
		console.log('Distancia: ',n);
		v2.write(n);
	});
});
