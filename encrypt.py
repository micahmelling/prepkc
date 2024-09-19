import hashlib
import pandas as pd


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def run_sha256_hash(value):
    return hashlib.sha256(value.encode()).hexdigest()


if __name__ == "__main__":
    df = pd.read_csv('student_data_with_fake_pii.csv')
    print(df.head())

    cols_to_encrypt = ['name', 'ssn']
    for col in cols_to_encrypt:
        df[col] = df[col].apply(run_sha256_hash)

    print(df.head())
