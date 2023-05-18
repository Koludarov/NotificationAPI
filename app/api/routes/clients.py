from fastapi import APIRouter, HTTPException
from app.api.models import Client
from app.schemas import ClientCreate, ClientUpdate

router = APIRouter()

@router.post("/clients", response_model=Client)
async def create_client(client_data: ClientCreate):
    # Создание клиента в базе данных и возврат созданного объекта
    client = await Client.create(**client_data.dict())
    return client

@router.put("/clients/{client_id}", response_model=Client)
async def update_client(client_id: int, client_data: ClientUpdate):
    # Обновление данных клиента в базе данных и возврат обновленного объекта
    client = await Client.get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    await client.update(**client_data.dict(exclude_unset=True)).apply()
    return client

@router.delete("/clients/{client_id}")
async def delete_client(client_id: int):
    # Удаление клиента из базы данных
    client = await Client.get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    await client.delete()
    return {"message": "Client deleted"}
