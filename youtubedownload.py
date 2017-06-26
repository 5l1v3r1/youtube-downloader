#!/usr/bin/env python

# Youtube video download script
 
from urllib import urlopen
import sys
 
print "\n--------------------------"
print " Youtube Video Downloader"
print "--------------------------\n"
 
try:
        video_url = sys.argv[1]
except:
        video_url = raw_input('[+] Enter video URL: ')
 
print "[+] Connecting..."
try:
        if(video_url.endswith('&feature=related')):
                video_id = video_url.split('www.youtube.com/watch?v=')[1].split('&feature=related')[0]
        elif(video_url.endswith('&feature=dir')):
                video_id = video_url.split('www.youtube.com/watch?v=')[1].split('&feature=dir')[0]
        elif(video_url.endswith('&feature=channel_page')):
                video_id = video_url.split('www.youtube.com/watch?v=')[1].split('&feature=channel_page')[0]
        else:
                video_id = video_url.split('www.youtube.com/watch?v=')[1]
except:
        print "[-] Invalid URL."
        exit(1)
 
print "[+] Parsing token..."
try:
        url = urlopen('http://www.youtube.com/watch?v=' + video_id + '&fmt=18').read()
        token_value = url.split('&t=')[1].split('&plid=')[0]
 
        download_url = "http://www.youtube.com/get_video?video_id=" + video_id + "&t=" + token_value + "&fmt=18"
except:
        print "[-] Error parsing token. Quitting."
        exit(1)
 
video_title = url.split('<title>YouTube - ')[1].split('</title>')[0]
if '&quot;' in video_title:
        video_title = video_title.replace('&quot;','"')
elif '&amp;' in video_title:
        video_title = video_title.replace('&amp;','&')
 
print "[+] Downloading " + '"' + video_title + '"...'
try:
        file = open(video_title + '.mp4', 'wb')
        download = urlopen(download_url)
        for line in download:
                file.write(line)
        file.close()
except:
        print "[-] Error downloading. Quitting."
        exit(1)
 
print "\n[+] Done. The video is saved on your desktop.\n"