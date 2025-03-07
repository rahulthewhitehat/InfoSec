# Implementation of Confidentiality

def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "d":
        shift = -shift  # Reverse shift for decryption

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char 

    return result


# Ask user whether to encrypt or decrypt
mode = input("Do you want to encrypt or decrypt? (enter 'e' or 'd'): ").strip().lower()

if mode not in ["e", "d"]:
    print("Invalid option. Please enter 'e for enc' or 'd for dec'.")
else:
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    
    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")
