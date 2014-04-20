import sys
sys.path.append('../')
from base import *


class TestGetMediaInfoResponse(BaseTest):
    """Testing the GetMediaInfo API Response from encoding.com"""
    xml_data = ""
    def setUp(self):
        self.xml_data = {
            "response": {
                "bitrate": "1807k",
                "duration": "6464.83",
                "audio_bitrate": "128k",
                "video_codec": "mpeg4",
                "video_bitrate": "1679k",
                "frame_rate": "23.98",
                "size": "640x352",
                "pixel_aspect_ratio": "1:1",
                "display_aspect_ratio": "20:11",
                "audio_codec": "ac3",
                "audio_sample_rate": "48000",
                "audio_channels": "2"
            }
        }

    def tearDown(self):
        pass

    

    def test_getmediainfo_response(self):
        """Test xmldict creating xml string from a dict and vice versa"""
        
        # print the dictionary from xml string
        termprint('WARNING', self.xml_data)
        self.iter8(self.xml_data)



if __name__ == '__main__':
    unittest.main()
