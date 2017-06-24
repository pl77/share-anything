const request = require('request');

const imgurClientID = '9c65f969001905d';
const url = 'https://api.imgur.com/3/image';

exports.image = (fileName, fileData) => {
  const formData = {
    image: fileData
  };

  request.post(
    {
      headers: {
        authorization: `Client-ID ${imgurClientID}`
      },
      url,
      formData
    },
    (err, response, body) => {
      if (err) {
        console.log(`Upload fialed: ${err}`);
      } else {
        const responseData = JSON.parse(body);
        console.log(responseData.data.link);
      }
    }
  );
};
