import streamlit as st
import pandas as pd
# para download de arquivo


def main():

    st.image('auctus_logo.png', width=200)
    #st.title('AUCTUS.ai - Inteligência Aumentada')
    st.title('Consulte o PREÇO: café')
    st.image('cafe.jpg', width=300)
    #st.header('Aplicação StreamLit gerada em Python')
    #st.subheader('Explorando funcionalidades')
    #st.text('Podemos fazer importação, manipulação, visualização interativa e modelagem de dados')

    if True:
        
        st.markdown('''

        _____________

        **Consultoria de preços**:

        * *Tipo* = tipo do seu café

        * *Estoque* = valor em função do estoque

        * *Quantidade* = quantidade de café

        * *Local (imposto)* = imposto de acordo com local

        ''')


    st.markdown('''
    	____________________
    	''')


    # criando botão
    check = st.checkbox('Ver valor do dólar')
    # se cliquei no botao:
    if check:
        st.markdown('Dólar = R$5.37')

    st.markdown('_____')


    # lista de opções
    st.markdown('### Tipo do café:')
    listaOpcoes = st.radio('escolha as opções', ('claro', 'marrom','escuro'))

    tipoCafe = 0
    if listaOpcoes == 'claro':
        st.markdown('**claro** escolhido!')
        tipoCafe=1

    if listaOpcoes == 'marrom':
        st.markdown('**marrom** escolhido!')
        tipoCafe=2

    if listaOpcoes == 'escuro':
        st.markdown('**escuro** escolhido!')
        tipoCafe=3


    st.markdown('_____')


    # lista de opções
    st.markdown('### Estoque:')
    listaOpcoes = st.selectbox('escolha as opções', ('pequeno', 'médio','grande'))

    estoque=0

    if listaOpcoes == 'pequeno':
        st.markdown('**pequeno** escolhido!')
        estoque=1

    if listaOpcoes == 'médio':
        st.markdown('**médio** escolhido!')
        estoque=2

    if listaOpcoes == 'grande':
        st.markdown('**grande** escolhido!')
        estoque=3

    st.markdown('_____')

    st.markdown('Quantidade (kg):')
    quantidade = st.slider('Escolha a quantidade de café:', min_value=1, max_value=1000)

    st.markdown('_____')

    calculo = tipoCafe * estoque * quantidade
    st.markdown('## **Preço calculado:** R$'+str(calculo))




if __name__ == '__main__':
	main()
