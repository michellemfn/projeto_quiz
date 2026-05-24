import streamlit as st

def mostrar():

    st.write("Pergunta 7: Que som é esse?")

    audio_file = open("sons/som7.mp3", "rb")

    st.audio(audio_file.read(), format="audio/mp3")

    # Variável inicial
    st.session_state.acerto = None

    col1, col2= st.columns(2)

    with col1:

        if st.button("A) Gravação em Hard Disk"):
            st.session_state.acerto = False

        if st.button("B) Gravação em Disquete"):
            st.session_state.acerto = True
            st.session_state.pontos += 1

    with col2:

        if st.button("C) Leitura de CD-ROM"):
            st.session_state.acerto = False

        if st.button("D) Leitura de um DVD"):
            st.session_state.acerto = False
            
          
    if st.session_state.acerto==True:
        st.success("Resposta Correta!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens/som7.jpg", width=300)
        with col2: 
           st.markdown("""
                        ### Gravação em Disquete
                       O Disquete (Floppy Disk) foi um dos principais meios de armazenamento de dados entre as décadas de 1980 e 2000.
                        Apesar de possuir pouca capacidade comparada aos padrões atuais, ele era amplamente utilizado 
                       para salvar trabalhos, jogos e programas. Seu formato mais famoso, o de 3½ polegadas, tornou-se 
                       tão icônico que o símbolo de “salvar” presente em muitos softwares até hoje continua representado 
                       pela imagem de um disquete. instantânea pela internet.
                        """)
        #if st.button("Próxima Pergunta"):
         #st.session_state.pagina = 4
           # st.rerun()
        
    elif st.session_state.acerto == False:
        st.error("Resposta Errada!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens/som7.jpg", width=300)
        with col2: 
           st.markdown("""
                        ### Gravação em Disquete
                       O Disquete (Floppy Disk) foi um dos principais meios de armazenamento de dados entre as décadas de 1980 e 2000.
                        Apesar de possuir pouca capacidade comparada aos padrões atuais, ele era amplamente utilizado 
                       para salvar trabalhos, jogos e programas. Seu formato mais famoso, o de 3½ polegadas, tornou-se 
                       tão icônico que o símbolo de “salvar” presente em muitos softwares até hoje continua representado 
                       pela imagem de um disquete.
                        """)

    if st.button(">>"):
        st.session_state.pagina = 8
        st.rerun()  
    
    
    
    
  