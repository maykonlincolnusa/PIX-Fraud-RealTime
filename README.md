<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:000d0a,30:002a18,65:005c3a,100:00e676&height=240&section=header&text=PIX%20Fraud%20RealTime&fontSize=56&fontColor=ffffff&fontAlignY=40&desc=Real-Time%20Fraud%20Detection%20for%20Brazilian%20PIX%20Payments&descAlignY=62&descSize=18&animation=fadeIn&fontAlignX=50" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=18&pause=1000&color=00E676&center=true&vCenter=true&width=760&lines=PIX+Transaction+Scored+in+%3C1+Second;Kafka+Streaming+%E2%86%92+LSTM+AIDS+%E2%86%92+Zero-Trust+Decision;SELS+Hash-Chain+%7C+Immutable+Audit+Ledger;Telegram+%2B+WhatsApp+Real-Time+Alerts;Sovereign+AI+Security+Platform+Integration;BACEN+PIX+%7C+LGPD+Compliant+%7C+AWS+sa-east-1" />
</p>

<br/>

<p align="center">
  <img src="https://img.shields.io/badge/⚡_Latência-%3C_1s-00e676?style=for-the-badge&labelColor=001a0d"/>
  <img src="https://img.shields.io/badge/FastAPI-WebSocket-009688?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=00251a"/>
  <img src="https://img.shields.io/badge/Kafka-Redpanda-FF4343?style=for-the-badge&logo=apachekafka&logoColor=white&labelColor=1a0000"/>
  <img src="https://img.shields.io/badge/PyTorch-LSTM_AIDS-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white&labelColor=1a0a00"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/TimescaleDB-PostgreSQL-FDB515?style=for-the-badge&logo=postgresql&logoColor=black&labelColor=1a1400"/>
  <img src="https://img.shields.io/badge/Prometheus-Metrics-E6522C?style=for-the-badge&logo=prometheus&logoColor=white&labelColor=1a0800"/>
  <img src="https://img.shields.io/badge/Grafana-Dashboards-F46800?style=for-the-badge&logo=grafana&logoColor=white&labelColor=1a0e00"/>
  <img src="https://img.shields.io/badge/Zero--Trust-Security-00C853?style=for-the-badge&labelColor=001a0a"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/SELS-Immutable_Ledger-1565c0?style=for-the-badge&labelColor=00091a"/>
  <img src="https://img.shields.io/badge/LGPD-Compliant-7B1FA2?style=for-the-badge&labelColor=0d001a"/>
  <img src="https://img.shields.io/badge/Terraform-AWS_sa--east--1-7B42BC?style=for-the-badge&logo=terraform&logoColor=white&labelColor=0d001a"/>
  <img src="https://img.shields.io/badge/Telegram-Alertas-26A5E4?style=for-the-badge&logo=telegram&logoColor=white&labelColor=001525"/>
  <img src="https://img.shields.io/badge/WhatsApp-Alertas-25D366?style=for-the-badge&logo=whatsapp&logoColor=white&labelColor=001a0d"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-82.4%25-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/HCL-4.1%25-7B42BC?style=for-the-badge&logo=terraform&logoColor=white"/>
  <img src="https://img.shields.io/badge/TypeScript-3.4%25-3178C6?style=for-the-badge&logo=typescript&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-FFD600?style=for-the-badge&labelColor=1a1400"/>
</p>

<br/>

> [!WARNING]
> Esta plataforma utiliza **exclusivamente dados públicos e sintéticos**. Nenhum dado interno ou proprietário é utilizado. É uma extensão direta do `Fraud-Master-Bank`, com módulo PIX especializado para o contexto regulatório brasileiro — **BACEN + LGPD**.

<br/>

## 📑 Índice

| | Seção |
|---|---|
| 🟢 | [Visão Geral](#-visão-geral) |
| 🏗️ | [Arquitetura em Tempo Real](#%EF%B8%8F-arquitetura-em-tempo-real) |
| ⚡ | [Pipeline de Decisão](#-pipeline-de-decisão) |
| 🛠️ | [Stack Tecnológico](#%EF%B8%8F-stack-tecnológico) |
| 📂 | [Estrutura do Projeto](#-estrutura-do-projeto) |
| 🚀 | [Quick Start](#-quick-start) |
| 🌐 | [Serviços & Portas](#-serviços--portas) |
| 📡 | [Endpoints PIX](#-endpoints-pix) |
| 🤖 | [Modelo LSTM AIDS](#-modelo-lstm-aids) |
| 🔗 | [SELS — Ledger Imutável](#-sels--ledger-imutável) |
| 🔐 | [Zero-Trust Security](#-zero-trust-security) |
| 🚨 | [Alertas em Tempo Real](#-alertas-em-tempo-real) |
| 📊 | [Observabilidade](#-observabilidade) |
| 🛡️ | [Integração Sovereign AI](#%EF%B8%8F-integração-sovereign-ai) |
| ☁️ | [Infraestrutura AWS](#%EF%B8%8F-infraestrutura-aws) |
| 🧪 | [Testes](#-testes) |

<br/>

---

## 🟢 Visão Geral

Plataforma de detecção de fraudes em transações **PIX** com latência inferior a **1 segundo**, construída sobre streaming Kafka/Redpanda, modelo LSTM AIDS em PyTorch, zero-trust middleware e ledger de auditoria imutável baseado em hash-chain (**SELS**). Pensada para times de prevenção a fraudes, compliance e forensic analytics no ecossistema financeiro brasileiro.

```
╔══════════════════════════════════════════════════════════════════════════╗
║                      PIX FRAUD REALTIME · FLUXO PRINCIPAL               ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║   Transação PIX Sintética / Real                                         ║
║        │                                                                 ║
║        ▼                                                                 ║
║   [ Zero-Trust Middleware ]  ──►  [ Kafka / Redpanda Producer ]          ║
║                                           │                              ║
║                                  ┌────────▼────────┐                    ║
║                                  │  Kafka Consumer  │                    ║
║                                  └────────┬────────┘                    ║
║                                           ▼                              ║
║              [ Feature Pipeline PIX ]  ──►  [ LSTM AIDS Score ]          ║
║                                           ▼                              ║
║                           [ SELS Hash-Chain Ledger ]                    ║
║                                           │                              ║
║          ┌────────────────────────────────┼──────────────────────┐      ║
║          ▼                                ▼                       ▼      ║
║   [ WebSocket /ws/pix ]   [ Telegram / WhatsApp Alert ]   [ Prometheus ] ║
║   [ Sovereign AI Webhook ]    [ Grafana Dashboard ]       [ TimescaleDB ]║
╚══════════════════════════════════════════════════════════════════════════╝
```

<br/>

---

## 🏗️ Arquitetura em Tempo Real

```mermaid
flowchart LR
    PIX["📱 Transação PIX\nSintética · Real"]

    subgraph ZT ["🔐 Zero-Trust Layer"]
        H1["x-api-key"]
        H2["x-service-id"]
        H3["x-signature (opt)"]
    end

    subgraph KAFKA ["⚡ Kafka · Redpanda"]
        KP["Producer\nPIX Events"]
        KC["Consumer\nRealtime Pipeline"]
        KP --> KC
    end

    subgraph MLPIPE ["🤖 ML Pipeline"]
        FE["Feature\nEngineering"]
        LSTM["LSTM AIDS\nPyTorch"]
        RULES["Risk Rules\nEngine"]
        ENS["Ensemble\nDecision"]
        FE --> LSTM --> RULES --> ENS
    end

    subgraph OBS ["📊 Observability"]
        PROM["Prometheus"]
        GRAF["Grafana"]
        TS[("TimescaleDB")]
        PROM --> GRAF
    end

    PIX --> ZT --> KAFKA
    KC --> MLPIPE
    ENS --> SELS["🔗 SELS\nHash-Chain"]
    SELS --> WS["🔌 WebSocket\n/ws/pix"]
    SELS --> ALERT["🚨 Alertas\nTelegram · WhatsApp"]
    SELS --> OBS
    ENS --> SOV["🛡️ Sovereign AI\nSecurity Platform"]

    style ZT fill:#001a0d,stroke:#00e676,color:#d4f5d4
    style KAFKA fill:#1a0000,stroke:#ff4343,color:#ffd4d4
    style MLPIPE fill:#0d001a,stroke:#ab47bc,color:#f0d4f5
    style OBS fill:#1a1000,stroke:#ffa726,color:#fff5d4
```

<br/>

---

## ⚡ Pipeline de Decisão

```
 📱 PIX         🔐 Zero-Trust     📡 Kafka          ⚙️ Features        🧠 LSTM
 Transação  ──►  Middleware   ──►  Redpanda     ──►  Engineering   ──►  AIDS Score
                                                                          │
 🚨 Alerta   ◄── 🔗 SELS       ◄── 🎯 Ensemble  ◄── 📋 Risk Rules  ◄───┘
  Telegram       Ledger             Decision         Engine
  WhatsApp       Hash-Chain         + Reason
                                    Codes
```

| Etapa | Tecnologia | Latência Típica |
|---|---|---|
| Ingestão Zero-Trust | FastAPI Middleware | ~2ms |
| Produção Kafka | Redpanda Producer | ~5ms |
| Feature Engineering | pandas · Feature Store | ~15ms |
| Inferência LSTM | PyTorch · CUDA opcional | ~50ms |
| Escrita SELS | SHA-256 · PostgreSQL | ~10ms |
| Broadcast WebSocket | FastAPI WS | ~3ms |
| **Total p99** | **Pipeline completo** | **< 1000ms ✅** |

<br/>

---

## 🛠️ Stack Tecnológico

```
╔══════════════════════════════════════════════════════════════════════╗
║  CAMADA               TECNOLOGIAS                                    ║
╠══════════════════════════════════════════════════════════════════════╣
║  API & Streaming      FastAPI · Uvicorn · WebSocket                  ║
║                       Kafka (Redpanda) Producer / Consumer           ║
╠══════════════════════════════════════════════════════════════════════╣
║  Machine Learning     PyTorch · LSTM AIDS (bidirecional)             ║
║                       Feature Pipeline PIX especializado             ║
║                       Feature Store · Scaler JSON                    ║
╠══════════════════════════════════════════════════════════════════════╣
║  Storage              TimescaleDB (PostgreSQL time-series)           ║
║                       SELS — Secure Event Ledger (hash-chain)        ║
╠══════════════════════════════════════════════════════════════════════╣
║  Segurança            Zero-Trust Middleware (API Key + Service ID)   ║
║                       SELS Hash-Chain · Assinatura HMAC opcional     ║
║                       LGPD Compliance · Eventos anonimizados         ║
╠══════════════════════════════════════════════════════════════════════╣
║  Alertas              Telegram Bot API · WhatsApp Business API       ║
╠══════════════════════════════════════════════════════════════════════╣
║  Observabilidade      Prometheus · Grafana (dashboards pré-provisionados) ║
╠══════════════════════════════════════════════════════════════════════╣
║  Infraestrutura       Terraform · AWS sa-east-1 (São Paulo)          ║
║                       Docker · Docker Compose                        ║
╠══════════════════════════════════════════════════════════════════════╣
║  Integração           Sovereign AI Security Platform (webhook)       ║
║                       Fraud-Master-Bank (base reutilizada)           ║
╚══════════════════════════════════════════════════════════════════════╝
```

<br/>

---

## 📂 Estrutura do Projeto

<details>
<summary><b>🗂️ Expandir estrutura completa</b></summary>

```
PIX-Fraud-RealTime/
│
├── 🧠 src/
│   ├── Backend/                    # Infraestrutura base (Fraud-Master-Bank)
│   ├── db/                         # Modelos de banco e migrações
│   │
│   ├── pix/                        # ★ Módulo PIX especializado
│   │   ├── api/                    # Routers FastAPI PIX
│   │   ├── mock/                   # Mock transações PIX sintéticas (padrões BR)
│   │   ├── features/               # Feature engineering PIX
│   │   ├── feature_store/          # Cache de features para scoring <1s
│   │   ├── ml/
│   │   │   ├── aids_lstm.py        # Arquitetura LSTM AIDS (PyTorch)
│   │   │   └── train_lstm.py       # Treinamento + export checkpoint .pt
│   │   ├── security/               # Zero-Trust middleware + SELS hash-chain
│   │   ├── services/               # Processamento, scoring, alertas, métricas
│   │   ├── streaming/              # Kafka Producer / Consumer PIX
│   │   └── ws/                     # WebSocket broadcast de decisões PIX
│   │
│   └── sovereign/                  # Integração Sovereign AI Security Platform
│
├── 🤖 models/
│   └── aids_scaler.json            # Scaler serializado do modelo LSTM
│
├── 📊 prometheus/                  # Scrape configs
├── 📈 grafana/
│   ├── dashboards/                 # Dashboards JSON pré-provisionados
│   └── provisioning/               # Auto-provisionamento
│
├── ☁️  infrastructure/
│   └── terraform/                  # IaC AWS sa-east-1
│
├── 🐳 docker/                      # Dockerfiles por serviço
├── 📓 notebooks/                   # Análise exploratória
├── 🧪 tests/                       # pytest + validação latência <1s
├── ⚙️  config/                      # Configurações por ambiente
│
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
└── .env.example
```

</details>

<br/>

---

## 🚀 Quick Start

**Pré-requisitos:** Docker >= 24 · docker compose >= 2 · Python >= 3.11

<table>
<tr>
<th>🐧 Linux / macOS</th>
<th>🪟 Windows (PowerShell)</th>
</tr>
<tr>
<td>

```bash
# 1. Clone o repositório
git clone https://github.com/maykonlincolnusa/PIX-Fraud-RealTime.git
cd PIX-Fraud-RealTime

# 2. Configure variáveis de ambiente
cp .env.example .env

# 3. Suba a stack completa
docker compose up -d --build
```

</td>
<td>

```powershell
# 1. Clone o repositório
git clone https://github.com/maykonlincolnusa/PIX-Fraud-RealTime.git
cd PIX-Fraud-RealTime

# 2. Configure variáveis de ambiente
Copy-Item .env.example .env

# 3. Suba a stack completa
docker compose up -d --build
```

</td>
</tr>
</table>

<br/>

---

## 🌐 Serviços & Portas

| Serviço | URL | Credenciais |
|---|---|---|
| ⚡ **API REST** | http://localhost:8000 | — |
| 📄 **Swagger UI** | http://localhost:8000/docs | — |
| 🔌 **WebSocket PIX** | `ws://localhost:8000/ws/pix` | x-api-key header |
| 📈 **Prometheus** | http://localhost:9090 | — |
| 📊 **Grafana** | http://localhost:3000 | `admin / admin` |
| 🗄️ **TimescaleDB** | `localhost:5432` | via `.env` |
| 🔴 **Redpanda** | `localhost:9092` | — |

<br/>

---

## 📡 Endpoints PIX

> [!IMPORTANT]
> Todos os endpoints `POST /api/v1/pix/*` exigem os headers **Zero-Trust** obrigatórios: `x-api-key` e `x-service-id`.

| Método | Endpoint | Descrição |
|---|---|---|
| `POST` | `/api/v1/pix/score` | Score de fraude online · **< 1s** |
| `POST` | `/api/v1/pix/mock/publish` | Publicar stream sintético no Kafka |
| `GET` | `/api/v1/pix/sels/verify` | Verificar integridade do hash-chain |
| `GET` | `/api/v1/pix/alerts` | Listar alertas de fraude PIX |
| `GET` | `/ws/pix` | WebSocket — broadcast realtime |
| `GET` | `/health` | Health check |
| `GET` | `/metrics` | Prometheus metrics |

<details>
<summary><b>📋 Exemplo · Score Online</b></summary>

```bash
curl -X POST http://localhost:8000/api/v1/pix/score \
  -H "Content-Type: application/json"           \
  -H "x-api-key: local-dev-key"                 \
  -H "x-service-id: ops-console"                \
  -d '{
    "payer_id":              "payer_1001",
    "payee_id":              "payee_9001",
    "amount":                23500,
    "city":                  "Sao Paulo",
    "state":                 "SP",
    "is_new_beneficiary":    true,
    "device_trust_score":    0.31,
    "failed_auth_count_24h": 4
  }'
```

**Resposta esperada:**

```json
{
  "transaction_id":   "PIX-20250318-0042a7",
  "fraud_score":      0.91,
  "decision":         "BLOCK",
  "latency_ms":       87,
  "reason_codes":     ["RC-NEW-BENEFICIARY", "RC-HIGH-VELOCITY", "RC-LOW-DEVICE-TRUST"],
  "sels_hash":        "a3f8c2d1e9b47f...",
  "alert_dispatched": true,
  "timestamp":        "2025-03-18T14:22:03Z"
}
```

</details>

<details>
<summary><b>📋 Exemplo · Stream Sintético Kafka</b></summary>

```bash
curl -X POST http://localhost:8000/api/v1/pix/mock/publish \
  -H "x-api-key: local-dev-key"      \
  -H "x-service-id: ops-console"     \
  -H "Content-Type: application/json" \
  -d '{
    "transactions_per_second": 20,
    "duration_seconds":        60,
    "fraud_ratio":             0.12
  }'
```

</details>

<br/>

---

## 🤖 Modelo LSTM AIDS

```
╔══════════════════════════════════════════════════════════════════════╗
║           LSTM AIDS · Anomaly Intrusion Detection System             ║
╠══════════════════════════════════════════════════════════════════════╣
║  Framework      PyTorch                                              ║
║  Arquitetura    LSTM bidirecional + camada densa de classificação    ║
║  Entrada        Sequência de features PIX normalizadas               ║
║  Saída          Probabilidade de fraude  [0.0 – 1.0]                ║
║  Threshold      Configurável via .env  (default: 0.72)              ║
║  Latência       < 50ms de inferência pura                           ║
║  Artefatos      models/aids_lstm.pt  ·  models/aids_scaler.json     ║
╚══════════════════════════════════════════════════════════════════════╝
```

**Features PIX utilizadas no modelo:**

| Feature | Descrição |
|---|---|
| `device_trust_score` | Score de confiança do dispositivo |
| `failed_auth_count_24h` | Autenticações falhas nas últimas 24h |
| `is_new_beneficiary` | Flag de novo beneficiário |
| `velocity_1h` | Volume de transações na última hora |
| `amount_zscore` | Z-score do valor vs. histórico do pagador |
| `hour_of_day` · `day_of_week` | Sazonalidade comportamental |
| `geo_risk_score` | Risco geográfico (cidade / estado) |

```bash
# Treinar novo checkpoint
python -m src.pix.ml.train_lstm

# Artefatos gerados:
# models/aids_lstm.pt        ← checkpoint PyTorch
# models/aids_scaler.json    ← parâmetros de normalização
```

<br/>

---

## 🔗 SELS — Ledger Imutável

O **Secure Event Ledger System** garante cadeia de custódia forense para cada decisão via **SHA-256 encadeado**. Adulteração retroativa é matematicamente detectável.

```
╔══════════════════════════════════════════════════════════════════════╗
║  SELS · SECURE EVENT LEDGER SYSTEM                                   ║
╠══════════════════════════════════════════════════════════════════════╣
║  Algoritmo    SHA-256 encadeado                                      ║
║               hash_n = SHA256( payload_n  +  hash_{n-1} )           ║
║  Storage      data/sels_ledger.jsonl   (append-only local)           ║
║               Tabela SQL: sels_events  (TimescaleDB)                 ║
║  Verificação  GET /api/v1/pix/sels/verify                            ║
║  Conteúdo     timestamp · decision · fraud_score · reason_codes      ║
╚══════════════════════════════════════════════════════════════════════╝
```

```mermaid
graph LR
    G["⬛ Genesis Block
    hash_0 = SHA256(seed)"]

    E1["📦 Evento #1
    score: 0.91  BLOCK
    h1 = SHA256(e1 + h0)"]

    E2["📦 Evento #2
    score: 0.23  ALLOW
    h2 = SHA256(e2 + h1)"]

    EN["📦 Evento #N
    score: ...
    hN = SHA256(eN + hN-1)"]

    G -->|"hash_0"| E1 -->|"hash_1"| E2 -->|"hash_2"| EN

    style G  fill:#001a0d,stroke:#00e676,color:#d4f5d4
    style E1 fill:#001a0d,stroke:#00e676,color:#d4f5d4
    style E2 fill:#001a0d,stroke:#00e676,color:#d4f5d4
    style EN fill:#001a0d,stroke:#00e676,color:#d4f5d4
```

<br/>

---

## 🔐 Zero-Trust Security

```
╔══════════════════════════════════════════════════════════════════════╗
║  ZERO-TRUST MIDDLEWARE · HEADERS OBRIGATÓRIOS                        ║
╠══════════════════════════════════════════════════════════════════════╣
║  x-api-key        Chave de acesso por serviço                        ║
║  x-service-id     Identificador único do serviço chamante            ║
║  x-signature      Assinatura HMAC — opcional (quando habilitado)     ║
╠══════════════════════════════════════════════════════════════════════╣
║  ●  Never trust, always verify                                       ║
║  ●  Least privilege por service-id                                   ║
║  ●  Audit trail SELS para cada decisão                               ║
║  ●  LGPD: eventos anonimizados antes de qualquer envio externo       ║
╚══════════════════════════════════════════════════════════════════════╝
```

<br/>

---

## 🚨 Alertas em Tempo Real

Configure no `.env`:

```bash
# Telegram
TELEGRAM_BOT_TOKEN=<token-do-bot>
TELEGRAM_CHAT_ID=<id-do-chat>

# WhatsApp Business API
WHATSAPP_API_URL=<url-da-api>
WHATSAPP_TOKEN=<token>
WHATSAPP_TO=<numero-destino>
```

**Formato do alerta recebido:**

```
🚨 FRAUDE PIX DETECTADA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Score:    0.91  ·  HIGH RISK
Decisão:  BLOCK
Motivos:  RC-NEW-BENEFICIARY · RC-HIGH-VELOCITY
SELS:     a3f8c2d1e9b47f...
Latência: 87ms ✓
Hora:     2025-03-18 14:22:03 (UTC-3)
```

<br/>

---

## 📊 Observabilidade

| Métrica | Descrição |
|---|---|
| `pix_fraud_score_histogram` | Distribuição de scores em tempo real |
| `pix_decision_total` | Contador por decisão: BLOCK · ALLOW · REVIEW |
| `pix_latency_p99_ms` | Latência p99 do pipeline completo |
| `pix_throughput_tps` | Transações processadas por segundo |
| `pix_kafka_lag` | Lag do consumer Kafka (Redpanda) |
| `sels_events_total` | Total de eventos registrados no ledger SELS |

> Grafana pré-provisionado com dashboards em `grafana/dashboards/` — zero configuração manual após `docker compose up`.

<br/>

---

## 🛡️ Integração Sovereign AI

Configure no `.env`:

```bash
SOVEREIGN_PLATFORM_WEBHOOK=https://sovereign.example.com/ingest
SOVEREIGN_PLATFORM_TOKEN=<token>
```

Ao detectar fraude, o módulo `src/sovereign` envia evento anonimizado — **nenhum dado pessoal transmitido** — apenas `fraud_score`, `reason_codes`, `sels_hash` e compliance profile `BR/LGPD`.

<br/>

---

## ☁️ Infraestrutura AWS

<details>
<summary><b>🌩️ Deploy Terraform · sa-east-1 (São Paulo)</b></summary>

```bash
cd infrastructure/terraform

# 1. Copiar variáveis
cp terraform.tfvars.example terraform.tfvars

# 2. Inicializar e aplicar
terraform init
terraform plan
terraform apply
```

> Região **`sa-east-1` (São Paulo)** garante menor latência para clientes brasileiros e conformidade LGPD para armazenamento de dados no Brasil.

</details>

<br/>

---

## 🧪 Testes

```bash
# Suíte completa
pytest

# Com relatório de cobertura
pytest --cov=src --cov-report=html

# Validação de latência < 1s (teste crítico de SLA)
pytest tests/test_pix_latency.py -v
```

> [!NOTE]
> O teste de latência valida que o pipeline completo — requisição → feature engineering → inferência LSTM → escrita SELS → resposta — é concluído em **menos de 1 segundo** sob carga normal.

<br/>

---

<p align="center">
  <a href="https://github.com/maykonlincolnusa">
    <img src="https://img.shields.io/badge/GitHub-maykonlincolnusa-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
  <img src="https://img.shields.io/badge/AWS-Solutions_Architect-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white"/>
  <img src="https://img.shields.io/badge/CISSP-Certified-003087?style=for-the-badge&labelColor=00091a"/>
  <img src="https://img.shields.io/badge/GCP-Data_Engineer-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white"/>
  <img src="https://img.shields.io/badge/CKA-Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white"/>
</p>

<p align="center">
  <b>Maykon Lincoln</b> · Senior Systems Engineer & AI Architect<br/>
  <sub>Enterprise AI/ML · Cybersecurity · Real-Time Systems · Cloud Infrastructure</sub>
</p>

<br/>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00e676,40:005c3a,75:002a18,100:000d0a&height=130&section=footer&text=Decisão%20em%20%3C1s%20·%20Ledger%20Imutável%20·%20LGPD%20Compliant&fontSize=15&fontColor=ffffff&fontAlignY=65&animation=fadeIn"/>
</p>
