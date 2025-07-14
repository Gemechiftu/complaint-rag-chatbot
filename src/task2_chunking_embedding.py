import os
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# Step 1: Load cleaned data
df = pd.read_csv("data/filtered_complaints.csv")

# Step 2: Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", " ", ""]
)

documents = []
metadatas = []

for idx, row in df.iterrows():
    complaint = row["Consumer complaint narrative"]
    product = row["Product"]
    complaint_id = row["Complaint ID"]
    
    chunks = text_splitter.split_text(complaint)
    
    for chunk in chunks:
        documents.append(chunk)
        metadatas.append({
            "product": product,
            "complaint_id": complaint_id
        })

# Step 3: Embedding
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(documents)

# Step 4: Store in FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Step 5: Save index + metadata
faiss.write_index(index, "vector_store/complaints_index.faiss")

with open("vector_store/metadata.pkl", "wb") as f:
    pickle.dump(metadatas, f)

print("✅ Vector store created and saved.")
df = pd.read_csv("data/filtered_complaints.csv")
df = pd.read_csv("filtered_complaints.csv")
