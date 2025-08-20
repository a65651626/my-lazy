
import os

# 设置 API 密钥（示例：OpenAI）
os.environ["LAZYLLM_SENSENOVA_API_KEY"] = "sk-cacM6j9A69tdMa3ih5Cas4OxssqgWZiX"

import lazyllm

chat1 = lazyllm.OnlineChatModule(source="sensenova",model="SenseChat-5-1202")

print(chat1("你好，你是DeepSeek吗？"))
print("===========================")
chat2 = lazyllm.OnlineMultiModalModule(source="sensenova",model="SenseNova-V6-5-Pro")
print(chat2("你好，你是DeepSeek吗？"))


#lazyllm.WebModule(chat, port=range(23466, 23470)).start().wait()

