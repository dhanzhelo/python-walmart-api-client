import json
import logging
import urllib
from .errors import *
from .config import WALMART_API_HTTP_RESPONSE_CODES, WALMART_API_URL, WALMART_API_CALLS, WALMART_API_FORMAT, \
    WALMART_API_PARAMS

LOGGER = logging.getLogger(__name__)


class WalmartApiClient(object):
    def __init__(self, api_key, call_format=None):
        self.api_key = api_key
        if call_format is None:
            self.call_format = WALMART_API_FORMAT['json']

    def search(self, params):
        result = self.call(WALMART_API_CALLS['search'], params)

        return result

    def get_call_url(self, call, params):
        return WALMART_API_URL % {
            'api_call': WALMART_API_CALLS[call],
            'api_key': self.api_key,
            'api_params': self.get_call_params(params)
        }

    @classmethod
    def get_call_params(cls, params):
        request_params = []
        for param_key, param_value in params.items():
            if param_key in WALMART_API_PARAMS:
                request_params.append(param_key + '=' + unicode(param_value))
            else:
                raise ValueError('Parameter %s must be in %s' % (param_key, str(WALMART_API_PARAMS)))

        return '&'.join(request_params)

    def call(self, call, params):
        url = self.get_call_url(call, params)
        LOGGER.info('Perform Walmart API request url: %s' % url)
        response = urllib.urlopen(url)

        if response.code in WALMART_API_HTTP_RESPONSE_CODES['success'].keys():

            return json.loads(response.read())

        elif response.code in WALMART_API_HTTP_RESPONSE_CODES['error'].keys():
            if response.code == 4001:
                raise WalmartAPICallErrorInvalidRequest()
            if response.code == 4002:
                raise WalmartAPICallErrorInvalidItemId()
            if response.code == 4003:
                raise WalmartAPICallErrorInvalidCategoryId()
            if response.code == 4005:
                raise WalmartAPICallErrorInvalidStartParam()
            if response.code == 4007:
                raise WalmartAPICallErrorInvalidResponseFormat()
            if response.code == 4008:
                raise WalmartAPICallErrorMissingItemId()
            if response.code == 4009:
                raise WalmartAPICallErrorMissingSearchQuery()
            if response.code == 4010:
                raise WalmartAPICallErrorStartIndexOutOfBounds()
        else:
            raise WalmartAPINetworkError()
