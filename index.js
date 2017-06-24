const fs = require('fs');
const request = require('request');

const clientID = '9c65f969001905d';
const uploadRoute = 'https://api.imgur.com/3/image';

if (!process.argv[2]) {
  console.log('No file specified');
  process.exit(1);
}

const fileName = process.argv[2];
const fileData = fs.readFileSync(fileName);

const formData = {
  image: fileData
};

request.post(
  {
    headers: {
      authorization: `Client-ID ${clientID}`
    },
    url: uploadRoute,
    formData: formData
  },
  (err, response, body) => {
    if (err) {
      console.log(`Upload failed: ${err}`);
    } else {
      const responseData = JSON.parse(body);
      console.log(responseData.data.link);
    }
  }
);
