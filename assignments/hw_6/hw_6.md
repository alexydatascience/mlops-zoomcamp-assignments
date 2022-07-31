# Q1. Refactoring
Question 1: The main block 
ans: see batch.py
```
if __name__ == "__main__":
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    main(year, month)
```

# Q2. Installing pytest
Question 2: The other file in the test folder 
ans: \_\_init__.py

# Q3. Writing first unit test
Question 3: How many rows after preprocessing 
ans: 2

# Q4. Mocking S3 with Localstack
Question 4: Command for creating a bucket with localstack
ans: ```aws --endpoint-url=http://localhost:4566 s3 mb s3://nyc-duration``` or ```awslocal s3 mb s3://nyc-duration```

# Q5. Creating test data
Question 5: Size for the test dataframe