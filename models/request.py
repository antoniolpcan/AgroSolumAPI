from datetime import datetime
from pydantic import BaseModel
from typing import List

class ModelForm(BaseModel):
    cor: str
    textura: str
    intemperizado: str
    regiao: str
    imagem: str