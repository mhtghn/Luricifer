import os


class Sync(object):

    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.init_sync()

    def init_sync(self):
        if not os.path.exists('./synced'):
            os.makedirs('./synced')

    def save_synced_lyrics(self, synced_lyrics):
        if not os.path.exists('./synced/'+self.artist):
            os.makedirs('./synced/'+self.artist)
        file = open('./synced/'+self.artist+'/'+self.title+'.sync', 'w')
        file.write(synced_lyrics)
        file.close()

    def is_synced(self):
        return os.path.isfile('./synced/'+self.artist+'/'+self.title+'.sync')

    def get_synced_lyrics(self):
        file = open('./synced/' + self.artist + '/' + self.title + '.sync', 'r')
        synced_lyrics = file.read()
        return synced_lyrics