import sys
import codecs

import pylast

API_KEY = 'ad91af6726dffe8181e71f7af9b66893'

# your console needs to support utf8 encoding, otherwise, you'll get junk for the long dash that
# lastfm uses for artist/title seperation
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer, 'strict')

username = sys.argv[1]
password = sys.argv[2]
secret = sys.argv[3]

network = pylast.LastFMNetwork(
    api_key = API_KEY,
    api_secret = secret,
    username = username,
    password_hash = pylast.md5(password))

user = network.get_user(username)
current = user.get_recent_tracks()[0]
url = current.track.get_url()
trackname = current.track.get_name()
artist = current.track.get_artist().get_name()
album = current.album

print ("%s listening to: %s %s - %s" % (username, artist, trackname, url))
