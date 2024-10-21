import re
# This function will check if the phone number is in the correct format.
def validate_phone(phone):
    # Define the pattern we expect for phone number:
    pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
    # Use re.match to see if the input matches the pattern. If it does, return True, if not return False.
    return bool(re.match(pattern, phone))
# This function will check if the social security number(SSN) is in the correct format.
def validate_ssn(ssn):
    # Define the pattern we expect for SSNs: 3digits - 2digits - 4digits.
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    # Use re.match to check if the input matches the SSN pattern.
    return bool(re.match(pattern, ssn))
# This function will check if the zip code is in the correct format.
def validate_zip(zip_code):
    # Define the pattern for zip codes.
    pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.match(pattern, zip_code))
# Main function
def main():
    # Ask user to enter their phone number. Input will be stored in the 'phone' variable.
    phone = input("Enter phone number (format: (123) 456-7890): ")
    # Ask user to enter their social security number. Input will be stored in the 'ssn' variable.
    ssn = input("Enter social security number (format: 123-45-6789): ")
    #Ask user to enter their zip code. Input will be stored in the 'zip_code' variable.
    zip_code = input("Enter zip code (format: 12345 or 12345-6789): ")
    # Check if the phone number, SNN number, and Zip code number is valid by calling the validate_phone function.
    # If function returns True, print that the phone number is valid.
    if validate_phone(phone):
        print("valid phone number.")
    else:
        print("Invalid phone number")
    if validate_ssn(ssn):
        print("Valid social security number.")
    else:
        print("Invalid social security number.")
    if validate_zip(zip_code):
        print("Valid zip code.")
    else:
        print("Invalid zip code.")
if __name__ == "__main__":
    main()

