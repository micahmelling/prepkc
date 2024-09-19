import pandas as pd
from faker import Faker


def read_data():
    return pd.read_csv('Student_performance_data _.csv')


def add_fake_pii(df):
    fake = Faker()
    df['name'] = [fake.name() for _ in range(len(df))]
    df['ssn'] = [fake.ssn() for _ in range(len(df))]
    return df


def save_data(df):
    df.to_csv('student_data_with_fake_pii.csv', index=False)


if __name__  == "__main__":
    student_df = read_data()
    student_df = add_fake_pii(student_df)
    save_data(student_df)
