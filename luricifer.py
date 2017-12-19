import argparse
import dbus
import sync
import time

from azlyrics import Azlyrics


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--sync', action='store_true',
        help='Displays the lyrics line per line and sync')
    return parser.parse_args()


def retrieve_spotify_metadata():
    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object(
        "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
    spotify_properties = dbus.Interface(
        spotify_bus, "org.freedesktop.DBus.Properties")
    return spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")


def restart_song():
    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object(
        "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
    spotify_player = dbus.Interface(
        spotify_bus, "org.mpris.MediaPlayer2.Player")
    spotify_player.Pause()
    # Best way I found to restart the song
    spotify_player.Next()
    spotify_player.Previous()
    time.sleep(3)
    spotify_player.Play()


def print_synced_lyrics(synced_lyrics):
    for synced_line in str(synced_lyrics).splitlines():
        time.sleep(float(synced_line.split('\t', 1)[0]))
        print(synced_line.split('\t', 1)[1])


if __name__ == '__main__':
    args = parse_args()
    metadata = retrieve_spotify_metadata()

    artist = metadata['xesam:artist'][0]
    title = metadata['xesam:title'].split(" (feat.", 1)[0]
    title = title.split(' (with', 1)[0]

    print('{0} - {1}'.format(artist, title))

    az = Azlyrics(artist, title)
    lyrics = az.get_lyrics()
    formatted_lyrics = az.format_lyrics(lyrics)
    sync = sync.Sync(artist, title)

    if args.sync:
        synced_lyrics = ''
        restart_song()
        for phrase in formatted_lyrics.splitlines():
            start_time = time.time()
            input()
            print(phrase)
            synced_lyrics += str(time.time() - start_time) + '\t' + phrase + '\n'
        sync.save_synced_lyrics(synced_lyrics)

    else:
        if not sync.is_synced():
            print(formatted_lyrics)
        else:
            synced_lyrics = sync.get_synced_lyrics()
            restart_song()
            print_synced_lyrics(synced_lyrics)
