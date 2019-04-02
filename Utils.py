# System imports
import os


class Utils(object):
    # Global variables
    MP3 = ".mp3"

    @staticmethod
    def list_songs_in_directory( path_to_music ):
        # List the files in the chosen directory
        artists_in_directory = os.listdir( path_to_music )
        artists_in_directory = Utils.filter_only_mp3_files( artists_in_directory )
        print( artists_in_directory )

        return artists_in_directory

    @staticmethod
    def remove_ds_store_files( artists_in_directory ):
        # List of all types of undesirable files
        ds_store = '.DS_Store'

        # Remove files that don't belong
        if ds_store in artists_in_directory:
            artists_in_directory.remove( ds_store )

    @staticmethod
    def filter_only_mp3_files( artists_in_directory ):

        for song in artists_in_directory:
            if not song.endswith( Utils.MP3 ):
                artists_in_directory.remove( song )

        return artists_in_directory
