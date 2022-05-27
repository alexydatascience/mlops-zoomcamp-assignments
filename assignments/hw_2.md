# Q1. Install MLflow
```
mlflow --vesion
mlflow, version 1.26.0
```
# Q2. Download and preprocess the data
```
python 02-experiment-tracking/homework/preprocess_data.py --raw_data_path data/ --dest_path prepared_data
cd prepared_data/
ls -1q | wc -l
4
```
Q3. Train a model with autolog
