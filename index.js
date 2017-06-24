const fs = require('fs');
const path = require('path');
const mime = require('mime-types');

if (!process.argv[2]) {
  console.log('No file specified');
  process.exit(1);
}

const filePath = process.argv[2];
const fileName = path.basename(filePath);
const mimeType = mime.lookup(filePath);
const fileData = fs.readFileSync(filePath);

let shareFunction = undefined;

if (mimeType.startsWith('image')) {
  shareFunction = require('./lib/image').image;
} else if (fileName.endsWith('txt')) {
  shareFunction = require('./lib/plaintext').plaintext;
} else if (mimeType.endsWith('javascript')) {
  shareFunction = require('./lib/source-code').program;
}

shareFunction(fileName, fileData);
