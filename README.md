










## Como usar o loader

O arquivo `scripts/loader.py` contém uma função flexível para carregar qualquer arquivo master do MERGE, permitindo filtros por split, quadrante, ano, artista, título e gêneros.
Para ver todos os metadados disponíveis para filtro, consulte `schema/data_dictionary.md` ou use `df.columns` após o load.

**Exemplo básico:**
```python
from scripts.loader import load_merge_master

# Carregar músicas do split de treino do quadrante 1 em 2010 do gênero 'pop'
df = load_merge_master(
    'metadata/master_metadata_audio_balanced.csv',
    split='train',
    split_type='split_70_15_15',
    quadrant=1,
    year=2010,
    genres='pop'
)
print(df.head())


## Exemplo de uso do loader.py

```python
from scripts.loader import load_merge_master

# Carregar todos os dados de treino de 2010 a 2012 do quadrante 1 e do gênero 'rock'
df = load_merge_master(
    'metadata/master_metadata_audio_balanced.csv',
    split='train',
    split_type='split_70_15_15',
    year=[2010, 2011, 2012],
    quadrant=1,
    genres='rock'
)
print(df[['song_id', 'artist', 'title', 'quadrant', 'year', 'genres']].head())

# Buscar por artista específico (busca parcial e case-insensitive)
df_adele = load_merge_master(
    'metadata/master_metadata_audio_balanced.csv',
    artist='adele'
)
print(df_adele[['song_id', 'artist', 'title']].head())

# Filtrar por múltiplos quadrantes ou gêneros
df_multi = load_merge_master(
    'metadata/master_metadata_audio_balanced.csv',
    quadrant=[1, 3],
    genres=['pop', 'rock']
)
print(df_multi[['song_id', 'artist', 'quadrant', 'genres']].head())
