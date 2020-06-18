# CorePhotosApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**corePhotos.create**](CorePhotosApi.md#corePhotos.create) | **POST** /boreholes/{borehole_id}/core_photos/ | Create a new core photo
[**corePhotos.delete**](CorePhotosApi.md#corePhotos.delete) | **DELETE** /boreholes/{borehole_id}/core_photos/{core_photo_id} | Delete a core_photo
[**corePhotos.readAll**](CorePhotosApi.md#corePhotos.readAll) | **GET** /boreholes/{borehole_id}/core_photos/ | Read all core photo ids in db, sorted by id
[**corePhotos.readOne**](CorePhotosApi.md#corePhotos.readOne) | **GET** /boreholes/{borehole_id}/core_photos/{core_photo_id} | Read one core photo
[**corePhotos.update**](CorePhotosApi.md#corePhotos.update) | **PUT** /boreholes/{borehole_id}/core_photos/{core_photo_id} | Update a core_photo


<a name="corePhotos.create"></a>
# **corePhotos.create**
> core_photos corePhotos.create(boreholeId, photo, data)

Create a new core photo

    Create a new core photo

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Integer**| Id of Borehole | [default to null]
 **photo** | **File**|  | [default to null]
 **data** | [**core_photos_data**](..//Models/core_photos_data.md)|  | [default to null]

### Return type

[**core_photos**](..//Models/core_photos.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

<a name="corePhotos.delete"></a>
# **corePhotos.delete**
> corePhotos.delete(boreholeId, corePhotoId)

Delete a core_photo

    Delete a core_photo

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Integer**| Id of Borehole | [default to null]
 **corePhotoId** | **Integer**| Id of Borehole | [default to null]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="corePhotos.readAll"></a>
# **corePhotos.readAll**
> List corePhotos.readAll(boreholeId)

Read all core photo ids in db, sorted by id

    Read all core photo ids in db, sorted by id

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Integer**| Id of Borehole | [default to null]

### Return type

[**List**](..//Models/core_photos.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: multipart/form-data

<a name="corePhotos.readOne"></a>
# **corePhotos.readOne**
> core_photos corePhotos.readOne(boreholeId, corePhotoId)

Read one core photo

    Read one core photo

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Integer**| Id of Borehole | [default to null]
 **corePhotoId** | **Integer**| Id of Borehole | [default to null]

### Return type

[**core_photos**](..//Models/core_photos.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="corePhotos.update"></a>
# **corePhotos.update**
> core_photos corePhotos.update(boreholeId, corePhotoId, photo, data)

Update a core_photo

    Update a core_photo

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Integer**| Id of Borehole | [default to null]
 **corePhotoId** | **Integer**| Id of Borehole | [default to null]
 **photo** | **File**|  | [default to null]
 **data** | [**core_photos_data**](..//Models/core_photos_data.md)|  | [default to null]

### Return type

[**core_photos**](..//Models/core_photos.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

