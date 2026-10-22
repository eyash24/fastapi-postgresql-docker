import fastapi as _fastapi
from typing import TYPE_CHECKING, List

import schema as _schema
import sqlalchemy.orm as _orm 
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session 

app = _fastapi.FastAPI()

@app.post("/api/contacts", response_model=_schema.Contact)
async def create_contact(
    contact:_schema.CreateContact, 
    db: _orm.session = _fastapi.Depends(_services.get_db)
):
    return await _services.create_contact(contact=contact, db=db)


@app.get("/api/contacts", response_model=List[_schema.Contact])
async def get_contacts(
    db: _orm.session = _fastapi.Depends(_services.get_db)
):
    return await _services.get_all_contacts(db=db)


@app.get('/api/contacts/{contact_id}', response_model=_schema.Contact)
async def get_contact(
    contact_id: int,
    db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    contact = await _services.get_contact(contact_id=contact_id, db=db)
    if contact is None:
        raise _fastapi.HTTPException(status_code=404, detail="Contact does not exist")
    return contact


@app.delete('/api/contacts/{contact_id}')
async def delete_contact(
    contact_id: int,
    db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    contact = await _services.get_contact(contact_id=contact_id, db=db)
    if contact is None:
        raise _fastapi.HTTPException(status_code=404, detail="Contact does not exist")

    await _services.delete_contact(contact=contact, db=db)

    return "successfully deleted user"


@app.put("/api/contacts/{contact_id}", response_model=_schema.Contact)
async def update_contact(
    contact_id: int,
    contact_data: _schema.CreateContact,
    db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    contact = await _services.get_contact(contact_id=contact_id, db=db)
    if contact is None:
        raise _fastapi.HTTPException(status_code=404, detail="Contact does not exist")

    return await _services.update_contact(
        contact_data=contact_data, contact=contact, db=db
    )


