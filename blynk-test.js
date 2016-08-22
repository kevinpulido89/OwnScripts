var Blynk = require('blynk-library');

var AUTH = 'cfe8144c7208459fa713654923dd9dab';

var blynk = new Blynk.Blynk(AUTH, options = {
  connector : new Blynk.TcpClient()
});

var v1 = new blynk.VirtualPin(1);
var v9 = new blynk.VirtualPin(9);

v1.on('write', function(param) {
  console.log('V1:', param[0]);
});

v9.on('read', function() {
  v9.write(new Date().getSeconds());
});

var term = new blynk.WidgetTerminal(3);
term.on('write', function(data) {
  term.write('You wrote:' + data + '\n');
  blynk.notify("HAHA! " + data);
});
