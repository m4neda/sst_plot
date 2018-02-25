import banpei
import pandas as pd
import matplotlib.pyplot as plt
import os


def load_columns_name():
    col_name = 'test'
    return col_name


def load_use_columns():
    use_col = 'test'
    return use_col


def pd_read_csv(input_path):
    df = pd.read_csv(
        input_path,
        parse_dates=["ReceivedAt", ],
        index_col="ReceivedAt",
        header=None,
        names=load_column_name(),
        usecols=load_use_columns(),
    )

    return df


def main():
    input_path = 'input.csv'
    df = pd_read_csv(input_path)


if __name__ == '__main__':
    main()