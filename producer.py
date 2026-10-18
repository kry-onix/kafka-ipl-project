from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
	bootstrap_servers="localhost:9092",
	value_serializer=lambda v:
	json.dumps(v).encode("utf-8"))

runs = wickets = 0
for ball in range(1,121):
	runs += random.choice([0, 1, 1, 2, 4, 6])
	if random.random() < 0.05 and wickets < 10:
		wickets += 1
	data = {"runs": runs,
		"wickets": wickets,
		"overs": ball / 6}
	producer.send("ipl-matches", value=data)
	print("sent:", data)
	time.sleep(1)
	if  wickets == 10:
		break
producer.flush()

