import webbrowser


class Movie:
	""" Summary of Movie class : 
		Represent the movie information and can open trailer youtube
		video on browser

		Attributes : 
			titile : a string represent the titile of movie
			storyline : a string that summary the movie 
			poster_image_url : a string that direct to movie poster image url
			trailer_youtube_url : a string that direct to trailer youtube video url

	"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""
			Inits Movie Class with movie titile, move storylie, poster image url,
			and trailer youtube url
		"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		

	def show_trailer(self):
		"""
			open the trailer youtube video on browser
		"""
		webbrowser.open(self.trailer_youtube_url)

