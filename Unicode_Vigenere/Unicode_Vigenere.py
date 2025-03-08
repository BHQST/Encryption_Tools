#! usr/bin/env python 3.11
"""
A simple script to rotate different conversions of encoding.
Key and string are hard coded. 
	You can uncomment for user input from cli.
"""
def printable_char(c: str) -> str:
	# Return a visible representation for non-printable character
	if c == ' ':
		return " "
	elif not c.isprintable():
		return f" "
		# Return Ascii code
		#return f"<0x{ord(c):02x}>" # comment on of depending on user preference
	return c
	
def display_rotated_string(input_str: str, key: str) -> str:
    print("Rotation Table:")
    header = (
        f"{'Char':<8}{'Oct':<8}{'Dec':<8}{'Hex':<8}"
        f"{'Key':<8}{'Dec':<8}"
        f"{'Char':<8}{'Oct':<8}{'Dec':<8}{'Hex':<8}"
    )
    print(header)
    print("-" * 77)
    
    rotated_chars = []  # Accumulate rotated characters to form final rotated string
    key_len = len(key)
    
    for i, char in enumerate(input_str):
        # Original character conversions
        orig_val = ord(char)
        orig_octal = format(orig_val, 'o')
        orig_hex = format(orig_val, 'x')
        
        # Determine the corresponding key character (cycling through the key)
        key_char = key[i % key_len]
        key_val = ord(key_char)
        
        # Compute rotated value (using modulo 256)
        rotated_val = (orig_val + key_val) % 256
        rotated_char = chr(rotated_val)
        rotated_chars.append(rotated_char)
        rotated_octal = format(rotated_val, 'o')
        rotated_hex = format(rotated_val, 'x')
        
        # Print the row for this character
        print(f"{printable_char(char):<8}{orig_octal:<8}{orig_val:<8}{orig_hex:<8}"
              f"{printable_char(key_char):<8}{key_val:<8}"
              f"{printable_char(rotated_char):<8}{rotated_octal:<8}{rotated_val:<8}{rotated_hex:<8}")
    
    rotated_string = ''.join(rotated_chars)
#    print("\nFinal Rotated String:")
#    print(rotated_string)
#    print()
    return rotated_string

def print_input_conversions(input_str: str) -> None:
    # Build space-separated conversion strings for the input string
    octal_str = " ".join(format(ord(c), 'o') for c in input_str)
    decimal_str = " ".join(str(ord(c)) for c in input_str)
    hex_str = " ".join(format(ord(c), 'x') for c in input_str)
    
    print("\nInput String Conversions:")
    print("Original String:->", input_str)
    print("Octal:->", octal_str)
    print("Decimal:->", decimal_str)
    print("Hex:->", hex_str)
    print()

def print_rotated_conversions(rotated_str: str) -> None:
    # Build space-separated conversion strings for the rotated string
    octal_str = " ".join(format(ord(c), 'o') for c in rotated_str)
    decimal_str = " ".join(str(ord(c)) for c in rotated_str)
    hex_str = " ".join(format(ord(c), 'x') for c in rotated_str)
    
    print("Rotated String Conversions:")
    print("Rotated String:->", rotated_str)
    print("Octal:->", octal_str)
    print("Decimal:->", decimal_str)
    print("Hex:->", hex_str)
    print()

def print_key_conversions(key: str) -> None:
    # Print a table for the key conversions: index, character, octal, decimal, hex
    print("Key Conversion Table:")
    print("{:<6}{:<8}{:<8}{:<6}".format("Char", "Oct", "Dec", "Hex"))
    print("-" * 27)
    
    for i, char in enumerate(key):
        octal_val = format(ord(char), 'o')
        decimal_val = ord(char)
        hex_val = format(ord(char), 'x')
        print("{:<6}{:<8}{:<8}{:<6}".format(printable_char(char), octal_val, decimal_val, hex_val))
    print()

def main():
    # User inputed key and string	
    #key = input("Enter the key (characters): ")
    #input_str = input("Enter the input string: ")
    
    # Hard-coded values
    key = "test"
    input_str = "this is a test"
    
    # Print the key conversion table
    print_key_conversions(key)
    # Get and display the rotation table; capture the rotated string
    rotated_str = display_rotated_string(input_str, key)
    # Print the original input string conversions
    print_input_conversions(input_str)
    # Print the rotated string conversions
    print_rotated_conversions(rotated_str)


if __name__ == "__main__":
    main()
