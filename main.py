import requests
import json
import os
from dotenv import load_dotenv

class CarWarmer:
    def __init__(self):
        # Load env file
        load_dotenv()
        # Assign variables based on env data
        api = os.getenv('API')
        lon = os.getenv('LON')
        lat = os.getenv('LAT')
        exclude = os.getenv('EXC')
        # Create url for api call
        url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api}&units=imperial&exclude={exclude}"
        self.gather_data(url)
        
    def gather_data(self, url):
        # Get data from Open Weather API
        data = requests.get(url)
        # Convert data to json
        weather_data = data.json()
        # Pull only current weather information data
        current_data = weather_data['current']
        # Pull only the weather informaiton from current weahter data
        weather = current_data['weather']
        # Coniditon is in a dict within a list
        condition_dict = weather[0]
        # Weather variables
        self.condition = condition_dict['main']
        self.temp = current_data['temp']
        self.feels_like = current_data['feels_like']
        self.description = condition_dict['description']
        self.check_weather()

    def check_weather(self):
        self.text_message = ''
        degree_sign = u'\N{DEGREE SIGN}'
        if self.temp < 36.0 and self.condition.lower() != "snow":
            self.text_message += f'Its currently {round(self.temp)}{degree_sign}F and feels like {round(self.feels_like)}{degree_sign}F, you might want to start your car.'
            self.text_message += f' The current weather can be described as "{self.description}"'
            print(self.text_message)
        if self.temp < 36.0 and self.condition.lower() == "snow":
            self.text_message += f'Its currently {round(self.temp)}{degree_sign}F and feels like {round(self.feels_like)}{degree_sign}F, you might want to start your car.'
            self.text_message += f' In addition, it is currently snowing. It would be wise to clean your windows.'
            self.text_message += f' The current weather can be described as "{self.description}"'
            print(self.text_message)

if __name__ == '__main__':
    app = CarWarmer()