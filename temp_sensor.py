import time
import adafruit_dht
import board

# Initialize the DHT11 sensor on GPIO19

def get_temp():

        # Set up GPIO mode
    
    try:
        # Read the temperature and humidity
        dht_device = adafruit_dht.DHT11(board.D26)
        print(dht_device,"DHT",type(dht_device))
        print(dir(dht_device),"python obj")
        
        # dht_device = adafruit_dht.DHT11(16)
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        if temperature is not None or humidity is not None:
            print(f"Temp: {temperature}°C    Humidity: {humidity}%")
            return f"Temp: {temperature}°C    Humidity: {humidity}%"
        else:
            print("Failed to retrieve data from sensor.")
            return "Failed to retrieve data from sensor."
    except RuntimeError as error:
        # Handle occasional sensor errors
        print(str(error.args[0]) + "Temp Error")
        dht_device.exit()
        return(str(error.args[0]) + "Temp Error")
    except Exception as e:
        print(f"Unexpected error: {e}")
        dht_device.exit()
        return f"Unexpected error: {e}"
    
