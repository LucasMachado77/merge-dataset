# Data Dictionary – MERGE Dataset (Masters Padronizados)

Este documento descreve os campos presentes nos arquivos `master_metadata` criados para cada modalidade e variante (audio, lyrics, bimodal; balanced, complete).

---

## 1. master_metadata_audio_balanced.csv

| Campo             | Tipo    | Descrição                                                      |
|-------------------|---------|----------------------------------------------------------------|
| song_id           | str     | Identificador único da música                                  |
| quadrant          | int     | Quadrante emocional (1 a 4)                                    |
| arousal           | float   | Valor de excitação emocional                                   |
| valence           | float   | Valor de valência emocional                                    |
| split_40_30_30    | str     | Split no esquema 40-30-30: 'train', 'val', 'test'              |
| split_70_15_15    | str     | Split no esquema 70-15-15: 'train', 'val', 'test'              |
| AllMusic Id               | str    | ID do AllMusic associado à faixa                        |
| AllMusic Extraction Date  | str    | Data da extração do AllMusic                            |
| Artist                   | str    | Nome do artista                                         |
| Title                    | str    | Título da música                                        |
| Relevance                | float  | Relevância atribuída                                    |
| Year                     | int    | Ano atribuído                                           |
| LowestYear               | int    | Ano mínimo atribuído                                    |
| Duration                 | float  | Duração em segundos                                     |
| Moods                    | str    | Moods principais (separados por ;)                      |
| MoodsAll                 | str    | Todos os moods atribuídos                               |
| MoodsAllWeights          | str    | Pesos dos moods atribuídos                              |
| Genres                   | str    | Gêneros musicais (separados por ;)                      |
| GenreWeights             | str    | Pesos dos gêneros                                       |
| Themes                   | str    | Temas principais                                        |
| ThemeWeights             | str    | Pesos dos temas                                         |
| Styles                   | str    | Estilos musicais                                        |
| StyleWeights             | str    | Pesos dos estilos                                       |
| AppearancesTrackIDs      | str    | IDs das aparições em faixas                             |
| AppearancesAlbumIDs      | str    | IDs das aparições em álbuns                             |
| Sample                   | str    | Indicação se é sample                                   |
| SampleURL                | str    | URL do sample                                           |
| ActualYear               | int    | Ano real do lançamento                                  |
| num_Genres               | int    | Número de gêneros atribuídos                            |
| num_MoodsAll             | int    | Número de moods atribuídos                              |

---

## 2. master_metadata_audio_complete.csv

**Mesmos campos do audio_balanced**.

---

## 3. master_metadata_lyrics_balanced.csv

| Campo             | Tipo    | Descrição                                                      |
|-------------------|---------|----------------------------------------------------------------|
| song_id           | str     | Identificador único da música                                  |
| quadrant          | int     | Quadrante emocional (1 a 4)                                    |
| arousal           | float   | Valor de excitação emocional                                   |
| valence           | float   | Valor de valência emocional                                    |
| split_40_30_30    | str     | Split no esquema 40-30-30: 'train', 'val', 'test'              |
| split_70_15_15    | str     | Split no esquema 70-15-15: 'train', 'val', 'test'              |
| AllMusic Id               | str    | ID do AllMusic associado à faixa                        |
| AllMusic Extraction Date  | str    | Data da extração do AllMusic                            |
| Artist                   | str    | Nome do artista                                         |
| Title                    | str    | Título da música                                        |
| Relevance                | float  | Relevância atribuída                                    |
| Year                     | int    | Ano atribuído                                           |
| LowestYear               | int    | Ano mínimo atribuído                                    |
| Duration                 | float  | Duração em segundos                                     |
| Moods                    | str    | Moods principais (separados por ;)                      |
| MoodsAll                 | str    | Todos os moods atribuídos                               |
| MoodsAllWeights          | str    | Pesos dos moods atribuídos                              |
| Genres                   | str    | Gêneros musicais (separados por ;)                      |
| GenreWeights             | str    | Pesos dos gêneros                                       |
| Themes                   | str    | Temas principais                                        |
| ThemeWeights             | str    | Pesos dos temas                                         |
| Styles                   | str    | Estilos musicais                                        |
| StyleWeights             | str    | Pesos dos estilos                                       |
| AppearancesTrackIDs      | str    | IDs das aparições em faixas                             |
| AppearancesAlbumIDs      | str    | IDs das aparições em álbuns                             |
| Sample                   | str    | Indicação se é sample                                   |
| SampleURL                | str    | URL do sample                                           |
| ActualYear               | int    | Ano real do lançamento                                  |
| num_Genres               | int    | Número de gêneros atribuídos                            |
| num_MoodsAll             | int    | Número de moods atribuídos                              |

---

## 4. master_metadata_lyrics_complete.csv

**Mesmos campos do lyrics_balanced**.

---

## 5. master_metadata_bimodal_balanced.csv

| Campo             | Tipo    | Descrição                                                      |
|-------------------|---------|----------------------------------------------------------------|
| song_id           | str     | Identificador único da música (copiado de Audio_Song)          |
| Lyric_Song        | str     | ID correspondente na versão de lyrics                          |
| quadrant          | int     | Quadrante emocional (1 a 4)                                    |
| arousal           | float   | Valor de excitação emocional                                   |
| valence           | float   | Valor de valência emocional                                    |
| split_40_30_30    | str     | Split no esquema 40-30-30: 'train', 'val', 'test'              |
| split_70_15_15    | str     | Split no esquema 70-15-15: 'train', 'val', 'test'              |
| AllMusic Id               | str    | ID do AllMusic associado à faixa                        |
| AllMusic Extraction Date  | str    | Data da extração do AllMusic                            |
| Artist                   | str    | Nome do artista                                         |
| Title                    | str    | Título da música                                        |
| Relevance                | float  | Relevância atribuída                                    |
| Year                     | int    | Ano atribuído                                           |
| LowestYear               | int    | Ano mínimo atribuído                                    |
| Duration                 | float  | Duração em segundos                                     |
| Moods                    | str    | Moods principais (separados por ;)                      |
| MoodsAll                 | str    | Todos os moods atribuídos                               |
| MoodsAllWeights          | str    | Pesos dos moods atribuídos                              |
| Genres                   | str    | Gêneros musicais (separados por ;)                      |
| GenreWeights             | str    | Pesos dos gêneros                                       |
| Themes                   | str    | Temas principais                                        |
| ThemeWeights             | str    | Pesos dos temas                                         |
| Styles                   | str    | Estilos musicais                                        |
| StyleWeights             | str    | Pesos dos estilos                                       |
| AppearancesTrackIDs      | str    | IDs das aparições em faixas                             |
| AppearancesAlbumIDs      | str    | IDs das aparições em álbuns                             |
| Sample                   | str    | Indicação se é sample                                   |
| SampleURL                | str    | URL do sample                                           |
| ActualYear               | int    | Ano real do lançamento                                  |
| num_Genres               | int    | Número de gêneros atribuídos                            |
| num_MoodsAll             | int    | Número de moods atribuídos                              |

---

## 6. master_metadata_bimodal_complete.csv

**Mesmos campos do bimodal_balanced**.

---

> **Nota:** Em todos os arquivos bimodal, `song_id` é baseado no campo `Audio_Song` dos CSVs originais e a coluna `Lyric_Song` é mantida para rastreamento cruzado entre modalidades.

---

**Se algum master tiver campos a mais/menos, rode o código abaixo para listar todos os campos:**

```python
import pandas as pd
df = pd.read_csv('master_metadata_NOME.csv')
for col in df.columns:
    print(f"| {col} |  |  |")
