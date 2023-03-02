from cryptography.fernet import Fernet

# Read secret file
with open('secret', 'rb') as input_file:
    ciphertext = input_file.read()

# Take key file and read the encryption key
with open('key.txt', 'rb') as key_file:
    key = key_file.read()

# Use Fernet for the seed
seed = Fernet(key)

# Decrypt the ciphertext using the seed
plaintext = seed.decrypt(ciphertext)

# Write the plaintext to the output file
with open('message.txt', 'wb') as output_file:
    output_file.write(plaintext)
