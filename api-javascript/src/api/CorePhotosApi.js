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
import CorePhotos from '../model/CorePhotos';
import CorePhotosData from '../model/CorePhotosData';

/**
* CorePhotos service.
* @module api/CorePhotosApi
* @version 0.0.1
*/
export default class CorePhotosApi {

    /**
    * Constructs a new CorePhotosApi. 
    * @alias module:api/CorePhotosApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the corePhotosCreate operation.
     * @callback module:api/CorePhotosApi~corePhotosCreateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CorePhotos} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new core photo
     * Create a new core photo
     * @param {Number} boreholeId Id of Borehole
     * @param {File} photo 
     * @param {module:model/CorePhotosData} data 
     * @param {module:api/CorePhotosApi~corePhotosCreateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CorePhotos}
     */
    corePhotosCreate(boreholeId, photo, data, callback) {
      let postBody = null;
      // verify the required parameter 'boreholeId' is set
      if (boreholeId === undefined || boreholeId === null) {
        throw new Error("Missing the required parameter 'boreholeId' when calling corePhotosCreate");
      }
      // verify the required parameter 'photo' is set
      if (photo === undefined || photo === null) {
        throw new Error("Missing the required parameter 'photo' when calling corePhotosCreate");
      }
      // verify the required parameter 'data' is set
      if (data === undefined || data === null) {
        throw new Error("Missing the required parameter 'data' when calling corePhotosCreate");
      }

      let pathParams = {
        'borehole_id': boreholeId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'photo': photo,
        'data': data
      };

      let authNames = [];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = CorePhotos;
      return this.apiClient.callApi(
        '/boreholes/{borehole_id}/core_photos/', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the corePhotosDelete operation.
     * @callback module:api/CorePhotosApi~corePhotosDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a core_photo
     * Delete a core_photo
     * @param {Number} boreholeId Id of Borehole
     * @param {Number} corePhotoId Id of Borehole
     * @param {module:api/CorePhotosApi~corePhotosDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    corePhotosDelete(boreholeId, corePhotoId, callback) {
      let postBody = null;
      // verify the required parameter 'boreholeId' is set
      if (boreholeId === undefined || boreholeId === null) {
        throw new Error("Missing the required parameter 'boreholeId' when calling corePhotosDelete");
      }
      // verify the required parameter 'corePhotoId' is set
      if (corePhotoId === undefined || corePhotoId === null) {
        throw new Error("Missing the required parameter 'corePhotoId' when calling corePhotosDelete");
      }

      let pathParams = {
        'borehole_id': boreholeId,
        'core_photo_id': corePhotoId
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
        '/boreholes/{borehole_id}/core_photos/{core_photo_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the corePhotosReadAll operation.
     * @callback module:api/CorePhotosApi~corePhotosReadAllCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/CorePhotos>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Read all core photo ids in db, sorted by id
     * Read all core photo ids in db, sorted by id
     * @param {Number} boreholeId Id of Borehole
     * @param {module:api/CorePhotosApi~corePhotosReadAllCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/CorePhotos>}
     */
    corePhotosReadAll(boreholeId, callback) {
      let postBody = null;
      // verify the required parameter 'boreholeId' is set
      if (boreholeId === undefined || boreholeId === null) {
        throw new Error("Missing the required parameter 'boreholeId' when calling corePhotosReadAll");
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
      let accepts = ['multipart/form-data'];
      let returnType = [CorePhotos];
      return this.apiClient.callApi(
        '/boreholes/{borehole_id}/core_photos/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the corePhotosReadOne operation.
     * @callback module:api/CorePhotosApi~corePhotosReadOneCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CorePhotos} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Read one core photo
     * Read one core photo
     * @param {Number} boreholeId Id of Borehole
     * @param {Number} corePhotoId Id of Borehole
     * @param {module:api/CorePhotosApi~corePhotosReadOneCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CorePhotos}
     */
    corePhotosReadOne(boreholeId, corePhotoId, callback) {
      let postBody = null;
      // verify the required parameter 'boreholeId' is set
      if (boreholeId === undefined || boreholeId === null) {
        throw new Error("Missing the required parameter 'boreholeId' when calling corePhotosReadOne");
      }
      // verify the required parameter 'corePhotoId' is set
      if (corePhotoId === undefined || corePhotoId === null) {
        throw new Error("Missing the required parameter 'corePhotoId' when calling corePhotosReadOne");
      }

      let pathParams = {
        'borehole_id': boreholeId,
        'core_photo_id': corePhotoId
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
      let returnType = CorePhotos;
      return this.apiClient.callApi(
        '/boreholes/{borehole_id}/core_photos/{core_photo_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the corePhotosUpdate operation.
     * @callback module:api/CorePhotosApi~corePhotosUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CorePhotos} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a core_photo
     * Update a core_photo
     * @param {Number} boreholeId Id of Borehole
     * @param {Number} corePhotoId Id of Borehole
     * @param {File} photo 
     * @param {module:model/CorePhotosData} data 
     * @param {module:api/CorePhotosApi~corePhotosUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CorePhotos}
     */
    corePhotosUpdate(boreholeId, corePhotoId, photo, data, callback) {
      let postBody = null;
      // verify the required parameter 'boreholeId' is set
      if (boreholeId === undefined || boreholeId === null) {
        throw new Error("Missing the required parameter 'boreholeId' when calling corePhotosUpdate");
      }
      // verify the required parameter 'corePhotoId' is set
      if (corePhotoId === undefined || corePhotoId === null) {
        throw new Error("Missing the required parameter 'corePhotoId' when calling corePhotosUpdate");
      }
      // verify the required parameter 'photo' is set
      if (photo === undefined || photo === null) {
        throw new Error("Missing the required parameter 'photo' when calling corePhotosUpdate");
      }
      // verify the required parameter 'data' is set
      if (data === undefined || data === null) {
        throw new Error("Missing the required parameter 'data' when calling corePhotosUpdate");
      }

      let pathParams = {
        'borehole_id': boreholeId,
        'core_photo_id': corePhotoId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'photo': photo,
        'data': data
      };

      let authNames = [];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = CorePhotos;
      return this.apiClient.callApi(
        '/boreholes/{borehole_id}/core_photos/{core_photo_id}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
