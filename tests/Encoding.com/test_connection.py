import sys
sys.path.append('../')
from base import *

class TestEncodingConnection(BaseTest):
    """Test connection to encoding.com API"""
    userid = ""
    userkey = ""
    url = ""
    def setUp(self):
        """Set the encoding.com API connection auth."""
        setattr(self, 'userid', ENCODING_API_USER)
        setattr(self, 'userkey', ENCODING_API_KEY)
        setattr(self, 'url', ENCODING_API_URL)

    def tearDown(self):
        pass

    def test_encoding_connection(self):
        data = {'userid': getattr(self, 'userid'), 
                'userkey': getattr(self, 'userkey'),
                'action': 'GetMediaList'
        }
        d = {'query': data}
        termprint('ERROR', "%s%s" % (self.url, d))
        
        j = self.apicall(d)
        self.assertTrue(type(j) is dict)
        self.iter8(j)

        # print some extra shit
        for i in j.get('response').get('media'):
            for k, v in i.items():
                termprint('WARNING', '%s = %s' % (k, v))
            print "------------\n"


if __name__ == '__main__':
    unittest.main()
