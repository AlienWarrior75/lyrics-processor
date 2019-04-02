from AZLyrics import *
from DarkLyrics import *
from LyricsOnDemand import *
from GeniusLyrics import *
from PLyrics import *


class LyricsFactory(object):

    @staticmethod
    def build_lyrics_processor( type, artists_in_directory, path_to_music, album_name='' ):
        if type == 'DarkLyrics':
            return DarkLyrics( artists_in_directory, path_to_music, album_name )
        if type == 'GeniusLyrics':
            return GeniusLyrics( artists_in_directory, path_to_music )
        if type == 'LyricsOnDemand':
            return LyricsOnDemand( artists_in_directory, path_to_music )
        if type == 'AZLyrics':
            return AZLyrics( artists_in_directory, path_to_music )
        if type == 'PLyrics':
            return PLyrics( artists_in_directory, path_to_music )

        assert 0, 'No lyrics processor implemented: ' + type