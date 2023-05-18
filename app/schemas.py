from pydantic import BaseModel

class ClientBase(BaseModel):
    phone: str
    operator_code: str
    tag: str
    timezone: str

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    pass

class MailingBase(BaseModel):
    start_time: datetime
    end_time: datetime
    message: str
    operator_code: str
    tag: str

class MailingCreate(MailingBase):
    pass

class MailingUpdate(MailingBase):
    pass

class MessageBase(BaseModel):
    status: str
    mailing_id: int
    client_id: int

class MessageCreate(MessageBase):
    pass
