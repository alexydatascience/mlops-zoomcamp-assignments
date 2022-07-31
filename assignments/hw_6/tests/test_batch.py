import pandas as pd
from datetime import datetime

from batch import prepare_data


def dt(hour, minute, second=0):
    return datetime(2021, 1, 1, hour, minute, second)

def test_prepare_data():
    data = [
        (None, None, dt(1, 2), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, 1, dt(1, 2, 0), dt(1, 2, 50)),
        (1, 1, dt(1, 2, 0), dt(2, 2, 1)),        
    ]
    columns = ['PUlocationID', 'DOlocationID', 'pickup_datetime', 'dropOff_datetime']
    df = pd.DataFrame(data, columns=columns)
    categorical = ['PUlocationID', 'DOlocationID']
    actual = prepare_data(df, categorical)

    expected = [
        {'PUlocationID': '-1',
        'DOlocationID': '-1',
        'pickup_datetime': pd.Timestamp('2021-01-01 01:02:00'),
        'dropOff_datetime': pd.Timestamp('2021-01-01 01:10:00'),
        'duration': 8.000000000000002
        },
        {'PUlocationID': '1',
        'DOlocationID': '1',
        'pickup_datetime': pd.Timestamp('2021-01-01 01:02:00'),
        'dropOff_datetime': pd.Timestamp('2021-01-01 01:10:00'),
        'duration': 8.000000000000002
        }
        ]

    expected = pd.DataFrame(expected)
    
    assert actual.equals(expected)
