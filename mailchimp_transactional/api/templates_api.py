# coding: utf-8

"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.42
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mailchimp_transactional.api_client import ApiClient

class TemplatesApi(object):
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
        """Add template  # noqa: E501

        Add a new template.  # noqa: E501
        """
        (data) = self.add_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def add_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add template  # noqa: E501

        Add a new template.  # noqa: E501
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
            '/templates/add', 'POST',
            body=body_params,
            response_type='InlineResponse20060') # noqa: E501

    def delete(self, body = {}, **kwargs):  # noqa: E501
        """Delete template  # noqa: E501

        Delete a template.  # noqa: E501
        """
        (data) = self.delete_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def delete_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete template  # noqa: E501

        Delete a template.  # noqa: E501
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
            '/templates/delete', 'POST',
            body=body_params,
            response_type='InlineResponse20064') # noqa: E501

    def info(self, body = {}, **kwargs):  # noqa: E501
        """Get template info  # noqa: E501

        Get the information for an existing template.  # noqa: E501
        """
        (data) = self.info_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def info_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get template info  # noqa: E501

        Get the information for an existing template.  # noqa: E501
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
            '/templates/info', 'POST',
            body=body_params,
            response_type='InlineResponse20061') # noqa: E501

    def list(self, body = {}, **kwargs):  # noqa: E501
        """List templates  # noqa: E501

        Return a list of all the templates available to this user.  # noqa: E501
        """
        (data) = self.list_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def list_with_http_info(self, body, **kwargs):  # noqa: E501
        """List templates  # noqa: E501

        Return a list of all the templates available to this user.  # noqa: E501
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
            '/templates/list', 'POST',
            body=body_params,
            response_type='list[InlineResponse20065]') # noqa: E501

    def publish(self, body = {}, **kwargs):  # noqa: E501
        """Publish template content  # noqa: E501

        Publish the content for the template. Any new messages sent using this template will start using the content that was previously in draft.  # noqa: E501
        """
        (data) = self.publish_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def publish_with_http_info(self, body, **kwargs):  # noqa: E501
        """Publish template content  # noqa: E501

        Publish the content for the template. Any new messages sent using this template will start using the content that was previously in draft.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method publish" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/templates/publish', 'POST',
            body=body_params,
            response_type='InlineResponse20063') # noqa: E501

    def render(self, body = {}, **kwargs):  # noqa: E501
        """Render html template  # noqa: E501

        Inject content and optionally merge fields into a template, returning the HTML that results.  # noqa: E501
        """
        (data) = self.render_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def render_with_http_info(self, body, **kwargs):  # noqa: E501
        """Render html template  # noqa: E501

        Inject content and optionally merge fields into a template, returning the HTML that results.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method render" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/templates/render', 'POST',
            body=body_params,
            response_type='InlineResponse20066') # noqa: E501

    def time_series(self, body = {}, **kwargs):  # noqa: E501
        """Get template history  # noqa: E501

        Return the recent history (hourly stats for the last 30 days) for a template.  # noqa: E501
        """
        (data) = self.time_series_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def time_series_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get template history  # noqa: E501

        Return the recent history (hourly stats for the last 30 days) for a template.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method time_series" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/templates/time-series', 'POST',
            body=body_params,
            response_type='list[InlineResponse20049]') # noqa: E501

    def update(self, body = {}, **kwargs):  # noqa: E501
        """Update template  # noqa: E501

        Update the code for an existing template. If null is provided for any fields, the values will remain unchanged.  # noqa: E501
        """
        (data) = self.update_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def update_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update template  # noqa: E501

        Update the code for an existing template. If null is provided for any fields, the values will remain unchanged.  # noqa: E501
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
            '/templates/update', 'POST',
            body=body_params,
            response_type='InlineResponse20062') # noqa: E501
