from dotenv import load_dotenv

from langchain_core.tools import tool
from langchain_ollama import Ollama
from langchain_tavily import Tavily

load_dotenv()

@tool
def triple(number: float) -> float:
    """
    Triple the input number.
    """
    return float(number) * 3

tools = [Tavily(max_results = 1), triple]

llm = Ollama(
    model = "qwen3:1.7b",
    temperature = 0,
    tools = tools
)