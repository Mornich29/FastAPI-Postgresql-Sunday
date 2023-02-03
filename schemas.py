import pydantic as _pydantic


class _BaseContact(_pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str


class Contact(_BaseContact):
    id: int

    class Config:
        orm_mode = True


class CreateContact(_BaseContact):
    pass