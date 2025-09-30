from src.agents.pdi_agent import pdi_agent
from src.agents.rag import load_or_create_index, search


def main():
    print(pdi_agent())
    return pdi_agent()


if __name__ == "__main__":
    index, documents = load_or_create_index()
    user = input("User prompt: ")
    results = search(user, index, documents, k=3)
    near_doc = results[0][0]
    answer = pdi_agent(user_prompt=user, near_doc=near_doc)

    print("\n--- Resposta ---")
    print(answer)