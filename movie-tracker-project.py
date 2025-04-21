# Basic Movie Tracker (No advanced keywords)

movie_data = []

def read_movies():
    file = open('movies.txt', 'r')
    for line in file:
        parts = []
        temp = ''
        for char in line.strip():
            if char == '|':
                parts.append(temp)
                temp = ''
            else:
                temp += char
        parts.append(temp)
        if len(parts) == 5:
            name = parts[0]
            director = parts[1]
            genre = parts[2]
            watched = parts[3] == 'yes'
            rating = float(parts[4])
            movie = {'name': name, 'director': director, 'genre': genre, 'watched': watched, 'rating': rating}
            movie_data.append(movie)
    file.close()

def write_movies():
    file = open('movies.txt', 'w')
    for movie in movie_data:
        line = movie['name'] + '|' + movie['director'] + '|' + movie['genre'] + '|' + ('yes' if movie['watched'] else 'no') + '|' + str(movie['rating']) + '\n'
        file.write(line)
    file.close()

def add():
    name = input("Name: ")
    director = input("Director: ")
    genre = input("Genre: ")
    watched = input("Watched (yes/no): ").lower() == 'yes'
    rating = float(input("Rating: "))
    movie = {'name': name, 'director': director, 'genre': genre, 'watched': watched, 'rating': rating}
    movie_data.append(movie)
    print("Added.")

def edit():
    name = input("Movie to change: ")
    for movie in movie_data:
        if movie['name'].lower() == name.lower():
            new_director = input("Director (" + movie['director'] + "): ")
            if new_director:
                movie['director'] = new_director
            new_genre = input("Genre (" + movie['genre'] + "): ")
            if new_genre:
                movie['genre'] = new_genre
            new_watched = input("Watched (yes/no) (" + ('yes' if movie['watched'] else 'no') + "): ")
            if new_watched:
                movie['watched'] = new_watched.lower() == 'yes'
            new_rating = input("Rating (" + str(movie['rating']) + "): ")
            if new_rating:
                if new_rating.replace('.', '', 1).isdigit():
                    movie['rating'] = float(new_rating)
                else:
                    print("Invalid rating.")
            print("Changed.")
            return
    print("Not found.")

def delete():
    name = input("Movie to remove: ")
    for movie in movie_data:
        if movie['name'].lower() == name.lower():
            movie_data.remove(movie)
            print("Removed.")
            return
    print("Not found.")

def find():
    key = input("Keyword: ").lower()
    found = False
    for movie in movie_data:
        if key in movie['name'].lower() or key in movie['director'].lower() or key in movie['genre'].lower():
            print(movie)
            found = True
    if not found:
        print("Nothing found.")

def unseen():
    seen = False
    for movie in movie_data:
        if not movie['watched']:
            print(movie)
            seen = True
    if not seen:
        print("Everything watched.")

def sort_by_genre():
    genre_list = []
    name_list = []
    for movie in movie_data:
        g = movie['genre']
        n = movie['name']
        if g not in genre_list:
            genre_list.append(g)
            name_list.append([n])
        else:
            i = genre_list.index(g)
            name_list[i].append(n)
    for i in range(len(genre_list)):
        print(genre_list[i] + ": " + ', '.join(name_list[i]))

def recommend():
    found = False
    for movie in movie_data:
        if movie['rating'] >= 8:
            print(movie)
            found = True
    if not found:
        print("No top picks.")

def start():
    try:
        read_movies()
    except:
        print("No file found.")

    while True:
        print("\n1. Add 2. Edit 3. Delete 4. Search 5. Unwatched 6. Group 7. Recommend 8. Save+Quit")
        action = input("Pick: ")
        if action == '1':
            add()
        elif action == '2':
            edit()
        elif action == '3':
            delete()
        elif action == '4':
            find()
        elif action == '5':
            unseen()
        elif action == '6':
            sort_by_genre()
        elif action == '7':
            recommend()
        elif action == '8':
            write_movies()
            print("Saved. Bye.")
            break
        else:
            print("Wrong input.")

start()
