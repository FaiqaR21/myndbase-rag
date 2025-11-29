from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Store embedding into the profile_documents table
def update_embedding(doc_id, embedding):
    return supabase.table("profile_documents").update({
        "embeddings": embedding
    }).eq("id", doc_id).execute()

# Fetch ALL documents for only a given profile
def get_documents_by_profile(profile_id):
    response = (
        supabase.table("profile_documents")
        .select("*")
        .eq("profile_id", profile_id)
        .eq("is_deleted", False)
        .execute()
    )
    return response.data
