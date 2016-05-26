
import fresh_tomatoes
import media

# Instantiate movie class for toy_story
toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

# print(toy_story.storyline)

# Instantiate movie class for avatar
avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=d1_JBMrrYw8")

# avatar.show_trailer()

# Instantiate movie class for the_angry_birds
the_angry_birds = media.Movie("The Angry Birds",
	"Find out why the birds are so angry",
	"https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png",
	"https://www.youtube.com/watch?v=QRmKa7vvct4")

# the_angry_birds.show_trailer()

# Arrange the instances and generate movie page
movies = [toy_story, avatar, the_angry_birds]
fresh_tomatoes.open_movies_page(movies)