# Projeto de NPL

Projetinho de análise de linguagem natural.

Entender como as palavras aparecem nos discos da banda.

# Pacotes
Seria legal utilizar o UV nesse projeto. Fica para o futuro. 

Vamos lá: 

Criando o venv

```shell
python -m venv .venv
```

Instalando as dependências

```shell
pip install httpx parsel
```

```shell
pip install dataparser
```

Ou no UV
```shell
uv add httpx parsel
```

# Inicio

A ideia é entender as palavras, como elas se relacionam. E uma visualização disso.

# Análise das letras do Dead Fish

## Técnica

- Captura dos dados
    - Baixar todas as letras
        - httpx + parsel - [Genius](genius.com)
    - Persistir
        - CSV

- Organização
    - Dataframe - Polars/Pandas

- Limpeza / Tratamento
    - Dataframe
    - Repo de stopwords

- Olhar os dados
    - Spacy
    - WorldCloud

## Análise: Perguntas

- Quais são as palavras mais usadas?
    - Por disco
    - Por Década
    - Em que contexto?

- Analise lexica
    - Quantas palavras por música (média por disco?)
    - Quantas palavras únicas por disco?

- Ver
    - Nuvem de palavras
    - Concord (analise de corpos linguística, verbos e etc)



# Scrapping 

[fluxo_scrapping.excalidraw](docs/fluxo_scrapping.excalidraw)

Vai ser no formato mais simples possível, forzão sem frescura, sem async sem nada.
A ideia aqui é a análise não o scrapping


# Dicas

Executar um script python e gerar as saídas dos print em um arquivo.

```shell
python scrapper.py > scrapper.log
```