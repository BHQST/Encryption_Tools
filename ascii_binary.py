# converts ascii or text into binary

def ascii_to_bin(x):
    binary_int = int.from_bytes(usr_input, "big")
    binary_string = bin(binary_int)
    return binary_string

usr_input = input("Enter message to convert to binary: ").encode()


binary_int = "0" + ascii_to_bin(usr_input)[2:]

print(binary_int)

