# Chatbot in Python

def chatbot():
    # Introduction message
    print("Chatbot: Hello there im your helper, Type 'bye' to exit.")
    
    # Start an infinite loop to keep the conversation going
    while True:
        # Get user input and convert it to lowercase for easier comparison
        msg = input("You: ").lower()

        # Check for different types of responses
        if msg == 'bye':
            print("Chatbot: Goodbye!")
            break  # Exit the loop if the user types "bye"
        elif 'hello' in msg:
            print("Chatbot: Hi there!")
        elif 'how are you' in msg:
            print("Chatbot: For more advanced answers, contact Amnon my creator!")
        else:
            print("Chatbot: I don't understand that.")

if __name__ == "__main__":
    chatbot()  # Run the chatbot
