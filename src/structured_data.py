# Teste de request a api da anthropic

from dotenv import load_dotenv

load_dotenv()
import anthropic
import httpx

print("Inicializado ...")
# Cliente criado para pular verificações de segurança exigidas pela rede do MPF

client = anthropic.Anthropic(http_client=httpx.Client(verify=False))

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
        "temperature": temperature,
    }

    if system:
        params["system"] = system

    message = client.messages.create(**params)
    return message.content[0].text


# def chat(messages):
#     message = client.messages.create(
#         model=model,
#         max_tokens=1000,
#         messages=messages,
#     )
#     # print(message.content[0].text)
#     return message.content[0].text


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

prompt = """
Generate three different samples AWS CLI commands. Each should be very short.
"""

add_user_message(messages, prompt)
add_assistant_message(
    messages, "Here are all three commands without any comments:\n```bash"
)

text = chat(messages, stop_sequences=["```"])
print(text.strip())
