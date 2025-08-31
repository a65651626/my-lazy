
import os

# 设置 API 密钥（示例：OpenAI）
#os.environ["LAZYLLM_SENSENOVA_API_KEY"] = "sk-cacM6j9A69tdMa3ih5Cas4OxssqgWZiX"


print(os.getenv("LAZYLLM_SENSENOVA_API_KEY"))  # 返回密钥值或 None

from lazyllm.common.queue import sqlite3_check_threadsafety
print(sqlite3_check_threadsafety())