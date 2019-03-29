#!/usr/bin/env python

from ..common import *
import requests
from bs4 import BeautifulSoup
import re

def xp1024_download(url, output_dir = '.', merge = True, info_only = False, **kwargs):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    
    title = soup.title.text.split('|')[0]
    m3u8_url = 'https://m3u8.cdnpan.com/' + re.split(r'id=',soup.iframe.get('src'))[1]

    print_info(site_info, title, 'm3u8', 0, m3u8_url=m3u8_url)
    if not info_only:
        download_url_ffmpeg(m3u8_url, title, 'mp4', output_dir=output_dir, merge=merge)


site_info = "http://h3.cnmbtgf.info"
download = xp1024_download
download_playlist = playlist_not_supported('xp1024')
