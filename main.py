# main.py

from retriever import get_relevant_chunks
from utils import generate_answer

def main():
    print("\n=== MYNDBASE RAG SYSTEM ===\n")

    # Ask required inputs
    profile_id = input("Enter Profile ID: ").strip()
    query = input("Enter your Query Description (QD): ").strip()

    print("\nFetching relevant documents...")
    contexts = get_relevant_chunks(query, profile_id)

    if not contexts:
        print("\n❌ No matching documents found for this profile.")
        return

    print("\nGenerating answer from LLM...\n")
    answer = generate_answer(contexts, query)

    print("\n=== FINAL ANSWER ===\n")
    print(answer)
    print("\n====================\n")

if __name__ == "__main__":
    main()
