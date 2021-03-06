﻿# -*- coding: UTF-8 -*-
# by Mafarricos
# email: MafaStudios@gmail.com
# This program is free software: GNU General Public License
import os,urllib
import links
from resources.libs import basic

def createstrm(name,imdbid,year,url):
	addon_id = links.link().salts_id
	addon_path = os.path.join(links.link().installfolder,addon_id)
	addon_getsettings = links.link().getSetting("salts_enabled")
	addon_pos = links.link().getSetting("salts_pos")
	if len(addon_pos) == 1: addon_pos = '0'+addon_pos
	srtmBasePath = links.link().strmPath
	addonplay = links.link().salts_play
	
	if not os.path.exists(addon_path) and addon_getsettings == 'true': links.link().setSetting("salts_enabled",'false')
	if addon_getsettings == 'true':
		strmPath = os.path.join(srtmBasePath,addon_pos+'.'+addon_id+'.strm')
		playurl = addonplay % (urllib.quote_plus(name),year,urllib.quote_plus(name).replace('+','-')+'-'+year)
		basic.writefile(strmPath,'w',playurl)