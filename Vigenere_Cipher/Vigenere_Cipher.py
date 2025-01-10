#! usr/bin/env python3
"""
Version: - 1.0
Date: 1/10/2025
Created by: - Ghost Squad

Desdcription:
    This script allows the user to encrypt or decrypt messages using the Vigenère cipher. 
    Users can provide the message directly or load it from a `.txt` file. 
    The script also includes a menu for user interaction and loops until the user chooses to exit.

Features:
    A menu driven program to encrypt and decrypt Vigenère encyptions.

Work List:
    Add a secondary menu for decryption that will output to file or print to screen.
"""

def vigenere_cipher_encrypt(message, password):
    """
    Encrypts a message using the Vigenère cipher.

    Args:
        message (str): The message to encrypt.
        password (str): The cipher key (alphabetic only).

    Returns:
        str: The encrypted message.
    """
    password = password.upper()
    encrypted_message = []
    password_index = 0

    for char in message:
        if char.isalpha():  # Only encrypt alphabetic characters
            shift = ord(password[password_index]) - ord('A')
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message.append(encrypted_char)
            password_index = (password_index + 1) % len(password)  # Cycle through the password
        else:
            encrypted_message.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(encrypted_message)

def vigenere_cipher_decrypt(message, password):
    """
    Decrypts a message using the Vigenère cipher.

    Args:
        message (str): The encrypted message to decrypt.
        password (str): The cipher key (alphabetic only).

    Returns:
        str: The decrypted message.
    """
    password = password.upper()
    decrypted_message = []
    password_index = 0

    for char in message:
        if char.isalpha():  # Only decrypt alphabetic characters
            shift = ord(password[password_index]) - ord('A')
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_message.append(decrypted_char)
            password_index = (password_index + 1) % len(password)  # Cycle through the password
        else:
            decrypted_message.append(char)  # Non-alphabetic characters remain unchanged

    return ''.join(decrypted_message)

def load_message_from_file(file_path):
    """
    Loads the content of a text file.

    Args:
        file_path (str): Path to the .txt file.

    Returns:
        str or None: The content of the file, or None if the file cannot be loaded.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found. Please check the file path.")
        return None

def main():
    """
    Main function to display the menu and handle user input.
    """
    while True:
        # Display menu options
        print("\n--- Vigenère Cipher ---")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice in {'1', '2'}:
            # Get the message or load it from a file
            input_message = input("Enter the message or the path to a .txt file: ").strip()
            if input_message.endswith(".txt"):
                message = load_message_from_file(input_message)
                if message is None:  # File loading failed
                    continue
            else:
                message = input_message

            # Get the password and validate it
            password = input("Enter the password for the cipher: ").strip()
            if not password.isalpha():
                print("Error: Password must contain only alphabetic characters.")
                continue

            # Perform encryption or decryption based on the choice
            if choice == '1':  # Encrypt
                encrypted_message = vigenere_cipher_encrypt(message, password)
                print("\nEncrypted message:")
                print(encrypted_message)
            elif choice == '2':  # Decrypt
                decrypted_message = vigenere_cipher_decrypt(message, password)
                print("\nDecrypted message:")
                print(decrypted_message)

        elif choice == '3':  # Quit the program
            print("Exiting the program. Goodbye!")
            break

        else:  # Handle invalid menu choice
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
