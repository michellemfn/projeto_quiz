import streamlit as st

def mostrar():

    st.write("Pergunta 2: Que som é esse?")
    #primeiro som 

    audio_file = open("sons\som2.mp3", "rb")

    st.audio(audio_file.read(), format="audio/mp3")

    # Variável inicial
    st.session_state.acerto = None

    col1, col2= st.columns(2)

    with col1:

        if st.button("A) Impressora laser aquecendo"):
            st.session_state.acerto = False

        if st.button("B) Avanço de papel contínuo"):
            st.session_state.acerto = False
            

    with col2:

        if st.button("C) Impressora ejetando folha"):
            st.session_state.acerto = False

        if st.button("D) Impressão a jato de tinta"):
            st.session_state.acerto = True
            st.session_state.pontos += 1

            
          
    if st.session_state.acerto==True:
        st.success("Resposta Correta!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens\som2.png", width=300)
        with col2: 
           st.markdown("""
                        ### Impressora a Jato de Tinta
                        A Impressora jato de tinta tornou-se muito popular nos anos 1990 e 2000. Seu som característico
                        do cabeçote se movendo rapidamente marcou a rotina de quem utilizava computadores naquela época. 
                        Representou um avanço na qualidade de impressão, permitindo criar textos e imagens coloridas com mais definição.
                        Também ficou conhecida pela preocupação com troca frequente de cartuchos de tinta.  
                        """)
        #if st.button("Próxima Pergunta"):
         #   st.session_state.pagina = 3
          #  st.rerun() 
        
    elif st.session_state.acerto == False:
        st.error("Resposta Errada!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens\som2.png", width=300)
        with col2: 
           st.markdown("""
                        ### Impressora a Jato de Tinta
                        A Impressora jato de tinta tornou-se muito popular nos anos 1990 e 2000. Seu som característico
                        do cabeçote se movendo rapidamente marcou a rotina de quem utilizava computadores naquela época. 
                        Representou um avanço na qualidade de impressão, permitindo criar textos e imagens coloridas com mais definição.
                        Também ficou conhecida pela preocupação com troca frequente de cartuchos de tinta.  
                        """)
    
    if st.button(">>"):
        st.session_state.pagina = 3
        st.rerun() 
    
    
    
    
  