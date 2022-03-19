

# Phantombot-pl-Importer
An importer for the phantombot playlist module. The bulk of the code (all of it except for a fix at this point) for this importer was made by Branden#1337 over on the [PhantomBot Community Discord server](https://discord.com/invite/YKvMd78)


The main difference is I will keep this up to date and provide support where possible and add new features.
Permission proof: 

![Permission proof](https://raw.githubusercontent.com/ICEconchy/Phantombot-pl-Importer/main/assets/Screenshot_2022-03-19%20224435.png)


## Setup - Python version
So to start of with you'll need urllib3

    pip install urllib3
    or
    python -m pip install urllib3

Depending on how your system is setup the command might change. 

## How to actually run it
Start by running the script with

    Python yt_playlist_to_txt.py
    or
    Python3 yt_playlist_to_txt.py

Then goto googles developer console and get a youtube api key. On the page it'll be called youtube data api for some reason.
1.  Log in to Google Developers Console.
2.  Create a new project or select existing project.
3.  On the new project dashboard, click Enable APIs and services.
4.  In the search, type youtube and select "youtube data api 3"
5.  Enable the API.
6.  Create a credential by going to the api page and clicking credentials, then create credentials.
7.  A screen will appear with the API key, keep that safe, you'll need it soon.

Then goto youtube and find your playlist you want to import. 
You probably have a link similarly to this:
https://www.youtube.com/watch?v=h98rqJv4qzo&list=PL3kXme0WFC_7biGeLKzSKGBH-Fdv8_lVs
This won't work, you'll need the playlist id which can be found at the end of the list= part of the url which in my case is this:
PL3kXme0WFC_7biGeLKzSKGBH-Fdv8_lVs



# Command Version

Many have recommended using the youtube-dl package to do what the python script does.
It requires [youtube-dl](https://youtube-dl.org/) and [jq](https://stedolan.github.io/jq/)

## Setup

Once you have installed youtube-dl and jq, execute this command


    youtube-dl -j --flat-playlist "https://www.youtube.com/watch?v=P7lE-G1oC34&list=PL9tY0BWXOZFsvIyhwbYAnF7A0LfrNq8uQ" | jq -r '.id' | sed 's_^_https://youtu.be/_' > playlist.txt
    
    


## FIN
Thats it! Once you give the script/command what it asks for it'll place a file called playlist.txt which you place in /addons/youtubePlayer
and use the command 

    !playlist importpl file [playlist name] [file]
