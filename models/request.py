from datetime import datetime
from pydantic import BaseModel
from typing import List

class ModelForm(BaseModel):
    cor: str
    textura: str
    umidade: int
    regiao: str
    imagem: str