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
    instance = new KrakRestApi.Boreholes();
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

  describe('Boreholes', function() {
    it('should create an instance of Boreholes', function() {
      // uncomment below and update the code to test Boreholes
      //var instane = new KrakRestApi.Boreholes();
      //expect(instance).to.be.a(KrakRestApi.Boreholes);
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instane = new KrakRestApi.Boreholes();
      //expect(instance).to.be();
    });

    it('should have the property easting (base name: "easting")', function() {
      // uncomment below and update the code to test the property easting
      //var instane = new KrakRestApi.Boreholes();
      //expect(instance).to.be();
    });

    it('should have the property northing (base name: "northing")', function() {
      // uncomment below and update the code to test the property northing
      //var instane = new KrakRestApi.Boreholes();
      //expect(instance).to.be();
    });

    it('should have the property elevation (base name: "elevation")', function() {
      // uncomment below and update the code to test the property elevation
      //var instane = new KrakRestApi.Boreholes();
      //expect(instance).to.be();
    });

  });

}));
