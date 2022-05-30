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
# Q3. Train a model with autolog
```
cd assignments/
python train.py --data_path ../prepared_data/
```
```
mlflow ui
```
# Q4. Launch the tracking server locally
```
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts
```
# Q5. Tune the hyperparameters of the model
```
cd assignments/
python hpo.py --data_path ../prepared_data/
```
ans: 6.628
# Q6. Promote the best model to the model registry
```
cd assignments/
python register_model.py  --data_path ../prepared_data/
```
ans: 6.55
