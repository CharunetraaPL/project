import random
import time
import math

def generate_telemetry():
    telemetry = {
        "battery_voltage": round(random.uniform(9.5, 12.6), 2),
        "imu": {
            "roll": round(random.uniform(-180, 180), 2),
            "pitch": round(random.uniform(-90, 90), 2),
            "yaw": round(random.uniform(-180, 180), 2),
            "temperature": round(random.uniform(20, 50), 2),
            "altitude": round(random.uniform(0, 100), 2),
        },
        "gps": {
            "latitude": round(random.uniform(-90, 90), 6),
            "longitude": round(random.uniform(-180, 180), 6),
            "altitude": round(random.uniform(10, 100), 2),
        },
        "connection_health": random.choices(
            ["Excellent", "Good", "Poor", "No Signal"],
            weights=[50, 30, 15, 5],
            k=1
        )[0]
    }
    return telemetry