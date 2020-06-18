# coding: utf-8

"""
    Krak REST API

    Krak REST API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CorePhotosApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def core_photos_create(self, borehole_id, photo, data, **kwargs):  # noqa: E501
        """Create a new core photo  # noqa: E501

        Create a new core photo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.core_photos_create(borehole_id, photo, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int borehole_id: Id of Borehole (required)
        :param file photo: (required)
        :param CorePhotosData data: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CorePhotos
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.core_photos_create_with_http_info(borehole_id, photo, data, **kwargs)  # noqa: E501

    def core_photos_create_with_http_info(self, borehole_id, photo, data, **kwargs):  # noqa: E501
        """Create a new core photo  # noqa: E501

        Create a new core photo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.core_photos_create_with_http_info(borehole_id, photo, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int borehole_id: Id of Borehole (required)
        :param file photo: (required)
        :param CorePhotosData data: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CorePhotos, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'borehole_id',
            'photo',
            'data'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method core_photos_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'borehole_id' is set
        if self.api_client.client_side_validation and ('borehole_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['borehole_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `borehole_id` when calling `core_photos_create`")  # noqa: E501
        # verify the required parameter 'photo' is set
        if self.api_client.client_side_validation and ('photo' not in local_var_params or  # noqa: E501
                                                        local_var_params['photo'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `photo` when calling `core_photos_create`")  # noqa: E501
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and ('data' not in local_var_params or  # noqa: E501
                                                        local_var_params['data'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data` when calling `core_photos_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'borehole_id' in local_var_params:
            path_params['borehole_id'] = local_var_params['borehole_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'photo' in local_var_params:
            local_var_files['photo'] = local_var_params['photo']  # noqa: E501
        if 'data' in local_var_params:
            form_params.append(('data', local_var_params['data']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/boreholes/{borehole_id}/core_photos/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CorePhotos',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def core_photos_delete(self, borehole_id, core_photo_id, **kwargs):  # noqa: E501
        """Delete a core_photo  # noqa: E501

        Delete a core_photo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.core_photos_delete(borehole_id, core_photo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int borehole_id: Id of Borehole (required)
        :param int core_photo_id: Id of Borehole (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.core_photos_delete_with_http_info(borehole_id, core_photo_id, **kwargs)  # noqa: E501

    def core_photos_delete_with_http_info(self, borehole_id, core_photo_id, **kwargs):  # noqa: E501
        """Delete a core_photo  # noqa: E501

        Delete a core_photo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.core_photos_delete_with_http_info(borehole_id, core_photo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int borehole_id: Id of Borehole (required)
        :param int core_photo_id: Id of Borehole (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'borehole_id',
            'core_photo_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method core_photos_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'borehole_id' is set
        if self.api_client.client_side_validation and ('borehole_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['borehole_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `borehole_id` when calling `core_photos_delete`")  # noqa: E501
        # verify the required parameter 'core_photo_id' is set
        if self.api_client.client_side_validation and ('core_photo_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['core_photo_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `core_photo_id` when calling `core_photos_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'borehole_id' in local_var_params:
            path_params['borehole_id'] = local_var_params['borehole_id']  # noqa: E501
        if 'core_photo_id' in local_var_params:
            path_params['core_photo_id'] = local_var_params['core_photo_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/boreholes/{borehole_id}/core_photos/{core_photo_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def core_photos_read_all(self, borehole_id, **kwargs):  # noqa: E501
        """Read all core photo ids in db, sorted by id  # noqa: E501

        Read all core photo ids in db, sorted by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.core_photos_read_all(borehole_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int borehole_id: Id of Borehole (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[CorePhotos]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.core_photos_read_all_with_http_info(borehole_id, **kwargs)  # noqa: E501

    def core_photos_read_all_with_http_info(self, borehole_id, **kwargs):  # noqa: E501
        """Read all core photo ids in db, sorted by id  # noqa: E501

        Read all core photo ids in db, sorted by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.core_photos_read_all_with_http_info(borehole_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int borehole_id: Id of Borehole (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[CorePhotos], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'borehole_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method core_photos_read_all" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'borehole_id' is set
        if self.api_client.client_side_validation and ('borehole_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['borehole_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `borehole_id` when calling `core_photos_read_all`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'borehole_id' in local_var_params:
            path_params['borehole_id'] = local_var_params['borehole_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/boreholes/{borehole_id}/core_photos/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CorePhotos]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def core_photos_read_one(self, borehole_id, core_photo_id, **kwargs):  # noqa: E501
        """Read one core photo  # noqa: E501

        Read one core photo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.core_photos_read_one(borehole_id, core_photo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int borehole_id: Id of Borehole (required)
        :param int core_photo_id: Id of Borehole (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CorePhotos
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.core_photos_read_one_with_http_info(borehole_id, core_photo_id, **kwargs)  # noqa: E501

    def core_photos_read_one_with_http_info(self, borehole_id, core_photo_id, **kwargs):  # noqa: E501
        """Read one core photo  # noqa: E501

        Read one core photo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.core_photos_read_one_with_http_info(borehole_id, core_photo_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int borehole_id: Id of Borehole (required)
        :param int core_photo_id: Id of Borehole (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CorePhotos, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'borehole_id',
            'core_photo_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method core_photos_read_one" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'borehole_id' is set
        if self.api_client.client_side_validation and ('borehole_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['borehole_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `borehole_id` when calling `core_photos_read_one`")  # noqa: E501
        # verify the required parameter 'core_photo_id' is set
        if self.api_client.client_side_validation and ('core_photo_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['core_photo_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `core_photo_id` when calling `core_photos_read_one`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'borehole_id' in local_var_params:
            path_params['borehole_id'] = local_var_params['borehole_id']  # noqa: E501
        if 'core_photo_id' in local_var_params:
            path_params['core_photo_id'] = local_var_params['core_photo_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/boreholes/{borehole_id}/core_photos/{core_photo_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CorePhotos',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def core_photos_update(self, borehole_id, core_photo_id, photo, data, **kwargs):  # noqa: E501
        """Update a core_photo  # noqa: E501

        Update a core_photo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.core_photos_update(borehole_id, core_photo_id, photo, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int borehole_id: Id of Borehole (required)
        :param int core_photo_id: Id of Borehole (required)
        :param file photo: (required)
        :param CorePhotosData data: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CorePhotos
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.core_photos_update_with_http_info(borehole_id, core_photo_id, photo, data, **kwargs)  # noqa: E501

    def core_photos_update_with_http_info(self, borehole_id, core_photo_id, photo, data, **kwargs):  # noqa: E501
        """Update a core_photo  # noqa: E501

        Update a core_photo  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.core_photos_update_with_http_info(borehole_id, core_photo_id, photo, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int borehole_id: Id of Borehole (required)
        :param int core_photo_id: Id of Borehole (required)
        :param file photo: (required)
        :param CorePhotosData data: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CorePhotos, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'borehole_id',
            'core_photo_id',
            'photo',
            'data'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method core_photos_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'borehole_id' is set
        if self.api_client.client_side_validation and ('borehole_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['borehole_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `borehole_id` when calling `core_photos_update`")  # noqa: E501
        # verify the required parameter 'core_photo_id' is set
        if self.api_client.client_side_validation and ('core_photo_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['core_photo_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `core_photo_id` when calling `core_photos_update`")  # noqa: E501
        # verify the required parameter 'photo' is set
        if self.api_client.client_side_validation and ('photo' not in local_var_params or  # noqa: E501
                                                        local_var_params['photo'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `photo` when calling `core_photos_update`")  # noqa: E501
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and ('data' not in local_var_params or  # noqa: E501
                                                        local_var_params['data'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data` when calling `core_photos_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'borehole_id' in local_var_params:
            path_params['borehole_id'] = local_var_params['borehole_id']  # noqa: E501
        if 'core_photo_id' in local_var_params:
            path_params['core_photo_id'] = local_var_params['core_photo_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'photo' in local_var_params:
            local_var_files['photo'] = local_var_params['photo']  # noqa: E501
        if 'data' in local_var_params:
            form_params.append(('data', local_var_params['data']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/boreholes/{borehole_id}/core_photos/{core_photo_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CorePhotos',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)