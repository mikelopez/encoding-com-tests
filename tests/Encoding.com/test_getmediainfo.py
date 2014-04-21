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

    def test_getmediainfo(self):
        mediaid = raw_input('Enter media id: ')
        data = {'userid': getattr(self, 'userid'), 
                'userkey': getattr(self, 'userkey'),
                'action': 'GetMediaInfo',
                'mediaid': mediaid
        }
        d = {'query': data}
        print "%s%s" % (self.url, d)
        
        # make api call and get teh json data return
        j = self.apicall(d)
        self.assertTrue(type(j) is dict)
        self.iter8(j)

        for i in j.get('response'):
            #print termprint('WARNING', '%s = %s' % (k, v))
            print "%s = %s" % (i, j.get('response').get(i))


if __name__ == '__main__':
    unittest.main()
