# A simple way to query APIs from Python

import datetime
import json
import os
from time import sleep

import requests


class RPApi(object):
    base_url = 'https://api.ravenpack.com/api/'

    def __init__(self,
                 api_key=os.environ.get('RP_API_KEY')):
        if api_key is None:
            raise ValueError(
                "Please initialize with an api_key "
                "or set your environment RP_API_KEY with a permanent token"
            )
        self.api_key = api_key

    def api_get(self, data, endpoint):
        """ The common way to do a request to the API passing headers"""
        response = requests.post(
            url=endpoint,
            headers=dict(API_KEY=self.api_key),
            data=json.dumps(data)
        )
        assert response.status_code is 200, 'Got an error {status}: {error_message}'.format(
            status=response.status_code, error_message=response.text
        )
        return response

    def get_entity_reference_inline(self, entities):
        # request some entity reference and return the results
        """

        :type entities: list
        """
        data = dict(
            return_type='preview',
            rp_entity_id_list=entities
        )
        endpoint = self.base_url + "entity-reference"
        response = self.api_get(data, endpoint)
        return response.json()

    def get_entity_mapping_inline(self, entities):
        # request some entity reference and return the results
        """

        :type entities: list
        """
        data = dict(
            return_type='preview',
            identifiers=entities
        )
        endpoint = self.base_url + "entity-mapping"
        response = self.api_get(data, endpoint)
        return response.json()

    def get_file_availability(self, token):
        data = dict(
            token=token
        )
        endpoint = self.base_url + "file-availability"
        response = self.api_get(data, endpoint).json()

        if not response['url']:
            return False  # when the file is not available we return False
        return response

    def get_analytics(self,
                      start_date, end_date,
                      entities=None,
                      filters=None,
                      return_type='dump',
                      format='csv',
                      wait=True,  # when a dump is requested, wait for it to be ready
                      ):
        endpoint = self.base_url + "analytics"
        data = dict(
            start_date=self.validate(start_date, 'date'),
            end_date=self.validate(end_date, 'date'),
            entities=entities,
            filters=filters,
            return_type=return_type,
            events=None,
        )
        if return_type == 'dump':
            data['format'] = format
        response = self.api_get(data, endpoint)
        if return_type == 'preview':
            return response.json()['records'] or []
        elif return_type == 'dump':
            token = response.json()['token']
            if not wait:
                return token  # just return the token
            self.yield_content_when_ready(token)

    def validate(self, value, field_type):
        if field_type == 'date':
            if isinstance(value, datetime.date):
                value = value.strftime('%Y-%m-%d')
        return value

    def yield_content_when_ready(self, token):
        available_file = None
        while not available_file:
            available_file = self.get_file_availability(token)
            if available_file:
                break
            sleep(.5)
        r = requests.get(available_file['url'],
                         headers=dict(API_KEY=self.api_key),
                         )
        for line in r.iter_lines(chunk_size=1024 * 32, decode_unicode=True):
            yield line
