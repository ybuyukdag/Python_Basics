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



####Chat-GPT-3.5 has no access to internet anymore.ITs' last access date is 2021. So, searching about 2022 and next will be unsuccessful. 
