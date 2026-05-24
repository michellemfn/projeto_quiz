import streamlit as st

def mostrar():

    st.write("Pergunta 4: Que som é esse?")

    audio_file = open("sons\som4.mp3", "rb")

    st.audio(audio_file.read(), format="audio/mp3")

    # Variável inicial
    st.session_state.acerto = None

    col1, col2= st.columns(2)

    with col1:

        if st.button("A) Fita Cassete Avançando"):
            st.session_state.acerto = False

        if st.button("B) Documento enviado via Fax"):
            st.session_state.acerto = False

    with col2:

        if st.button("C) Digitação de comando no MS-DOS"):
            st.session_state.acerto = False

        if st.button("D) Discagem em Telefone Antigo"):
            st.session_state.acerto = True
            st.session_state.pontos += 1
            
          
    if st.session_state.acerto==True:
        st.success("Resposta Correta!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens\som4.png", width=300)
        with col2: 
           st.markdown("""
                        ### Discagem em Telefone Antigo
                        O Telefone de disco funcionava por meio de pulsos mecânicos enviados 
                        pela linha telefônica. Cada número girado no disco gerava uma quantidade
                        específica de pulsos, criando o famoso som ritmado da discagem. Esse áudio 
                        tornou-se um dos sons mais marcantes da história das telecomunicações e 
                       ainda desperta nostalgia em muitas pessoas.
                        """)
        #if st.button("Próxima Pergunta"):
         #st.session_state.pagina = 4
           # st.rerun()
        
    elif st.session_state.acerto == False:
        st.error("Resposta Errada!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens\som4.png", width=300)
        with col2: 
           st.markdown("""
                        ### Discagem em Telefone Antigo
                        O Telefone de disco funcionava por meio de pulsos mecânicos enviados 
                        pela linha telefônica. Cada número girado no disco gerava uma quantidade
                        específica de pulsos, criando o famoso som ritmado da discagem. Esse áudio 
                        tornou-se um dos sons mais marcantes da história das telecomunicações e 
                       ainda desperta nostalgia em muitas pessoas. 
                        """)

    if st.button(">>"):
        st.session_state.pagina = 5
        st.rerun()  
    
    
    
    
  