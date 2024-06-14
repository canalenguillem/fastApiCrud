# uvicorn app:app --reload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import user_routes

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost:5173",  # Aquí añade el origen de tu frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router)
