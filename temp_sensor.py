import time
import adafruit_dht
import board

# Initialize the DHT11 sensor on GPIO19
dht_device = adafruit_dht.DHT11(board.D19)

try:
    while True:
        try:
            # Read the temperature and humidity
            temperature = dht_device.temperature
            humidity = dht_device.humidity
            print(f"Temp: {temperature}°C    Humidity: {humidity}%")
        except RuntimeError as error:
            # Handle occasional sensor errors
            print(error.args[0])
        time.sleep(2)

except KeyboardInterrupt:
    dht_device.exit()
    print("Program stopped by user")