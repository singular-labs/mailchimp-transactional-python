# coding: utf-8
"""
    Mailchimp Transactional API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.42
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import datetime
import requests
import json

class ApiClientError(Exception):
    def __init__(self, text, status_code):
        self.text = text
        self.status_code = status_code

class ApiClient(object):
    def __init__(self):
        self.host = "https://mandrillapp.com/api/1.0"
        self.user_agent = 'Swagger-Codegen/1.0.42/python'
        self.format_list = ['json', 'xml', 'php', 'yaml']
        self.content_type = 'application/json'
        self.default_output_format = 'json'
        self.accepts = ['application/json', 'application/xml', 'application/x-php', 'application/x-yaml; charset=utf-8']

    def set_default_output_format(self, output_format):
        if output_format in self.format_list:
            self.default_output_format = output_format

    def call_api(self, resource_path, method, header_params=None, body=None, **kwargs):
        # header parameters
        headers = header_params or {}
        headers['User-Agent'] = self.user_agent
        headers['Content-Type'] = self.content_type

        # request url
        url = self.host + resource_path

        use_default_output_format = True

        if body and 'outputFormat' in body:
            format = body['outputFormat'].lower()
            if format in self.format_list:
                url += '.%s' % format
                del body['outputFormat']
                use_default_output_format = False

        if use_default_output_format and self.default_output_format in self.format_list:
            url += '.%s' % self.default_output_format        

        # perform request and return response
        res = self.request(method, url, body, headers)

        try:
            if 'application/json' in res.headers.get('content-type'):
                data = res.json()
            else:
                data = res.text
        except Exception as err:
            data = None

        if data:
            if (res.ok):
                return data
            else:
                raise ApiClientError(text = data, status_code = res.status_code)
        else:
            return res

    def request(self, method, url, body=None, headers=None, timeout=300.0):
        if method == 'POST':
            return requests.post(url, data=json.dumps(body), headers=headers, timeout=timeout)
        else:
            raise ValueError(
                "http method must be `POST`"
            )