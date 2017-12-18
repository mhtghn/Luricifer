import argparse
import dbus
import AZlyrics


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--line', action='store_true',
        help='Displays the lyrics line per line')
    return parser.parse_args()


def retrieve_spotify_metadata():
    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object(
        "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
    spotify_properties = dbus.Interface(
        spotify_bus, "org.freedesktop.DBus.Properties")
    return spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")


if __name__ == '__main__':
    args = parse_args()
    metadata = retrieve_spotify_metadata()

    artist = metadata['xesam:artist'][0]
    title = metadata['xesam:title'].split(" (feat.", 1)[0]
    title = title.split(' (with', 1)[0]

    print('{0} - {1}'.format(artist, title))

    az = AZlyrics.Azlyrics(artist, title)
    lyrics = az.get_lyrics()
    formatted_lyrics = az.format_lyrics(lyrics)

    if args.line:
        for phrase in formatted_lyrics.splitlines():
            print(phrase)
            input()
    else:
        print(formatted_lyrics)
