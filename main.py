import json


# Load existing knowledge from a JSON file
def load_knowledge(filename="knowledge.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# Save updated knowledge to the JSON file
def save_knowledge(data, filename="knowledge.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# Function to get an answer or learn new one
def chatbot():
    knowledge = load_knowledge()

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        if user_input in knowledge:
            print(f"Chatbot: {knowledge[user_input]}")
        else:
            print("Chatbot: I don't know the answer. Can you teach me?")
            new_answer = input("Type the answer or say 'skip' to ignore: ").strip()
            if new_answer.lower() != "skip":
                knowledge[user_input] = new_answer
                save_knowledge(knowledge)
                print("Chatbot: Thanks! I've learned something new.")


if __name__ == "__main__":
    chatbot()
