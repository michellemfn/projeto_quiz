import streamlit as st

def mostrar():

    st.write("Pergunta 5: Que som é esse?")

    audio_file = open("sons\som5.mp3", "rb")

    st.audio(audio_file.read(), format="audio/mp3")

    # Variável inicial
    st.session_state.acerto = None

    col1, col2= st.columns(2)

    with col1:

        if st.button("A) Máquina de escrever elétrica digitando texto"):
            st.session_state.acerto = False

        if st.button("B) Leitor de cartão perfurado processando dados"):
            st.session_state.acerto = False

    with col2:

        if st.button("C) Impressora matricial imprimindo em formulário contínuo"):
            st.session_state.acerto = True
            st.session_state.pontos += 1

    

        if st.button("D) Scanner realizando digitalização rápidao"):
            st.session_state.acerto = False
            
          
    if st.session_state.acerto==True:
        st.success("Resposta Correta!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens\som5.png", width=300)
        with col2: 
           st.markdown("""
                        ### Impressora matricial imprimindo formulário contínuo
                       A Impressora matricial ficou famosa pelo som alto e repetitivo produzido 
                       durante a impressão. Diferente das impressoras modernas, ela utilizava pequenas 
                       agulhas que batiam contra uma fita com tinta para formar os caracteres no papel.
                       Muito usada em bancos, mercados e escritórios nas décadas de 1980 e 1990, também era 
                       conhecida pelo uso de formulários contínuos com folhas conectadas por serrilhas laterais.
                        """)
        #if st.button("Próxima Pergunta"):
         #st.session_state.pagina = 4
           # st.rerun()
        
    elif st.session_state.acerto == False:
        st.error("Resposta Errada!")
        col1, col2= st.columns(2)
        with col1:
            st.image("imagens\som5.png", width=300)
        with col2: 
           st.markdown("""
                        ### Impressora matricial imprimindo formulário contínuo
                       A Impressora matricial ficou famosa pelo som alto e repetitivo produzido 
                       durante a impressão. Diferente das impressoras modernas, ela utilizava pequenas 
                       agulhas que batiam contra uma fita com tinta para formar os caracteres no papel.
                       Muito usada em bancos, mercados e escritórios nas décadas de 1980 e 1990, também era 
                       conhecida pelo uso de formulários contínuos com folhas conectadas por serrilhas laterais.
                        """)

    if st.button(">>"):
        st.session_state.pagina = 6
        st.rerun()  
    
    
    
    
  