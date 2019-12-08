#import pylint
# import pandas as pd
# # from sklearn.linear_model import LinearRegression

# lmao = pd.read_csv("data.csv")

# print("hello world")
# print(lmao)

import pandas as pd
import numpy as np
from scipy.spatial import distance

movieInfo = pd.read_csv("movies.csv", usecols = ['movieId', 'title'], dtype = {'movieId' : 'int32', 'title' : 'str'})

movieRatings = pd.read_csv("ratings.csv", usecols = ['userId', 'movieId', 'rating'], dtype = {'userId' : 'int32', 'movieId' : 'int32', 'rating' : 'float32'})

movieLinks = pd.read_csv("links.csv", usecols = ['movieId', 'imdbId', 'tmdbId'])

mergedDf = pd.merge(movieRatings, movieInfo, on = 'movieId')

finalDataFrame = pd.merge(mergedDf, movieLinks, on = 'movieId')

finalDataFrame.dropna(axis = 0, how = 'any')
#finalDataFrame.truncate(before = 50000, after = 100000);
#finalDataFrame = finalDataFrame.tail(50000);
finalDataFrame = finalDataFrame.drop(labels = 'tmdbId', axis = 1)
#print(finalDataFrame.describe());

finalDataFrame = finalDataFrame.query('rating >= 4')
#print(finalDataFrame);

dictArr = []

for index, row in finalDataFrame.iterrows():
    dictArr.append({'userId':row['userId'],
                    'movieId':row['movieId'],
                    'rating':row['rating'],
                    'title':row['title'],
                    'imdbId':row['imdbId'],
                    'dist':0})
    
    
mot = 'seven'
    
def searchMovie(movtitle):
    for element in dictArr:
        if element['title'].split(' ')[0].lower() == movtitle.split(' ')[0].lower():
            # searchedId = element['imdbId']
            # print(searchedId)
            return element
    print('the movie you requested is not available in dataset')
    return -1


searchedElement = searchMovie(mot)

def getSearchedMovieId():
    return searchedElement['imdbId']


def findDistances(movid):
    for element in dictArr:
        if element['movieId'] == movid:
            element['dist'] = 999999999
        else:
            p2 = (element['movieId'], element['userId'], element['rating'])
            element['dist'] = distance.euclidean(p1,p2)


#print(searchMovie(mot));
imdbIds = []

if searchedElement != -1:
    searchedMovie = searchedElement
    p1 = (searchedMovie['movieId'], searchedMovie['userId'], searchedMovie['rating'])
    findDistances(searchedMovie['movieId'])

    #print(sorted(dictArr, key = lambda i : i['dist'])[0:10]);

    sortedArray = sorted(dictArr, key = lambda i : i['dist'])[0:100]

    sortedArrayCleaned = [dict(t) for t in {tuple(d.items()) for d in sortedArray}]

    finalChoice = sortedArrayCleaned[0:5]

    for elem in finalChoice:
        imdbIds.append(elem['imdbId'])

    #print(sortedArrayCleaned[0:5])

else:
    print('The requested Movie is not available in dataset')           
    
 


