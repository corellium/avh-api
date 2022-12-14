/**
 * Arm API
 *    This documents the Arm Virtual Hosting REST API.  For other examples and API clients such as python or javascript please see [API Clients (python/javascript)](https://github.com/ARM-software/avh-api).   For a guide on using this interface please see [API Quickstart](https://intercom.help/arm-avh/en/articles/6134791-quickstart-for-the-api-docs)   ## Links   - [API Quickstart](https://intercom.help/arm-avh/en/articles/6134791-quickstart-for-the-api-docs)   - [API Clients (python/javascript)](https://github.com/arm-software/avh-api)   
 *
 * The version of the OpenAPI document: 3.15.0-15704
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
    factory(root.expect, root.AvhApi);
  }
}(this, function(expect, AvhApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AvhApi.SubscriberInvite();
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

  describe('SubscriberInvite', function() {
    it('should create an instance of SubscriberInvite', function() {
      // uncomment below and update the code to test SubscriberInvite
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be.a(AvhApi.SubscriberInvite);
    });

    it('should have the property couponOptions (base name: "coupon_options")', function() {
      // uncomment below and update the code to test the property couponOptions
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

    it('should have the property plan (base name: "plan")', function() {
      // uncomment below and update the code to test the property plan
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

    it('should have the property trial (base name: "trial")', function() {
      // uncomment below and update the code to test the property trial
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

    it('should have the property couponCode (base name: "coupon_code")', function() {
      // uncomment below and update the code to test the property couponCode
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

    it('should have the property domain (base name: "domain")', function() {
      // uncomment below and update the code to test the property domain
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

    it('should have the property aggregate (base name: "aggregate")', function() {
      // uncomment below and update the code to test the property aggregate
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

    it('should have the property useBy (base name: "use_by")', function() {
      // uncomment below and update the code to test the property useBy
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

    it('should have the property active (base name: "active")', function() {
      // uncomment below and update the code to test the property active
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

    it('should have the property reusable (base name: "reusable")', function() {
      // uncomment below and update the code to test the property reusable
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

    it('should have the property createdAt (base name: "createdAt")', function() {
      // uncomment below and update the code to test the property createdAt
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

    it('should have the property updatedAt (base name: "updatedAt")', function() {
      // uncomment below and update the code to test the property updatedAt
      //var instance = new AvhApi.SubscriberInvite();
      //expect(instance).to.be();
    });

  });

}));