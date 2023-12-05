import getpass
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")


from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Qdrant

dict_to_iterate = {"unstructured": [{"dataset": 1}, {"dataset": 2}, {"dataset": 3}]}



for key, value in dict_to_iterate.items():
    print(key, value)
    for v in value:
        file_path = key + "_" + list(v)[0] + list(v)[1]
        with open(file_path, 'r') as file:
            file_content = file.read()
            print(file_content)
            #load_function(file_content, namespace=file_path)

def load_function(file_path:str =None ):
    loader = TextLoader(f"synthetic_data/{file_path}")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=400, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    print(docs)
    embeddings = OpenAIEmbeddings()
    QDRANT_CLIENT = os.getenv('QDRANT_CLIENT')
    qdrant = Qdrant.from_documents(
        docs,
        embeddings,
        url=QDRANT_CLIENT,
        prefer_grpc=True,
        api_key= os.getenv('QDRANT_KEY'),
        collection_name=file_path,
    )
    return qdrant
