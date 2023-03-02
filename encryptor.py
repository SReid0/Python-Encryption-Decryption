from cryptography.fernet import Fernet

# Take input file and read plaintext
with open('letter.txt', 'rb') as input_file:
    plaintext = input_file.read()

# Use Fernet library for the key
key = Fernet.generate_key()

# Use Fernet library for seed
seed = Fernet(key)

# Encrypt the plaintext using the seed
ciphertext = seed.encrypt(plaintext)

# Write the ciphertext to the output file
with open('secret', 'wb') as output_file:
    output_file.write(ciphertext)

# Write the key to a separate file for later decryption
with open('key.txt', 'wb') as key_file:
    key_file.write(key)
