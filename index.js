const argv = require('minimist')(process.argv.slice(2));

if (argv._.length === 0) {
  console.log('No file specified.');
  process.exit(1);
}

const fs = require('fs');
const path = require('path');

const filePath = process.argv[2];

const fileStats = fs.statSync(filePath);
const sizeMB = Math.ceil(fileStats.size / 1000000);

if (sizeMB >= 1024) {
  console.log('File size is too large. (1GB limit for now).');
  process.exit(1);
}

const fileName = path.basename(filePath);
const fileExtension = fileName.split('.')[1];

const extensions = require('./lib/extensions');
const hosts = require('./lib/hosts');

let share = hosts[argv.h];

if (!share) {
  if (sizeMB <= 10 && extensions.imgur.includes(fileExtension)) {
    share = hosts.imgur;
  } else if (sizeMB <= 1 && extensions.gist.includes(fileExtension)) {
    share = hosts.gist;
  } else {
    share = hosts.anonfile;
  }
}

share(fileName, filePath);
