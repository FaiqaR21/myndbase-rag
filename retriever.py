import supabase_client
import numpy as np
import ast
from embeddings import get_embedding

def get_relevant_chunks(query, profile_id, top_k=3):
    query_embedding = np.array(get_embedding(query), dtype=float)

    documents = supabase_client.get_documents_by_profile(profile_id)

    for doc in documents:
        emb = doc["embeddings"]

        # Convert from string → Python list if needed
        if isinstance(emb, str):
            emb = ast.literal_eval(emb)

        doc_embedding = np.array(emb, dtype=float)

        # Cosine similarity
        similarity = np.dot(query_embedding, doc_embedding) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(doc_embedding)
        )

        doc["score"] = similarity

    documents = sorted(documents, key=lambda x: x["score"], reverse=True)

    return [doc["content"]["text"] for doc in documents[:top_k]]
