'use strict';

/**
 * Module dependencies.
 */
 var errorHandler = require('./errors.server.controller'),
 _ = require('lodash'),
 exec = require('child_process').exec,
 fs = require('fs');

 exports.process = function(req, res) {

  fs.readFile(req.files.doc.path, function (err, data) {
   if (err) {
    console.log('Problem while saving the file.');
    return res.status(400).send({
      message: errorHandler.getErrorMessage(err)
    });
  } else {
    var newPath = __dirname + '/uploads/'+req.files.doc.name;
    fs.writeFile(newPath, data, function (err) {
      var python = 'python '+__dirname + '/ml/docProcessor.py' + ' ' + newPath;
      var child = exec(python, function(err, stdout, stderr) {
        if (err) {
          console.log('Problem while analyze.');
          return res.status(400).send({
            message: errorHandler.getErrorMessage(err)
          });
        } else {
          var result = JSON.parse(stdout);
          res.json(result);
        }
      });
    });
  }

});

};
