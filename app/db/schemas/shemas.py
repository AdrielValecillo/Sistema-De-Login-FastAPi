from pydantic import BaseModel, EmailStr

class TareaBase(BaseModel):
    titulo: str
    descripcion: str
    completada: bool = False

class TareaCreate(TareaBase):
    pass

class TareaResponse(TareaBase):
    id: int

    class Config:
        from_attributes = True


class UsuarioBase(BaseModel):
    username: str
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True