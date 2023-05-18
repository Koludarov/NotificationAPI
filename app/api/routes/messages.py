from fastapi import APIRouter, HTTPException
from app.api.models import Message
from app.schemas import MessageCreate

router = APIRouter()

@router.post("/messages", response_model=Message)
async def create_message(message_data: MessageCreate):
    # Создание сообщения в базе данных и возврат созданного объекта
    message = await Message.create(**message_data.dict())
    return message

@router.get("/messages/{message_id}", response_model=Message)
async def get_message(message_id: int):
    # Получение сообщения из базы данных по его идентификатору
    message = await Message.get(message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message
