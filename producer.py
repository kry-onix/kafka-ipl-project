from kafka import KafkaProducer
import json 
# import time

producer = KafkaProducer(
    bootstrap_servers = "localhost:9092",
        value_serializer = lambda v:
    json.dumps(v).encode("utf-8")
)
# matches = [
#     {
#         "team1": "CSK",
#         "team2": "MI",
#         "runs": 180,
#         "wickets": 5,
#         "overs": 20
#     },
#     {
#         "team1": "RCB",
#         "team2": "KKR",
#         "runs": 165,
#         "wickets": 7,
#         "overs": 20
#     },
#     {
#         "team1": "MI",
#         "team2": "DC",
#         "runs": 195,
#         "wickets": 4,
#         "overs": 20
#     }
# ]
# for match in matches:
#     producer.send("ipl-matches",
# value=match)
#     print("sent:", match)
#     time.sleep(2)
# producer.flush()
# producer.close()    

data = {
    "runs":100,
    "wickets": 2,
    "overs": 12
}
producer.send("ipl-matches", value=data)
producer.flush()
print("IPL data sent:", data)
