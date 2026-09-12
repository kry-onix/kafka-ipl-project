from kafka import KafkaConsumer
import json
import numpy as np 
from model import model

consumer = KafkaConsumer(
    "ipl-matches",
bootstrap_servers="localhost:9092",
    value_deserializer=lambda v:
json.loads(v.decode("utf-8")),
    auto_offset_reset="earliest"
)
print("Waiting for IPL data...")

for message in consumer:
    data = message.value

    runs =data["runs"]
    wickets = data["wickets"]
    overs = data["overs"]
    run_rate = runs/overs
    wickets_remaining = 10 - wickets

    input_data = np.array([[
        runs,
        wickets,
        overs,
        run_rate,
        wickets_remaining
    ]])
    prediction = model.predict(input_data)
    print("\n---IPL Prediction ---")
    print("Current Runs:", runs)
    print("Wickets Lost: ", wickets)
    print("Overs: ", overs)
    print("Run Rate: ", round(run_rate, 2))
    print("Wickets Remaining: ", wickets_remaining)
    print("Predicted Final Score: ", round(prediction[0]))