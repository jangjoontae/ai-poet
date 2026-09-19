import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import time

# api_key 
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

st.title("_AI 시인_ :sunglasses:")

title = st.text_input("시의 주제를 입력하세요", "가을")
st.write("시의 주제는 ", title)

if st.button("시 작성"):
  with st.spinner("Wait for it...", show_time=True):
    # LLM 모델 생성
    model = init_chat_model(
      "gpt-5.5",
      timeout=120,
      max_tokens=1000,
      max_retries=10,  # Default; increase for unreliable networks
      api_key = api_key
    )

    # prompt 생성
    prompt = ChatPromptTemplate.from_messages([
      ('system', "You are a helpful assistant"),
      ('user', '{input}')
    ])
    # output parser and chain
    chain = prompt | model | StrOutputParser()
    # chain invoke + response 출력
    response = chain.invoke({"input":title+" 에 대한 시를 작성해줘"})
    st.write(response)
    
  st.button("rerun")
