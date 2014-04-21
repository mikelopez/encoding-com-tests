import sys
sys.path.append('../')
from base import *

class TestEncodingJob(BaseTest):
    """Test connection to encoding.com API"""
    userid = ""
    userkey = ""
    url = ""
    source = ""
    video = ""
    format = {}
    query = {'userid': ENCODING_API_USER, 
                'userkey': ENCODING_API_KEY,
                'action': '',
                'source': [],
                'notify': '',
                'instant': 'no',
                'format': {}}

    def setUp(self):
        """Set the encoding.com API connection auth."""
        setattr(self, 'userid', ENCODING_API_USER)
        setattr(self, 'userkey', ENCODING_API_KEY)
        setattr(self, 'url', ENCODING_API_URL)
        setattr(self, 'source', SAMPLE_VIDEO_DOWNLOAD)
        setattr(self, 'video', SAMPLE_VIDEO)

    def tearDown(self):
        pass

    def test_addmedia(self):
        """Create an encoding job
        Requires 
        - source
        - format
        - action AddMedia
        """
        s3 = "%s:%s" % (urllib.quote_plus(AMAZON_ACCESS_KEY), \
                        urllib.quote_plus(AMAZON_SECRET_ACCESS_KEY))
        s3auth = s3
        print s3auth
        format = {
            'keep_aspect_ratio': 'yes',
            'output': 'vidly'

        }
        formatmp4 = {
            'output': 'mp4',
            'keep_aspect_ratio': 'yes',
            'destination': \
                    'http://%s@bd-encode-finish.s3.amazonaws.com/' % (s3auth)}
        formatpic = {
            'output': 'thumbnail',
            'destination': \
                    'http://%s@bd-encode-finish.s3.amazonaws.com/' % s3auth}

        self.query['action'] = 'AddMedia'
        self.query['source'] = [self.source]
        self.query['video'] = 'sample-video.mp4'
        self.query['format'] = [format, formatmp4, formatpic]
        
        d = {'query': self.query}
        print "%s%s" % (self.url, d)
        j = self.apicall(d)
        self.assertTrue(type(j) is dict)
        self.iter8(j)

        for i in j.get('response', []):
            #print termprint('WARNING', '%s = %s' % (k, v))
            print "%s = %s" % (i, j.get('response').get(i))


if __name__ == '__main__':
    unittest.main()
