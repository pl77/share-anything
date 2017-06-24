const fs = require('fs');
const mime = require('mime');

const { image } = require('./lib/image');

if (!process.argv[2]) {
  console.log('No file specified');
  process.exit(1);
}

const fileName = process.argv[2];
const fileData = fs.readFileSync(fileName);

const mimeType = mime.lookup(process.argv[2]);

if (mimeType.startsWith('image')) {
  image(fileName, fileData);
}
