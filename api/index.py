from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "🚀 Finanças Enterprise API - FUNCIONANDO!",
        "status": "success",
        "endpoints": ["/health", "/predict/{ticker}", "/dashboard"],
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health():
    return {"status": "OK", "deploy": "Vercel"}

@app.get("/predict/{ticker}")
async def predict(ticker: str):
    try:
        data = yf.download(ticker, period="1mo", progress=False)
        preco = float(data['Close'].iloc[-1])
        return {"ticker": ticker, "preco": round(preco, 2), "status": "success"}
    except:
        return {"error": "Ticker inválido"}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    return """
    <h1>🚀 Finanças Enterprise PRO</h1>
    <p>API funcionando! Teste: /predict/PETR4.SA</p>
    <script>
        fetch('/predict/PETR4.SA').then(r=>r.json()).then(data=> 
            document.body.innerHTML += `<p>PETR4.SA: $${data.preco}</p>`
        );
    </script>
    """
