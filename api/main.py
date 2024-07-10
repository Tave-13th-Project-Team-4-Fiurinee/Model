import uvicorn
from fastapi import FastAPI
from .router import router as recommendation_router
# from mangum import Mangum

app = FastAPI()
app.include_router(recommendation_router, prefix='/api')

@app.get('/')
async def read_root():
    return {"message": "Welcome to the Flower Recommendation API!"}

# handler = Mangum(app=app)