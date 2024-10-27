def main():
    # List to store the sentences.
    sentences = []

    print("Enter sentences (type 'DONE' to stop):")

    while True:
        # Asks for a sentence.
        sentence = input("Enter a sentence: ")

        # Check if the user wants to stop.
        if sentence.strip().upper() == 'DONE':
            break

        # Add sentence to the list.
        sentences.append(sentence)

    # Display each input sentence.
    print("\nYou entered the following sentences:")
    for s in sentences:
        print(s)

    # Display the total count of sentences.
    print(f"\nTotal number of sentences: {len(sentences)}")


# Run the main function
if __name__ == "__main__":
    main()
