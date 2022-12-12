from imdb import Cinemagoer
import pandas as pd
import mysql.connector

DATA = pd.read_csv("movie.metadata.tsv", sep = "\t", header = None, index_col=0, names = ["WIKIPEDIA ID", "FREEBASE ID", "NAME", "RELEASE DATE", "BOX OFFICE", "RUNTIME", "LANGUAGES", "COUNTRIES", "GENRES"])

ia = Cinemagoer()

db = mysql.connector.connect(
  host ="mysql.micro-ondes.ch",
  user ="r4d4r",
  passwd ="1MotDePasse",
  database = "ada_raw_imdb"
)

cursor = db.cursor()


for index, row in DATA.iterrows():
	cursor.execute("SELECT wikipedia_id FROM RAW_DATA WHERE wikipedia_id = %s", (str(index),))
	if cursor.fetchall():
		continue
	cnt = 1
	while True:
		try:
			film = ia.search_movie(row['NAME'])[0]
			break
		except IndexError:
			if cnt > 9:
				print(row['NAME'])
				break
			else:
				cnt += 1
		except KeyboardInterrupt:
			exit()
		except:
			print(row['NAME'], "not found")
	try:
		if film["title"].casefold() == row['NAME'].casefold() and film["year"] == pd.to_datetime(row['RELEASE DATE']).year:
			film = ia.get_movie(film.movieID).data
			cast = list()
			for person in film['cast']:
				cast.append(person.data["name"])
			cursor.execute("INSERT INTO RAW_DATA (wikipedia_id, imdb_id, title, cast, genres, runtimes, countries, languages, box_office, rating, votes, plot, synopsis) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
				(
					str(index), 
					str(film['imdbID']), 
					str(film["title"].casefold()), 
					str(cast), 
					str(film['genres']) if 'genres' in film else 'NULL', 
					str(film['runtimes']) if 'runtimes' in film else 'NULL', 
					str(film['countries']) if 'countries' in film else 'NULL', 
					str(film['languages']) if 'languages' in film else 'NULL', 
					str(film['box office']) if 'box office' in film else 'NULL', 
					str(film['rating']) if 'rating' in film else 'NULL', 
					str(film['votes']) if 'votes' in film else 'NULL', 
					str(film['plot']) if 'plot' in film else 'NULL', 
					str(film['synopsis']) if 'synopsis' in film else 'NULL'
				))
			db.commit()
	except Exception as e:
		print(e)

db.close()