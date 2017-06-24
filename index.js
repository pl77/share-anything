const fs = require('fs');
const path = require('path');

const extensions = require('./lib/extensions');
const hosts = require('./lib/hosts');

if (!process.argv[2]) {
  console.log('No file specified.');
  process.exit(1);
}

const filePath = process.argv[2];
const fileName = path.basename(filePath);
const fileExtension = fileName.split('.')[1];
const fileData = fs.readFileSync(filePath);

let shareFunction = undefined;

if (extensions.sources.includes(fileExtension)) {
  shareFunction = hosts.gist;
}

shareFunction(fileName, fileData);
