from fastapi import APIRouter


router = APIRouter(prefix='/api/v1/first', tags=['first'])


@router.get("/")
async def root():
    return {"message": "Hello World"}

