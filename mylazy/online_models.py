from typing import Dict, List, Union

from lazyllm import OnlineChatModule, OnlineEmbeddingModule


from lazyllm.module import OnlineEmbeddingModuleBase

class CustomOnlineEmbeddingModule(OnlineEmbeddingModuleBase):
    """CustomOnlineEmbeddingModule"""

    def __init__(self, embed_url, embed_model_name, api_key, model_series):
        super().__init__(
            embed_url=embed_url, embed_model_name=embed_model_name,
            api_key=api_key, model_series=model_series
        )

    def _encapsulated_data(self, text: str, **kwargs) -> Dict[str, str]:
        json_data = {"inputs": text, "model": self._embed_model_name}
        if len(kwargs) > 0:
            json_data.update(kwargs)

        return json_data

    def _parse_response(
            self,
            response: Union[List[List[str]], Dict]
        ) -> Union[List[List[str]], Dict]:
        return response


DOUBAO_API_KEY = "2150c1fe-ed47-46ca-bcf7-50b602ae4e7e"
DEEPSEEK_API_KEY = "sk-32c57d9508a14cb5ae0568ef1f353a74"
QWEN_API_KEY = "sk-4b7fbf9908224ca5aab5ceebef329e82"

llm = OnlineChatModule(
    source="sensenova",model="SenseNova-V6-5-Turbo",
    api_key='sk-cacM6j9A69tdMa3ih5Cas4OxssqgWZiX',
)

embedding_model = OnlineEmbeddingModule(
    source="doubao",
    embed_model_name="doubao-embedding-large-text-240915",
    api_key=DOUBAO_API_KEY,
)

custom_embedding_model = CustomOnlineEmbeddingModule(
    embed_url="",
    embed_model_name="BAAI/bge-m3",
    api_key="",
    model_series="bge"
)

rerank_model = OnlineEmbeddingModule(
    source="qwen",
    api_key=QWEN_API_KEY,
    type="rerank"
)
