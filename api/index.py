from flask import Flask
from ytmusicapi import YTMusic
app = Flask(__name__)
# YTMusic.setup(filepath="headers_auth.json")

ytmusic = YTMusic('../oauth.json')





@app.route("/")
def home():
    return "Hello, World!!s!"


@app.route("/search/<query>")
def search(query):
    return   ytmusic.search(query)


@app.route("/artist/<query>")
def artist(query):
    return  ytmusic.get_artist(query)

@app.route("/homefeed")
def homefeed():
    return  ytmusic.get_home(12) 

@app.route("/relatedsongs/<query>")
def relatedsongs(query):
    return  ytmusic.get_song_related(query)   

@app.route("/lyrics/<query>")
def lyrics(query):
    return  ytmusic.get_lyrics(query)    
    
# Explore Tab 


@app.route("/moodsgenre")
def moodsgenre():
    return  ytmusic.get_mood_categories()     
                   

@app.route("/moodsplaylist/<query>")
def moodsplaylist(query):
    return  ytmusic.get_mood_playlists(query)    
    

# @app.route("/charts")
# def charts():
#     return  ytmusic.get_charts(country="IN")    

# Library

@app.route("/libraryplaylist")
def libraryplaylist():
    return  ytmusic.get_library_playlists() 


@app.route("/librarysongs")
def librarysongs():
    return  ytmusic.get_library_songs(40)       

@app.route("/libraryalbums")
def libraryalbums():
    return  ytmusic.get_library_albums()       

@app.route("/libraryartists")
def libraryartists():
    return  ytmusic.get_library_artists()

@app.route("/librarysubscriptions")
def librarysubscriptions():
    return  ytmusic.get_library_subscriptions()


@app.route("/likedsongs")
def likedsongs():
    return  ytmusic.get_liked_songs(100) 

@app.route("/history")
def history():
    return  ytmusic.get_history()  

# Playlist 
                      
@app.route("/playlist/<query>")
def playlist(query):
    return  ytmusic.get_playlist(query) 

#songs
    
@app.route("/songs/<query>")
def songs(query):
    return  ytmusic.get_song(query) 

if __name__ == "__main__":app.run(debug=True)