# IAI-SLE
Self Learning Activity
# Simple Python AI Agent

A beginner-friendly, text-based conversational AI agent implemented in Python. This project demonstrates basic programming principles like infinite loops, conditional statements, and handling user input without relying on complex external libraries.

## Features

- **Interactive Loop**: Stays active and continuously prompts for input until told to close.
- **Keyword Recognition**: Responds to everyday text commands.
- **Fallback Catch-All**: Gracefully handles unknown phrases with a default reply.

## Supported Commands

The agent is configured to recognize the following phrases:
- `hello` - Greets the user.
- `help` - Offers basic guidance.
- `give me link of github` - Provides the URL for GitHub.
- `bye` / `exit` - Terminates the program.

## Prerequisites

- Python 3.x installed on your computer.

## How to Run

1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the folder containing `agent.py`.
4. Execute the script using the following command:

```bash
python agent.py
```

## How It Works

The script operates through five foundational logic components:
1. **Infinite Loop (`while True:`)**: Keeps the program running indefinitely so you can have a continuous conversation.
2. **Input Capture (`input()`)**: Pauses execution to capture whatever you type in the terminal.
3. **Control Flow (`if`/`elif`/`else`)**: Tests your input text against pre-programmed strings to trigger the right answer.
4. **Breaking Statements (`break`)**: Instantly stops the active execution loop when `exit` or `bye` is invoked.
5. **Fallback Catch-All (`else`)**: Safely triggers a standard error message whenever input words do not match any rules.
