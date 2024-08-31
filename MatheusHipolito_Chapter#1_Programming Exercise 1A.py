# Matheus H Hipolito
# 2024-08-26
# This program helps to pre-sell cinema tickets.
# There are 20 tickets in total, and each person can buy up to 4 tickets.
# The program will keep asking people how many tickets they want to buy until all tickets are sold.

MAX_TICKETS = 20  # Total tickets available
MAX_TICKETS_PER_BUYER = 4  # Maximum tickets one person can buy


def sell_tickets():
    remaining_tickets = MAX_TICKETS  # How many tickets are left
    total_buyers = 0  # Count of how many people bought tickets

    while remaining_tickets > 0:  # Keep going as long as there are tickets left
        print("\nTickets remaining:", remaining_tickets)  # Show how many tickets are left
        tickets_requested = input(f"How many tickets would you like to buy (1-{min(MAX_TICKETS_PER_BUYER, remaining_tickets)})? ")

        # Check if the input is a number
        if tickets_requested.isdigit():
            tickets_requested = int(tickets_requested)  # Convert input to an integer

            # Check if the number is within the allowed range
            if 1 <= tickets_requested <= min(MAX_TICKETS_PER_BUYER, remaining_tickets):
                remaining_tickets -= tickets_requested  # Subtract the number of tickets bought from the total
                total_buyers += 1  # Add one to the number of buyers
                print(f"You successfully bought {tickets_requested} ticket(s)!")
            else:
                print(f"You can only buy between 1 and {min(MAX_TICKETS_PER_BUYER, remaining_tickets)} tickets.")
        else:
            print("Please enter a valid number.")  # Ask again if the input is not a number

    print("\nAll tickets have been sold!")  # Shows when all tickets are sold
    print(f"Total number of buyers: {total_buyers}")  # Show the total number of people who bought tickets


# Start the ticket selling process
sell_tickets()






