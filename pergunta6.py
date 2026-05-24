import streamlit as st

def mostrar():

    st.write("Pergunta 6: Que som é esse?")

    audio_file = open("sons\som6.mp3", "rb")

    st.audio(audio_file.read(), format="audio/mp3")

    # Variável inicial
    st.session_state.acerto = None

    col1, col2= st.columns(2)

    with col1:

        if st.button("A) Sons do MSN Messenger"):
            st.session_state.acerto = True
            st.session_state.pontos += 1
            
        if st.button("B) Sons do jogo Paciência"):
            st.session_state.acerto = False
           

    with col2:

        if st.button("C) Sons do ICQ"):
            st.session_state.acerto = False

        if st.button("D) Sons do Skype"):
            st.session_state.acerto = False
            
          
    if st.session_state.acerto==True:
        st.success("Resposta Correta!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens\som6.png", width=300)
        with col2: 
           st.markdown("""
                        ### Sons do MSN Messenger
                       O MSN Messenger marcou uma geração com seus sons característicos de login, envio de mensagens e notificações de conversa. 
                       Muito popular nos anos 2000, o programa se tornou um símbolo da comunicação online da época, principalmente entre 
                       adolescentes e estudantes. Muitos usuários personalizavam status, emoticons e até os toques das conversas, tornando os sons 
                       do MSN facilmente reconhecíveis e associados ao início das redes sociais e da comunicação instantânea pela internet.
                        """)
        #if st.button("Próxima Pergunta"):
         #st.session_state.pagina = 4
           # st.rerun()
        
    elif st.session_state.acerto == False:
        st.error("Resposta Errada!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens\som6.png", width=300)
        with col2: 
           st.markdown("""
                        ### Sons do MSN Messenger
                        O MSN Messenger marcou uma geração com seus sons característicos de login, envio de mensagens e notificações de conversa. 
                       Muito popular nos anos 2000, o programa se tornou um símbolo da comunicação online da época, principalmente entre 
                       adolescentes e estudantes. Muitos usuários personalizavam status, emoticons e até os toques das conversas, tornando os sons 
                       do MSN facilmente reconhecíveis e associados ao início das redes sociais e da comunicação instantânea pela internet.
                        """)

    if st.button(">>"):
        st.session_state.pagina = 7
        st.rerun()  
    
    
    
    
  