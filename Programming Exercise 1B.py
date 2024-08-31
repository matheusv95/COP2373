# This code simulates a Magic 8 ball, a toy that gives you random answer to yes or no questions.
# The code has two parts:
# 1. Creating a file with a list of responses.
# 2. Reading the responses from the file, and telling user to ask a yes/no question, and then randomly display one of responses.

import random  # Import the random module to generate random numbers

def create_responses_file():
    # List of all the possible responses
    responses = [
        "Yes, of course!",
        "Without a doubt, yes.",
        "You can count on it.",
        "For sure!",
        "Ask me later!",
        "I'm not sure.",
        "I can't tell you right now.",
        "I'll tell you after my nap.",
        "No way!",
        "I don't think so.",
        "Without a doubt, no.",
        "The answer is clearly NO!"
    ]
    # Open the file in write mode ("w"), which creates the file if it doesn't exist
    with open("8ball_responses.txt", "w") as file:
        # Write each response to the file, followed by a newline character "\n"
        for response in responses:
            file.write(response + "\n")

def magic_8_ball():
    # Open the file in read mode ("r") and read all the lines into a list
    with open("8ball_responses.txt", "r") as file:
        responses = file.readlines()

    # Remove any extra whitespace characters (like newline characters) from each response
    responses = [response.strip() for response in responses]

    while True:
        # Ask the user to input a yes/no question
        question = input("Ask a yes/no question (or type 'quit' to exit): ")

        # If the user types 'quit', break out of the loop and end the program
        if question.lower() == 'quit':
            print("Goodbye!")
            break

        # Randomly select a response from the list and print it
        print(random.choice(responses))

# Run the functions when the script starts
create_responses_file()  # Create the file with responses
magic_8_ball()  # Start the Magic 8 Ball game
