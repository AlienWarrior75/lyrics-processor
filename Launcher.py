# Custom imports
from LyricsFactory import *
from Utils import *


# This class will invoke the LyricsProcessor program, passing a list of songs and passes to individual web scrapers
class Launcher(object):

    @staticmethod
    def start_process():
        lyrics_processors = [ 'GeniusLyrics', 'DarkLyrics', 'AZLyrics', 'LyricsOnDemand', 'PLyrics' ]

        # List the files in the chosen directory
        path_to_music = '/Users/rallaby/Downloads/Process Lyrics/Wu-Tang Clan - The Saga Continues/'

        artists_in_directory = Utils.list_songs_in_directory( path_to_music )
        Utils.remove_ds_store_files( artists_in_directory )

        for processor in lyrics_processors:
            factory = LyricsFactory.build_lyrics_processor( processor, artists_in_directory, path_to_music )
            factory.process_lyrics()


if __name__ == '__main__':
    Launcher.start_process()
