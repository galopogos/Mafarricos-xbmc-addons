# Addons resolver
# This program is free software; you can redistribute it and/or modify
# it under the terms of version 2 of the GNU General Public License as
# published by the Free Software Foundation.
# MafaStudios@gmail.com

class link:
	def __init__(self):
		import base64
		self.rato_id = 'plugin.video.ratotv'		
		self.rato_base = base64.urlsafe_b64decode('aHR0cDovL3d3dy5yYXRvdHYubmV0LyVz')
		self.rato_play = base64.urlsafe_b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnJhdG90di8/dXJsPSVzJm1vZGU9NDQmbmFtZT0lcw==')
		self.rato_search = self.rato_base % base64.urlsafe_b64decode('P2RvPXNlYXJjaCZzdWJhY3Rpb249c2VhcmNoJnNlYXJjaF9zdGFydD0xJnN0b3J5PSVz')	
		self.genesis_id = 'plugin.video.genesis'		
		self.genesis_play = base64.urlsafe_b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLmdlbmVzaXMvP2FjdGlvbj1wbGF5Jm5hbWU9JXMmdGl0bGU9JXMmeWVhcj0lcyZpbWRiPSVzJnVybD0lcw==')
		self.sdp_id = 'plugin.video.Sites_dos_Portugas'
		self.sdp_search = base64.urlsafe_b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLlNpdGVzX2Rvc19Qb3J0dWdhcy8/dXJsPUlNREIlc0lNREImbW9kZT05MDAwJm5hbWU9JXMmYXV0b21hdGljbz0lcw==')
		self.sdp_search_add = []
		self.sdp_search_add.append(base64.urlsafe_b64decode('aHR0cDovL3d3dy50dWdhLWZpbG1lcy5pbmZvL3NlYXJjaD9xPSVz'))
		self.sdp_search_add.append(base64.urlsafe_b64decode('aHR0cDovL3d3dy5jaW5lbWF0dWdhLmV1L3NlYXJjaD9xPSVz'))
		self.sdp_search_add.append(base64.urlsafe_b64decode('aHR0cDovL3d3dy50dWdhLWZpbG1lcy51cy9zZWFyY2g/cT0lcw=='))
		self.sdp_search_add.append(base64.urlsafe_b64decode('aHR0cDovL2ZvaXRhdHVnYWNpbmVtYW9ubGluZS5ibG9nc3BvdC5wdC9zZWFyY2g/cT0lcw=='))
		self.sdp_search_add.append(base64.urlsafe_b64decode('aHR0cDovL3d3dy5tb3ZpZS10dWdhLmJsb2dzcG90LnB0L3NlYXJjaD9xPSVz'))
		self.sdp_search_add.append(base64.urlsafe_b64decode('aHR0cDovL3d3dy5jaW5lbWFlbWNhc2EucHQvc2VhcmNoP3E9JXM='))
		self.sdp_search_add.append(base64.urlsafe_b64decode('aHR0cDovL3RvcHB0Lm5ldC8/cz0lcw=='))
		self.wt_id = 'plugin.video.wt'
		self.wt_base = base64.urlsafe_b64decode('aHR0cDovL3d3dy53YXJlenR1Z2EudHYvJXM=')
		self.wt_play = base64.urlsafe_b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnd0Lz91cmw9JXMmbW9kZT01Jm5hbWU9JXM=')
		self.wt_search = base64.urlsafe_b64decode('aHR0cDovL3d3dy53YXJlenR1Z2EudHYvcGFnaW5hdGlvbi5hamF4LnBocD9wPTEmb3JkZXI9ZGF0ZSZ3b3Jkcz0lcyZtZWRpYVR5cGU9bW92aWVz')
		self.yts_search = base64.urlsafe_b64decode('aHR0cHM6Ly95dHMucmUvYXBpL2xpc3RpbWRiLmpzb24/aW1kYl9pZD0lcw==')
		self.kmediatorrent_id = 'plugin.video.kmediatorrent'
		self.kmediatorrent_play = base64.urlsafe_b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLmttZWRpYXRvcnJlbnQvcGxheS8lcw==')
		self.stream_id = 'plugin.video.stream'
		self.stream_play = base64.urlsafe_b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnN0cmVhbS9wbGF5LyVz')
		self.ice_id = 'plugin.video.icefilms'
		self.ice_base = base64.urlsafe_b64decode('aHR0cDovL3d3dy5pY2VmaWxtcy5pbmZv')
		self.ice_play = base64.urlsafe_b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLmljZWZpbG1zLz9tb2RlPTEwMCZ1cmw9JXM=')
		self.salts_id = 'plugin.video.salts'
		self.salts_play = base64.urlsafe_b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnNhbHRzLz90aXRsZT0lcyZ2aWRlb190eXBlPU1vdmllJm1vZGU9Z2V0X3NvdXJjZXMmZGlhbG9nPVRydWUmeWVhcj0lcyZzbHVnPSVz')
		
		self.abelhas_id = 'plugin.video.abelhas'
		self.abelhas_search = base64.urlsafe_b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLmFiZWxoYXMvP21vZGU9MjMmdXJsPWh0dHA6Ly9hYmVsaGFzLnB0L2FjdGlvbi9TZWFyY2hGaWxlcyZuYW1lPSVz')
		self.abelhas_ref_data = base64.urlsafe_b64decode('eydIb3N0JzogJ2FiZWxoYXMucHQnLCAnQ29ubmVjdGlvbic6ICdrZWVwLWFsaXZlJywgJ1JlZmVyZXInOiAnaHR0cDovL2FiZWxoYXMucHQvJywnQWNjZXB0JzogJ3RleHQvaHRtbCxhcHBsaWNhdGlvbi94aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3E9MC45LGltYWdlL3dlYnAsKi8qO3E9MC44JywnVXNlci1BZ2VudCc6J01vemlsbGEvNS4wIChXaW5kb3dzIE5UIDYuMSkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzI4LjAuMTQ2OC4wIFNhZmFyaS81MzcuMzYnLCdSZWZlcmVyJzogJ2h0dHA6Ly9hYmVsaGFzLnB0Lyd9')
		self.abelhas_endlogin = base64.urlsafe_b64decode('aHR0cDovL2FiZWxoYXMucHQvYWN0aW9uL1NlYXJjaEZpbGVz')
		self.abelhas_formcont = base64.urlsafe_b64decode('eydzdWJtaXRTZWFyY2hGaWxlcyc6ICdQcm9jdXJhcicsICdGaWxlVHlwZSc6ICd2aWRlbycsICdJc0dhbGxlcnknOiAnRmFsc2UnLCAnRmlsZU5hbWUnOiAlc30=')
		
		self.yify_id = 'plugin.video.yifymovies.hd'
		self.yify_play = base64.urlsafe_b64decode('cGx1Z2luOi8vcGx1Z2luLnZpZGVvLnlpZnltb3ZpZXMuaGQvP2FjdGlvbj1wbGF5Jm5hbWU9JXMmdXJsPSVz')
		self.yify_search = base64.urlsafe_b64decode('aHR0cDovL3lpZnkudHYvP3M9JXM=')