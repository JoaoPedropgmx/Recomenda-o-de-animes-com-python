import pandas as pd
from AnilistPython import Anilist

anilist = Anilist()
generos = {"Ação": "Action",
           "Romance": "Romance",
           "Aventura": "Adventure",
           "Drama": "Drama",
           "Ecchi": "Ecchi",
           "Fantasia": "Fantasy",
           "Slice of life": "Slice of Life",
           "Esporte": "Sports",
           "Terror": "Thriller",
           "Musica": "Music",
           "Comédia": "Comedy"
           }

genero_Input = input("Qual Gênero de Anime Gostaria de Ver no Momento? ")
genero = generos[genero_Input.capitalize()]
ano = input("Gostaria de ver Animes de qual ano? ")
if ano == "":
    ano = list(range(1990, 2022))

r = anilist.search_anime(genre=[genero], year=ano)
dataf = pd.DataFrame(r)
df = pd.DataFrame().assign(Animes=dataf['name_romaji'],
                           Episódios=dataf['airing_episodes'],
                           Formato=dataf['airing_format'])

pd.set_option('display.max_rows', 1000, 'display.max_columns', 500)
df = df[(df['Formato'] == 'TV') | (df['Formato'] == 'ONA')]
df['Episódios'].fillna(0, inplace=True)
Lista = df.iloc[:30].reset_index(drop=True)
Lista.index += 1
print(Lista)

