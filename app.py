from flask import Flask,render_template,url_for,request
import knn
from imdb import IMDb


ls = knn.imdbIds

ia = IMDb()

def get_movies(imdb_ids):
  movies_data = []
  for id in imdb_ids:
    movie = ia.get_movie(id)
    movies_data.append(movie)
  
  return movies_data


print(get_movies(ls))

# print(knn.imdbIds)
print(knn.getSearchedMovieId())

app = Flask(__name__)

@app.route('/')
def index():
    movie = ia.get_movie(knn.getSearchedMovieId())
    movies = get_movies(ls)

    genres = ''
    for genre in movie['genres']:
        genres += " / " + genre
  
    movie['genres'] = genres

    return render_template('index.html', current_movie=movie, recommended_movies=movies)

if __name__ == "__main__":
  app.run(debug=True)