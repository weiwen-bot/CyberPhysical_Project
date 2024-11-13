import time
import adafruit_dht
import board

# Initialize the DHT11 sensor on GPIO19

def get_temp():

        # Set up GPIO mode
    dht_device = adafruit_dht.DHT11(board.D19)

    try:
        # Read the temperature and humidity
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        print(f"Temp: {temperature}°C    Humidity: {humidity}%")
        return(f"Temp: {temperature}°C    Humidity: {humidity}%")
    except RuntimeError as error:
        # Handle occasional sensor errors
        print(str(error.args[0]) + "Temp Error")
        return(str(error.args[0]) + "Temp Error")
