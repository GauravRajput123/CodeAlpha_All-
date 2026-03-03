def chatbot():
    print("🤖 Simple Chatbot Started (type 'bye' to exit)")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi there! 😊")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye! 👋")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()