import requests
import streamlit as st

def get_mistral_responses(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={"input":{'topic':input_text}})
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
    return response.json().get('output', {}).get('content', 'No content found')


def get_gemma_responses(input_text):
    response = requests.post("http://localhost:8001/poem/invoke",
                             json={"input":{'topic':input_text}})
    return response.json()['output']['content']

st.title('LANGCHAIN DEMO USING APIS')
input_text = st.text_input("Write an essay on : ")
input_text1 = st.text_input("Write a poem on : ")

if input_text:
    st.write(get_mistral_responses(input_text))

if input_text1:
    st.write(get_gemma_responses(input_text1))