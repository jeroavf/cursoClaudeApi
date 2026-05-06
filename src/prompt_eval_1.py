# Teste de request a api da anthropic

import json

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

# model = "claude-sonnet-4-6"
model = "claude-haiku-4-5"


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
    }
    if system:
        params["system"] = system
    if stop_sequences:
        params["stop_sequences"] = stop_sequences

    response = client.messages.create(**params)
    return response.content[0].text


def generate_dataset():
    prompt = """
Generate an evaluation dataset for a prompt evaluation. The dataset will be used to evaluate prompts that generate Python, JSON, or Regex specifically for AWS-related tasks. Generate an array of JSON objects, each representing task that requires Python, JSON, or a Regex to complete.

Example output:
```json
[
  {
    "task": "Description of task",
  },
  ...additional
]
```

* Focus on tasks that can be solved by writing a single Python function, a single JSON object, or a single regex
* Focus on tasks that do not require writing much code

Please generate 3 objects.
"""

    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"])
    return json.loads(text)


# =====================


def run_prompt(test_case):
    """Merges the prompt and test case input, then returns the result"""
    prompt = f"""
Please solve the following task:

{test_case["task"]}
"""

    messages = []
    add_user_message(messages, prompt)
    output = chat(messages)
    return output


def run_test_case(test_case):
    """Calls run_prompt, then grades the result"""
    output = run_prompt(test_case)

    # TODO - Grading
    score = 10

    return {"output": output, "test_case": test_case, "score": score}


def run_eval(dataset):
    """Loads the dataset and calls run_test_case with each case"""
    results = []

    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)

    return results


# Inicio ========================
# Gerar dataset

dataset = generate_dataset()
print(dataset)

with open("dataset.json", "w") as f:
    json.dump(dataset, f, indent=2)


# Avaliar dataset
with open("dataset.json", "r") as f:
    dataset = json.load(f)

results = run_eval(dataset)


# show results
print("==============================\n Resultados \n==============================\n")
print(json.dumps(results, indent=2))
