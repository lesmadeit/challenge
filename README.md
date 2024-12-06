Image Hash Spoofing Tool

This is a Python-based tool for generating an altered image file that appears identical to the original image but has a SHA-based hash (SHA-512) starting with a specified hexadecimal prefix, to demonstrate how file hashes can be manipulated while preserving the image's visual integrity.


Features
 - Accepts an image file as input and modifies it to produce a hash with a desired prefix
 - Supports common image formats like JPEG and PNG.
 - Uses the SHA-512 hashing algorithm by default, with flexibility to use other SHA-based algorithms.
 - Ensures that the altered file is visually identical to the original

 Usage 

 Preriquisites
 - Python 3.7 or later
 - Install the required Python library:
 ``` pip install pillow ```

Running the Script

1. Command Syntax:
``` python challenge.py <target_hex_prefix> <original_image> <altered_image>  ```

- challenge.py: the name of the script.
- <target_hex_prefix>: The desired prefix for the hash (e.g. 0x24)
- <original_image>: The path to the input image file (e.g., original.jpg).
- <altered_image>: The path where the altered image will be saved (e.g., altered.jpg).

2. python challenge.py 0x24 original.jpg altered.jpg

3. Output:
- The altered image is saved as altered.jpg.
- The terminal will display the following:
Target Prefix: The one specified when running the script without the '0x'(eg. 24)
Original Image: (original.jpg)
Altered Image: (altered.jpg)

How It Works
1. Image Processing:
- The script uses the Pillow library to normalize the image format and ensure consistency.

2. Hash Calculation:
- The hashlib library calculates the file's hash based on the SHA-512 algorithm
- The hash is recalculated after each modification to check if it matches the desired prefix.

3. File Modification:
- A "nonce" (a small piece of data) is appended to the end of the image file.
- This process is repeated, incrementing the nonce, until the calculated hash begins with the specified prefix.

4. Result:
- Once the desired hash is achieved, the script stops and saves the altered file.

5. Keyboard Interrupt Handling: I've wrapped the modify_image loop inside a try-except block. This catches the KeyboardInterrupt error when you press Ctrl+C and exits gracefully without a traceback.
Graceful exit: When the KeyboardInterrupt is caught, a message is printed, and the script exits cleanly using sys.exit(0).


Examples of Target Prefixes

Short Prefixes(quick to compute):
- 0x1a
- 0xff
- 0x4c

Longer Prefixes(more challenging):
- 0xdead
- 0xbeef
- 0x12345678

Limitations
- Execution time increases exponentially with longer prefixes due to the computational effort required to find a matching hash.
- Only visually identical modifications are guaranteed; metadata changes may occur.

Dependencies
Python Libraries:
- Pillow: For image processing.
- hashlib: For hash computation (built into Python).

Development and Testing
1. Directory Setup:
- Place the script (challenge.py) and input image (original.jpg) in the same directory.
- Or provide full file paths during execution.
2. Testing:
- Try different target prefixes to observe how prefix length affects execution time.
- Verify the altered image's hash using:

``` certutil -hashfile altered.jpg SHA512 ```


Example Workflow
1. Prepare the Input:
- Ensure the input image (original.jpg) exists in your working directory.

2. Run the Script:

``` python challenge.py 0x24 original.jpg altered.jpg ```

3. Output:
A new file altered.jpg is created with the desired hash prefix (0x24).

4. Verify the result:

``` certutil -hashfile altered.jpg SHA512 ```













