from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    PromptTemplate
)
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Qdrant
from langchain.output_parsers import PydanticOutputParser
from qdrant_client.http import models as rest
from pydantic import BaseModel, Field
from langchain.document_loaders.csv_loader import CSVLoader

from langchain.chat_models import ChatOpenAI


import csv
from typing import Dict, List, Optional
from langchain.document_loaders.base import BaseLoader
from langchain.docstore.document import Document


loader = CSVLoader(
    file_path="./src/dataset_small.csv", source_column="title")

data = loader.load()

embeddings = OpenAIEmbeddings()

qdrant = Qdrant.from_documents(
    data,
    embeddings,
    location=":memory:",  # Local mode with in-memory storage only
    collection_name="my_documents",
)

qa = RetrievalQA.from_chain_type(
  llm=ChatOpenAI(),
  chain_type="stuff",
  retriever=qdrant.as_retriever(),
  return_source_documents=True
)

while True:
  user_input = input("Hi, I'm an AI librarian, what can I help you with?\n")

  book_request = "You are a librarian. Help the user answer their question. " +\
  f"\nUser:{user_input}"
  result = qa({"query": book_request})
  print(result["result"])

#print(qa({"query":"You are a librarian. Help the user by answering his question. User: A book from 1998"}))
