import openai


openai.api_key = 'OWN_API_KEY'

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
