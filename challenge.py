import hashlib
from PIL import Image
import sys
import os

def calculate_hash(file_path, hash_algorithm="sha512"):
    
    # Calculate the hash of a file.
    hash_func = hashlib.new(hash_algorithm)
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def modify_image(file_path, output_path, target_prefix, hash_algorithm="sha512"):

    # Modify the image to produce a hash with the desired prefix.
    img = Image.open(file_path)
    img = img.convert("RGB")  # Normalize format to ensure consistency.
    img.save(output_path)  # Save to initialize the file.

    # Open the output file in binary append mode.
    with open(output_path, "ab") as f:
        nonce = 0
        while True:
            try:
                # Append a nonce to the end of the file.
                f.seek(0, os.SEEK_END)
                f.write(nonce.to_bytes(8, byteorder="big"))
                
                # Calculate hash and check prefix.
                current_hash = calculate_hash(output_path, hash_algorithm)
                if current_hash.startswith(target_prefix):
                    print(f"Success! Hash: {current_hash}")
                    return

                # Remove the nonce and increment.
                nonce += 1
                f.seek(-8, os.SEEK_END)
                f.truncate()
            except KeyboardInterrupt:
                print("\nProcess interrupted by user. Exiting gracefully.")
                sys.exit(0)

def main():
    try:
        if len(sys.argv) != 4:
            print("Usage: python challenge.py <target_hex_prefix> <original_image> <altered_image>")
            sys.exit(1)

        target_prefix = sys.argv[1].lstrip("0x")  # Remove '0x' if present.
        original_image = sys.argv[2]
        altered_image = sys.argv[3]

        if not os.path.exists(original_image):
            print(f"Error: File '{original_image}' not found.")
            sys.exit(1)

        print(f"Target Prefix: {target_prefix}")
        print(f"Original Image: {original_image}")
        print(f"Altered Image: {altered_image}")
        
        modify_image(original_image, altered_image, target_prefix)

    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting gracefully.")
        sys.exit(0)

if __name__ == "__main__":
    main()
