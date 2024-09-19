import pandas as pd


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


def mask_data(df, col):
    df[col] = 'xxxxx'
    return df


if __name__ == "__main__":
    df = pd.read_csv('student_data_with_fake_pii.csv')
    print(df.head())

    cols_to_mask = ['name', 'ssn']
    for col in cols_to_mask:
        df = mask_data(df, col)

    print(df.head())
