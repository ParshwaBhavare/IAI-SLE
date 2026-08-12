# Create a very simple AI agent in Python for a beginner.

# The agent should:
# 1. Ask the user for input.
# 2. Understand simple commands such as hello, help, and bye.
# 3. Give an appropriate response.
# 4. Keep running until the user types "exit".
# 5. Use simple Python code.
# 6. Add comments explaining the code.
# 7. Do not use complicated libraries.

# Generate the complete code for agent.py and explain how it works.
#Here is a simple AI agent implemented in Python:
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
