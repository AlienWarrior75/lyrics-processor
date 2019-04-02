# System imports
import sys
import requests
from bs4 import BeautifulSoup
from mutagen.id3 import ID3
from mutagen import mp3
from mutagen import id3
import re

# Custom imports
from Utils import *
from LyricsSite import *

# Tested Single songs:
# Chevelle - Joyride (Omen)
# Dandy Warhols - Everyday should be a holiday
# Badflower - Ghost

# Tested Full Albums:
# Every Time I Die - From Parts Unknown
# Haste the Day - Coward
# Foo Fighters - Concrete Gold
# Brand New - 3 Demos, Reworked EP
# A Tribe Called Quest - We Got It From Here... Thank you 4 Your Service
# Propagandhi - Victory Lap
# Killswitch Engage - Incarnate
# Hatebreed - The Concrete Confessional
# Avenged Sevenfold - The Stage
# Transplants - Take Cover EP
# Sam Roberts Band - Lo-Fantasy
# Face to Face - Protection
# Foo Fighters - Sonic Highways
# Green Day - Revolution Radio
# Eminem - Revival
# In Flames - Battles
# In Flames - Siren Charms
# Babymetal - Babymetal (contained Japanese characters in filenames and lyrics)
# Weezer - Everything Will Be Alright In The End
# Silverstein - I Am Alive In Everything I Touch
# Lagwagon - Hang
# Hellyeah - Blood for Blood
# Megadeth - Dystopia
# Refused - Freedom
# Korn - Serenity of Suffering
# Nine Inch Nails - Not the Actual Events
# NOFX - First Ditch Effort
# NOFX - Backstage Passport Soundtrack
# NOFX - I Heard They Suck Live!!
# NOFX - Stoke Extinguisher
# Ghost BC - Popestar EP
# Protest The Hero - Pacific Myth EP
# Parkway Drive - Reverence
# Our Last Night - Younger Dreams
# Our Last Night - Selective Hearing EP
# A Perfect Circle - Eat the Elephant
# Nine Inch Nails - Bad Witch
# Drake - Scorpion
# Between the Buried and Me - Automata II
# Eminem - Kamikaze
# Lil Wayne - Tha Block Is Hot
# Lil Wayne - Lights Out
# Lil Wayne - 500 Degreez
# Lil Wayne - Tha Carter I
# Lil Wayne - Tha Carter II
# Lil Wayne - Tha Carter III
# Lil Wayne - Tha Carter IV Deluxe Edition
# Lil Wayne - Tha Carter V
# Atreyu - In Our Wake
# Alice In Chains - Rainer Fog
# Alkaline Trio - Is this thing cursed?
# Nicki Minaj - Pink Friday
# Nicki Minaj - Pinkprint
# Weezer - The Teal Album
# The Flatliners - Dead Language
# The Flatliners - Mass Candescence EP
# The Flatliners - Division of Spoils
# The Flatliners - Cynics EP
# New Found Glory - From The Screen To Your Stereo Part I
# New Found Glory - From The Screen To Your Stereo Part II
# NOFX - Hepatitis Bathtub 7 inch
# Architects - Hollow Crown
# Architects - Lost Forever Lost Together
# Architects - Nightmares
# Architects - Ruin
# Architects - The Here And Now
# In Flames - I, The Mask
# Children of Bodom - Hexed (Deluxe Version)
# Descendents - SpazzHazard
# Faith No More - Sol Invictus
# New Found Glory - Makes Me Sick Again
# Jimmy Eat World - Integrity Blues
# Pennywise - Yesterdays
# The Offspring - Days Go By
# Refused - Servants of Death EP
# Violent Soho - Hungry Ghost
# Violent Soho - Waco
# Propagandhi - The Recovered EP
# Propagandhi - Sacrifice Split 7"
# Propagandhi - FYP Split 7"
# Weezer - The White Album
# Weezer - The Black Album
# Weezer - Pacific Daydream
# Hellyeah - 333
# Hellyeah - Band of Brothers
# Hellyeah - Unden!Able
# Hot Water Music/The Bouncing Souls - Tour Split EP
# The Bouncing Souls - Menzingers Split EP
# Our Last Night - Let Light Overcome EP
# The Bouncing Souls - Crucial Moments EP



class AZLyrics(LyricsSite):

    URL = 'http://www.azlyrics.com/lyrics/'

    def process_lyrics( self ):

        # List all the test_songs in the song's directory
        for index, song_in_directory in enumerate( self.artists_in_directory ):
            print( index, song_in_directory )

            song_with_dash = re.sub( Utils.MP3, '', song_in_directory )
            print('Song With Dash: ' + song_with_dash )
            artist, song = song_with_dash.split( ' - ' )

            # Remove any special characters from the song name for AZLyrics using regex
            song_for_html = re.sub( '[^A-Za-z0-9 ]+', '', song )

            # Ensure we have parsed things correctly
            print( 'Artist: ' + artist, 'Song:' + song, 'Song For HTML: ' + song_for_html )

            # Prepare the artist and song for web scrape
            url_artist = ''.join( c.lower() for c in artist if not c.isspace() )
            print( 'URL Artist: ' + url_artist )

            url_song = ''.join( c.lower() for c in song_for_html if not c.isspace() )
            print( 'URL Song: ' + url_song )

            # Lookup the url on AZLyrics the format is /lyrics/artist/song.html
            url = self.URL + url_artist + '/' + url_song + '.html'
            print( 'URL: ' + url )

            # User Agent
            headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

            response = requests.get( url, headers=headers )

            if not response.status_code == 200:
                sys.exit( response.status_code )

            # Parse the web page
            page = BeautifulSoup( response.content, 'html.parser' )

            # Debugging the web parse
            # print( response.content )
            # print( page.prettify() )

            # This is specific to AZLyrics
            # Get the lyrics from the web page
            lyrics = page.select(
                'body > div.container.main-page > div > div.col-xs-12.col-lg-8.text-center > div:nth-of-type(5)' )
            # print(lyrics)

            # Clean the lyrics and prepare to update mp3 file
            for i in lyrics:
                print( 'Lyrics Retrieved: ' + i.get_text() )
                clean_lyrics = i.get_text()

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
