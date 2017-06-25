const fs = require('fs');
const request = require('request');

const url = 'https://anonfile.com/api/upload';

exports.upload = (fileName, filePath) => {
  const fileData = fs.readFileSync(filePath);

  const formData = {
    file: {
      value: fileData,
      options: {
        filename: fileName
      }
    }
  };

  request.post(
    {
      url,
      formData
    },
    (err, httpResponse, body) => {
      if (err) {
        console.log(`Upload failed ${err}`);
      } else {
        const responseData = JSON.parse(body);
        console.log(responseData.data.file.url.short);
      }
    }
  );
};
