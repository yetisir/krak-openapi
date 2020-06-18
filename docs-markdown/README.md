# Documentation for Krak REST API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BoreholesApi* | [**boreholes.create**](Apis/BoreholesApi.md#boreholes.create) | **POST** /boreholes/ | Create a new borehole
*BoreholesApi* | [**boreholes.delete**](Apis/BoreholesApi.md#boreholes.delete) | **DELETE** /boreholes/{borehole_id} | Delete a borehole
*BoreholesApi* | [**boreholes.readAll**](Apis/BoreholesApi.md#boreholes.readall) | **GET** /boreholes/ | Read all boreholes in db, sorted by id
*BoreholesApi* | [**boreholes.readOne**](Apis/BoreholesApi.md#boreholes.readone) | **GET** /boreholes/{borehole_id} | Read one borehole
*BoreholesApi* | [**boreholes.update**](Apis/BoreholesApi.md#boreholes.update) | **PUT** /boreholes/{borehole_id} | Update a borehole
*CorePhotosApi* | [**corePhotos.create**](Apis/CorePhotosApi.md#corephotos.create) | **POST** /boreholes/{borehole_id}/core_photos/ | Create a new core photo
*CorePhotosApi* | [**corePhotos.delete**](Apis/CorePhotosApi.md#corephotos.delete) | **DELETE** /boreholes/{borehole_id}/core_photos/{core_photo_id} | Delete a core_photo
*CorePhotosApi* | [**corePhotos.readAll**](Apis/CorePhotosApi.md#corephotos.readall) | **GET** /boreholes/{borehole_id}/core_photos/ | Read all core photo ids in db, sorted by id
*CorePhotosApi* | [**corePhotos.readOne**](Apis/CorePhotosApi.md#corephotos.readone) | **GET** /boreholes/{borehole_id}/core_photos/{core_photo_id} | Read one core photo
*CorePhotosApi* | [**corePhotos.update**](Apis/CorePhotosApi.md#corephotos.update) | **PUT** /boreholes/{borehole_id}/core_photos/{core_photo_id} | Update a core_photo


<a name="documentation-for-models"></a>
## Documentation for Models

 - [Boreholes](.//Models/Boreholes.md)
 - [CorePhotos](.//Models/CorePhotos.md)
 - [CorePhotosData](.//Models/CorePhotosData.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
