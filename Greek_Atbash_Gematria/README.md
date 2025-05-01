# Greek Atbash Cipher GUI

A desktop GUI application for encrypting Greek text using the Atbash cipher with optional ROT (rotation) shifting. The program also computes Greek gematria (numerical values of Greek letters) and presents a user-friendly interface built with Tkinter.

## Features

- Encrypts Greek text using the Atbash cipher
- Optional ROT shift encryption (adjustable by the user)
- Supports both uppercase and lowercase output
- Automatically removes accents from Greek input
- Displays original and encrypted gematria values and their numeric sums
- Clean and responsive GUI with copy/paste context menu support
- Input validation and error handling

## Technologies Used

- Python 3.x
- Tkinter (standard GUI library)
- unicodedata (for Unicode normalization)

This application relies only on Python’s standard library.

## Project Structure

```
GreekAtbashCipher/
├── main.py              # GUI interface built with Tkinter
├── atbash_core.py       # Cipher logic and gematria calculations
├── README.md            # Project documentation
└── requirements.txt     # Dependency file (minimal)
```

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Tkinter (pre-installed with most Python distributions)

### Running the Application

1. Clone or download the repository:

   ```bash
   git clone https://github.com/BHQST/Encryption_Tools/GreekAtbashCipher.git
   cd GreekAtbashCipher
   ```

2. Start the application:

   ```bash
   python3 main.py
   ```

## Usage Instructions

1. Enter valid Greek text in the input field.
2. Select the desired output case (Upper or Lower).
3. Optionally set a ROT shift value using the spinbox.
4. Click the "Encrypt" button.
5. The encrypted result and gematria details will be displayed in the output area.

## Gematria Support

Greek gematria values are assigned based on classical mappings. The application handles both uppercase and lowercase characters and includes special cases such as the final sigma (ς). Accents are automatically removed during normalization.

## Author

Developed by **Ghost Squad**  
Designed for educational, linguistic, and cryptographic use.

## License

This project is released for personal and academic use only. Redistribution or commercial use requires attribution. For licensing inquiries, please contact the author.

---

## requirements.txt

```txt
# Standard library only; no external dependencies required

# Optional: For environments missing tkinter (e.g., minimal Linux)
tk
```


No matter if UPPER of LOWER the value remains the same. 
[ΑΒΓΔΕϚΖΗΘΙΚΛΜΝΞΟΠϞΡΣΤΥΦΧΨΩϠ]
[αβγδεϛζηθικλμνξοπϟρστυφχψωϡ]

Α > 1 < α
Β > 2 < β
Γ > 3 < γ
Δ > 4 < δ
Ε > 5 < ε
Ϛ > 6 < ϛ
Ζ > 7 < ζ
Η > 8 < η
Θ > 9 < θ
Ι > 10 < ι
Κ > 20 < κ
Λ > 30 < λ
Μ > 40 < μ
Ν > 50 < ν
Ξ > 60 < ξ
Ο > 70 < ο
Π > 80 < π
Ϟ > 90 < ϟ
Ρ > 100 < ρ
Σ > 200 < σ
Τ > 300 < τ
Υ > 400 < υ
Φ > 500 < φ
Χ > 600 < χ
Ψ > 700 < ψ
Ω > 800 < ω
Ϡ > 900 < ϡ    # This one is commented out or not included. it gave different results.

