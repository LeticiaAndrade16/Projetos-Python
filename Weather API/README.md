# 🌤️ Weather API

API REST para consulta de informações meteorológicas em tempo real, desenvolvida com **Python** e **FastAPI**, integrada à **OpenWeatherMap API**.

## ✨ Funcionalidades

* 🌡️ Consulta de dados climáticos atuais por cidade
* 🌡️ Temperatura atual e sensação térmica
* 📉 Temperaturas mínima e máxima
* 💧 Umidade
* 🌤️ Descrição das condições climáticas
* 💨 Velocidade do vento
* 🇧🇷 Respostas em português (pt-BR)
* ✅ Validação do nome da cidade
* 🩺 Endpoint `/health` para verificar o status da API
* ⚠️ Tratamento de erros da API externa
* 📚 Documentação interativa automática via Swagger/OpenAPI

## 🛠️ Tecnologias

* [Python 3.11+](https://www.python.org/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Requests](https://docs.python-requests.org/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [OpenWeatherMap API](https://openweathermap.org/api)

## 📁 Estrutura do projeto

```text
Weather API/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

> O arquivo `.env` não deve ser enviado para o GitHub, pois contém a chave de acesso da API.

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/LeticiaAndrade16/Projetos-Python.git
cd Projetos-Python/Weather%20API
```

### 2. Crie e ative um ambiente virtual

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a API Key

Crie um arquivo `.env` na raiz do projeto:

```env
WEATHER_API_KEY=sua_chave_aqui
```

Você pode obter uma chave através da [OpenWeatherMap API](https://openweathermap.org/api).

> 🔐 Por segurança, nunca compartilhe sua API Key ou envie o arquivo `.env` para o GitHub.

## ▶️ Como executar

Execute:

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

### 📚 Swagger UI

A documentação interativa está disponível em:

```text
http://127.0.0.1:8000/docs
```

Também é possível acessar a documentação OpenAPI em:

```text
http://127.0.0.1:8000/openapi.json
```

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

---

### `GET /health`

Verifica o status da API.

**Resposta:**

```json
{
  "status": "ok",
  "service": "Weather API",
  "version": "1.0.0"
}
```

---

### `GET /tempo/{cidade}`

Retorna as condições climáticas atuais de uma cidade.

#### Parâmetros

| Nome     | Tipo   | Descrição                       |
| -------- | ------ | ------------------------------- |
| `cidade` | string | Nome da cidade a ser consultada |

#### Exemplo de requisição

```text
GET /tempo/São Paulo
```

#### Exemplo de resposta

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

#### Possíveis erros

| Código | Descrição                          |
| ------ | ---------------------------------- |
| `401`  | API Key inválida                   |
| `404`  | Cidade não encontrada              |
| `429`  | Limite de requisições atingido     |
| `503`  | Serviço meteorológico indisponível |
| `500`  | API Key não configurada            |

## 🔐 Segurança

A chave da OpenWeatherMap é armazenada em uma variável de ambiente utilizando `python-dotenv`.

O arquivo `.env` está incluído no `.gitignore` para evitar que informações sensíveis sejam publicadas no repositório.

## 📄 Licença

Este projeto está sob a licença MIT.

---

Desenvolvido por **Leticia Vitoria** 👩‍💻
