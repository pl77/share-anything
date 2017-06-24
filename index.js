const fs = require('fs');
const mime = require('mime');

if (!process.argv[2]) {
  console.log('No file specified');
  process.exit(1);
}

const fileName = process.argv[2];
const fileData = fs.readFileSync(fileName);
const mimeType = mime.lookup(process.argv[2]);

let shareFunction = undefined;

if (mimeType.startsWith('image')) {
  shareFunction = require('./lib/image').image;
} else if (mimeType === 'text/plain') {
  shareFunction = require('./lib/plaintext').plaintext;
}

shareFunction(fileName, fileData);
