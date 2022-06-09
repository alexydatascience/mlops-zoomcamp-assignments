# Q1. Converting the script to a Prefect flow
ans: train_model
# Q2. Parameterizing the flow
```
python assignments/hw_3/homework.py
```
```
prefect orion start
```
ans: 11.637
# Q3. Saving the model and artifacts
```
python assignments/hw_3/homework.py
```
```
stat dv-2021-08-15.b 
```
ans: 13,000 bytes
# Q4. Creating a deployment with a CronSchedule
```
cd assignments/
prefect deployment create homework.py
```
ans: 0 9 15 * *
# Q5. Viewing the Deployment
```
cd assignments/
prefect deployment create homework.py
```
ans: 4
# Q6. Creating a work-queue
ans: ```prefect work-queue ls```
