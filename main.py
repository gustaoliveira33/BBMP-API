import uvicorn
from fastapi import FastAPI
from src.routers import health

app = FastAPI()

app.include_router(health.router, prefix='/api')

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=7000, reload=True)
