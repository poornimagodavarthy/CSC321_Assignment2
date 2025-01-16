from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

plaintext = 'hello this is random text'


def ECB_encrypt(file_path, key):
    block_size = AES.block_size
    ciphertext = b""
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_path, 'r') as file:
        while True:
            chunk  = file.read(block_size).encode()
            if not chunk:
                break
            if len(chunk) < block_size:
                chunk = pad(chunk, block_size, style='pkcs7')
            encrypted_chunk = cipher.encrypt(chunk)
            ciphertext += encrypted_chunk
    return ciphertext

#pkcs #7 padding, fill with 4444
def decrypt(ciphertext, key):
    pass

# XOR with initialization vector
#XOR prev blocks
def CBC_encrypt(file_path, key, initialization_vector):
    block_size = AES.block_size
    ciphertext = b""
    with open(file_path, 'r') as file:
        cipher = AES.new(key, AES.MODE_ECB)
        chunk = file.read(block_size).encode()
        curr_chunk = bytes([initialization_vector ^ chunk])
        ciphertext += cipher.encrypt(curr_chunk)
        while True:
            chunk  = file.read(block_size).encode()
            if not chunk:
                break
            if len(chunk) < block_size:
                chunk = pad(chunk, block_size, style='pkcs7')
            #curr_chunk = curr_chunk ^ chunk
            encrypted_chunk = cipher.encrypt(curr_chunk)
            ciphertext += encrypted_chunk
    return ciphertext
def submit():
    pass
def verify():
    pass

def main():
    key = get_random_bytes(16)
    file_path = './test'

    #ECB
    ciphertext = ECB_encrypt(file_path, key)
    print(ciphertext)

    #CBC
    intilization_vector = get_random_bytes(16)
    encrypted = CBC_encrypt(file_path, key, intilization_vector)
    print(encrypted)

main()