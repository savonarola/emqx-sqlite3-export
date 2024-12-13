import json
import os
import sqlite3
import sys

from flask import Flask, Response, request

db_file = os.environ.get('DB_FILE')
if db_file is None:
    sys.exit("DB_FILE environment variable must be set")

app = Flask(__name__)


@app.route('/message_published', methods=['POST'])
def message_published():
    data = request.get_json()

    sensor_id = sensor_id_from_topic(data["topic"])
    if sensor_id is None:
        # Just ignore messages that don't match the expected
        # topic format: sensor/<sensor_id>/data
        return Response(status=200)

    paylaod = json.loads(data["payload"])
    temperature = paylaod["temperature"]
    created_at = data["publish_received_at"] // 1000

    conn = sqlite3.connect(db_file)
    conn.execute(
        "INSERT INTO measurements(sensor_id, temperature, created_at) "
        "VALUES (?, ?, ?)",
        (sensor_id, temperature, created_at)
    )
    conn.commit()
    conn.close()
    return Response(status=200)


def sensor_id_from_topic(topic):
    segments = topic.split('/', 3)
    if len(segments) < 3 or segments[0] != "sensor" or segments[2] != "data":
        return None
    return segments[1]
