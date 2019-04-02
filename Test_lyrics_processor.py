# System Imports
import unittest

# Custom imports
from LyricsFactory import *
from Utils import *


class TestLyricsProcessors(unittest.TestCase):

    def test_AZLyrics_processor(self):
        lyrics_processors = [ 'AZLyrics' ]

        path_to_music = '/Users/user/Downloads/New Music/The Bouncing Souls - Crucial Moments (2019)/'

        artists_in_directory = Utils.list_songs_in_directory( path_to_music )
        Utils.remove_ds_store_files( artists_in_directory )

        for processor in lyrics_processors:
            factory = LyricsFactory.build_lyrics_processor( processor, artists_in_directory, path_to_music )
            factory.process_lyrics()

    def test_PLyrics_processor(self):
        lyrics_processors = [ 'PLyrics' ]

        path_to_music = '/Users/user/Downloads/New Music/Screeching Weasel - Carnival Of Schadenfreude (2011)/'

        artists_in_directory = Utils.list_songs_in_directory( path_to_music )
        Utils.remove_ds_store_files( artists_in_directory )

        for processor in lyrics_processors:
            factory = LyricsFactory.build_lyrics_processor( processor, artists_in_directory, path_to_music )
            factory.process_lyrics()

    def test_GeniusLyrics_processor(self):
        lyrics_processors = [ 'GeniusLyrics' ]

        path_to_music = '/Users/user/Downloads/New Music/Sublime With Rome - Sirens (2015)/'

        artists_in_directory = Utils.list_songs_in_directory( path_to_music )
        Utils.remove_ds_store_files( artists_in_directory )

        for processor in lyrics_processors:
            factory = LyricsFactory.build_lyrics_processor( processor, artists_in_directory, path_to_music )
            factory.process_lyrics()

    def test_LyricsOnDemand_processor(self):
        lyrics_processors = [ 'LyricsOnDemand' ]

        path_to_music = '/Users/user/Downloads/New Music/Screeching Weasel - Snappy Answers For Stupid Questions (1992)/'

        artists_in_directory = Utils.list_songs_in_directory( path_to_music )
        Utils.remove_ds_store_files( artists_in_directory )

        for processor in lyrics_processors:
            factory = LyricsFactory.build_lyrics_processor( processor, artists_in_directory, path_to_music )
            factory.process_lyrics()

    @unittest.skip( '2017-10-25: OpenDNS Blocking this website' )
    def test_DarkLyrics_processor(self):
        lyrics_processors = [ 'DarkLyrics' ]

        album_name = 'Searching For Zero'

        path_to_music = '/Users/user/Downloads/Process Lyrics/TestingLyricsProcessor/DarkLyricsTests/'

        artists_in_directory = Utils.list_songs_in_directory( path_to_music )
        Utils.remove_ds_store_files( artists_in_directory )

        for processor in lyrics_processors:
            factory = LyricsFactory.build_lyrics_processor( processor, artists_in_directory, path_to_music, album_name )
            factory.process_lyrics()