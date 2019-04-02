# System Imports
from abc import abstractmethod

# Custom imports

# Super class of all Lyric Websites, contains common methods


class LyricsSite(object):

    def __init__(self, artists_in_directory, path_to_music ):
        self.artists_in_directory = artists_in_directory
        self.path_to_music = path_to_music

    @abstractmethod
    def process_lyrics(self):
        raise NotImplementedError()