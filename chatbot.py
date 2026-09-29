def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Predefined rules and responses
    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you today?"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks for asking! How are you?"
    elif user_input in ["what is your name", "what is your name?"]:
        return "I am a simple rule-based AI assistant created in Python."
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Try asking 'hello' or 'how are you'."

def start_chat():
    print("=== Simple Rule-Based Chatbot ===")
    print("Type 'bye' or 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Bot: {response}")
        
        if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
            break

if __name__ == "__main__":
    start_chat()