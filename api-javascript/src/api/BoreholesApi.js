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


import ApiClient from "../ApiClient";
import Boreholes from '../model/Boreholes';

/**
* Boreholes service.
* @module api/BoreholesApi
* @version 0.0.1
*/
export default class BoreholesApi {

    /**
    * Constructs a new BoreholesApi. 
    * @alias module:api/BoreholesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the boreholesCreate operation.
     * @callback module:api/BoreholesApi~boreholesCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Boreholes} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new borehole
     * Create a new borehole
     * @param {module:model/Boreholes} boreholes Borehole to create
     * @param {module:api/BoreholesApi~boreholesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Boreholes}
     */
    boreholesCreate(boreholes, callback) {
      let postBody = boreholes;
      // verify the required parameter 'boreholes' is set
      if (boreholes === undefined || boreholes === null) {
        throw new Error("Missing the required parameter 'boreholes' when calling boreholesCreate");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Boreholes;
      return this.apiClient.callApi(
        '/boreholes/', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the boreholesDelete operation.
     * @callback module:api/BoreholesApi~boreholesDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a borehole
     * Delete a borehole
     * @param {Number} boreholeId Id of the borehole to get
     * @param {module:api/BoreholesApi~boreholesDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    boreholesDelete(boreholeId, callback) {
      let postBody = null;
      // verify the required parameter 'boreholeId' is set
      if (boreholeId === undefined || boreholeId === null) {
        throw new Error("Missing the required parameter 'boreholeId' when calling boreholesDelete");
      }

      let pathParams = {
        'borehole_id': boreholeId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/boreholes/{borehole_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the boreholesReadAll operation.
     * @callback module:api/BoreholesApi~boreholesReadAllCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Boreholes>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Read all boreholes in db, sorted by id
     * Read all boreholes in db, sorted by id
     * @param {module:api/BoreholesApi~boreholesReadAllCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Boreholes>}
     */
    boreholesReadAll(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Boreholes];
      return this.apiClient.callApi(
        '/boreholes/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the boreholesReadOne operation.
     * @callback module:api/BoreholesApi~boreholesReadOneCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Boreholes} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Read one borehole
     * Read one borehole
     * @param {Number} boreholeId Id of the borehole to get
     * @param {module:api/BoreholesApi~boreholesReadOneCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Boreholes}
     */
    boreholesReadOne(boreholeId, callback) {
      let postBody = null;
      // verify the required parameter 'boreholeId' is set
      if (boreholeId === undefined || boreholeId === null) {
        throw new Error("Missing the required parameter 'boreholeId' when calling boreholesReadOne");
      }

      let pathParams = {
        'borehole_id': boreholeId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Boreholes;
      return this.apiClient.callApi(
        '/boreholes/{borehole_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the boreholesUpdate operation.
     * @callback module:api/BoreholesApi~boreholesUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Boreholes} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a borehole
     * Update a borehole
     * @param {Number} boreholeId Id of the borehole to get
     * @param {Object} opts Optional parameters
     * @param {module:model/Boreholes} opts.boreholes 
     * @param {module:api/BoreholesApi~boreholesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Boreholes}
     */
    boreholesUpdate(boreholeId, opts, callback) {
      opts = opts || {};
      let postBody = opts['boreholes'];
      // verify the required parameter 'boreholeId' is set
      if (boreholeId === undefined || boreholeId === null) {
        throw new Error("Missing the required parameter 'boreholeId' when calling boreholesUpdate");
      }

      let pathParams = {
        'borehole_id': boreholeId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Boreholes;
      return this.apiClient.callApi(
        '/boreholes/{borehole_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
