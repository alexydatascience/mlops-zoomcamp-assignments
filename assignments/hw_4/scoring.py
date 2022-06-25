import argparse
import pickle
import pandas as pd


CATEGORICAL = ['PUlocationID', 'DOlocationID']


def read_data(filename):
    df = pd.read_parquet(filename)

    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[CATEGORICAL] = df[CATEGORICAL].fillna(-1).astype('int').astype('str')

    return df


def run(year, month):
    with open('model.bin', 'rb') as f_in:
        dv, lr = pickle.load(f_in)

    df = read_data(f'../../data/fhv_tripdata_{year:04d}-{month:02d}.parquet')
    dicts = df[CATEGORICAL].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = lr.predict(X_val)
    print(y_pred.mean())

    return y_pred


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--year",
        default=2021,
        type=int
    )
    parser.add_argument(
        "--month",
        default=3,
        type=int
    )
    args = parser.parse_args()

    run(args.year, args.month)
