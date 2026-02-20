
from openai import OpenAI
from config import OPENAI_MODEL
from prompt import SYSTEM_PROMPT

client = OpenAI()

def generate_reply(user_input, context=""):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": context + user_input}
    ]
    res = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=messages
    )
    return res.choices[0].message.content
