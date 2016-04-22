from .config import WALMART_API_ERROR_CODES

__all__ = [
    'WalmartAPIError',
    'WalmartAPINetworkError',
    'WalmartAPICallErrorInvalidRequest',
    'WalmartAPICallErrorInvalidItemId',
    'WalmartAPICallErrorInvalidCategoryId',
    'WalmartAPICallErrorInvalidStartParam',
    'WalmartAPICallErrorInvalidResponseFormat',
    'WalmartAPICallErrorMissingItemId',
    'WalmartAPICallErrorMissingSearchQuery',
    'WalmartAPICallErrorStartIndexOutOfBounds'
]


class WalmartAPIError(Exception):
    def __init__(self, *args, **kwargs):
        super(WalmartAPIError, self).__init__()
        self.args = args
        self.code = kwargs.pop('code', None)
        self.msg = kwargs.pop('msg', None)

    def __str__(self):  # pragma: no cover
        if self.code is not None and self.msg is None:
            return 'Walmart API error: %(msg)s (%(code)s)' % self.__dict__
        return Exception.__str__(self)


class WalmartAPICallErrorInvalidRequest(WalmartAPIError):
    def __init__(self, *args, **kwargs):
        super(WalmartAPIError, self).__init__()
        self.msg = kwargs.pop('msg', WALMART_API_ERROR_CODES[4001])

    def __str__(self):
        return 'Walmart API error: %(msg)s' % self.__dict__


class WalmartAPICallErrorInvalidItemId(WalmartAPIError):
    def __init__(self, *args, **kwargs):
        super(WalmartAPIError, self).__init__()
        self.msg = kwargs.pop('msg', WALMART_API_ERROR_CODES[4002])

    def __str__(self):
        return 'Walmart API error: %(msg)s' % self.__dict__


class WalmartAPICallErrorInvalidCategoryId(WalmartAPIError):
    def __init__(self, *args, **kwargs):
        super(WalmartAPIError, self).__init__()
        self.msg = kwargs.pop('msg', WALMART_API_ERROR_CODES[4003])

    def __str__(self):
        return 'Walmart API error: %(msg)s' % self.__dict__


class WalmartAPICallErrorInvalidStartParam(WalmartAPIError):
    def __init__(self, *args, **kwargs):
        super(WalmartAPIError, self).__init__()
        self.msg = kwargs.pop('msg', WALMART_API_ERROR_CODES[4005])

    def __str__(self):
        return 'Walmart API error: %(msg)s' % self.__dict__


class WalmartAPICallErrorInvalidResponseFormat(WalmartAPIError):
    def __init__(self, *args, **kwargs):
        super(WalmartAPIError, self).__init__()
        self.msg = kwargs.pop('msg', WALMART_API_ERROR_CODES[4007])

    def __str__(self):
        return 'Walmart API error: %(msg)s' % self.__dict__


class WalmartAPICallErrorMissingItemId(WalmartAPIError):
    def __init__(self, *args, **kwargs):
        super(WalmartAPIError, self).__init__()
        self.msg = kwargs.pop('msg', WALMART_API_ERROR_CODES[4008])

    def __str__(self):
        return 'Walmart API error: %(msg)s' % self.__dict__


class WalmartAPICallErrorMissingSearchQuery(WalmartAPIError):
    def __init__(self, *args, **kwargs):
        super(WalmartAPIError, self).__init__()
        self.msg = kwargs.pop('msg', WALMART_API_ERROR_CODES[4009])

    def __str__(self):
        return 'Walmart API error: %(msg)s' % self.__dict__


class WalmartAPICallErrorStartIndexOutOfBounds(WalmartAPIError):
    def __init__(self, *args, **kwargs):
        super(WalmartAPIError, self).__init__()
        self.msg = kwargs.pop('msg', WALMART_API_ERROR_CODES[4010])

    def __str__(self):
        return 'Walmart API error: %(msg)s' % self.__dict__


class WalmartAPINetworkError(WalmartAPIError):
    def __init__(self, *args, **kwargs):
        super(WalmartAPIError, self).__init__()
        self.msg = 'Walmart API Unknown Error'

    def __str__(self):  # pragma: no cover
        return 'Walmart API error: %(msg)s' % self.__dict__


