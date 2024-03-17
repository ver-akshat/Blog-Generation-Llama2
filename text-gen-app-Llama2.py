import streamlit as st
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate

def returnLlama2Response(input_text,num_words,writing_style):
    llm=CTransformers(model="C:\\Users\\91868\\Downloads\\llama-2-7b-chat.ggmlv3.q8_0.bin",model_type='llama',
                      config={'max_new_tokens':256,'temperature':0.2})
    template="""
    Write a blog for {writing_style} perspective for the topic {input_text} within limit of {num_words} words.
"""
    prompt=PromptTemplate(input_variables=["writing_style","input_text","num_words"],template=template)

    response=llm(prompt.format(writing_style=writing_style,input_text=input_text,num_words=num_words))
    print(response)
    return response

# Defining streamlit config and building UI for this text generation app

st.set_page_config(page_title="Generate Blogs !!",layout="centered")
st.header("Generate Blogs!!")
input_text=st.text_input("Enter the blog topic for which you want to generate text")
col1,col2=st.columns([4,5])
with col1:
    num_words=st.text_input("Number of Words")
with col2:
    writing_style=st.selectbox("Generate the blog for",
                               ('Data Scientists','Five year old child','Scholars','Common man'),index=0)
submit=st.button("Generate!")
if submit:
    st.write(returnLlama2Response(input_text,num_words,writing_style))