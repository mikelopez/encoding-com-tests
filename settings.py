VIDLY_API_USER, VIDLY_API_KEY = None, None
ENCODING_API_USER, ENCODING_API_KEY = None, None

# selected url
ENCODING_API_URL = "http://manage.encoding.com/?json="

try:
    from local_settings import *
except ImportError:
    pass


