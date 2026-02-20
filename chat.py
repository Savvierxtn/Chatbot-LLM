
from llm import generate_reply
from retriever import retrieve_context

while True:
    user = input("You: ")
    if user.lower() == "quit":
        break
    context = retrieve_context(user)
    print("Bot:", generate_reply(user, context))
