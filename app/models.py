from pydantic import BaseModel
from typing import List, Optional

class Patrulha(BaseModel):
    codigo: str
    descricao: str

class Questionario(BaseModel):
    pergunta: str
    resposta: Optional[str] = None

class Localizacao(BaseModel):
    nome: str
    latitude: float
    longitude: float
    questionarios: List[Questionario]

class Missao(BaseModel):
    data_inicio: str
    data_fim: str
    descricao: str
    localizacoes: List[Localizacao]

class Missao(BaseModel):
    nome: str
    Nplaca: str
    ponto_referencia: str
    regiao: str
    aderioprograma: str
    motivo_vizita: str

    