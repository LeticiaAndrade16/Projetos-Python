# 🌤️ Weather API

API REST simples para consulta de informações meteorológicas em tempo real, construída com **FastAPI** e integrada à **OpenWeatherMap API**.

## ✨ Funcionalidades

- Consulta de dados climáticos atuais por nome de cidade
- Retorno de temperatura, sensação térmica, mínima/máxima, umidade, descrição do clima e velocidade do vento
- Respostas em português (pt-BR)
- Documentação interativa automática via Swagger (`/docs`)

## 🛠️ Tecnologias

- [Python 3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Requests](https://docs.python-requests.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [OpenWeatherMap API](https://openweathermap.org/api)

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/weather-api.git
cd weather-api
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure sua chave de API:

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:
```
WEATHER_API_KEY=sua_chave_aqui
```

> Você pode obter uma chave gratuita em [openweathermap.org/api](https://openweathermap.org/api).

## ▶️ Como rodar

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

Documentação interativa (Swagger UI): `http://127.0.0.1:8000/docs`

## 📚 Endpoints

### `GET /`
Verifica se a API está funcionando.

**Resposta:**
```json
{
  "mensagem": "Weather API funcionando!",
  "docs": "/docs"
}
```

### `GET /tempo/{cidade}`
Retorna as condições climáticas atuais de uma cidade.

**Parâmetros:**
| Nome   | Tipo   | Descrição                  |
|--------|--------|-----------------------------|
| cidade | string | Nome da cidade (ex: `Sao Paulo`) |

**Exemplo de requisição:**
```
GET /tempo/Sao Paulo
```

**Exemplo de resposta:**
```json
{
  "cidade": "São Paulo",
  "pais": "BR",
  "temperatura": 24.5,
  "sensacao_termica": 24.9,
  "temperatura_minima": 22.1,
  "temperatura_maxima": 26.3,
  "umidade": 68,
  "descricao": "nuvens dispersas",
  "velocidade_vento": 3.6
}
```

**Erros possíveis:**
| Código | Descrição                              |
|--------|------------------------------------------|
| 404    | Cidade não encontrada                    |
| 500    | API Key não configurada / erro no serviço meteorológico |


## 📄 Licença

Este projeto está sob a licença MIT.

---

Desenvolvido por Leticia Vitoria 👩‍💻
