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

message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)

print(message.content[0].text)