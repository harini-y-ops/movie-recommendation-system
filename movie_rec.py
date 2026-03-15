import random
movies=[
    {"title":"Inception","genre":"sci-fi","director":"Christopher Nolan","rating":8.8},
    {"title":"The Godfather","genre":"crime","director":"Francis Ford Coppola","rating":9.2},
    {"title":"Titanic","genre":"romance","director":"James Cameron","rating":7.9},
    {"title":"The Dark Knight","genre":"action","director":"Christopher Nolan","rating":9.0},
    {"title":"Parasite","genre":"thriller","director":"Bong Joon-ho","rating":8.5},
    {"title":"Toy Story","genre":"animation","director":"John Lasseter","rating":8.3},
    {"title":"The Conjuring","genre":"horror","director":"James Wan","rating":7.5},
    {"title":"Forrest Gump","genre":"drama","director":"Robert Zemeckis","rating":8.8},
    {"title":"Superbad","genre":"comedy","director":"Greg Mottola","rating":7.6},
    {"title":"Interstellar","genre":"adventure","director":"Christopher Nolan","rating":8.7}
]
print("------MENU------")
print("1.Recommend movie")
print("2.Random movie")
print("3.Search by director")
print("4.Exit")
choice=input("Enter your choice: ")
if choice=="1":
    genre=set(movie["genre"]for movie in movies)
    print("Available genres:\n", ", ".join(genre))
    genre=input("Enter the preferred genre: ").lower()
    rating=float(input("Enter the rating of the movie: "))
    recommended=[movie for movie in movies if movie["genre"]==genre and movie ["rating"]>=rating]
    if recommended:
        print("Recommended movies\n")
        for movie in recommended:
            print(f" {movie['title']} — {movie['director']} — {movie['rating']}")
    else:
        print("No movies found! Try a different genre")
    
elif choice =="2":
    movie=random.choice(movies)
    print("Random movie recommendation: ")
    print(f"{movie['title']}-{movie['genre']}-{movie['rating']}")
    
elif choice =="3":
    director=input("Enter the director name: ").lower()
    found=False
    for movie in movies:
        if movie["director"].lower()==director:
            print(f"{movie['title']}-{movie['rating']}")
            found=True
        if not found:
            print("No movies from the director")
        
         
elif choice =="4":
    print("Exiting program!")

else:
    print("Invalid choice please try again")
