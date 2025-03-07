# Ex 2 - Implementation Of Integrity

import hashlib

def generate_hash(text, algorithm):
  
    if algorithm == "md5":
        hash_obj = hashlib.md5(text.encode())
    elif algorithm == "sha1":
        hash_obj = hashlib.sha1(text.encode())
    elif algorithm == "sha256":
        hash_obj = hashlib.sha256(text.encode())
    elif algorithm == "sha512":
        hash_obj = hashlib.sha512(text.encode())
    else:
        return "Invalid algorithm selected."

    return hash_obj.hexdigest()  # Return the hexadecimal digest

# Get user input
text = input("Enter the text to hash: ")
print("Select hashing algorithm: md5, sha1, sha256, sha512")
algorithm = input("Enter the algorithm: ").strip().lower()

# Generate and display the hash
hashed_text = generate_hash(text, algorithm)
print(f"Hashed Output ({algorithm}): {hashed_text}")
