from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import FAISS
import os

def extract_prompt_FAISS(style):
    os.environ['OPENAI_API_KEY'] = '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'

    embeddings = OpenAIEmbeddings()
    docs = CSVLoader("./data/train_red.csv", encoding = 'utf-8').load()

    db = FAISS.from_documents(
        docs, 
        embeddings
    )

    query =  f"Please suggest a prompt based on the following style: {style}.\
               just provide the prompt, exclusively the prompt.\
               not any additional comments or anything."
    
    response = db.similarity_search(query)
    
    return response[0].page_content