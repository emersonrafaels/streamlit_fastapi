import streamlit as st
import requests

def send_data_to_api(name, description, price, tax):
    url = "http://localhost:8000/items/"
    data = {
        "name": name,
        "description": description,
        "price": price,
        "tax": tax
    }
    response = requests.post(url, json=data)
    return response.json()

def main():
    st.title('Aplicativo Streamlit Integrado com FastAPI')

    with st.form("my_form"):
        name = st.text_input("Nome do Produto")
        description = st.text_input("Descrição do Produto")
        price = st.number_input("Preço do Produto", format="%.2f", step=0.01)
        tax = st.number_input("Imposto sobre o Produto", format="%.2f", step=0.01)
        submitted = st.form_submit_button("Enviar para API")

        if submitted:
            response = send_data_to_api(name, description, price, tax)
            st.write("Resposta da API:")
            st.json(response)

if __name__ == '__main__':
    main()
