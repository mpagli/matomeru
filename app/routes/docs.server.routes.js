'use strict';

/**
 * Module dependencies.
 */
var users = require('../../app/controllers/users.server.controller'),
  docs = require('../../app/controllers/docs.server.controller');

module.exports = function(app) {
  app.route('/docs/process')
    .put(docs.processFile);

};