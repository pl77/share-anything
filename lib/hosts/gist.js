const fs = require('fs');
const request = require('request');

const url = 'https://api.github.com/gists';

exports.upload = (fileName, filePath) => {
  const fileData = fs.readFileSync(filePath);

  const form = {
    public: true,
    files: {}
  };

  form.files[fileName] = {
    content: fileData.toString()
  };

  request.post(
    {
      url,
      body: JSON.stringify(form),
      headers: {
        'User-Agent': 'tallpants'
      }
    },
    (err, response, body) => {
      if (err) {
        console.log(`Upload failed: ${err}`);
      } else {
        const responseData = JSON.parse(body);
        console.log(responseData.html_url);
      }
    }
  );
};
