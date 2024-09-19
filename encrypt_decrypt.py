import pandas as pd
from cryptography.fernet import Fernet


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def encrypt_value(value, cipher):
    return cipher.encrypt(str(value).encode())


def decrypt_value(encrypted_value, cipher):
    return cipher.decrypt(encrypted_value).decode()


if __name__ == "__main__":
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    print(key)
    print()

    df = pd.read_csv('student_data_with_fake_pii.csv')
    print(df.head())
    print()

    cols_to_encrypt = ['name', 'ssn']
    for col in cols_to_encrypt:
        df[col] = df[col].apply(lambda x: encrypt_value(x, cipher_suite))

    print(df.head())
    print()

    for col in cols_to_encrypt:
        df[col] = df[col].apply(lambda x: decrypt_value(x, cipher_suite))

    print(df.head())
