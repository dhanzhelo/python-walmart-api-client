WALMART_API_URL = 'http://api.walmartlabs.com/v1/%(api_call)s?apiKey=%(api_key)s&%(api_params)s'

WALMART_API_CALLS = {
    'search': 'search'
}

WALMART_API_FORMAT = {
    'json': 'json',
    'xml': 'xml'
}

WALMART_API_PARAMS = [
    'apiKey',
    'lsPublisherId',
    'query',
    'categoryId',
    'start',
    'sort',
    'order',
    'numItems',
    'format',
    'responseGroup',
    'facet',
    'facet.filter',
    'facet.range'
]

WALMART_API_STOCK = {
    'available': [
        u'Available',
        u'Limited Supply',
        u'Last few items'
    ],
    'not_available': [
        u'Not available'
    ]
}

WALMART_API_ERROR_CODES = {
    4001: 'Invalid request',
    4002: 'Invalid item Id',
    4003: 'Invalid category id',
    4005: 'Invalid start param',
    4007: 'Invalid response format',
    4008: 'Missing item id',
    4009: 'Missing search query',
    4010: 'Start index out of bounds',
    5000: 'Internal Server Error'
}

WALMART_API_HTTP_RESPONSE_CODES = {
    'success': {
        200: 'Ok',
        201: 'Ok - Created',
    },
    'error': {
        400: 'Bad Request',
        403: 'Forbidden',
        404: 'Wrong endpoint',
        414: 'Request URI too long',
        500: 'Internal Server Error',
        502: 'Bad Gateway',
        503: 'Service Unavailable/ API maintenance',
        504: 'Gateway Timeout'
    }
}
