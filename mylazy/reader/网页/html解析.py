from lazyllm.tools.rag import DocNode
from bs4 import BeautifulSoup
from lazyllm.tools.rag import Document


def processHtml(file, extra_info=None):
    text = ''
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
        soup = BeautifulSoup(data, 'lxml')
        for element in soup.stripped_strings:
            text += element + '\n'
    node = DocNode(text=text, metadata=extra_info or {})
    return [node]


doc = Document(dataset_path="/mylazy/reader/网页")  ###抓取本地文件位置
doc.add_reader("*.html", processHtml)
data = doc._impl._reader.load_data(input_files=["Y:/mylazy/网页/webPage.html"]) ###抓取具体文件
print(f"data: {data}")
print(f"text: {data[0].text}")
