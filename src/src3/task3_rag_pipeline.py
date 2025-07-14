from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub

# Load FAISS index
db = FAISS.load_local("vector_store", HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"))

# Create retriever
retriever = db.as_retriever(search_kwargs={"k": 5})

# Define Prompt
template = """You are a financial analyst assistant for CrediTrust. 
Use the following retrieved complaint excerpts to answer the question.
If the context doesn't contain the answer, say you don't have enough information.

Context: {context}
Question: {question}
Answer:"""
prompt = PromptTemplate.from_template(template)

# Load LLM (or use pipeline)
llm = HuggingFaceHub(repo_id="google/flan-t5-base", model_kwargs={"temperature": 0.5, "max_length": 512})

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type_kwargs={"prompt": prompt})

# Example query
question = "What issues do people face with credit cards?"
result = qa_chain.run(question)

print("Answer:", result)
