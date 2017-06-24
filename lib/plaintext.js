const request = require('request');

const pastebinAPIKey = '787778417205c18cda84007232ba03e7';
const url = 'https://pastebin.com/api/api_post.php';

exports.plaintext = (fileName, fileData) => {
  const formData = {
    api_dev_key: pastebinAPIKey,
    api_option: 'paste',
    api_paste_name: fileName,
    api_paste_code: fileData.toString()
  };

  request.post(
    {
      url,
      formData
    },
    (err, response, body) => {
      console.log(body);
    }
  );
};
