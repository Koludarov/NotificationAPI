from fastapi import APIRouter, HTTPException
from app.api.models import Mailing
from app.schemas import MailingCreate, MailingUpdate

router = APIRouter()

@router.post("/mailings", response_model=Mailing)
async def create_mailing(mailing_data: MailingCreate):
    # Создание рассылки в базе данных и возврат созданного объекта
    mailing = await Mailing.create(**mailing_data.dict())
    return mailing

@router.put("/mailings/{mailing_id}", response_model=Mailing)
async def update_mailing(mailing_id: int, mailing_data: MailingUpdate):
    # Обновление данных рассылки в базе данных и возврат обновленного объекта
    mailing = await Mailing.get(mailing_id)
    if not mailing:
        raise HTTPException(status_code=404, detail="Mailing not found")
    await mailing.update(**mailing_data.dict(exclude_unset=True)).apply()
    return mailing

@router.delete("/mailings/{mailing_id}")
async def delete_mailing(mailing_id: int):
    # Удаление рассылки из базы данных
    mailing = await Mailing.get(mailing_id)
    if not mailing:
        raise HTTPException(status_code=404, detail="Mailing not found")
    await mailing.delete()
    return {"message": "Mailing deleted"}
