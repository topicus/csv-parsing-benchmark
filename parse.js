var csv = require('fast-csv');
var fs = require('fs');
var stream = fs.createReadStream('test.csv');

csv
 .fromStream(stream)
 .on('end', function(){
     console.log('done');
 });
