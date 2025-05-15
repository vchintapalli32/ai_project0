
#1 Input Question
user_question = input("Enter your question:")

#2 Import template and give prompt

from langchain.prompts import PromptTemplate

text = """ You are a senior data engineer with AI/ML experience
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