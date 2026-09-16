from fastapi import FastAPI, HTTPException, Path
import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


app = FastAPI(
    title="Weather API",
    description="API para consulta de informações meteorológicas.",
    version="1.0.0"
)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.get("/")
def home():
    return {
        "mensagem": "Weather API funcionando!",
        "docs": "/docs"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/tempo/{cidade}")
def consultar_tempo(
    cidade: str = Path(
        ...,
        min_length=2,
        max_length=100,
        description="Nome da cidade para consulta do clima"
    )
):

    cidade = cidade.strip()

    if not cidade:
        raise HTTPException(
            status_code=400,
            detail="O nome da cidade não pode estar vazio."
        )

    if not API_KEY:
        raise HTTPException(
            status_code=500,
            detail="API Key não configurada."
        )

    parametros = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    try:
        resposta = requests.get(
            BASE_URL,
            params=parametros,
            timeout=10
        )
    except requests.RequestException:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível conectar ao serviço meteorológico."
        )

    if resposta.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="Cidade não encontrada."
        )

    if resposta.status_code == 401:
        raise HTTPException(
            status_code=401,
            detail="API Key inválida."
        )

    if resposta.status_code == 429:
        raise HTTPException(
            status_code=429,
            detail="Limite de requisições da API meteorológica atingido."
        )

    if resposta.status_code != 200:
        raise HTTPException(
            status_code=resposta.status_code,
            detail="Erro ao consultar serviço meteorológico."
        )

    dados = resposta.json()

    return {
        "cidade": dados["name"],
        "pais": dados["sys"]["country"],
        "temperatura": dados["main"]["temp"],
        "sensacao_termica": dados["main"]["feels_like"],
        "temperatura_minima": dados["main"]["temp_min"],
        "temperatura_maxima": dados["main"]["temp_max"],
        "umidade": dados["main"]["humidity"],
        "descricao": dados["weather"][0]["description"],
        "velocidade_vento": dados["wind"]["speed"]
    }