/**
 * Krak REST API
 * Krak REST API
 *
 * The version of the OpenAPI document: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.KrakRestApi);
  }
}(this, function(expect, KrakRestApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new KrakRestApi.CorePhotosApi();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('CorePhotosApi', function() {
    describe('corePhotosCreate', function() {
      it('should call corePhotosCreate successfully', function(done) {
        //uncomment below and update the code to test corePhotosCreate
        //instance.corePhotosCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('corePhotosDelete', function() {
      it('should call corePhotosDelete successfully', function(done) {
        //uncomment below and update the code to test corePhotosDelete
        //instance.corePhotosDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('corePhotosReadAll', function() {
      it('should call corePhotosReadAll successfully', function(done) {
        //uncomment below and update the code to test corePhotosReadAll
        //instance.corePhotosReadAll(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('corePhotosReadOne', function() {
      it('should call corePhotosReadOne successfully', function(done) {
        //uncomment below and update the code to test corePhotosReadOne
        //instance.corePhotosReadOne(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('corePhotosUpdate', function() {
      it('should call corePhotosUpdate successfully', function(done) {
        //uncomment below and update the code to test corePhotosUpdate
        //instance.corePhotosUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
