import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_mistralai.chat_models import ChatMistralAI

load_dotenv()


MODEL_NAME = os.getenv("MODEL_NAME", "open-mistral-7b")

llm = ChatMistralAI(
    model=MODEL_NAME,
    temperature=0.8
)

class Profile(BaseModel):
    name: str = Field(description="Имя пользователя")
    age: int = Field(description="Возраст в годах")
    premium: bool = Field(description="Есть премиум-подписка")

structured_llm = llm.with_structured_output(Profile)

result = structured_llm.invoke("Создай профиль русского пользователя средних лет")
print(type(result))   # <class '__main__.Profile'>
print(result.name)    # Алексей Петрович
print(result.age)     # 37
print(result.premium) # False
