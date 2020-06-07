import sys
from imdb import IMDb

def main():
    # create an instance of the IMDb class
    ia = IMDb()
    # get movies from user
    print("Welcome to common-actors! \nThis tool will give you the common actors from a selection of given movies\n")
    while True:
        try:
            num_movies = int(input("How many movies would you like to enter? "))
        except ValueError:
            print("Please enter a number!")
            #better try again... Return to the start of the loop
            continue
        else:
            break

    movies = []
    for i in range(num_movies):
        movies.append(input("Enter movie number "+str(i+1)+ ": "))

    #find movies with similar names to users input
    search_results = []
    for movie in movies:
        search_results.append(ia.search_movie(movie))

    #check we got results for each input
    missing_result = False
    i = 0
    for result in search_results:
        if not result:
            print("No movie found called : "+movies[i])
            print("Please try again")
            missing_result = True
        i +=1


    if missing_result == False:
        #get ID of each movie and assign to objects (assume first result is the movie wanted)
        movie_IDs = []
        for result in search_results:
            movie_IDs.append(result[0].movieID)
            
        #get movie objects for each ID
        movie_objects = []
        for id in movie_IDs:
            movie_objects.append(ia.get_movie(id))
            print(len(movie_objects), "Movie found: "+ia.get_movie(id).get('title'))

        #get cast for each movie
        movie_casts = []
        for obj in movie_objects:
            movie_casts.append(obj.get('cast'))

        #check we got a cast for each movie
        cast_exist = True
        i = 0
        for cast in movie_casts:
            if not cast:
                cast_exist = False
                print("Unfortunately there is no cast for "+movie_objects[i].get('title'))
                print("Please try again with a different movie\n")
            i+=1

        if cast_exist:
            #get intersection of all movie casts (common actors)
            common_actors = set.intersection(*map(set,movie_casts))
            if common_actors:
                print("Common actors found "+ str(len(common_actors))+ ": ")
                for actor in common_actors:
                    print(actor.get('name'))
                    if len(sys.argv) > 1:
                        if sys.argv[1]=='-wiki':
                            import webbrowser
                            webbrowser.open('https://en.wikipedia.org/wiki/'+actor.get('name'))  # makes annoying output in CLI, but not much of an issue
            else:
                print("No common actors")
        else:
            main()
            
if __name__ == "__main__":
    main()

