# Teste de ajuste de temperatura , de deterministico até mais aleatorio 

from dotenv import load_dotenv
load_dotenv()
import httpx, anthropic

print("Inicializado ...")
# Cliente criado para pular verificações de segurança exigidas pela rede do MPF

client = anthropic.Anthropic(
    http_client=httpx.Client(verify=False)
)

print("Client criado ...")

##from anthropic import Anthropic
##client = Anthropic()

model = "claude-sonnet-4-6"

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text

messages = []


# With system prompt
system = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""
temperatura=1.0 #random
#temperatura=0.0 #deterministico 
while True:
    user_input = input("> ")
    add_user_message(messages,user_input)
    #answer = chat(messages, system=system,temperature=temperatura)
    answer = chat(messages,temperature=temperatura) #sem contexto
    print(answer)









