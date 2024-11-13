import time
import adafruit_dht
import board

# Initialize the DHT11 sensor on GPIO19

def get_temp():

        # Set up GPIO mode
    
    try:
        # Read the temperature and humidity
        dht_device = adafruit_dht.DHT11(board.D16)
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        # print(f"Temp: {temperature}°C    Humidity: {humidity}%")
        return(f"Temp: {temperature}°C    Humidity: {humidity}%")
    except Exception as error:
        # Handle occasional sensor errors
        print(str(error) + "Temp Error")
        return(str(error) + "Temp Error")
