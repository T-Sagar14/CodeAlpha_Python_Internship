print("🤖 Welcome to CodeAlpha Chatbot")
print("Type 'bye' to exit.\n")

while True:

    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi! Welcome to CodeAlpha Internship Program.")

    elif user_input == "how are you":
        print("Bot: I am doing great!")

    elif user_input == "what is your name":
        print("Bot: My name is CodeAlpha Chatbot.")

    elif user_input == "who created you":
        print("Bot: I was created using Python programming.")

    elif user_input == "what is codealpha":
        print("Bot: CodeAlpha is a platform that provides internships and learning opportunities for students in programming, web development, AI, and more.")

    elif user_input == "tell me about codealpha":
        print("Bot: CodeAlpha helps students improve their technical skills through real-time projects and internship experiences.")

    elif user_input == "what can you do":
        print("Bot: I can answer simple questions and chat with users.")

    elif user_input == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs! 😄")

    elif user_input == "bye":
        print("Bot: Goodbye! Thanks for using CodeAlpha Chatbot.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
