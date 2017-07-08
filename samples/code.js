const fs = require('fs');

const fileBuffer = fs.readFileSync(process.argv[2]);
const fileContentsAsString = fileBuffer.toString();

console.log('File contents: ');
console.log(fileContentsAsString);
