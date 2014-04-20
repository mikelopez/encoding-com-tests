import sys
sys.path.append('../../')
from termprint import *
#import xmltodict
#import xmldict

import simplejson
import os
import urllib
import unittest
import requests

from settings import ENCODING_API_USER, ENCODING_API_KEY, \
                           VIDLY_API_USER, VIDLY_API_KEY, \
                           ENCODING_API_URL



class BaseTest(unittest.TestCase):
    """Base test for all tests"""
    def iter8(self, data, step=0):
        """recursive print"""
        for k, v in data.items():
            spacer = " " * step
            termprint('INFO', '%s%s' % (spacer, k))
            if type(v) is dict:
                self.iter8(v, step=(step+2))