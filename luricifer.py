import dbus
import AZlyrics

session_bus = dbus.SessionBus()
spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                     "/org/mpris/MediaPlayer2")
spotify_properties = dbus.Interface(spotify_bus,
                                    "org.freedesktop.DBus.Properties")
metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

artist = metadata['xesam:artist'][0]
title = metadata['xesam:title'].split(" (feat.",1)[0]
title = title.split(" (with",1)[0]

az = AZlyrics.Azlyrics(artist, title)
lyrics = az.get_lyrics()
formatedLyrics = az.format_lyrics(lyrics)
listedLyrics = formatedLyrics.split('\n')
print(artist, "-" ,title)
for phrase in listedLyrics:
    print(phrase)
    input()
