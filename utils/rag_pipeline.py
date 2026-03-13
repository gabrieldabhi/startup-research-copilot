import faiss
import numpy as np

from utils.document_loader import load_documents
from models.embeddings import get_embedding
from config.config import CHUNK_SIZE, TOP_K


def split_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def build_vector_store(data_path):

    try:

        documents = load_documents(data_path)

        chunks = []
        metadata = []

        for doc in documents:

            text_chunks = split_text(doc["content"], CHUNK_SIZE)

            for chunk in text_chunks:
                chunks.append(chunk)
                metadata.append(doc["filename"])

        embeddings = [get_embedding(chunk) for chunk in chunks]

        embeddings = np.array(embeddings)

        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(dimension)

        index.add(embeddings)

        return index, chunks, metadata

    except Exception as e:

        print("Vector store build error:", e)

        return None, [], []


def retrieve_context(query, index, chunks, metadata):

    try:

        query_embedding = get_embedding(query)

        query_embedding = np.array([query_embedding])

        distances, indices = index.search(query_embedding, TOP_K)

        results = []

        for idx in indices[0]:

            results.append({
                "text": chunks[idx],
                "source": metadata[idx]
            })

        return results

    except Exception as e:

        print("RAG retrieval error:", e)

        return []