from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from openai.embeddings_utils import get_embedding
import openai
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = os.environ.get("OPENAI_API_BASE_URL")

myllm = OpenAI()
mychat = ChatOpenAI()
myembeddings = OpenAIEmbeddings()

def my_get_embedding(text):
    return get_embedding(text, engine='text-embedding-ada-002')