import streamlit as st

def mostrar():

    st.write("Pergunta 3: Que som é esse?")

    audio_file = open("sons/som3.mp3", "rb")

    st.audio(audio_file.read(), format="audio/mp3")

    # Variável inicial
    st.session_state.acerto = None

    col1, col2= st.columns(2)

    with col1:

        if st.button("A) HD antigo realizando leitura de inicialização"):
            st.session_state.acerto = False

        if st.button("B) Rádio comunicador sincronizando frequência"):
            st.session_state.acerto = False
            

    with col2:

        if st.button("C) Drive de disquete acessando arquivos do sistema"):
            st.session_state.acerto = False

        if st.button("D) Tentativa de Conexão em Internet Discada"):
            st.session_state.acerto = True
            st.session_state.pontos += 1
            
          
    if st.session_state.acerto==True:
        st.success("Resposta Correta!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens/som3.png", width=300)
        with col2: 
           st.markdown("""
                        ### Tentativa de Conexão em Internet Discada
                        O som da Internet discada era produzido pela comunicação entre o modem do computador 
                       e a central telefônica durante o processo de conexão. Aqueles ruídos metálicos e chiados 
                       representavam a troca de sinais digitais pela linha telefônica comum. Nos anos 1990 e 
                       início dos 2000, esse áudio tornou-se um símbolo da chegada da internet às casas, 
                       embora também fosse lembrado pela lentidão da conexão e pelo fato de ocupar a
                       linha telefônica enquanto estava em uso. 
                        """)
        #if st.button("Próxima Pergunta"):
         #st.session_state.pagina = 4
           # st.rerun()
        
    elif st.session_state.acerto == False:
        st.error("Resposta Errada!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens/som3.png", width=300)
        with col2: 
           st.markdown("""
                        ### Tentativa de Conexão em Internet Discada
                         O som da Internet discada era produzido pela comunicação entre o modem do computador 
                       e a central telefônica durante o processo de conexão. Aqueles ruídos metálicos e chiados 
                       representavam a troca de sinais digitais pela linha telefônica comum. Nos anos 1990 e 
                       início dos 2000, esse áudio tornou-se um símbolo da chegada da internet às casas, 
                       embora também fosse lembrado pela lentidão da conexão e pelo fato de ocupar a
                       linha telefônica enquanto estava em uso.   
                        """)

    if st.button(">>"):
        st.session_state.pagina = 4
        st.rerun()  
    
    
    
    
  