movie_title = []
parental_rating = [] 
bechdel_rating = []
imdb_rating = []
genre = []

count = 1

for movie_input in range(5):
	movie_inp = raw_input("Enter movie title #{0}: ".format(count))
	rating_inp = raw_input("\tEnter the parental rating: ")
	bechdel_inp = raw_input("\tEnter the Bechdel Test rating 1 - 3: ")
	imdb_inp = raw_input("\tEnter the IMDB rating: ")
	genre_inp = raw_input("\tEnter the genre: ")

	movie_title.append(movie_inp)
	parental_rating.append(rating_inp)
	bechdel_rating.append(bechdel_inp)
	imdb_rating.append(imdb_inp)
	genre.append(genre_inp)

	count = count + 1

lists_combined = zip(movie_title, parental_rating, bechdel_rating, imdb_rating, genre)

for movie_title, parental_rating, bechdel_rating, imbdb_rating, genre in lists_combined:
	print "{0}, {1}, {2}, {3}, {4}".format(movie_title, parental_rating, bechdel_rating, imbdb_rating, genre)
