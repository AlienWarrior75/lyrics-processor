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

# 2018-02-10 Changed Artist to include '-' between spaces in the name

# Full Albums Tested:
# Wu-Tang Clan - The Saga Continues
# Finch - Back to Oblivion
# Germs - The Complete Anthology (MIA)
# Kanye West - 808's & Heartbreak
# Kanye West - Graduation
# Devil You Know - The Beauty Of Destruction
# Kanye West - Late Registration
# Kanye West - The College Dropout
# Kanye West - My Beautiful Dark Twisted Fantasy
# Kanye West - Yeezus
# Kanye West – The Life Of Pablo
# Between The Buried And Me - Automata I
# Dandy Warhols - Distortland (2 songs missing)
# Descendents - Hypercaffium Spazzinate
# I Killed the Prom Queen - Beloved
# Ministry - AmeriKKKant
# Pennywise - Never Gonna Die
# Jay-Z - Reasonable Doubt
# Jay-Z - In My Lifetime, Volume 1
# Soulfly - Ritual
# Soulfly - Arcangel
# Drake - Views
# Architects - All Our Gods Have Abandoned Us
# Architects - Daybreaker
# Architects - Holy Hell
# Drake - More Life
# Cardi B - Invasion of Privacy
# Papa Roach - Crooked Teeth
# Papa Roach - Who Do You Trust
# The Used - The Canyon
# POD - Circles
# The Roots - ...and then you shoot your cousin
# Foo Fighters - Concrete and Gold
# A Day To Remember - Bad Vibrations
# Descendents - Who We Are 7 inch
# Faith No More - Sol Invictus
# The Distillers - Man Vs. Magnet, Blood In Gutters
# The Bouncing Souls - Simplicity

class GeniusLyrics(LyricsSite):

    URL = 'http://genius.com/'

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
            # url_artist = ''.join( c.lower() for c in artist if not c.isspace() )
            url_artist = artist.replace(' ', '-')
            print( 'URL Artist: ' + url_artist )

            # url_song = '-'.join( c.lower() for c in song_for_html if not c.isspace() )
            url_song = song_for_html.replace(' ', '-')
            print( 'URL Song: ' + url_song )

            # Lookup the url on Genius the format is /artist-song-name-lyrics
            url = self.URL + url_artist + '-' + url_song + '-lyrics'
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
                sys.exit( response.status_code )

            print( response.content )

            # Parse the webpage
            page = BeautifulSoup( response.content, 'html.parser' )
            # Locate on the GeniusLyrics page the actual content of the lyrics
            # This is specific to GeniusLyrics
            # Get the lyrics from the web page
            lyrics = page.findAll( "div", { "class": "song_body-lyrics" } )
            print(lyrics)

            # If the lyrics returned were empty, move to next song
            if not lyrics:
                continue

            for i in lyrics:
                web_page_clean_lyrics = i.get_text()

            print( web_page_clean_lyrics )

            # Remove 'More from Genius' tag
            removed_genius_lyrics = web_page_clean_lyrics.replace('More on Genius','')

            # Remove the Title of the song from the lyrics
            removed_title_lyrics = removed_genius_lyrics.replace(song + ' Lyrics','')

            # Remove leading carriage returns and blanks
            lstrip_lyrics = removed_title_lyrics.lstrip()

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
