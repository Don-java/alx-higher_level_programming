#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

function statusCodes (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log('code: ' + response.statusCode);
    }
  });
}
statusCodes(url);
