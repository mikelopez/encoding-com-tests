import sys
sys.path.append('../')
from base import *
from xml_request import *

class TestXML2Dict(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_xml_to_dict(self):
        xml = """
<root xmlns="http://defaultns.com/"
      xmlns:a="http://a.com/"
      xmlns:b="http://b.com/">
  <x>1</x>
  <a:y>2</a:y>
  <b:z>3</b:z>
</root>
        """
        self.assertTrue(xmltodict.parse(xml, process_namespaces=True) == {
            'http://defaultns.com/:root': {
                'http://defaultns.com/:x': '1',
                'http://a.com/:y': '2',
                'http://b.com/:z': '3',
            }
        })

        x = xmltodict.parse(xml_request, process_namespaces=True)
        termprint('INFO', x)

if __name__ == '__main__':
    unittest.main()
