import lazyllm                                          #(1)

chat = lazyllm.OnlineChatModule(source="sensenova")                       #(2)
while True:
    query = input("query(enter 'quit' to exit): ")      #(3)
    if query == "quit":                                 #(4)
        break
    res = chat.forward(query)                           #(5)
    print(f"answer: {res}")                             #(6)