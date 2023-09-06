from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
import os

def extract_prompt(style, chain_type='stuff'):
    os.environ['OPENAI_API_KEY'] = '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'

    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI(temperature = 0.0)
    docs = CSVLoader("data/train_clean.csv").load()

    db = DocArrayInMemorySearch.from_documents(
        docs, 
        embeddings
    )

    retriever = db.as_retriever()

    qa_stuff = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type=chain_type, 
        retriever=retriever, 
        verbose=False
    )

    query =  f"Please suggest a prompt based on the following style: {style}.\
               just provide the prompt, exclusively the prompt.\
               not any additional comments or anything."
    
    response = qa_stuff.run(query)
    
    return response