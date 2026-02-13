from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain.chat_models import init_chat_model
import os

# LLM interaction function
def get_expert_advice(user_input, expert_type):
    """
    Get advice from an LLM based on the user input and selected expert type.

    Args:
        user_input (str): The question or input text from the user.
        expert_type (str): The type of expert selected by the user.

    Returns:
        str: The response from the LLM.
    """
    # Define system messages based on expert type
    system_messages = {
        "心理学の専門家": "あなたは心理学の専門家です。心理学に関する質問に答えてください。",
        "栄養学の専門家": "あなたは栄養学の専門家です。栄養に関する質問に答えてください。"
    }

    # Initialize the LLM
    model = init_chat_model("gpt-4")

    # Create the conversation messages
    system_message = system_messages.get(expert_type, "")
    prompt = f"{system_message}\n質問: {user_input}\n回答:"

    # Get the response from the LLM
    response = model.invoke(prompt)
    return response

# Streamlit app
st.title("専門家のアドバイスを得るアプリ")

st.write("このアプリでは、以下の専門家からアドバイスを得ることができます：")
st.write("- 心理学の専門家\n- 栄養学の専門家")
st.write("ラジオボタンで専門家を選択し、質問を入力してください。")
st.write("送信ボタンを押すと、専門家からのアドバイスが表示されます。")

selected_item = st.radio(
    "専門家を選んでください。", ["心理学の専門家", "栄養学の専門家"]
)

st.divider()

user_input = st.text_input("質問を入力してください。")
if st.button("送信"):
    if user_input.strip():
        try:
            # Get advice from the selected expert
            advice = get_expert_advice(user_input, selected_item)
            st.write(f"### {selected_item}の回答:")
            st.write(advice)
        except Exception as e:
            st.error(f"エラーが発生しました: {str(e)}")
    else:
        st.warning("質問を入力してください！")

