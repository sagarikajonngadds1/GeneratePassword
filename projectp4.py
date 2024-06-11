import random
import string

def generate_password(length, complexity):
    characters = string.ascii_lowercase
    if complexity >= 2:
        characters += string.ascii_uppercase
    if complexity >= 3:
        characters += string.digits
    if complexity == 4:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired password length: "))
    print("Select the complexity level: ")
    print("1. Lowercase letters")
    print("2. Lowercase and Uppercase letters")
    print("3. Lowercase, Uppercase letters, and digits")
    print("4. Lowercase, Uppercase letters, digits, and symbols")
    complexity = int(input("Enter complexity level (1-4): "))
    if complexity not in [1, 2, 3, 4]:
        print("Invalid complexity level. Please choose a value between 1 and 4.")
        return

    password = generate_password(length, complexity)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()