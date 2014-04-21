import sys
sys.path.append('../../')
from termprint import *
#import xmltodict
#import xmldict

import simplejson
import os
import urllib
import httplib
import unittest
import requests

from settings import ENCODING_API_USER, ENCODING_API_KEY, \
                           VIDLY_API_USER, VIDLY_API_KEY, \
                           ENCODING_API_URL, SAMPLE_VIDEO, SAMPLE_VIDEO_DOWNLOAD, \
                           AMAZON_SECRET_ACCESS_KEY, AMAZON_ACCESS_KEY



class BaseTest(unittest.TestCase):
    """Base test for all tests"""
    def iter8(self, data, step=0):
        """recursive print"""
        for k, v in data.items():
            spacer = " " * step
            termprint('INFO', '%s%s' % (spacer, k))
            if type(v) is dict:
                self.iter8(v, step=(step+2))
            if type(v) is list:
                for i in v:
                    self.iter8(i, step=(step+4))

    def apicall(self, data):
        """Do the api call"""
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        params = urllib.urlencode({'json': simplejson.dumps(data)})
        path = ''
        # make the connection
        conn = httplib.HTTPConnection(self.url)
        conn.request('POST', path, params, headers)
        # get the response
        response = conn.getresponse()
        response_data = response.read()
        conn.close()
        # make the json dict response
        j = simplejson.loads(response_data)
        return j
