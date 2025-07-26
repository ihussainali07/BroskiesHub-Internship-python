def chatbot():
    print("🤖 Chatbot: Hi! I'm ChatBot. Type 'bye' to exit.")

    while True:

        user_input = input("You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hello there! How can I assist you today?")

        elif user_input == "how are you":
            print("🤖 Chatbot: I'm just a bunch of code, but I'm doing great! 😄")

        elif user_input == "what is your name":
            print("🤖 Chatbot: I'm a simple Python chatbot created by using if-else.")

        elif user_input == "help":
            print("🤖 Chatbot: You can ask me things like:")
            print("   - hello")
            print("   - how are you")
            print("   - what is your name")
            print("   - what can you do")
            print("   - bye")

        elif user_input == "what can you do":
            print("🤖 Chatbot: I can answer basic questions and chat with you!")
            print("           I'm built using Python and simple if-else logic.")

        elif user_input == "who created you":
            print("🤖 Chatbot: I was created by a student learning Python!")

        elif user_input == "what's the weather like":
            print("🤖 Chatbot: I don't have access to live weather updates, but I hope it's sunny! ☀️")

        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day! 👋")
            break

        else:
            print("🤖 Chatbot: Sorry, I didn't understand that. Try typing 'help' to see what I can do.")

chatbot()
