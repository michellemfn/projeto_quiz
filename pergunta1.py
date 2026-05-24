import streamlit as st

def mostrar():
    
    st.write("Pergunta 1: Que som é esse?")
    #primeiro som 

    audio_file = open("sons\som1.mp3", "rb")

    st.audio(audio_file.read(), format="audio/mp3")

    # Variável inicial
    if "acerto" not in st.session_state:
        st.session_state.acerto = None

    col1, col2= st.columns(2)

    with col1:

        if st.button("A) Vírus detectado"):
            st.session_state.acerto = False

        if st.button("B) Erro do Windows"):
            st.session_state.acerto = True
            st.session_state.pontos += 1

    with col2:

        if st.button("C) Internet não conectou"):
            st.session_state.acerto = False

        if st.button("D) Arquivo corrompido"):
            st.session_state.acerto = False
            
        
    if st.session_state.acerto==True:
        st.success("Resposta Correta!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens\som1.png", width=300)
        with col2: 
            st.markdown("""
                            ### Som de Erro do Windows
                            O clássico som de erro do **Windows**
                            tornou-se um dos efeitos sonoros mais conhecidos da computação.
                            Presente principalmente nas versões Windows 95, 98 e XP, ele era 
                            reproduzido quando ocorria algum problema no sistema, como comandos inválidos, 
                            falhas de abertura ou mensagens de alerta. 
                            """)
        
    elif st.session_state.acerto == False:
        st.error("Resposta Errada!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens\som1.png", width=300)
        with col2: 
            st.markdown("""
                        ### Som de Erro do Windows
                        O clássico som de erro do **Windows**
                        tornou-se um dos efeitos sonoros mais conhecidos da computação.
                        Presente principalmente nas versões Windows 95, 98 e XP, ele era 
                        reproduzido quando ocorria algum problema no sistema, como comandos inválidos, 
                        falhas de abertura ou mensagens de alerta. 
                        """)

    if st.button(">>"):
        st.session_state.pagina = 2
        st.rerun() 
    
   
    
    
    
  