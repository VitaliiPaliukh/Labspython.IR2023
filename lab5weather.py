from enum import Enum

class WeatherType(Enum):
    SUNNY = 1
    CLOUDY = 2
    RAINY = 3
    FOGGY = 4


class Weather:
    def __init__(self, day, city , country, temp, humidity, wind_speed, weather_type ):
        self.day = day
        self.city = city
        self.country = country
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.weather_type = weather_type

    def __str__(self):
        return f"date: {self.day}, city: {self.city}, country: {self.country}, temp: {self.temp}°С ,\
              humidity: {self.humidity}%, wind: {self.wind_speed}m/s , Weather type: {self.weather_type.name} "
    
    def __repr__(self):
        return f"Wheather('{self.day}, {self.city}, {self.country}, {self.temp}, {self.humidity}, {self.wind_speed}') "


class WeatherCalendar(Weather):
    def __init__(self):
        self.weather_info = []

    def add_weather_info(self, weather):
        self.weather_info.append(weather)

    def find_max_temperature(self, day):
        max_temp = None
        for info in self.weather_info:
            if info.day == day:
                if max_temp is None or info.temp > max_temp:
                        max_temp = info.temp

        if max_temp is not None:
            result = max_temp
        else:
            result = "Not enough data" 
        return result    

    def is_lviv_weather(self, humitidy, weather_type):
        if humitidy > 80 and weather_type == WeatherType.RAINY:
            result = "The typical day in Lviv"
        else:
            result = "u r the lucky man"
        return result   
         
    def get_day(self, record):
        return record.day

    def sort_weather_info(self):
        self.weather_info.sort(key = self.get_day)




            
       
                    
