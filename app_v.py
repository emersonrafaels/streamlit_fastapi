import streamlit as st
import numpy as np

class Chat_Score():

    def __init__(self):

        # OBTENDO OS VALORES DEFAULT
        self.actions, self.scores_default_criar, self.scores_default_visualizar = self.options_default()

    def options_default(self):

        # Opções de ação para o usuário
        actions = ["Criar/Editar um score",
                        "Visualizar pesos de um score existente"]

        # Opções - Score Criar/Editar
        scores_default_criar = ["Infra Civil"]

        # Opções - Score Criar/Editar
        scores_default_visualizar = ["Infra Civil",
                                          "Regulatório - Funcionamento Bancário"]

        return actions, scores_default_criar, scores_default_visualizar

    def main(self):

        with st.chat_message("assistant"):
            st.write("Olá, eu sou o Score Maker Assistant")

            # Opções de ação para o usuário
            action = st.selectbox("O que você gostaria de fazer?",
                                  options=self.actions)

            if action == self.actions[0]:
                actions_score = st.selectbox("Selecione qual score deseja criar/editar",
                                              options=self.scores_default_criar)
            else:
                actions_score = st.selectbox("Selecione qual score deseja visualizar",
                                             options=self.scores_default_visualizar)

if __name__ == '__main__':
    chat_score = Chat_Score()
    chat_score.main()