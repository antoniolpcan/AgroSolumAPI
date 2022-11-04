from datetime import datetime
from pydantic import BaseModel
from typing import List

class ModelForm(BaseModel):
    cor: str
    umidade: str
    regiao: str
    tipo_areia: str
    cascalho: bool
    argila: bool
    data_analise: datetime

class Semente(BaseModel):
    nome: str
    preco: float
    descricao: str
    url: str

class Resultados(BaseModel):
    solo: str
    sementes: List[Semente]