xml_request="""<?xml version="1.0"?>

<query>

	<!-- Main fields -->
    
    <userid>[UserID]</userid>
    <userkey>[UserKey]</userkey>
    <action>[Action]</action>
    <mediaid>[MediaID]</mediaid>
    <source>[SourceFile]</source>
    <notify>[NotifyURL]</notify>
    
    <format>
    
		<!-- Format fields -->
        
        <output>[Output format]</output>
        <video_codec>[Video Codec]</video_codec>
        <audio_codec>[Audio Codec]</audio_codec>
        <bitrate>[Video bitrate]</bitrate>
        <audio_bitrate>[Audio bitrate]</audio_bitrate>
        <audio_sample_rate>[Audio quality]</audio_sample_rate>
        <audio_volume>[Volume]</audio_volume>
        <size>[Size]</size>
        <crop_left>[Crop Left]</crop_left>
        <crop_top>[Crop Top]</crop_top>
        <crop_right>[Crop Right]</crop_right>
        <crop_bottom>[Crop Bottom]</crop_bottom>
        <keep_aspect_ratio>[yes/no]</keep_aspect_ratio>
        <thumb_time>[Thumb time]</thumb_time>
        <thumb_size>[Thumb size]</thumb_size>
        <add_meta>[yes/no]</add_meta>
        
        <rc_init_occupancy>[RC Occupancy]</rc_init_occupancy>
        <minrate>[Min Rate]</minrate>
        <maxrate>[Max Rate]</maxrate>
        <bufsize>[RC Buffer Size]</bufsize>
        
        <keyframe>[Keyframe Period (GOP)]</keyframe>
        <start>[Start From]</start>
        <duration>[Result Duration]</duration>
        
		<!-- Metadata fields (OPTIONAL) -->
        <metadata>
                <title>[Title]</title>
                <copyright>[Copyright]</copyright>
                <author>[Author]</author>
                <description>[Description]</description>
                <album>[Album]</album>
        </metadata>
        
		<!-- Destination fields -->
        <destination>[DestFile]</destination>
        <thumb_destination>[Thumb Dest]</thumb_destination>
        
		<!-- Logo fields (OPTIONAL) -->
        <logo>
                <logo_source>[LogoURL]</logo_source>
                <logo_x>[LogoLeft]</logo_x>
                <logo_y>[LogoTop]</logo_y>
                <logo_mode>[LogoMode]</logo_mode>
                <logo_threshold>[LogoTreshold]</logo_threshold>
        </logo>
        
		<!-- Turbo Encoding switch (OPTIONAL) -->
        <turbo>[yes/no]</turbo>
    </format>

</query>
"""
