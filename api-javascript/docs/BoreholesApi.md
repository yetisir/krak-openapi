# KrakRestApi.BoreholesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boreholesCreate**](BoreholesApi.md#boreholesCreate) | **POST** /boreholes/ | Create a new borehole
[**boreholesDelete**](BoreholesApi.md#boreholesDelete) | **DELETE** /boreholes/{borehole_id} | Delete a borehole
[**boreholesReadAll**](BoreholesApi.md#boreholesReadAll) | **GET** /boreholes/ | Read all boreholes in db, sorted by id
[**boreholesReadOne**](BoreholesApi.md#boreholesReadOne) | **GET** /boreholes/{borehole_id} | Read one borehole
[**boreholesUpdate**](BoreholesApi.md#boreholesUpdate) | **PUT** /boreholes/{borehole_id} | Update a borehole



## boreholesCreate

> Boreholes boreholesCreate(boreholes)

Create a new borehole

Create a new borehole

### Example

```javascript
import KrakRestApi from 'krak_rest_api';

let apiInstance = new KrakRestApi.BoreholesApi();
let boreholes = new KrakRestApi.Boreholes(); // Boreholes | Borehole to create
apiInstance.boreholesCreate(boreholes, (error, data, response) => {
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
 **boreholes** | [**Boreholes**](Boreholes.md)| Borehole to create | 

### Return type

[**Boreholes**](Boreholes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## boreholesDelete

> boreholesDelete(boreholeId)

Delete a borehole

Delete a borehole

### Example

```javascript
import KrakRestApi from 'krak_rest_api';

let apiInstance = new KrakRestApi.BoreholesApi();
let boreholeId = 56; // Number | Id of the borehole to get
apiInstance.boreholesDelete(boreholeId, (error, data, response) => {
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
 **boreholeId** | **Number**| Id of the borehole to get | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## boreholesReadAll

> [Boreholes] boreholesReadAll()

Read all boreholes in db, sorted by id

Read all boreholes in db, sorted by id

### Example

```javascript
import KrakRestApi from 'krak_rest_api';

let apiInstance = new KrakRestApi.BoreholesApi();
apiInstance.boreholesReadAll((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Boreholes]**](Boreholes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## boreholesReadOne

> Boreholes boreholesReadOne(boreholeId)

Read one borehole

Read one borehole

### Example

```javascript
import KrakRestApi from 'krak_rest_api';

let apiInstance = new KrakRestApi.BoreholesApi();
let boreholeId = 56; // Number | Id of the borehole to get
apiInstance.boreholesReadOne(boreholeId, (error, data, response) => {
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
 **boreholeId** | **Number**| Id of the borehole to get | 

### Return type

[**Boreholes**](Boreholes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## boreholesUpdate

> Boreholes boreholesUpdate(boreholeId, opts)

Update a borehole

Update a borehole

### Example

```javascript
import KrakRestApi from 'krak_rest_api';

let apiInstance = new KrakRestApi.BoreholesApi();
let boreholeId = 56; // Number | Id of the borehole to get
let opts = {
  'boreholes': new KrakRestApi.Boreholes() // Boreholes | 
};
apiInstance.boreholesUpdate(boreholeId, opts, (error, data, response) => {
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
 **boreholeId** | **Number**| Id of the borehole to get | 
 **boreholes** | [**Boreholes**](Boreholes.md)|  | [optional] 

### Return type

[**Boreholes**](Boreholes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

