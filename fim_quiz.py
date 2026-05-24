import streamlit as st
import time

def mostrar_final():

    st.balloons()
    st.header("Fim do Game")
    st.subheader(f"Pontuação: {st.session_state.pontos} de 7")
    st.subheader("Agradecemos a sua participação!") 
    st.write("")
    st.write("CRÉDITOS:")   
    st.write("- Sistema criado para a exposição da História da Computação em Python com a biblioteca Streamlit")  
    st.write("- Efeitos sonoros por freesound_community, Christianne Santos, KindKinder do Pixabay")   
    st.write("- Imagens criadas por inteligência artificial generativa (Gemini) sob avaliação humana")
    st.write("- Curiosidades criadas com apoio de inteligência artificial generativa (ChatGPT) sob avaliação humana") 
    st.write("")
   

    # Botão reiniciar
    if st.button("REINICIAR QUIZ"):
        st.session_state.pagina = 1
        st.session_state.pontos = 0
        st.rerun()
    else:
         st.write("(O quiz será reiniciado automaticamente em 30 segundos)")
         time.sleep(30)
         st.session_state.pagina = 1
         st.session_state.pontos = 0
         st.rerun()

   