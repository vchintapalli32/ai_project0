
#1 Input Question
user_question = input("Enter your question:")

#2 Import template and give prompt

from langchain.prompts import PromptTemplate

text = """ You are a senior data engineer with AI/ML experience and answer the question in same tone as the user input question
{question}

"""
prompt = PromptTemplate(
            input_variables = ["question"],
            template = text
)

#3 Make LLM call
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="gemma2-9b-it",
    api_key="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"
)

#4 Create Chain

chain = prompt | llm 

#5 Response 

result = chain.invoke({"question":user_question})
print(result.content)