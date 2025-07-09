# Projeto 1: ETL, Exploração e Redesign do MERGE Dataset

Este projeto realiza um processo completo de Engenharia de Dados sobre o MERGE Dataset, um conjunto de dados para Reconhecimento de Emoção em Música. O trabalho inclui a extração, transformação e carga (ETL) dos dados originais, a refatoração da sua estrutura, a criação de um loader modular e uma análise exploratória detalhada.

## 1. Estrutura do Projeto

O repositório está organizado da seguinte forma:

-   **/data**: Pasta designada para conter os dados brutos do MERGE dataset após o download.
-   **/metadata**: Armazena os ficheiros de metadados consolidados e padronizados (`master_metadata_...csv`) gerados pelo processo de ETL.
-   **/scripts**: Contém todos os scripts e notebooks de processamento.
    -   `loader.py`: Módulo principal para carregar os dados consolidados de forma flexível.
    -   `EDA.ipynb`: Notebook com a Análise Exploratória de Dados.
    -   `conferir_existencia.ipynb`: Script de validação para verificar a integridade referencial entre os metadados e os ficheiros de dados.
    -   Notebooks de ETL (`audio_balanced.ipynb`, `lyrics_complete.ipynb`, etc.): Scripts responsáveis por transformar os dados brutos nos ficheiros master da pasta `/metadata`.
-   **/schema**: Inclui o dicionário de dados (`data_dictionary.md`).
-   **/imagens_relatorio**: Contém as visualizações geradas e utilizadas no relatório.
-   `relatorio_merge_dataset.md`: O ficheiro fonte em Markdown do relatório final do projeto.
-   `relatorio_merge_dataset.pdf`: O ficheiro PDF do relatório final do projeto.
-   `CHANGELOG.md`: Registo de alterações e versões do projeto.
-   `README.md`: Este ficheiro. Apresenta uma visão geral do projeto e as instruções de uso.

## 2. Como Executar o Projeto

### Pré-requisitos

Certifique-se de que tem Python 3 e o ambiente Jupyter instalados. As principais bibliotecas utilizadas são:

-   pandas
-   matplotlib
-   seaborn

Pode instalar todas as dependências com o seguinte comando:

```bash
pip install pandas matplotlib seaborn jupyterlab
```

### Ordem de Execução

1.  **(Opcional) Executar os Scripts de ETL:** Os ficheiros `master_metadata_...csv` já estão gerados e incluídos na pasta `/metadata`. Se quiser gerá-los novamente, execute os notebooks correspondentes na pasta `/scripts` (ex: `audio_balanced.ipynb`). *Nota: será necessário ajustar os caminhos dos ficheiros de dados brutos dentro de cada notebook.*

2.  **Executar a Análise Exploratória:**
    * Abra o ambiente Jupyter Lab ou Jupyter Notebook na pasta raiz do projeto.
    * Navegue e abra o ficheiro `EDA.ipynb`.
    * No menu, selecione `Run` > `Run All Cells` para executar a análise e gerar todas as visualizações.

### Usando o Loader

O script `scripts/loader.py` permite carregar qualquer subconjunto de dados de forma programática.

**Exemplo de uso:**

```python
from scripts.loader import load_merge_master

# Carregar o subconjunto de áudio balanceado
df = load_merge_master('metadata/master_metadata_audio_balanced.csv')

# Carregar apenas os dados de treino do quadrante 1
df_filtrado = load_merge_master(
    'metadata/master_metadata_audio_balanced.csv',
    split='train',
    split_type='split_70_15_15',
    quadrant=1
)

print(df_filtrado.head())
```

## 3. Relatório Final

O relatório detalhado do projeto, incluindo a análise das visualizações, pode ser encontrado no ficheiro `relatorio_merge_dataset.md` e a sua versão final em `relatorio_merge_dataset.pdf`.