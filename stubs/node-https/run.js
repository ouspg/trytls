var https = require('https');
var fs = require('fs');

var host = process.argv[2];
var port = process.argv[3];
var ca   = process.argv[4];

if (process.argv.length >= 6) {
    console.log("UNSUPPORTED");
    process.exit()
}

var options = {
   host: host,
   port: port,
   path: '/',
   method: 'GET'
};

if (ca !== undefined) {
    options['ca'] = [ fs.readFileSync(ca) ];
}

options.agent = new https.Agent(options);

https.get(options, (res) => {
   res.setEncoding('utf8');
   res.on('end', () => {
       console.log("ACCEPT");
   });
}).on('error', (e) => {
   console.error("REJECT");
});
