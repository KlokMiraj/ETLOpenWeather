def transform_data(data):
    transformed_data = {
        "city_timezone": data["timezone"],
        "temperature": data["data"][0]["temp"] - 273.15,  # Kelvin to Celsius
        "feels_like": data["data"][0]["feels_like"] - 273.15,  # Kelvin to Celsius
        "pressure": data["data"][0]["pressure"],
        "humidity": data["data"][0]["humidity"],
        "wind_speed": data["data"][0]["wind_speed"],
        "clouds": data["data"][0]["clouds"],
        "weather_description": data["data"][0]["weather"][0]["description"]
    }

    return transformed_data
