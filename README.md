# Vídeos das apresentações
 - [Apresentação de Trabalho da disciplina: Processamento de Linguagem Natural com Deep Learning](https://www.youtube.com/watch?v=DQalRiW9tkQ)
 - [Script do Webscraper em funcionamento](https://www.youtube.com/watch?v=WFKFqMN_Fr8)

# NPL Reviews Steam

Este projeto combina a coleta de reviews da Steam com abordagens de aprendizado de máquina e processamento de linguagem natural (NLP). Ele oferece ferramentas para realizar análise de sentimentos, classificação de texto e experimentações com modelos de aprendizado.

## Estrutura do Projeto

O repositório está organizado da seguinte forma:

- `notebooks/` - Contém notebooks Jupyter/Colab com experimentos de NPL:
  - **SVM+bow+embeddings.ipynb**: Modelo SVM utilizando dados pré processados com: Bag-of-Words, embeddings com TF-IDF e Word2Vec. Link para google colab: [svm+bow+embeddings](https://colab.research.google.com/drive/1OJoI-slaaax2ZpWLYi3a8OadJDvzbbQN#scrollTo=VN5gq_1mOEI9)
  - **BERT.ipynb**: Experimento com modelo BERT.  Link para google colab: [bert-google-colab](https://colab.research.google.com/drive/13vYXu-FyJ8zq3pPHa2Tr1mks4Rljcd0f)
  - **in_context_learning_(LLMs).ipynb**: Testes usando uma api de LLM's nas classificações de reviews, com a API da OpenAI utilizando o gpt-3.5. Link para google colab:  [in_context_learning](https://colab.research.google.com/drive/1-Bu2zmMsbN2ijYPrHuQpYQqmCc1r1mI2)

- `steam-review-collection-bot/` - Webscraper para raspagem das reviews no website de Steam:
  - **main.py**: Ponto de entrada para o bot de coleta.
  - `service/steam_scraper.py`: Service responsável pela extração de reviews da Steam.
  - **requirements.txt**: Dependências necessárias para execução.

- `review_data_Cyberpunk_2077.json` - Dados de reviews coletados como exemplo.

- `webdrivers/` - Contém o WebDriver para automação com Selenium.

## Requisitos

- **Python 3.10+**
- WebDriver compatível com o navegador utilizado.
- Dependências listadas no `requirements.txt`.

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/npl-reviews-steam.git
   cd npl-reviews-steam
   ```

2. Instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r steam-review-collection-bot/requirements.txt
   ```

3. Caso o WebDriver não seja compatível com seu navegador atual, baixe um WebDriver compatível e substitua o atual na pasta webdrivers.

## Uso

### Coleta de Reviews
Para iniciar o bot de coleta:
```bash
python steam-review-collection-bot/main.py
```
Certifique-se de configurar o WebDriver e ajustar os parâmetros no script, como o tipo do review o idioma a quantidade de amostrar e nome do arquivo de dataset.

### Execução dos Notebooks
Os notebooks estão localizados na pasta `notebooks/` e podem ser abertos com Jupyter Notebook ou JupyterLab:
```bash
pip install notebook
jupyter notebook notebooks/
```

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:
1. Realize um fork do repositório.
2. Crie um branch para sua feature/correção: `git checkout -b minha-feature`.
3. Envie um pull request com uma descrição clara da sua contribuição.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
