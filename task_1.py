from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def ECB_encrypt(file_path, key, output_path):
    block_size = AES.block_size
    ciphertext = b""
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_path, 'rb') as file:
        if ".bmp" in file_path:
            header_size = 54
            header = file.read(header_size)
            ciphertext+=header
        while True:
            chunk  = file.read(block_size)
            if not chunk:
                break
            if len(chunk) < block_size:
                chunk = pad(chunk, block_size, style='pkcs7')
            encrypted_chunk = cipher.encrypt(chunk)
            ciphertext += encrypted_chunk
    
    with open(output_path, 'wb') as output_file:
        output_file.write(ciphertext)
    #return ciphertext

def CBC_encrypt(file_path, key, initialization_vector):
    block_size = AES.block_size
    ciphertext = b""

    with open(file_path, 'rb') as file:
        if ".bmp" in file_path:
            header_size = 54
            header = file.read(header_size)
            ciphertext+=header

        #cipher = AES.new(key, AES.MODE_CBC)
        cipher = AES.new(key, AES.MODE_ECB)

        chunk = file.read(block_size)
        if not chunk:
            return ciphertext
        if len(chunk) < block_size:
            chunk = pad(chunk, block_size, style='pkcs7')
        curr_chunk = bytes([b1 ^ b2 for b1, b2 in zip(chunk, initialization_vector)])
        encrypted_chunk = cipher.encrypt(curr_chunk)
        ciphertext += encrypted_chunk
        prev_encrypted = encrypted_chunk
        while True:
            chunk  = file.read(block_size)
            if not chunk:
                break
            if len(chunk) < block_size:
                chunk = pad(chunk, block_size, style='pkcs7')
            curr_chunk = bytes([b1 ^ b2 for b1, b2 in zip(chunk, prev_encrypted)])
            encrypted_chunk = cipher.encrypt(curr_chunk)
            ciphertext += encrypted_chunk
            prev_encrypted = encrypted_chunk
    return ciphertext

def ECB_decrypt(cipherfile, cipher_ecb, output_path):
    plaintext = b""
    header_size= 54
    with open(cipherfile, "rb") as ciphertext:
        header = ciphertext.read(header_size)
        pixel_data = ciphertext.read()
    plaintext+= unpad(cipher_ecb.decrypt(pixel_data), AES.block_size, style="pkcs7")
    with open(output_path, 'wb') as bmp_file:
        bmp_file.write(header)
        bmp_file.write(plaintext)
        
def submit():
    pass
def verify():
    pass

def main():
    key = get_random_bytes(16)
    #ECB
    #encryption
    file_path2 = "/Users/poorn1/Desktop/Security_Assignment/mustang.bmp"
    output_path = "./output"
    ECB_encrypt(file_path2, key, output_path)
    #decryption
    cipher_ecb = AES.new(key, AES.MODE_ECB)
    decoded_output = "./decoded_output.bmp"
    ECB_decrypt(output_path, cipher_ecb, decoded_output)

    #CBC
    #encryption
    initialization_vector = get_random_bytes(16)
    key2 = get_random_bytes(16)
    cbc_ciphertext = CBC_encrypt(file_path2, key2, initialization_vector)
    #print(cbc_ciphertext)

    #decryption
    cipher_cbc = AES.new(key2, AES.MODE_CBC, iv=initialization_vector)
    #decrypted_cbc = unpad(cipher_cbc.decrypt(cbc_ciphertext), AES.block_size, style='pkcs7')

    #decrypted_cbc = unpad(cipher_cbc.decrypt(cbc_ciphertext), AES.block_size, style='pkcs7')
    #print(decrypted_cbc)
main()