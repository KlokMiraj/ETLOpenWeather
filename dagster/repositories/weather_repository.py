from abc import ABC, abstractmethod

class WeatherRepository(ABC):
    @abstractmethod
    def get_weather_data(self, location: str) -> WeatherData:
        pass
    