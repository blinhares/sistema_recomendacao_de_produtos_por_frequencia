import streamlit as st
from recomenda_produto import RecomendaProdutos
from sistema_recomendacao_de_produtos_por_frequencia.code.qr_code_generator import add_qr_code_to
from sistema_recomendacao_de_produtos_por_frequencia.code.get_ip import get_local_ip

import altair as alt
from PIL import Image

def add_qr_code_addrs_to(
        _st,
        _caption="QR Code",
        _use_column_width=True):
    
    local_addrs =f"http://{get_local_ip()}:8501"


    add_qr_code_to(
        _st,
        local_addrs,
        'meu_ip_qr.png',
        _caption,
        _use_column_width)

def main():
    # Add a sidebar_description:
    add_sidebar_description = st.sidebar.markdown('''
    Sabe aquele anuncio que surge quando voce vai comprar um item e aparece "Pessoas que compram isso, também compraram isso"? Pois, bem, é isso que vamos fazer aqui.

    Para mais detalhes click no botão abaixo:

    [![Bruno](https://img.shields.io/badge/Blinhares-white?logo=github&logoColor=181717&style=for-the-badge&label=git)](https://github.com/blinhares/)

    ''')
    add_qr_code_addrs_to(
        st.sidebar,
        'Leia Este QrCode Para ter Acesso em Outros Dispositivos Locais',
        True)
    
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

if __name__ == "__main__":
    main()