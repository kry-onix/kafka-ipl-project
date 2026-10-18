# Kafka IPL Project

Real-time IPL score prediction using Apache Kafka and Linear Regression.

# How it works
-Producer.py streams simulated ball-by-ball data every second
-consumer.py computes run rate and predicts final score
-model.py trains the model and saves model.pkl

## Result 
R2 score : 0.99 (small sample dataset, 18 rows)

## Limitations 
Training data is a small hand-made sample and the live stream is simulated.

## Run 
python3 model.py
python3 consumer.py
python3 producer.py

## Tech 
Python, Apache Kafka, Numpy, Scikit-learn, Joblib

