import pandas as pd
import matplotlib.pyplot as plt

def plot_rsa():
    plt.figure(figsize=(10,6))
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    pd.set_option('display.width', None)
    rsa_data = pd.read_csv('rsa_data.csv', header=None, names=[
        'Key Size (bits)', 'Sign Time', 'Verify Time', 'Encrypt Time', 'Decrypt Time', 
        'Sign Throughput', 'Verify Throughput', 'Encrypt Throughput', 'Decrypt Throughput'
    ])
    

    rsa_data['Sign Throughput (bytes/sec)'] = rsa_data['Sign Throughput'] * (rsa_data['Key Size (bits)'] / 8)
    rsa_data['Verify Throughput (bytes/sec)'] = rsa_data['Verify Throughput'] * (rsa_data['Key Size (bits)'] / 8)
    rsa_data['Encrypt Throughput (bytes/sec)'] = rsa_data['Encrypt Throughput'] * (rsa_data['Key Size (bits)'] / 8)
    rsa_data['Decrypt Throughput (bytes/sec)'] = rsa_data['Decrypt Throughput'] * (rsa_data['Key Size (bits)'] / 8)

    plt.plot(rsa_data['Key Size (bits)'], rsa_data['Sign Throughput (bytes/sec)'], label='Sign Throughput', marker='o')
    plt.plot(rsa_data['Key Size (bits)'], rsa_data['Verify Throughput (bytes/sec)'], label='Verify Throughput', marker='o')
    plt.plot(rsa_data['Key Size (bits)'], rsa_data['Encrypt Throughput (bytes/sec)'], label='Encrypt Throughput', marker='o')
    plt.plot(rsa_data['Key Size (bits)'], rsa_data['Decrypt Throughput (bytes/sec)'], label='Decrypt Throughput', marker='o')

    plt.xlabel('RSA Key Size (bits)')
    plt.ylabel('Throughput (bytes/sec)')
    plt.title('RSA Key Size vs Throughput for Four RSA Functions')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_aes():
    plt.figure(figsize=(10,6))
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    pd.set_option('display.width', None)
    aes_data = pd.read_csv('aes_data.csv', header=None, names=[
        'type', '16 bytes', '64 bytes', '256 bytes', '1024 bytes', '8192 bytes', '16384 bytes'
    ])
    #print(aes_data)
    for column in aes_data.columns[1:]:
        aes_data[column] = aes_data[column] * 1000
        plt.plot(aes_data['type'], aes_data[column], label=column)
    plt.xlabel('AES Key Size (bits)')
    plt.ylabel('Throughput (bytes/sec)')
    plt.title('AES Key Size vs Throughput for Different Block Sizes')
    plt.legend()
    plt.grid(True)
    plt.show()
def main():
    plot_aes()
    
main()