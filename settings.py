VIDLY_API_USER, VIDLY_API_KEY = None, None
ENCODING_API_USER, ENCODING_API_KEY = None, None

# selected url
ENCODING_API_URL = "manage.encoding.com:80"

# video used in testst 
SAMPLE_VIDEO = 'sample-video.mp4'

try:
    from local_settings import *
except ImportError:
    pass


