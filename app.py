import streamlit as st

def message_default():

    # INICIANDO A MENSAGEM DEFAULT
    message_default = [{"role": "assistant",
                        "content": "Olá, eu sou o Score Maker Assistant"}]

    # Opções de ação para o usuário
    actions = ["Definir um novo score", "Editar um score existente"]
    action = st.selectbox("O que você gostaria de fazer?", options=actions)

def clear_chat_history():
    st.session_state.messages = message_default

# INICIANDO A SESSION STATE DE MENSAGENS
if "messages" not in st.session_state.keys():
    st.session_state.messages = message_default

# INSERINDO AS MENSAGENS
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# CRIANDO O BOTÃO PARA LIMPAR A CONVERSA - SIDEBAR
st.sidebar.button('Limpar conversa', on_click=clear_chat_history)

# ESPAÇO PARA O PROMPT
if prompt := st.chat_input():
    # SALVANDO A MENSAGEM DO USUÁRIO
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = "Resultado"
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)