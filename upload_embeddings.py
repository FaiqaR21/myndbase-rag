import supabase_client
from embeddings import get_embedding

def upload_all_embeddings():
    # Get all documents regardless of profile/app
    docs = supabase_client.supabase.table("profile_documents").select("*").execute().data

    for doc in docs:
        text = doc["content"]["text"]    # extract JSON text
        embedding = get_embedding(text)

        print(f"Uploading embedding for document {doc['id']}...")
        supabase_client.update_embedding(doc["id"], embedding)

    print("All embeddings uploaded successfully.")

if __name__ == "__main__":
    upload_all_embeddings()
