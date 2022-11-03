from datetime import datetime
from pydantic import BaseModel

class ModelForm(BaseModel):
    cor: str
    umidade: str
    regiao: str
    tipo_areia: str
    cascalho: bool
    argila: bool
    data_analise: datetime