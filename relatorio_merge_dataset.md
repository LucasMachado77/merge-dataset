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

- Estrutura final dos arquivos master (listar todos os arquivos gerados)
- Visualizações (inserir as imagens exportadas do notebook, com breve descrição)
    - Exemplo: Distribuição dos quadrantes, splits, arousal/valence...

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
