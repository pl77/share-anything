const argv = require('minimist')(process.argv.slice(2));

if (argv._.length === 0) {
  console.log('No file specified.');
  process.exit(1);
}

const fs = require('fs');
const path = require('path');

const extensions = require('./lib/extensions');
const hosts = require('./lib/hosts');

const filePath = process.argv[2];
const fileName = path.basename(filePath);
const fileExtension = fileName.split('.')[1];
const fileData = fs.readFileSync(filePath);

let share = hosts[argv.h];

if (!share) {
  if (extensions.gist.includes(fileExtension)) {
    share = hosts.gist;
  } else if (extensions.imgur.includes(fileExtension)) {
    share = hosts.imgur;
  }
}

share(fileName, fileData);
