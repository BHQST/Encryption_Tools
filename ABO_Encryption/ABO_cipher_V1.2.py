#! usr/bin/env Python3 
"""
ABO cipher: A base-9 Enconding and Decoding System

Description:
    This script implements a cipher based on Base-9 encoding. It converts ASCII
    values to Base-9, then maps them to a custom ABO-like notation. The cipher
    supports both encryption and decryption of strings and files. Users can
    choose whether to print results to the screen or write them to files.

Version: 1.2
Date: 12/28/2024
Created by: Ghost Squad

Features:
    - Menu-driven interface for encryption and decrpytion
    - Supports input as plain text or from a '.txt' file
    - Provides output as plain text on-screen or to a '.txt' file
    - Comprehensive error handling for invalid input or file operations
"""

# Converts ASCII value to Base-9
def ascii_to_base9(s):
    """
    Converts a string into Base-9 representation and maps it to a custom ABO notation.

    Parameters:
        s (str): Input string to be encrypted.

    Returns:
        tuple: ASCII values, Base-9 representation, and ABO mapping.
    """
    def to_base9(n):
        if n == 0:
            return "000"
        digits = []
        while n:
            digits.append(int(n % 9))
            n //= 9
        return ''.join(str(x) for x in digits[::-1]).zfill(3)

    def base9_to_ABO(base9_str):
        mapping = {
            '0': 'AA', '1': 'AB', '2': 'AO',
            '3': 'BA', '4': 'BB', '5': 'BO',
            '6': 'OA', '7': 'OB', '8': 'OO'
        }

        return ''.join(mapping[digit] for digit in base9_str)

    ascii_values = [ord(char) for char in s]
    base9_values = [to_base9(value) for value in ascii_values]
    ABO_values = [base9_to_ABO(value) for value in base9_values]
    return ascii_values, base9_values, ABO_values

# Converts ABO notation back to ASCII
def ABO_to_ascii(abo_str):
    """
    Converts an ABO-encoded string back into its original ASCII representation.

    Parameters:
        abo_str (str): Input ABO string to be decrypted.

    Returns:
        tuple: Base-9 representation, ASCII values, and the decrypted string.
    """
    reverse_mapping = {
        'AA': '0', 'AB': '1', 'AO': '2',
        'BA': '3', 'BB': '4', 'BO': '5',
        'OA': '6', 'OB': '7', 'OO': '8'
    }

    # Strip spaces and process the ABO string in chunks of 2
    abo_str = abo_str.replace(' ', '')
    base9_str = ''.join(reverse_mapping[abo_str[i:i+2]] for i in range(0, len(abo_str), 2))

    # Convert Base-9 chunks back to ASCII values
    def base9_to_int(base9_str):
        return int(base9_str, 9)

    ascii_values = [base9_to_int(base9_str[i:i+3]) for i in range(0, len(base9_str), 3)]
    decrypted_message = ''.join(chr(ascii_val) for ascii_val in ascii_values)

    return base9_str, ascii_values, decrypted_message

# Main Menu
def main():
    """
    Main Menu for the ABO Cipher program. Handles user input and output options.
    """
    while True:
        print("\n###### ABO CIPHER MENU ######")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit\n")    

        choice = input("Choose an option: ").strip().lower()

        if choice == '1':
            # Encrypted a message
            message = input("\nEnter message or '.txt' file to encrypt: ").strip()

            if message.endswith(".txt"):
                try:
                    with open(message, 'r') as file:
                        message = file.read().strip()
                except FileNotFoundError:
                    print(f"\n{message} not found. Please try again.")
                    continue

            # Encrypt the input
            ascii_values, base9_output, ABO_output = ascii_to_base9(message)        
            ABO_chunks = ' '.join(''.join(ABO_output)[i:i+2] for i in range(0, len(''.join(ABO_output)), 2))

            # Output options
            print("\nHow would you like to output the encrypted message?")
            print("1. Print to screen")
            print("2. Write to file")
            output_choice = input("Chose an option: ").strip()

            if output_choice == '1':
                """
                Uncomment the desired options to print to screen.
                """
                #print("\nASCII Value:", ' '.join(map(str, ascii_values)))      # Prints as ASCII values
                #print("\nBase9 conversion:", ' '.join(base9_output))        # Prints as Base9
                #print("\nABO in chunks of 2:", ABO_chunks)              # Prints as chunks of 2
                print("\nABO Joined string:", ''.join(ABO_output))          # Prints as string
                
            elif output_choice == '2':
                output_file = input("Enter the output file name (e.g., encrypted.txt): ").strip()
                if not output_file.endswith(".txt"):
                    output_file += ".txt"
                with open(output_file, 'w') as file:
                    """
                    Uncomment the desired options to write to file.
                    """
                    file.write("ABO String: " + ' '.join(ABO_output) + '\n')                 # Writes as string
                    #file.write("ABO Chunks of 2: " + (ABO_chunks) + '\n')                 # Writes as chunks of 2
                    #file.write("ASCII Values: " + ' '.join(map(str, ascii_values)) + '\n')       # Writes as ASCII values 
                    #file.write("Base9 conversion: " + ' '.join(base9_output))               # Writes as Base9
                print(f"\nEncrypted message written to {output_file}")
            else:
                print("Invalid choice. Returning to main menu.")

        # Decrypt the user input message
        elif choice == '2':
            # Decrypt a message
            message = input("\nEnter ABO string to Decrypt (with or without spaces) or a '.txt' file: ")

            if message.endswith(".txt"):
                try:
                    with open(message, 'r') as file:
                        message = file.read().strip()
                        ##content = file.read()
                except FileNotFoundError:
                    print(f"\n{message} not found. Please try again.")
                    continue
            
            # Decrypting the input
            try:
                base9_str, ascii_values, decrypted_message = ABO_to_ascii(message)

                # Output options
                print("\nHow would you like to output the decrypted message?")
                print("1. Print to screen")
                print("2. Write to file")
                output_choice = input("Chose an option: ").strip()

                if output_choice == '1':
                    """
                    Uncomment the desired options to print to screen.
                    """
                    #print("\nBase9 Representation: ", ' '.join([base9_str[i:i+3] for i in range(0, len(base9_str), 3)]))      # Prints as Base9
                    #print("\nASCII Value: ", ' '.join(map(str, ascii_values)))                                         # Prints as ASCII values
                    print("\nDecrypted message:", decrypted_message)                                             # Prints as string

                elif output_choice == '2':
                    output_file = input("Enter the output file name (e.g., decrypted.txt): ").strip()
                    if not output_file.endswith(".txt"):
                        output_file += ".txt"
                    with open(output_file, 'w') as file:
                        """
                        Uncomment the desired options to write to file.
                        """
                        file.write("Decrypted Message: " + (decrypted_message) + '\n')                                         # Writes as string
                        #file.write("Base9 Representation: " + ' '.join([base9_str[i:i+3] for i in range(0, len(base9_str), 3)]) + '\n')    # Writes as Base9 
                        #file.write("ASCII Values: " + ' '.join(map(str, ascii_values)))                                           # Writes as ASCII values

                    print(f"\nDecrypted message written to {output_file}")
                else:
                    print("Invalid choice. Returning to main menu.")
            except (KeyError, ValueError):
                print("\nInvalid ABO string. Decryption failed.")
                           
        elif choice == '3':
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Entry point
if __name__ == "__main__":
    main()
