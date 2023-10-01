#!/usr/bin/env python3

import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    with open(MOVIE_DATA, 'r') as f:
        data = csv.DictReader(f)
        directors=defaultdict(list)
        for line in data:
            director = line.get("director_name", "")
            movie    = line.get("movie_title",)
            year      = line.get("title_year",)
            score    = line.get("imdb_score",0)
            m = Movie(title=movie, year=year, score=score)
            if m.year != '':
                if int(m.year) > MIN_YEAR:
                    directors[director].append(m)
                else:
                    continue
        return directors

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    filtered_dict = defaultdict(list)
    for k in directors.keys():
        if len(directors[k]) >= MIN_MOVIES:
            filtered_dict[(k, _calc_mean(directors[k]))] = directors[k]

    return filtered_dict

def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return round(sum([float(movie.score) for movie in movies])/len(movies), 1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60

    for counter, item in enumerate(sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True), 1):
        (director, avg), movies = item
        print(fmt_director_entry.format(counter=counter, director=director, avg=avg))
        print(sep_line)
        for movie in movies:
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))
        if counter == NUM_TOP_DIRECTORS:
            break

def main():
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
