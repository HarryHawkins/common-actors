from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()
# get 2 movies from user
movie_A = input("Enter your first movie: ")
movie_B = input("Enter your second movie: ")
#find movies with similar names to users input
search_results_A = ia.search_movie(movie_A)
search_results_B = ia.search_movie(movie_B)
if not search_results_A:
    print("No movie found called :",movie_A)
    print("Please try again")
if not search_results_B:
    print("No movie found called :",movie_B)
    print("Please try again")
if search_results_A and search_results_B:
    #movie A is set to first result
    movieID_A = search_results_A[0].movieID
    movie_object_A = ia.get_movie(movieID_A)
    print("First movie found: ",movie_object_A.get('title'))
    #movie B is set to first result
    movieID_B = search_results_B[0].movieID
    movie_object_B = ia.get_movie(movieID_B)
    print("Second movie found: ",movie_object_B.get('title'))

    #get casts and find common cast members
    cast_A = movie_object_A.get('cast')
    cast_B = movie_object_B.get('cast')
    if cast_A and cast_B:
        common_actors = list(set(cast_A)&set(cast_B))
        if common_actors:
            print("Common actors found ", len(common_actors), ": ")
            for actor in common_actors:
                print(actor.get('name'))
        else:
            print("No common actors")
    else:
        if not cast_A:
            print("Cast not found for ",movie_object_A.get('title'))
        if not cast_B:
            print("Cast not found for ",movie_object_A.get('title'))

#TODO maybe port to OOP structure, but for now simple enough as a script
