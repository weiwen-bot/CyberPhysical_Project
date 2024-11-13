import Adafruit_DHT
import time


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 19

try:
    while True:

        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            print(f"Temp: {temperature:.1f}C  Humidity: {humidity:.1f}%")
        else:
            print("Failed to retrieve data from the sensor")

        time.sleep(2)

except KeyboardInterrupt:
    print("Program stopped by user") 