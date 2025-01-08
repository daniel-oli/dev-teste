from fastapi import FastAPI
from app import models
import secrets
from fastapi import FastAPI, HTTPException
from app.models import Missao, Localizacao, Questionario, Patrulha

app = FastAPI()

databese = []



@app.get("/")
def read_root():
    return {"teste patrulamento rural"}


# Simulando um banco de dados com uma lista
database = {
    "patrulhas": [
        {"codigo": "123", "descricao": "Patrulha A"},
        {"codigo": "456", "descricao": "Patrulha B"}
    ],
    "missoes": {
        "123": {
            "data_inicio": "2023-10-01",
            "data_fim": "2023-10-10",
            "descricao": "Missão de patrulhamento rural",
            "localizacoes": [
                {
                    "nome": "Local A",
                    "latitude": -23.55052,
                    "longitude": -46.633308,
                    "questionarios": [
                        {"pergunta": "Verificou a cerca?", "resposta": None}
                    ]
                }
            ]
        }
    }
}

def gerar_token():
    return secrets.token_hex(16)
