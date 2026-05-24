import streamlit as st

import pergunta1

import pergunta2

import pergunta3

import pergunta4

import pergunta5

import pergunta6

import pergunta7

import fim_quiz

st.markdown("""
<style>

p, h1, h2, h3 {
    text-shadow: 0 0 5px #00FF00;
}

</style>
""", unsafe_allow_html=True)

st.title("HISTÓRIA DA COMPUTAÇÃO")
st.markdown("## Sons & Nostalgia")

# Guarda a página atual
if "pagina" not in st.session_state:
    st.session_state.pagina = 1

# Guarda pontuação
if "pontos" not in st.session_state:
    st.session_state.pontos = 0

# Decide qual pergunta mostrar
if st.session_state.pagina == 1:
    pergunta1.mostrar()

elif st.session_state.pagina == 2:
    pergunta2.mostrar()

elif st.session_state.pagina == 3:
   pergunta3.mostrar()

elif st.session_state.pagina == 4:
   pergunta4.mostrar()

elif st.session_state.pagina == 5:
   pergunta5.mostrar()

elif st.session_state.pagina == 6:
   pergunta6.mostrar()

elif st.session_state.pagina == 7:
   pergunta7.mostrar()
   
else:
    fim_quiz.mostrar_final()
    
