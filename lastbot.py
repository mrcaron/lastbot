import sys
import codecs

# your console needs to support utf8 encoding, otherwise, you'll get junk for the long dash that
# lastfm uses for artist/title seperation
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer, 'strict')

username = sys.argv[1]

import feedparser

feedurl = "http://ws.audioscrobbler.com/1.0/user/%s/recenttracks.rss" % username

feed = feedparser.parse( feedurl );

lasttitle = feed.entries[0].title
lastlink = feed.entries[0].link

print ("Mike's last track was: ", lasttitle, "(", lastlink, ")")
