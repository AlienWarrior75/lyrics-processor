# System imports
import sys
import requests
from bs4 import BeautifulSoup
from mutagen.id3 import ID3
from mutagen import mp3
from mutagen import id3
import re

# Custom Imports
from LyricsSite import *
from Utils import *

# Full Albums Tested:
# Rancid - Honor is all we know
# NOFX - They've Actually Gotten Worse Live!


class PLyrics(LyricsSite):

    URL = 'http://www.plyrics.com/lyrics/'

    def process_lyrics(self):
        # List all the test_songs in the song's directory
        for index, song_in_directory in enumerate( self.artists_in_directory ):
            print( index, song_in_directory )

            song_with_dash = re.sub( Utils.MP3, '', song_in_directory )
            print('Song With Dash: ' + song_with_dash )
            artist, song = song_with_dash.split( ' - ' )

            # Remove any special characters from the song name for PLyrics using regex
            song_for_html = re.sub( '[^A-Za-z0-9 ]+', '', song )

            # Ensure we have parsed things correctly
            print( 'Artist: ' + artist, 'Song:' + song, 'Song For HTML: ' + song_for_html )

            # Prepare the artist and song for web scrape
            url_artist = ''.join( c.lower() for c in artist if not c.isspace() )
            print( 'URL Artist: ' + url_artist )

            url_song = ''.join( c.lower() for c in song_for_html if not c.isspace() )
            print( 'URL Song: ' + url_song )

            # Lookup the url on PLyrics the format is /lyrics/artist/song.html
            url = self.URL + url_artist + '/' + url_song + '.html'
            print( 'URL: ' + url )

            # User Agent
            headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

            response = requests.get( url, headers=headers )

            if not response.status_code == 200:
                sys.exit( response.status_code )

            # Parse the webpage
            page = BeautifulSoup( response.content, 'html.parser' )

            # Locate on the PLyrics page the actual content of the lyrics
            content_to_remove = page.findAll( "div", { "class": "content_lyr" } )

            # Remove all scripts, a hrefs, h1, h3 and p tags from the page/soup
            # Javascripts
            for content_to_remove in page( 'script' ):
                text0 = content_to_remove.extract()
            # Ahrefs (links)
            for content_to_remove in page( 'a' ):
                text1 = content_to_remove.extract()

            # Header1 -- this is the title of the song
            for content_to_remove in page( 'h1' ):
                text2 = content_to_remove.extract()

            # Header3 -- This is the band name
            for content_to_remove in page( 'h3' ):
                text3 = content_to_remove.extract()

            # Header4 -- Thanks to name for adding/correcting these lyrics
            for content_to_remove in page( 'h4' ):
                text4 = content_to_remove.extract()

            # Various paragraphs from the page
            for content_to_remove in page( 'p' ):
                text5 = content_to_remove.extract()

            # This is specific to PLyrics
            # body > div:nth-child(1) > div.sheet > div.content_lyr > <!-- start of lyrics -->
            # Get the lyrics from the web page
            lyrics = page.select(
                'body > div:nth-of-type(1) > div.sheet > div.content_lyr ' )

            # If the lyrics returned were empty, move to next song
            if not lyrics:
                continue

            for i in lyrics:
                web_page_clean_lyrics = i.get_text()

            # Remove leading carriage returns and blanks
            lstrip_lyrics = web_page_clean_lyrics.lstrip()
            # Remove trailing carriage returns and blanks
            clean_lyrics = lstrip_lyrics.rstrip()
            print( 'Lyrics Retrieved: ' + clean_lyrics )

            # Reference the filename in to be updated
            song_file = self.path_to_music + artist + ' - ' + song + '.mp3'
            print( 'Song File: ' + song_file )

            # Get the ID3 metadata from the physical file
            song_id3 = ID3( song_file )
            tag = mp3.MP3( song_file )
            print( tag )

            # Update the Lyrics tag in the ID3 tags
            atom = u"USLT::'eng'"
            if lyrics is None:
                if atom in tag: del tag[ atom ]
            else:
                tag[ atom ] = id3.USLT()
                tag[ atom ].text = clean_lyrics
                tag[ atom ].encoding = 1
                tag[ atom ].lang = "eng"
                tag[ atom ].desc = u""
            tag.save()
