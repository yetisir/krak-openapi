# BoreholesApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boreholes.create**](BoreholesApi.md#boreholes.create) | **POST** /boreholes/ | Create a new borehole
[**boreholes.delete**](BoreholesApi.md#boreholes.delete) | **DELETE** /boreholes/{borehole_id} | Delete a borehole
[**boreholes.readAll**](BoreholesApi.md#boreholes.readAll) | **GET** /boreholes/ | Read all boreholes in db, sorted by id
[**boreholes.readOne**](BoreholesApi.md#boreholes.readOne) | **GET** /boreholes/{borehole_id} | Read one borehole
[**boreholes.update**](BoreholesApi.md#boreholes.update) | **PUT** /boreholes/{borehole_id} | Update a borehole


<a name="boreholes.create"></a>
# **boreholes.create**
> boreholes boreholes.create(boreholes)

Create a new borehole

    Create a new borehole

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholes** | [**Boreholes**](..//Models/Boreholes.md)| Borehole to create |

### Return type

[**boreholes**](..//Models/boreholes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="boreholes.delete"></a>
# **boreholes.delete**
> boreholes.delete(boreholeId)

Delete a borehole

    Delete a borehole

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Integer**| Id of the borehole to get | [default to null]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

<a name="boreholes.readAll"></a>
# **boreholes.readAll**
> List boreholes.readAll()

Read all boreholes in db, sorted by id

    Read all boreholes in db, sorted by id

### Parameters
This endpoint does not need any parameter.

### Return type

[**List**](..//Models/boreholes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="boreholes.readOne"></a>
# **boreholes.readOne**
> boreholes boreholes.readOne(boreholeId)

Read one borehole

    Read one borehole

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Integer**| Id of the borehole to get | [default to null]

### Return type

[**boreholes**](..//Models/boreholes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="boreholes.update"></a>
# **boreholes.update**
> boreholes boreholes.update(boreholeId, boreholes)

Update a borehole

    Update a borehole

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **boreholeId** | **Integer**| Id of the borehole to get | [default to null]
 **boreholes** | [**Boreholes**](..//Models/Boreholes.md)|  | [optional]

### Return type

[**boreholes**](..//Models/boreholes.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

