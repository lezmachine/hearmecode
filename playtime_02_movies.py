#		Their parental guidance rating (G, PG, PG-13, R)
#		Their Bechdel Test Rating (See http://shannonvturner.com/bechdel or http://bechdeltest.com/)
#		Their IMDB Rating from 0 - 10 (See http://imdb.com/)
# 		Their genre according to IMDB

#	The Big Lebowski, R, 1, 8.6, Comedy / Crime
#	Heathers, R, 3, 7.3, Comedy / Crime / Drama
#	Rushmore, R, 3, 7.7, Comedy / Drama
#	Journey to the West, PG-13, 2, 6.8, Action / Adventure / Comedy
#	Grey Gardens, PG, BT, 7.7, Documentary / Comedy / Drama

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

for i in lists_combined:
	print "{0}, {1}, {2}, {3}, {4}".format(i[0], i[1], i[2], i[3], i[4],)
