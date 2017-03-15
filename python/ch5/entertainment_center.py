#!/usr/bin/python

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
			"A story of a boy and his toys that come to life.",
			"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
			"http://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
			"A marine on an alien planet",
			"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser_Poster.jpg",
			"http://www.youtube.com/watch?v=9ceBgWV8io")

yoga = media.Movie("Heart Chakra Yoga",
			"Yoga sequence for the heart chakra",
			"https://i.ytimg.com/vi/TMq0Bt-G7wM/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=1fOIwRL9sDJcfDENPqTUyryXz0I",
			"https://www.youtube.com/watch?v=TMq0Bt-G7wM")



movies = [toy_story, avatar, yoga]
#fresh_tomatoes.open_movies_page(movies)
print media.Movie.VALID_RATINGS
print media.Movie.__doc__
#print toy_story.storyline
#print avatar.storyline
#avatar.show_trailer()
#yoga.show_trailer()
