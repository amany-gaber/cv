import uvicorn
from fastapi import APIRouter
from services import *

service = APIRouter(
    prefix="/specific-job",
    tags=["Perdict"]
)


if __name__ == "__main__":
    uvicorn.run(service)

# uvicorn main:app --reload
