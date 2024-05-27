
<p align="center"><img src="https://img.shields.io/badge/Blinhares-white?logo=github&logoColor=181717&style=for-the-badge&label=git" /><p align="center">

# Recomendação Básica de Produtos

Este projeto se destina a das uma explicação breve de como funciona um sistema de recomendação e implementa-lo.

Existem diversas abordagem que podem ser utilizada, aqui vamos utilizar a abordagem de Popularidade nao qual recomendaremos produtos populares dado um certo item comprado.

Sabe aquele anuncio que surge quando voce vai comprar um item e aparece "Pessoas que compram isso, também compraram isso"? Pois, bem, é isso que vamos fazer.

Esse tipo de abordagem é uma abordagem simples, requer poucas informações e tem um grande potencial de uso.

Como um comerciante, o que voce faria se soubesse que se uma pessoa ao comprar banana, tem 90% de probabilidade de comprar aveia e 40% de probabilidade de comprar leite condensado. O que voce faria?

## Ferramentas Utilizadas

[![Python](https://img.shields.io/badge/PYTHON-white?style=for-the-badge&logo=python&logoColor=3776AB)](https://www.python.org/)
[![streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ](https://pandas.pydata.org/)

## Mão na Massa

Como comentado anteriormente, a abordagem adotada nesse projeto é uma abordagem simples para um assunto que pode ser bem complicado.

Apesar de ser uma abordagem simples, tentei deixar o código o mais legível possível com uma documentação e estrutura que facilite ao máximo o entendimento e a reutilização do código.

Nosso código funciona da seguinte maneira...

Declaramos uma lista de produtos, que neste caso foi:

```python
[
            'arroz',
            'feijão',
            'macarrão',
            'carne',
            'frango',
            'banana',
            'maçã',
            'cerveja',
            'refrigerante',
            'água',
        ]
```

Para simular nosso clientes e suas compras, realizamos uma escolha aleatória e sem repetição dos itens na lista acima e juntamos em um DataFrame. O número de vezes que isso é feito esta declarado na variável abaixo:

```python
self._num_carrinhos:int = 500
```

Como podem vez, simulamos 500 compras.

Agora vamos a nossa lógica!

Queremos saber com que frequência a pessoa que compra um produto A compra um produto B. Para isso seguimos os seguintes passos...

1. Pegamos o DataFrame com todas as compras e filtramos todos os carrinhos que possuíssem o produto A;

2. Percorremos todos os carrinhos listando todos os produtos e a frequência com que eles ocorrem;

3. Retornamos isso em um DataFrame para ser plotado.

Simplesmente isso.

Fique a vontade pra ver o código, talvez ele esclareça mais que minhas palavras.

## Utilização

### Clonando Repositório

```bash
git clone https://github.com/blinhares/sistema_recomendacao_de_produtos_por_frequencia.git
```

### Dependências

Existem algumas dependências necessárias para rodar o projeto, e vamos resolver isso facilmente com a instalação do poetry. Poetry é uma ferramenta interessante e recomendo conhece-la caso não tenha familiaridade.

```bash
pip install poetry
```

Acesse a pasta onde o repositório foi clonado. Estando na mesma pasta em que os arquivos `poetry.lock e pyproject.toml` execute o comando:

```bash
poetry install
```

Pronto, ambiente virtual criado e dependências instaladas.

### Rodando o WebApp

```bash
streamlit run sistema_recomendacao_de_produtos_por_frequencia/main.py
```
Ou

```bash
python -m streamlit run sistema_recomendacao_de_produtos_por_frequencia/main.py
```

Ou ainda melhor, pode rodar o script sem baixar como o comando:

```bash
streamlit run https://raw.githubusercontent.com/blinhares/sistema_recomendacao_de_produtos_por_frequencia/0cdc274d3413c581893506c8fe7fb096b13183fc/sistema_recomendacao_de_produtos_por_frequencia/main.py
```

### Como Funciona

![alt text](<https://github.com/blinhares/sistema_recomendacao_de_produtos_por_frequencia/blob/0cdc274d3413c581893506c8fe7fb096b13183fc/sistema_recomendacao_de_produtos_por_frequencia/Captura%20de%20tela%20de%202024-05-25%2022-02-27.png>)


O app tem a intenção de recomendar algo a partir do momento em que se tem algo no carrinho, logo, no campo `Adicione Produtos no Carrinho` deve-se adicionar 'produtos ao carrinho' e, como retorno o app vai mostrando, de maneira ranqueada, os produtos com maior probabilidade de serem adquiridos de acordo com as informações geradas pelo algorítimo.

__Atenção__
 Voce vai observar que os produtos nao mostram muita distinção probabilística entre um produto e outro. Isso se da porque o computador nao possui preferencia por produtos A ou B, os carrinhos foram gerados aleatoriamente mas em um caso real essas diferenças vao ser mais significativos uma vez que o comportamento humano tende a ser mais 'tendencioso'.

  ![visitors](https://visitor-badge.laobi.icu/badge?page_id=blinhares.sistema_recomendacao_de_produtos_por_frequencia)
