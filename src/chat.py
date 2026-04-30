# Teste de request a api da anthropic 

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

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    #print(message.content[0].text)
    return message.content[0].text


messages = []

# #add mensagem inicial
# add_user_message(messages,"Defina computação quantica em uma frase")

# #obter resposta do claude 
# answer = chat(messages)

# # adicione resposta do claude ao history
# add_assistant_message(messages, answer)

# # adicione outra pergunta na sequencia 
# add_user_message(messages, "Forneça outra explicação")

# # resposta final com todo o contexto 
# final_answer = chat(messages)

while True:
    # get user input
    user_input = input("> ")
    #print(">", user_input)

    # add user input to list of messages
    add_user_message(messages, user_input)

    # call claude with chat function
    answer = chat(messages)

    # add generated text to list of messages 
    add_assistant_message(messages,answer)

    # print generated text 
    print("---")
    print(answer)
    print("---")









