import os

# 设置 API 密钥（示例：OpenAI）
os.environ["LAZYLLM_SENSENOVA_API_KEY"] = "sk-cacM6j9A69tdMa3ih5Cas4OxssqgWZiX"

import lazyllm
documents = lazyllm.Document(dataset_path="data_kb")

retriever = lazyllm.Retriever(doc=documents,group_name="CoarseChunk",similarity="bm25_chinese",topk=3, output_format='content', join=' ' )
retriever.start()

prompt = ('You will act as an AI question-answering assistant and complete a dialogue task.'
          'In this task, you need to provide your answers based on the given context and questions.')

llm=lazyllm.OnlineChatModule(source="sensenova",model='SenseChat-5-1202').prompt(lazyllm.ChatPrompter(instruction=prompt, extra_keys=['context_str']))

query = input('请输入您的问题\n')
res = llm({"query": query, "context_str": retriever(query=query)})

print(f'With RAG Answer: {res}')

