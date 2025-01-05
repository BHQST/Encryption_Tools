# ABO Cipher: A Base-9 Encoding and Decoding System

## Description
The ABO Cipher is a custom cryptographic tool that encodes text into Base-9, mapping 
the resulting values into a unique ABO-like notation. The scrip allows users to encrypt and 
decrypt messages or text files, with flexibility in outputting results to the screen or saving 
them to files. This repository provides a Python implementation of the ABO Cipher with 
a menu-driven interface for ease of use.

---

## Work List
- [ ] May add a gui and some other minor functions.
- [ ] Fix the Multiple Write outputs to write to file correctly

---

## Features
- **Encrypt Messages**: Convert text to custom ABO notation.
- **Decrypt Messages**: Decode ABO notation back to readable text.
- **File support**: Encrypt of decrypt from '.txt' files.
- **Output options**: Print results to the screen or save to files.
- **Error Handling**: Gracefully handles invalid input or file errors.
- **Menu-Driven Interface**: Easy navigation for users.

---

## Requirements
 - **Python Version**: Python 3.7 or later.

 - **Operating System**: Any OS with Python installed.

---

## Installation
1. Clone the repository:
 ```bash
 git clone https://github.com/BHQST/Encryption_Tools.git
 ```

2. Navigate to the directory:
 ```bash
 cd Encryption_Tools/ABO_Encryption
 ```

3. Run the script:
 ```bash
 python3 ABO_Encryption.py
 ```
---

## Usage
1: Encrypt a Message
	- Enter a string or provide a '.txt' file to encrypt
	- The output can either be displayed on the screen or saved to file.
2: Decrypt a Message
	- Enter an ABO string (with or without spaces) or provide a '.txt' file containing the string to decrypt.
	- The decrypted message can be displayed on the screen or save to file.
3: Quit 
	- Exit the program 

---

## Example Usage
$ python3 abo_cipher.py
######MENU######
1. Encrypt a message
2. Decrypt a message
3. Quit

Choose an option: 1

Enter the message to encrypt: Hello World

ABO Conversion: AAOOAAABAOAOABBAAAABBAAAABBABAAABABOABAAOAABBABAABBAOAABBAAAABAOAB

///////////////////////////////////////////////////////////////////////////

$ python3 abo_cipher.py
######MENU######
1. Encrypt a message
2. Decrypt a message
3. Quit

Choose an option: 2

Enter ABO string to Decrypt (with or without spaces): AAOOAAABAOAOABBAAAABBAAAABBABAAABABOABAAOAABBABAABBAOAABBAAAABAOAB

ABO Conversion: Hello World

///////////////////////////////////////////////////////////////////////////

The above examples can also read from a '.txt' and output to a '.txt'

---

## Error Handling
- If an invalid ABO string is provided for decryption, the program will output: Invalid ABO string. Decryption failed.
- If a specified '.txt' file cannot be found, the program will output: File not found. Please ensure the file exists and try again.

---

## License
- Please refer to LICENSE

---

## Contributions
- Contributions are wilcome! Feel free to fork the repository, makes changes, and submit a pull request.

---

## Contact 
- Created by Ghost Squad
- For inquiries or support, please contact:
- [theforgedesign@protonmail.com]
- Enjoy encrypting with the ABO cipher!
