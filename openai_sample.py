import openai


openai.api_key = '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'

messages = [ {"role" : "system","content": "You are an intelligent assistant."} ]

while True:
    query = input ("User: ")
    if messages:
        messages.append(
            {"role" : "user", "content": query},
        )
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", messages = messages
        )
    
    reply = chat.choices[0]["message"]["content"]
    print("ChatGPT: "+reply)
    messages.append({"role":"assistant","content": reply})