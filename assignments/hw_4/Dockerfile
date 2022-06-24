FROM agrigorev/zoomcamp-model:mlops-3.9.7-slim

WORKDIR /APP
COPY [ "Pipfile", "Pipfile.lock", "scoring.py", "./" ]
RUN ls && apt-get update && \
    apt-get install wget unzip zip -y && \
    pip install -U pip && \
    pip install pipenv && \
    mkdir ../../data && \
    pipenv install --system --deploy && \
    wget -P ../../data https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_2021-04.parquet && \
    mv ../app/model.bin . && \
    python scoring.py --year=2021 --month=4