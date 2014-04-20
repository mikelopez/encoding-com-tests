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
		d = urllib.urlencode(data)
		print "%s%s" % (self.url, d)
		
		headers = {'content-type': 'application/x-www-form-urlencoded'}
		r = requests.post(self.url, headers=headers)
		print r.text

		params = urllib.urlencode({'xml':etree.tostring(xml)})

        conn = httplib.HTTPConnection(self.url)
        conn.request(method, path, params, headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        
		#termprint('INFO', r.json())


if __name__ == '__main__':
	unittest.main()