import string
import random

def make_password(length, level):
    if length < 4:
        raise ValueError("Password length must be at least 4.")
    
    # Define character sets based on complexity level
    if level == 1:
        char_pool = string.ascii_letters
    elif level == 2:
        char_pool = string.ascii_letters + string.digits
    elif level == 3:
        char_pool = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level.")
    
    password_chars = []
    
    # Ensure the first character is not a special character
    first_char_pool = string.ascii_letters + string.digits
    first_char = random.choice(first_char_pool)
    password_chars.append(first_char)
    
    # Add required characters based on the complexity level
    if level == 3:
        password_chars.append(random.choice(string.ascii_uppercase))
        password_chars.append(random.choice(string.ascii_lowercase))
        password_chars.append(random.choice(string.digits))
        password_chars.append(random.choice(string.punctuation))
        remaining_length = length - 5
    else:
        remaining_length = length - 1
    
    # Fill the rest of the password with random characters
    password_chars += random.choices(char_pool, k=remaining_length)
    
    # Shuffle the list to ensure randomness except the first character
    random.shuffle(password_chars[1:])
    
    # Join the list to form the final password string
    return ''.join(password_chars)

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length < 4:
            print("Password length must be at least 4.")
            return
        
        # Prompt the user for the desired complexity level
        print("Select the complexity level of the password:")
        print("1. Low (letters only)")
        print("2. Medium (letters and digits)")
        print("3. High (letters, digits, and special characters)")
        
        level = int(input("Enter the complexity level (1, 2, or 3): "))
        
        # Generate the password
        password = make_password(length, level)
        
        # Display the generated password
        print("Generated password:", password)
    
    except ValueError as e:
        print(f"Invalid input: {e}")

# Run the main function
if __name__ == "__main__":
    main()
