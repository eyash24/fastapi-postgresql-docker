from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schema as _schema

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_contact(
    contact: _schema.CreateContact,
    db: "Session"
) -> _schema.Contact:
    contact = _models.Contact(**contact.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)

    return _schema.Contact.model_validate(contact)

async def get_all_contacts(db:"Session") -> List[_schema.Contact]:
    contacts = db.query(_models.Contact).all()
    return [_schema.Contact.model_validate(contact) for contact in contacts]

async def get_contact(contact_id: int, db:"Session") -> _schema.Contact:
    # options: 0 -> return pydantic object
    # options: 1 -> returns orm object 
    contact = db.query(_models.Contact).filter(_models.Contact.id == contact_id).first()

    if not contact:
        return None

    return contact

async def delete_contact(contact: _models.Contact,db:"Session"):
    db.delete(contact)
    db.commit()

async def update_contact(
        contact_data: _schema.CreateContact,
        contact: _models.Contact,
        db: "Session"
) -> _schema.Contact:
    contact.first_name = contact_data.first_name
    contact.last_name = contact_data.last_name
    contact.email = contact_data.email
    contact.phone_number = contact_data.phone_number

    db.commit()
    db.refresh(contact)

    return _schema.Contact.model_validate(contact)