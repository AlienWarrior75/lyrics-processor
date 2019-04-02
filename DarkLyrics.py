# System imports
import sys
import requests
from bs4 import BeautifulSoup
from mutagen.id3 import ID3
from mutagen import mp3
from mutagen import id3
import re

# Custom imports
from LyricsSite import *


# Full Albums Tested:
# Cancer Bats - Searching for Zero
# Killswitch Engage - Incarnate
#
# 2017-10-25: OpenDNS Blocking this website


class DarkLyrics(LyricsSite):

    URL = 'http://www.darklyrics.com/lyrics/'

    def __init__( self, artists_in_directory, path_to_music, album ):
        LyricsSite.__init__( self, artists_in_directory, path_to_music )
        self.album = album

    def process_lyrics( self ):

        # List all the test_songs in the song's directory
        for index, song_in_directory in enumerate( self.artists_in_directory ):
            print( index, song_in_directory )

            song_with_dash = re.sub( '.mp3', '', song_in_directory )
            print('Song With Dash: ' + song_with_dash )
            artist, song = song_with_dash.split( ' - ' )

            # Remove any special characters from the song name for AZLyrics using regex
            song_for_html = re.sub( '[^A-Za-z0-9 ]+', '', song )

            album_for_html = re.sub( '[^A-Za-z0-9 ]+', '', self.album )

            # Ensure we have parsed things correctly
            print( 'Artist: ' + artist, 'Song:' + song, 'Song For HTML: ' + song_for_html, 'Album for HTML: ' + album_for_html)

            # Prepare the artist and song for web scrape
            url_artist = ''.join( c.lower() for c in artist if not c.isspace() )
            print( 'URL Artist: ' + url_artist )

            url_song = ''.join( c.lower() for c in song_for_html if not c.isspace() )
            print( 'URL Song: ' + url_song )

            url_album = ''.join( c.lower() for c in album_for_html if not c.isspace() )
            print( 'URL Album: ' + url_album )

            # Lookup the url on DarkLyrics the format is /lyrics/artist/album.html
            # Songs are inline
            url = self.URL + url_artist + '/' + url_album + '.html'
            print( 'URL: ' + url )

            # User Agent
            headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
            MAX_RETRIES = 20
            session = requests.Session()
            adapter = requests.adapters.HTTPAdapter( max_retries=MAX_RETRIES )
            session.mount( 'https://', adapter )
            session.mount( 'http://', adapter )

            response = session.get( url, headers=headers )

            if not response.status_code == 200:
                session.close()
                sys.exit( response.status_code ) # TODO: Replace with exception

            print( response.content )
            # response = requests.get( url, headers=headers )

            # Parse the webpage
            page = BeautifulSoup( response.content, 'html.parser' )

            # Debugging the web parse
            # print( response.content )
            # print( page.prettify() )

            # Get the listing of test_songs of the album so we can determine the array limits
            album_listing_html = page.select( '#main > div.cntwrap > div > div.albumlyrics' )

            for j in album_listing_html:
                album_listing = j.get_text().splitlines()
                print( j.get_text() )

            # first element in the list is blank
            # Second element in the list is album name
            album_listing.pop(0)
            album_name = album_listing.pop(0)

            # This is specific to DarkLyrics
            # Get the lyrics from the web page
            # Dark Lyrics: #main > div.cntwrap > div > div.lyrics
            # This gets the lyrics for the whole album
            lyrics = page.select(
                '#main > div.cntwrap > div > div.lyrics' )
            # print(lyrics)

            # Clean the lyrics of HTML crap
            for i in lyrics:
                print( 'Lyrics Retrieved: ' + i.get_text() )
                clean_lyrics = i.get_text()

            # This regex will split the entire album lyrics into song chunks
            clean_lyrics_list = re.split("[0-9]{1,2}\. [a-zA-Z]+.*", clean_lyrics )

            if song in clean_lyrics:
                print( song )

            for i in clean_lyrics_list:
                print("Song: " + i )

            for i in range( len( album_listing ) ):
                print( album_listing[i] )

                if song in album_listing[i]:
                    song_lyrics = clean_lyrics_list.pop(i + 1)
                    print(song_lyrics)

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
                tag[ atom ].text = song_lyrics
                tag[ atom ].encoding = 1
                tag[ atom ].lang = "eng"
                tag[ atom ].desc = u""
            tag.save()
