tuple = ("banana", "apple", "orange")
print(tuple[1])
print(tuple[0:2])
print(tuple[-2])
favs = ("Inception", "Interstellar", "Tenet", "The Dark Knight", "Dunkirk")
print("Top 3 movies:", favs[:3])
print("Last movie:", favs[-1])

favs = ("Inception", "Interstellar", "Tenet", "The Dark Knight", "Dunkirk")
print("Top 3 movies:", favs[:3])
print("Last movie:", favs[-1])

favs = ("Inception", "Interstellar", "Tenet", "The Dark Knight", "Dunkirk")
print("Top 3 movies:", favs[:3])
print("Last movie:", favs[-1])

try:
    favs[0] = "Oppenheimer"
except TypeError as e:
    print("Error:", e)
