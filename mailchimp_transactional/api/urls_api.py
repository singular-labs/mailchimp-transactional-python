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

class UrlsApi(object):
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

    def add_tracking_domain(self, body = {}, **kwargs):  # noqa: E501
        """Add tracking domains  # noqa: E501

        Add a tracking domain to your account.  # noqa: E501
        """
        (data) = self.add_tracking_domain_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def add_tracking_domain_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add tracking domains  # noqa: E501

        Add a tracking domain to your account.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_tracking_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/urls/add-tracking-domain', 'POST',
            body=body_params,
            response_type='InlineResponse20071') # noqa: E501

    def check_tracking_domain(self, body = {}, **kwargs):  # noqa: E501
        """Check cname settings  # noqa: E501

        Checks the CNAME settings for a tracking domain. The domain must have been added already with the add-tracking-domain call.  # noqa: E501
        """
        (data) = self.check_tracking_domain_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def check_tracking_domain_with_http_info(self, body, **kwargs):  # noqa: E501
        """Check cname settings  # noqa: E501

        Checks the CNAME settings for a tracking domain. The domain must have been added already with the add-tracking-domain call.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_tracking_domain" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/urls/check-tracking-domain', 'POST',
            body=body_params,
            response_type='InlineResponse20071') # noqa: E501

    def list(self, body = {}, **kwargs):  # noqa: E501
        """List most clicked urls  # noqa: E501

        Get the 100 most clicked URLs.  # noqa: E501
        """
        (data) = self.list_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def list_with_http_info(self, body, **kwargs):  # noqa: E501
        """List most clicked urls  # noqa: E501

        Get the 100 most clicked URLs.  # noqa: E501
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
            '/urls/list', 'POST',
            body=body_params,
            response_type='list[InlineResponse20067]') # noqa: E501

    def search(self, body = {}, **kwargs):  # noqa: E501
        """Search most clicked urls  # noqa: E501

        Return the 100 most clicked URLs that match the search query given.  # noqa: E501
        """
        (data) = self.search_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def search_with_http_info(self, body, **kwargs):  # noqa: E501
        """Search most clicked urls  # noqa: E501

        Return the 100 most clicked URLs that match the search query given.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/urls/search', 'POST',
            body=body_params,
            response_type='list[InlineResponse20068]') # noqa: E501

    def time_series(self, body = {}, **kwargs):  # noqa: E501
        """Get url history  # noqa: E501

        Return the recent history (hourly stats for the last 30 days) for a URL  # noqa: E501
        """
        (data) = self.time_series_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def time_series_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get url history  # noqa: E501

        Return the recent history (hourly stats for the last 30 days) for a URL  # noqa: E501
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
            '/urls/time-series', 'POST',
            body=body_params,
            response_type='list[InlineResponse20069]') # noqa: E501

    def tracking_domains(self, body = {}, **kwargs):  # noqa: E501
        """List tracking domains  # noqa: E501

        Get the list of tracking domains set up for this account.  # noqa: E501
        """
        (data) = self.tracking_domains_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def tracking_domains_with_http_info(self, body, **kwargs):  # noqa: E501
        """List tracking domains  # noqa: E501

        Get the list of tracking domains set up for this account.  # noqa: E501
        """

        all_params = ['body']  # noqa: E501

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tracking_domains" % key
                )
            params[key] = val
        del params['kwargs']

        # add api_key to body params
        params['body']['key'] = self.api_key

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.api_client.call_api(
            '/urls/tracking-domains', 'POST',
            body=body_params,
            response_type='list[InlineResponse20070]') # noqa: E501
