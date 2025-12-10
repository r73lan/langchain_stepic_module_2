from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from langchain_mistralai.chat_models import ChatMistralAI

load_dotenv() 

MODEL_NAME = os.getenv("MODEL_NAME", "open-mistral-7b")

llm = ChatMistralAI(
    model=MODEL_NAME,
    temperature=0.8
)

prompt1 = PromptTemplate.from_template("Назови 5 популярных достопримечательностей в городе {city}.")
prompt2 = PromptTemplate.from_template("Составь маршрут на 3 дня по городу {city}, включив следующие места: {places_list}.")

chain = (
    {"city": RunnablePassthrough()}
    | RunnablePassthrough.assign(
        places_list=lambda x: (prompt1 | llm | StrOutputParser()).invoke(x)
    )
    | prompt2
    | llm
    | StrOutputParser()
)

# Запуск
result = chain.invoke({"Париж"})
print(result)