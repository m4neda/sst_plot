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
        names=load_columns_name(),
        usecols=load_use_columns(),
    )

    return df


def load_sst_model(w, m=2, k=None, L=None):
    return banpei.SST(w, m, k, L)


def sst_detect(model, data):
    return model.detect(data)


def calculate_params_by_window(w):
    m = 2
    k = w
    L = w // 2
    return m, k, L


def main():
    w = 24
    input_path = 'input.csv'
    target = 'RSRP'

    df = pd_read_csv(input_path)

    m, k, L = calculate_params_by_window(w)

    model = load_sst_model(w, m, k, L)
    data = df[target]
    results = sst_detect(model, data)


if __name__ == '__main__':
    main()