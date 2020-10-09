import json
import urllib3
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    
    logger.debug(event)
    
    CITY = event['currentIntent']['slots']['location']
    API_KEY = "56223e9f24789c3edf97b1cccd0c0a0f"
    
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    
    http = urllib3.PoolManager()
    
    # Fetch url
    resp = http.request('GET', URL)

    # Load url response to json
    result = json.loads(resp.data.decode('utf-8')) 

    # json elements
    temperature = result["main"]["temp"]
    pressure = result["main"]["pressure"]
    humidity = result["main"]["humidity"]
    weather_report = result["weather"][0]["description"]
    
    msg = "Temperature: {}, Pressure: {}, Humidity: {}, Weather Report: {}".format(temperature, pressure, humidity, weather_report)

    return {
        "sessionAttributes": event["sessionAttributes"],
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content" : msg
            }
        }
    }
