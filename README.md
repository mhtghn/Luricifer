 
Luricifer
============

A simple CLI tool to fetch lyrics from AZlyrics of the playing Spotify song using the API from `https://github.com/mracos/python-azlyrics`
on Debian based distribution (tested with Ubuntu 17.10)

-------------

Installation
----------------------

You can download Luricifer by cloning the `Git Repo <https://github.com/mhtghn/Luricifer>` and simply installing its requirements::



    $ git clone https://github.com/mhtghn/Luricifer.git
    
    $ cd Luricifer
    
    $ sudo pip install -r requirements.txt
    
Usage
----------------------
You need to have the Spotify app (not the web player) launched and a song playing

If you already synced the lyrics or if you want to display all the lyrics at once : 

    $ python luricifer.py
    
If you want to sync the lyrics to the song : 

    $ python luricifer.py --sync
    
Press `<Enter>` to display the next line.
