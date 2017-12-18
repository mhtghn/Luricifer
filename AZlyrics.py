import sys, re
from urllib import request, error
from bs4 import BeautifulSoup


class Azlyrics(object):

    def __init__(self, artist, music):
        self.artist = artist
        self.music = music

    def normalize_str(self, str):
        return re.sub(r'\W+', '', str.lower())

    def normalize_artist_music(self):
        return self.normalize_str(self.artist), self.normalize_str(self.music)

    def url(self):
        if not self.artist and not self.music:
            self.artist = "rickastley"
            self.music = "nevergonnagiveyouup"
        return "http://azlyrics.com/lyrics/{}/{}.html".format(*self.normalize_artist_music())

    def get_page(self):
        try:
            page = request.urlopen(self.url())
            return page.read()
        except error.HTTPError as e:
            if e.code == 404:
                print("Music not found")
                sys.exit(1)

    def extract_lyrics(self, page):
        soup = BeautifulSoup(page, "html.parser")
        lyrics_tags = soup.find_all("div", attrs={"class": None, "id": None})
        lyrics = [tag.getText() for tag in lyrics_tags]
        return lyrics

    def format_lyrics(self, lyrics):
        formated_lyrics = "\n".join(lyrics)
        return formated_lyrics

    def format_title(self):
        return "{} by {}".format(self.music.title(), self.artist.title())

    def get_lyrics(self):
        page = self.get_page()
        lyrics = self.extract_lyrics(page)
        return lyrics
