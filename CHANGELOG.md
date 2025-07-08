# Changelog

## [1.0.0] - 2025-07-09

### Adicionado (Added)

-   Estrutura inicial do projeto com pastas para `/data`, `/metadata`, `/scripts`, e `/schema`.
-   Scripts ETL em formato de Jupyter Notebook para extrair, transformar e carregar os dados dos subconjuntos originais do MERGE.
-   Criação de ficheiros `master_metadata` consolidados, unificando os dados de metadados, emoção e splits.
-   Módulo Python `scripts/loader.py` com a função `load_merge_master` para carregar e filtrar os dados de forma programática.
-   Notebook de Análise Exploratória de Dados (`scripts/EDA.ipynb`) com visualizações detalhadas sobre as distribuições de classes, conteúdo e integridade do dataset.
-   Dicionário de dados (`schema/data_dictionary.md`) documentando o schema dos novos ficheiros de metadados.
-   Relatório final do projeto (`relatorio_merge_dataset.pdf`) com a metodologia, resultados e discussão do trabalho realizado.
-   `README.md` completo com a descrição do projeto e instruções de uso.