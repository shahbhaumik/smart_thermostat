# Using forecast api from here https://github.com/ZeevG/python-forecast.io
# Importing datetime module to get current date and time
import forecastio
from datetime import datetime

# API key obtained from https://developer.forecast.io


class forecast:
        def __init__(self, lat, lng):
                self.api_key = ''
                self.lat = 33.466413
                self.lng = -111.898420
                self.current_time = datetime.now()
                self.hourly_time = list()
                self.hourly_temp = list()

        def get_forecast(self):
                daily_forecast = forecastio.load_forecast(self.api_key, self.lat, self.lng, time=self.current_time)
                byhour = daily_forecast.hourly()
                for hourlyData in byhour.data:
                        self.hourly_time.append(hourlyData.time)
                        self.hourly_temp.append(hourlyData.temperature)

getting_fore = forecast(33.466, -111.89)
getting_fore.get_forecast()
print getting_fore.hourly_temp, getting_fore.hourly_time
