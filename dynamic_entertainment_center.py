import media
import urllib
import json
import fresh_tomatoes

movies = []
tmdb_api_key = "" #Get the api key from "https://www.themoviedb.org/"

connection = urllib.urlopen("https://api.themoviedb.org/3/movie/top_rated?api_key=" + tmdb_api_key)
jsonData = connection.read()
jsonToPython = json.loads(jsonData)
#print(json.dumps(jsonToPython, indent=4, sort_keys=True))


#A single querry to the api give 20 result so increasing the range will give IndexOutOfBound error.
#Due to not availability of trailer video movies array contain less than 20 Movies Object
for x in range(20):
    try:
        movie_info = jsonToPython['results'][x]
        title = movie_info['title']
        storyline = ''
        if jsonToPython['results'][x]['overview'] != "":
            storyline = movie_info['overview']
        else:
            storyline = "Not Available"
        image_url = ""
        if movie_info['poster_path'] is not None:
            image_url = "https://image.tmdb.org/t/p/w500/" + str(movie_info['poster_path'])
        else:
            image_url = "https://image.tmdb.org/t/p/w500/" + str(movie_info['backdrop_path'])
        movie_id = str(movie_info['id'])
        videos_json = urllib.urlopen(
            "https://api.themoviedb.org/3/movie/" + movie_id + "/videos?api_key=" + tmdb_api_key).read()
        trailer_key = json.loads(videos_json)['results'][0]['key']
        trailer_url = "http://youtube.com/watch?v=" + str(trailer_key)
        movies.append(media.Movie(title, storyline, image_url, trailer_url))
    except:
        print ""

fresh_tomatoes.open_movies_page(movies)