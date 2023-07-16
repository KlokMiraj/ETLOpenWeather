from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from weather_data_pipeline.app.models.weather import Weather

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/weather_data_pipeline"

engine= create_engine(DATABASE_URL)
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

def insertData(transformed_data):
    db = SessionLocal()
    weather_data= Weather(**transformed_data)
    db.add(weather_data)
    db.commit()
    db.close()
    
def getData():
    db = SessionLocal()
    weather_data= db.query(Weather).all()
    db.close()
    return weather_data

def deleteData():
    db = SessionLocal()
    db.query(Weather).delete()
    db.commit()
    db.close()
    
def updateData(id, data):
    db = SessionLocal()
    db.query(Weather).filter(Weather.id == id).update(data)
    db.commit()
    db.close()
    
def getWithIndex(index):
    db= SessionLocal()
    weather_in_city=db.query(Weather).filter(Weather.index == index).all()
    db.commit()
    db.close()
    
    return weather_in_city