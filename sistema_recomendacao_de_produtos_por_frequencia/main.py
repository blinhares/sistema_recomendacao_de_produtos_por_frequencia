import streamlit as st
from recomenda_produto import RecomendaProdutos
import altair as alt

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.markdown('''
Sabe aquele anuncio que surge quando voce vai comprar um item e aparece "Pessoas que compram isso, também compraram isso"? Pois, bem, é isso que vamos fazer aqui.

Para mais detalhes click no botão abaixo:
            
[![Bruno](https://img.shields.io/badge/Blinhares-white?logo=github&logoColor=181717&style=for-the-badge&label=git)](https://github.com/blinhares/)
            
''')

st.header('Recomendação de Produtos',
          divider='rainbow')


rec = RecomendaProdutos()

lista_produtos = rec._list_produtos # type: ignore


produtos = st.multiselect(
    label='Adicione Produtos no Carrinho',
    options=lista_produtos,
    default=lista_produtos[1:3])

df = rec.retornar_sujestoes(produtos)
df.reset_index(inplace=True)

c = (
alt.Chart(df)
.mark_bar()# type: ignore
.encode( 
    alt.X("Produto",sort='-y'),y="%") # type: ignore
).interactive()

st.altair_chart(c, use_container_width=True)

st.markdown(
    '[![Bruno](https://img.shields.io/badge/Blinhares-white?logo=github&logoColor=181717&style=for-the-badge&label=git)](https://github.com/blinhares/)')
