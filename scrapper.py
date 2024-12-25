"""
CSV =

Album: Labirinto da...
Data: 2024
Música: Adeus adeus
letra: A vida permeava

Exemplo:
Labirinto da..., 2024, Adeus adeus, A vida permeava
"""
from os import write

from httpx import get
from parsel import Selector
from csv import DictWriter
import dateparser

def letra(url: str) -> str:
    """Pega a letra de um música."""
    response = get(url)
    s = Selector(response.text)
    letra = '\n'.join(s.css('[data-lyrics-container]::text').getall())
    return letra

def faixas(url: str) -> list[tuple[str, str]]:
    response = get(url)
    s = Selector(response.text)

    musicas = s.css('div.chart_row-content')
    # print(len(musicas))
    # for musica in musicas:
    #     print(
    #         musica.css('h3::text').get().strip(),
    #         musica.css('a').attrib['href']
    #           )

    return [
        (musica.css('h3::text').get().strip(), musica.css('a').attrib['href'])
        for musica in musicas
    ]

def discos(url: str) -> list[tuple[str | None, ...]]:
    response = get(url)
    s = Selector(response.text)

    # discos = s.css('div.kwiTTk')
    discos = s.css('.ZvWhZ') #OBS: O ZvWhZ é o css do disco. O ponto indica uma class css

    # resultado: list[tuple[str | None, str | None, str | None]] = []
    resultado = []

    for disco in discos:
        disco_url = disco.css('.kqeBAm').attrib['href']
        disco_nome = disco.css('.gpuzaZ::text').get()
        disco_ano = disco.css('.cedmJJ::text').get()

        resultado.append(
            (disco_url, disco_nome, disco_ano)
        )

    return resultado


url = 'https://genius.com/artists/Dead-fish/albums'

with open('musicas.csv', 'w', encoding="utf-8") as f:
    writer = DictWriter(f, ['album', 'data', 'musica', 'letra'])
    writer.writeheader()
    for disco in discos(url):
        print(disco)
        for faixa in faixas(disco[0]):
            # print(faixa)
            # print(letra(faixa[1]))
            row = {
                'album': disco[1],
                'data': dateparser.parse(disco[2]),
                'musica': faixa[0],
                'letra': letra(faixa[1])
            }
            print(row)
            writer.writerow(row)
