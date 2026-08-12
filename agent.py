# Create a very simple AI agent in Python for a beginner.

while True:
    user_input = input("You: ")
    
    if user_input == "hello":
        print("AI: Hello! How can I help you today?")
    elif user_input == "help":
        print("AI: I can help you with basic questions. Just ask!")
    elif user_input == "give me link of github":
        print("AI: https://github.com/")
    elif user_input == "bye":
        print("AI: Goodbye! Have a great day!")
        break
    elif user_input == "exit":
        print("AI: Exiting the program.")
        break
    else:
        print("AI: I'm not sure how to respond to that.")
