import webbrowser

# TODO(yusong): 4
# Your task is to write a movie class in media.py. To do this, think about what 
# the properties of a movie are that need to be encapsulated in a movie object 
# such as movie titles, box art, poster images, and movie trailer URLs. Look at 
# what open_movies_page() does with a list of movie objects for hints on how to 
# design your movie class.

class Movie(object):
	"""docstring for Movie"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)