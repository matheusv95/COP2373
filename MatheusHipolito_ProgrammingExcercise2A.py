# Matheus_Hipolito_Chapter5_AssignmentA.py
# This program asks the user to enter an email message. It checks if the message contains any common spam words,
# then gives the message a "spam score" and tells the user how likely the message is spam.

# Function to check the email for spam words
def check_for_spam(message, spam_words):
    spam_score = 0  # Start the spam score at 0
    matched_words = []  # List to store any spam words found in the message

    # Go through each word in the spam words list
    for word in spam_words:
        # Check if the spam word is in the email message (case doesn't matter)
        if word.lower() in message.lower():
            spam_score += 1  # Add 1 to the score if the word is found
            matched_words.append(word)  # Add the found word to the matched words list

    return spam_score, matched_words  # Return the spam score and matched words

# Function to decide how likely the message is spam based on the spam score
def rate_spam(spam_score):
    # Use if-elif statements to decide how likely the message is spam
    if spam_score > 20:
        return "Very likely spam"
    elif spam_score > 10:
        return "Likely spam"
    elif spam_score > 5:
        return "Possibly spam"
    else:
        return "Unlikely to be spam"

# Main function that runs the program
def main():
    # List of common spam words or phrases
    SPAM_WORDS = ["Free", "Buy now", "Limited time", "Act now", "Offer expires", "Money back",
                  "Guarantee", "100% satisfied", "Click here", "Call now", "Earn extra cash",
                  "Risk-free", "Congratulations", "Winner", "Lowest price", "No cost", "Trial",
                  "Unsubscribe", "Save big", "Get paid", "Urgent", "Fast cash", "Incredible deal",
                  "Special promotion", "No obligation", "Credit card", "No hidden fees",
                  "Apply now", "Order today", "Cheap"]

    # Ask the user to type an email message
    email_message = input("Please enter your email message: ")

    # Call the check_for_spam function to get the spam score and matched words
    spam_score, matched_words = check_for_spam(email_message, SPAM_WORDS)

    # Call the rate_spam function to find out how likely the message is spam
    spam_likelihood = rate_spam(spam_score)

    # Show the user the spam score and how likely the message is spam
    print(f"Spam score: {spam_score}")
    print(f"Likelihood that the message is spam: {spam_likelihood}")

    # If any spam words were found, show them to the user
    if len(matched_words) > 0:
        print("The following words/phrases caused it to be marked as spam:")
        print(", ".join(matched_words))

# Run the main function to start the program
if __name__ == "__main__":
    main()
