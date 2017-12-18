 
Luricifer
============

A simple CLI tool to fetch lyrics from AZlyrics of the playing Spotify song using the API from `https://github.com/mracos/python-azlyrics`
on Debian based distribution (tested with Ubuntu 17.10)

-------------

Installation
----------------------

You can download Luricifer by cloning the `Git Repo <https://github.com/mhtghn/Luricifer>` and simply installing its requirements::



    $ git clone https://github.com/mhtghn/Luricifer.git
    
    $ sudo pip install bs4
    
    $ sudo pip install dbus
    
Usage
----------------------
You need to have the Spotify app (not the web player) launched and a song playing

    $ cd Luricifer
    $ python Luricifer.py
    
Press Enter to display the next line.
