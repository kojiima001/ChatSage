import json

# Load knowledge base from JSON file
def load_knowledge_base(filename="knowledge.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: Knowledge base file not found!")
        return {}

# Function to retrieve answers
def get_answer(question, knowledge):
    return knowledge.get(question.lower(), "I don't know the answer to that.")

# Main function to test the chatbot
def chatbot_test():
    knowledge = load_knowledge_base()
    if not knowledge:
        return
    
    print("Chatbot Test - Ask me anything! (Type 'exit' to quit)")
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Goodbye!")
            break
        response = get_answer(user_input, knowledge)
        print("Bot:", response)

if __name__ == "__main__":
    chatbot_test()
