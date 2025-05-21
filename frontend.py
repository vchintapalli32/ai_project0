import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
load_dotenv()

#1 UI title 
st.set_page_config(page_title = "My First Chatbot",layout = "centered")
st.title("My First Chatbot")
st.markdown("Ask Any Question and Get Instant Reply")

#2 User inputs question
user_question = st.text_input("Ask Your Question")

if st.button("Get Answer") and user_question.strip():
    with st.spinner("Fetching Answer...."):
        text = """ You are a senior data engineer with AI/ML experience and answer the question in same tone as the user input question
{question}

"""
        prompt = PromptTemplate(
            input_variables = ["question"],
            template = text
        )
        llm = ChatGroq(
    model="gemma2-9b-it",
    api_key="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"
        )
        chain = prompt | llm 

        try:
            result = chain.invoke({"question":user_question})
            st.success("Here is your answer")
            st.write(result.content)
        except Exception as e:
            st.error(f"something is wrong: {str(e)}")

else:
    st.caption("Powered by Venkatesh Chintapalli")