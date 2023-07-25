from imdb import IMDb


def get_number_of_movies():
    while True:
        try:
            num_movies = int(input("How many movies would you like to enter? "))
        except ValueError:
            print("Please enter a number!")
            continue
        else:
            break
    return num_movies


def get_movie_names(num_movies):
    movies = []
    for i in range(num_movies):
        movies.append(input(f"Enter movie number {i+1}: "))
    return movies


def get_search_results(ia, movies):
    search_results = []
    for movie in movies:
        search_results.append(ia.search_movie(movie))
    return search_results


def check_search_results(search_results, movies):
    missing_result = False
    for i, result in enumerate(search_results):
        if not result:
            print(f"No movie found called : {movies[i]}")
            print("Please try again")
            missing_result = True
    return missing_result


def get_movie_objects_and_casts(ia, search_results):
    movie_objects = []
    movie_casts = []
    for result in search_results:
        movie = ia.get_movie(result[0].movieID)
        movie_objects.append(movie)
        print(f"Movie {len(movie_objects)} found: {movie.get('title')}")
        movie_casts.append(movie.get('cast'))
    return movie_objects, movie_casts


def check_casts(movie_objects, movie_casts):
    cast_exist = True
    for i, cast in enumerate(movie_casts):
        if not cast:
            cast_exist = False
            print(f"Unfortunately there is no cast for {movie_objects[i].get('title')}")
            print("Please try again with a different movie\n")
    return cast_exist


def print_common_actors(movie_casts):
    common_actors = set.intersection(*map(set, movie_casts))
    if common_actors:
        print(f"Common actors found {len(common_actors)}: ")
        for actor in common_actors:
            print(actor.get('name'))
    else:
        print("No common actors")


def main():
    ia = IMDb()
    print("Welcome to common-actors! \nThis tool will give you the common actors from a selection of given movies\n")
    num_movies = get_number_of_movies()
    movies = get_movie_names(num_movies)
    search_results = get_search_results(ia, movies)
    missing_result = check_search_results(search_results, movies)
    if not missing_result:
        movie_objects, movie_casts = get_movie_objects_and_casts(ia, search_results)
        cast_exist = check_casts(movie_objects, movie_casts)
        if cast_exist:
            print_common_actors(movie_casts)


if __name__ == "__main__":
    main()
