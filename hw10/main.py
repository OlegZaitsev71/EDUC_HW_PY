from fastapi import FastAPI

from hw10.routers import main_router

app = FastAPI(title="User Management API")
app.include_router(main_router)