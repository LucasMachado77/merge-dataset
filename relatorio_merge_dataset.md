# Relatório Final – Projeto MERGE Dataset: ETL, Exploração & Redesign

## 1. Introdução

Descreva brevemente o propósito do projeto, importância do MERGE dataset, e os desafios enfrentados na versão original.

## 2. Objetivos

- Reestruturar e padronizar o MERGE dataset
- Facilitar o uso para análises de emoção em música
- Criar scripts para centralização e limpeza dos dados

## 3. Metodologia

### 3.1. Exploração Inicial do Dataset

- Análise dos arquivos originais, modalidades (audio, lyrics, bimodal) e variantes (balanced, complete)
- Identificação de inconsistências e fragmentações

### 3.2. Redesign do Schema

- Padronização de nomes de campos (song_id, artist, title, quadrant, etc.)
- Unificação dos splits (70-15-15, 40-30-30) nos masters

### 3.3. Scripts ETL

- Criação de scripts Python para consolidar os dados em arquivos master

## 4. Resultados
### 4.1. Análise da Distribuição de Classes e Emoções


![Figura 1: Distribuição por Quadrante Emocional](imagens_relatorio/figura1_quadrantes.png)
A análise da distribuição de classes (Figura 1) revela que o dataset é notavelmente balanceado, com uma contagem quase idêntica de músicas em cada um dos quatro quadrantes emocionais. Esta é uma característica ideal, pois previne o enviesamento do modelo de classificação para uma emoção específica.


![Figura 2: Dispersão Arousal x Valence](imagens_relatorio/figura2_dispersao_arousal_valence.png)
O gráfico de dispersão entre Arousal e Valence (Figura 2) valida a estrutura do dataset. Observam-se quatro agrupamentos distintos de dados, cada um correspondendo a um quadrante, o que demonstra a correlação direta entre os valores contínuos de emoção e as classes categóricas.


![Figura 3: Distribuição de Arousal e Valence](imagens_relatorio/figura3_distribuicao_arousal_valence.png)
Adicionalmente, a distribuição bimodal (dois picos) observada para os valores de Arousal e Valence (Figura 3) é consistente com o modelo de emoção em quadrantes, onde as músicas tendem a se agrupar em extremos de alta/baixa energia e positividade/negatividade.


### 4.2. Análise de Conteúdo e Metadados

![Figura 4: Top 15 Gêneros Musicais](imagens_relatorio/figura4_top_generos.png)
A análise de gêneros musicais (Figura 4) mostra uma predominância expressiva do gênero 'pop/rock'. Embora o dataset contenha uma variedade de gêneros, esta concentração sugere que qualquer modelo treinado com estes dados terá, provavelmente, um melhor desempenho e generalização para músicas dentro deste estilo.


![Figura 5: Top 10 Artistas](imagens_relatorio/figura5_top_artistas.png)
A lista dos artistas mais frequentes (Figura 5) revela uma diversidade de estilos musicais, abrangendo desde o Blues e Jazz clássico até o Heavy Metal, o que enriquece a variedade do dataset apesar da predominância do gênero pop/rock.


![Figura 6: Distribuição por Ano de Lançamento](imagens_relatorio/figura6_distribuicao_ano.png)
A Figura 6 mostra que o dataset possui uma grande variedade temporal, com músicas que abrangem muitas décadas, apesar da difícil legibilidade do eixo dos anos.


### 4.3. Análise de Integridade dos Dados


![Figura 7: Mapa de Dados Faltantes](imagens_relatorio/figura7_dados_faltantes.png)
O mapa de dados faltantes (Figura 7) indica que os campos centrais para a tarefa de classificação (ID da música e valores emocionais) estão 100% completos. No entanto, muitos metadados secundários, como 'themes' e 'styles', são esparsos. Uma observação crítica é a ausência de dados nas colunas de 'split', indicando um problema na consolidação deste subconjunto específico, o que exigiria atenção antes de treinar um modelo.





## 5. Discussão

- O que melhorou em relação ao dataset original?
- Como as visualizações ajudam a entender os dados?
- Limitações e possíveis melhorias futuras

## 6. Conclusão

Resumo do que foi alcançado e como o novo formato facilita futuras análises.

## 7. Anexos

- README.md do projeto
- Scripts principais (ETL e loader)

---

**Sugestão:**  
- Exporte imagens dos gráficos do notebook e cole no relatório (coloque legendas explicativas).
- Adapte textos e exemplos conforme sua experiência real com o dataset.
