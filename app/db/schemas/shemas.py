from pydantic import BaseModel

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
