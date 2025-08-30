# aula4_questao6.py

musicas = []

with open("spotify-2023.csv", "r", encoding="latin-1") as f:
    linhas = f.readlines()

# Cabeçalho: track_name,artist(s)_name,artist_count,released_year,...
for linha in linhas[1:]:
    if '"' in linha:  # ignora linhas com aspas
        continue
    partes = linha.strip().split(",")
    if len(partes) < 9:
        continue
    
    track_name = partes[0]
    artist = partes[1]
    year = int(partes[3])
    streams = int(partes[8])

    if 2012 <= year <= 2022:
        musicas.append([track_name, artist, year, streams])

# Escolhe a mais tocada de cada ano
mais_tocadas = {}
for m in musicas:
    track, artist, year, streams = m
    if year not in mais_tocadas or streams > mais_tocadas[year][3]:
        mais_tocadas[year] = m

# Ordena por ano
resultado = [mais_tocadas[ano] for ano in sorted(mais_tocadas)]
print(resultado)
