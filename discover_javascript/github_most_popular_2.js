var https = require('https');

var options = {
  hostname: 'api.github.com',
  path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
  headers: {
    'User-Agent': 'Holberton_School',
    'Authorization': 'token a2eaac77d1b665a2f1fea8ce17cd48178cd21a69'
  }
};

function streamToString(stream, cb) {
    const chunks = [];
    stream.on('data', (chunk) => {
	chunks.push(chunk);
    });
    stream.on('end', () => {
	cb(chunks.join(''));
    });
};


var callback = function(jsonString) {
    console.log(typeof jsonString);
    console.log(jsonString);
};


var req = https.request(options, function(res) {
    streamToString(res, callback)
});

req.end();

