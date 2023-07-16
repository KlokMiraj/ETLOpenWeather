from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from weather_data_pipeline.app.models.weather import Weather

BASE= declarative_base()

def load_data(weather_data, session):
    for data in weather_data:
        weather= Weather(**data)
        session.add(weather)
    session.commit()