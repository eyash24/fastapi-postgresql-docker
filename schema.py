import datetime as _dt
import pydantic as _pydantic

class _BaseContact(_pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str

class Contact(_BaseContact):
    model_config = _pydantic.ConfigDict(from_attributes=True)
    id: int
    date_created: _dt.datetime

class CreateContact(_BaseContact):
    pass

