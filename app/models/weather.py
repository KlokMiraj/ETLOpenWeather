from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session

Base= declarative_base()

class Weather(Base):
    __tablename__= "weather"
    
    id = Column(Integer, primary_key=True, index=True)
    city= Column(String)
    temperature= Column(Float)
    humidity= Column(Integer)
    wind_speed = Column(Float)
    
