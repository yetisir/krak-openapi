# KrakRestApi.CorePhotosApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**corePhotosCreate**](CorePhotosApi.md#corePhotosCreate) | **POST** /boreholes/{borehole_id}/core_photos/ | Create a new core photo
[**corePhotosDelete**](CorePhotosApi.md#corePhotosDelete) | **DELETE** /boreholes/{borehole_id}/core_photos/{core_photo_id} | Delete a core_photo
[**corePhotosReadAll**](CorePhotosApi.md#corePhotosReadAll) | **GET** /boreholes/{borehole_id}/core_photos/ | Read all core photo ids in db, sorted by id
[**corePhotosReadOne**](CorePhotosApi.md#corePhotosReadOne) | **GET** /boreholes/{borehole_id}/core_photos/{core_photo_id} | Read one core photo
[**corePhotosUpdate**](CorePhotosApi.md#corePhotosUpdate) | **PUT** /boreholes/{borehole_id}/core_photos/{core_photo_id} | Update a core_photo



## corePhotosCreate

> CorePhotos corePhotosCreate(boreholeId, photo, data)

Create a new core photo

Create a new core photo

### Example

```javascript
import KrakRestApi from 'krak_rest_api';

let apiInstance = new KrakRestApi.CorePhotosApi();
let boreholeId = 56; // Number | Id of Borehole
let photo = "/path/to/file"; // File | 
let data = new KrakRestApi.CorePhotosData(); // CorePhotosData | 
apiInstance.corePhotosCreate(boreholeId, photo, data, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Number**| Id of Borehole | 
 **photo** | **File**|  | 
 **data** | [**CorePhotosData**](CorePhotosData.md)|  | 

### Return type

[**CorePhotos**](CorePhotos.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## corePhotosDelete

> corePhotosDelete(boreholeId, corePhotoId)

Delete a core_photo

Delete a core_photo

### Example

```javascript
import KrakRestApi from 'krak_rest_api';

let apiInstance = new KrakRestApi.CorePhotosApi();
let boreholeId = 56; // Number | Id of Borehole
let corePhotoId = 56; // Number | Id of Borehole
apiInstance.corePhotosDelete(boreholeId, corePhotoId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Number**| Id of Borehole | 
 **corePhotoId** | **Number**| Id of Borehole | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## corePhotosReadAll

> [CorePhotos] corePhotosReadAll(boreholeId)

Read all core photo ids in db, sorted by id

Read all core photo ids in db, sorted by id

### Example

```javascript
import KrakRestApi from 'krak_rest_api';

let apiInstance = new KrakRestApi.CorePhotosApi();
let boreholeId = 56; // Number | Id of Borehole
apiInstance.corePhotosReadAll(boreholeId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Number**| Id of Borehole | 

### Return type

[**[CorePhotos]**](CorePhotos.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: multipart/form-data


## corePhotosReadOne

> CorePhotos corePhotosReadOne(boreholeId, corePhotoId)

Read one core photo

Read one core photo

### Example

```javascript
import KrakRestApi from 'krak_rest_api';

let apiInstance = new KrakRestApi.CorePhotosApi();
let boreholeId = 56; // Number | Id of Borehole
let corePhotoId = 56; // Number | Id of Borehole
apiInstance.corePhotosReadOne(boreholeId, corePhotoId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Number**| Id of Borehole | 
 **corePhotoId** | **Number**| Id of Borehole | 

### Return type

[**CorePhotos**](CorePhotos.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## corePhotosUpdate

> CorePhotos corePhotosUpdate(boreholeId, corePhotoId, photo, data)

Update a core_photo

Update a core_photo

### Example

```javascript
import KrakRestApi from 'krak_rest_api';

let apiInstance = new KrakRestApi.CorePhotosApi();
let boreholeId = 56; // Number | Id of Borehole
let corePhotoId = 56; // Number | Id of Borehole
let photo = "/path/to/file"; // File | 
let data = new KrakRestApi.CorePhotosData(); // CorePhotosData | 
apiInstance.corePhotosUpdate(boreholeId, corePhotoId, photo, data, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Number**| Id of Borehole | 
 **corePhotoId** | **Number**| Id of Borehole | 
 **photo** | **File**|  | 
 **data** | [**CorePhotosData**](CorePhotosData.md)|  | 

### Return type

[**CorePhotos**](CorePhotos.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

