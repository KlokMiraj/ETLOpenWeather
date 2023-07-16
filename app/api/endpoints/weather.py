from fastapi import APIRouter, FastAPI

router = APIRouter()

@router.get("/weather/{location}")
async def get_weather(location: str):
    return {"location": location, "weather": "sunny"}


app= FastAPI()

app.include_router(router)
