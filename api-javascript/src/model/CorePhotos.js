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

import ApiClient from '../ApiClient';
import CorePhotosData from './CorePhotosData';

/**
 * The CorePhotos model module.
 * @module model/CorePhotos
 * @version 0.0.1
 */
class CorePhotos {
    /**
     * Constructs a new <code>CorePhotos</code>.
     * @alias module:model/CorePhotos
     * @param photo {File} 
     * @param data {module:model/CorePhotosData} 
     */
    constructor(photo, data) { 
        
        CorePhotos.initialize(this, photo, data);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, photo, data) { 
        obj['photo'] = photo;
        obj['data'] = data;
    }

    /**
     * Constructs a <code>CorePhotos</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CorePhotos} obj Optional instance to populate.
     * @return {module:model/CorePhotos} The populated <code>CorePhotos</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CorePhotos();

            if (data.hasOwnProperty('photo')) {
                obj['photo'] = ApiClient.convertToType(data['photo'], File);
            }
            if (data.hasOwnProperty('data')) {
                obj['data'] = CorePhotosData.constructFromObject(data['data']);
            }
        }
        return obj;
    }


}

/**
 * @member {File} photo
 */
CorePhotos.prototype['photo'] = undefined;

/**
 * @member {module:model/CorePhotosData} data
 */
CorePhotos.prototype['data'] = undefined;






export default CorePhotos;

