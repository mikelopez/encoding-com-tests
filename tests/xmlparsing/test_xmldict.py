import sys
sys.path.append('../')
from base import *
from xml_request import *

class TestXMLDict(BaseTest):
    """Testing the xmldict library"""
    xml_data = xml_request
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_xmldict(self):
        """Test xmldict creating xml string from a dict and vice versa"""
        xml = self.xml_data
        from_string = xmldict.xml_to_dict(xml)

        d = {'contact': {'fname': 'Joe', 'lname': 'Smith'},
             'query': {'field': 'ass', 'where': 'ass'}}

        from_dict = xmldict.dict_to_xml(d)

        # print the dict created from xml string
        termprint('INFO', from_string)

        # print the xml string created from dict
        termprint('WARNING', from_dict)


if __name__ == '__main__':
    unittest.main()
