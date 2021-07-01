import random

def add_one(x):
    return x + 1


def recommend_movie(movie_list):

    if type(movie_list) != list: 
        raise TypeError('The input has to be a list, you fool!')
    rec = random.choice(movie_list)
    return [rec.upper()][0]

