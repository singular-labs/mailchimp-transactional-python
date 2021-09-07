# coding: utf-8

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.35
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_transactional.api_client import ApiClient

class WebhooksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_key='', api_client = None):
        self.api_key = api_key
        if api_client:
            self.api_client = api_client
        else:
            self.api_client = ApiClient()

    def add(self, body = {}, **kwargs):  # noqa: E501
        """Add webhook  # noqa: E501

        Add a new webhook.  # noqa: E501
        """
        (data) = self.add_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def add_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add webhook  # noqa: E501

        Add a new webhook.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/webhooks/add', 'POST',
            body=body_params,
            response_type='InlineResponse20072') # noqa: E501

    def delete(self, body = {}, **kwargs):  # noqa: E501
        """Delete webhook  # noqa: E501

        Delete an existing webhook.  # noqa: E501
        """
        (data) = self.delete_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def delete_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete webhook  # noqa: E501

        Delete an existing webhook.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/webhooks/delete', 'POST',
            body=body_params,
            response_type='InlineResponse20075') # noqa: E501

    def info(self, body = {}, **kwargs):  # noqa: E501
        """Get webhook info  # noqa: E501

        Given the ID of an existing webhook, return the data about it.  # noqa: E501
        """
        (data) = self.info_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def info_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get webhook info  # noqa: E501

        Given the ID of an existing webhook, return the data about it.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method info" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/webhooks/info', 'POST',
            body=body_params,
            response_type='InlineResponse20073') # noqa: E501

    def list(self, body = {}, **kwargs):  # noqa: E501
        """List webhooks  # noqa: E501

        Get the list of all webhooks defined on the account.  # noqa: E501
        """
        (data) = self.list_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def list_with_http_info(self, body, **kwargs):  # noqa: E501
        """List webhooks  # noqa: E501

        Get the list of all webhooks defined on the account.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/webhooks/list', 'POST',
            body=body_params,
            response_type='list[InlineResponse20071]') # noqa: E501

    def update(self, body = {}, **kwargs):  # noqa: E501
        """Update webhook  # noqa: E501

        Update an existing webhook.  # noqa: E501
        """
        (data) = self.update_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def update_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update webhook  # noqa: E501

        Update an existing webhook.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/webhooks/update', 'POST',
            body=body_params,
            response_type='InlineResponse20074') # noqa: E501
