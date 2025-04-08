import sqlite3
import random
import time
import paho.mqtt.publish as publish
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY,
    temperature REAL,
    humidity REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)''')
conn.commit()
TEMP_THRESHOLD = 30
while True:
    temperature = round(random.uniform(25, 35), 2)
    humidity = round(random.uniform(40, 70), 2)
    print(f"Simulated Temp: {temperature}°C, Humidity: {humidity}%")
    cursor.execute("INSERT INTO sensor_data (temperature, humidity) VALUES (?, ?)", (temperature, humidity))
    conn.commit()
    if temperature > TEMP_THRESHOLD:
        publish.single("home/alert", f"ALERT: High Temp {temperature}°C", hostname="test.mosquitto.org")
        print("⚠️ ALERT SENT!")

    time.sleep(5) 
