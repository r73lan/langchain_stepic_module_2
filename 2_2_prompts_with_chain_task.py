prompt1_doc = '''
Шаблон предназначен для первого контактного сообщения клиенту
с предложением пройти анонимный опрос от бренда.
Параметры:
  {client_name} – имя клиента, к которому обращается менеджер;
  {brend_name} – название бренда, от лица которого ведётся общение.
'''

prompt2_doc = '''
Шаблон предназначен для генерации списка оригинальных подарков
для конкретного человека на основе его имени и хобби.
Параметры:
  {gift_target_name} – имя человека, для которого подбираются подарки;
  {hobbies_list} – список хобби и интересов этого человека, на основании которых подбираются идеи подарков.
'''

prompt3_doc = '''
Шаблон предназначен для формального уведомления клиента
о зафиксированных нарушениях правил дорожного движения его автомобилем.
Параметры:
  {client_name} – имя владельца или пользователя автомобиля;
  {car_make} – марка (бренд, модель) автомобиля;
  {id_car} – государственный регистрационный номер автомобиля;
  {violations_list} – перечень зафиксированных нарушений правил дорожного движения.
'''


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



prompt1 = PromptTemplate.from_template("Привет, {client_name}! Меня зовут Оксана и я представляю бренд {brend_name}. Я хотела бы задать вам несколько вопросов, Вы не против участия в анонимном опросе?")

prompt2 = PromptTemplate.from_template("Составь список подарков для человека: {gift_target_name}. {gift_target_name} имеет следующие хобби: {hobbies_list}. Предложи оригинальные подарки, которые могут обрадовать этого человека на основании описанной информации.")

prompt3 = PromptTemplate.from_template("Добрый день, {client_name}. На машине марки {car_make} с государственным номером {id_car} были нарушены следующие правила дорожного движения: {violations_list}")

message_1_1 = prompt1.format(client_name="Арнольд", brend_name="Орифлейм")
message_1_2= prompt1.format(client_name="Марина", brend_name="Деловые технологии")
message_2_1 = prompt2.format(gift_target_name='мой батя', hobbies_list='рыбалка, крафтовое пиво, ходить в дрочильню, баня, путешествия')
message_2_2 = prompt2.format(gift_target_name='Дмитрий', hobbies_list='фитнес,  скалолазание')
message_3_1 = prompt3.format(client_name="Аркадий", car_make="Lada Granta", id_car='о492са178', violations_list='1. Превышение скорости на 100 км/ч')
message_3_2 = prompt3.format(client_name="Зинаида", car_make="BMW", id_car='о223са78', violations_list='1. Езда в нетрезвом состоянии')

print(message_1_1)
print(message_1_2)
print(message_2_1)
print(message_2_2)
print(message_3_1)
print(message_3_2)