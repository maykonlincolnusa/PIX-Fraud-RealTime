<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:000d0a,40:003322,80:005c3a,100:00a86b&height=230&section=header&text=PIX%20Fraud%20RealTime&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=%3C1s%20Real-Time%20Fraud%20Detection%20for%20Brazilian%20PIX%20Payments&descAlignY=60&descSize=17&animation=fadeIn" alt="PIX Fraud RealTime Banner"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Latência-&lt;%201s-00e676?style=for-the-badge&logo=lightning&logoColor=black"/>
  <img src="https://img.shields.io/badge/FastAPI-WebSocket-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Kafka-Redpanda-FF4343?style=for-the-badge&logo=apachekafka&logoColor=white"/>
  <img src="https://img.shields.io/badge/PyTorch-LSTM%20AIDS-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
  <img src="https://img.shields.io/badge/TimescaleDB-PostgreSQL-FDB515?style=for-the-badge&logo=postgresql&logoColor=black"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Prometheus-Métricas-E6522C?style=for-the-badge&logo=prometheus&logoColor=white"/>
  <img src="https://img.shields.io/badge/Grafana-Dashboards-F46800?style=for-the-badge&logo=grafana&logoColor=white"/>
  <img src="https://img.shields.io/badge/Zero--Trust-Security-00C853?style=for-the-badge&logo=shield&logoColor=white"/>
  <img src="https://img.shields.io/badge/SELS-Immutable%20Ledger-1565c0?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/LGPD-Compliant-7B1FA2?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Terraform-AWS%20sa--east--1-7B42BC?style=for-the-badge&logo=terraform&logoColor=white"/>
  <img src="https://img.shields.io/badge/Telegram-Alertas-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"/>
  <img src="https://img.shields.io/badge/WhatsApp-Alertas-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-82.4%25-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-FFD600?style=for-the-badge"/>
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=19&pause=900&color=00E676&center=true&vCenter=true&width=780&lines=PIX+Transaction+Scored+in+%3C1+Second;Kafka+Streaming+%E2%86%92+LSTM+AIDS+%E2%86%92+Zero-Trust+Decision;SELS+Hash-Chain+%7C+Immutable+Audit+Ledger;Telegram+%2B+WhatsApp+Real-Time+Fraud+Alerts;Sovereign+AI+Security+Platform+Integration;BACEN+PIX+%7C+LGPD+Compliant+%7C+AWS+sa-east-1" alt="Typing SVG"/>
  </a>
</p>

---

## 📑 Índice

- [Visão Geral](#-visão-geral)
- [Arquitetura em Tempo Real](#-arquitetura-em-tempo-real)
- [Stack Tecnológico](#-stack-tecnológico)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Módulos Principais](#-módulos-principais)
- [Quick Start](#-quick-start)
- [Serviços & Portas](#-serviços--portas)
- [Endpoints PIX](#-endpoints-pix)
- [Modelo LSTM AIDS](#-modelo-lstm-aids)
- [SELS — Ledger Imutável](#-sels--ledger-imutável)
- [Zero-Trust Security](#-zero-trust-security)
- [Alertas em Tempo Real](#-alertas-em-tempo-real)
- [Observabilidade](#-observabilidade)
- [Integração Sovereign AI](#-integração-sovereign-ai)
- [Infraestrutura AWS](#-infraestrutura-aws)
- [Testes](#-testes)
- [Licença](#-licença)

---

## 🟢 Visão Geral

O **PIX Fraud RealTime** é uma plataforma de detecção de fraudes em transações PIX com latência **inferior a 1 segundo**, construída sobre streaming Kafka/Redpanda, modelo LSTM AIDS em PyTorch, zero-trust middleware e um ledger de auditoria imutável baseado em hash-chain (SELS). É uma extensão direta do projeto `Fraud-Master-Bank`, adicionando um módulo PIX especializado para o contexto regulatório brasileiro (BACEN + LGPD).

```
╔══════════════════════════════════════════════════════════════════════════╗
║                      PIX FRAUD REALTIME · VISÃO GERAL                   ║
║                                                                          ║
║   Transação PIX Sintética / Real                                         ║
║        │                                                                 ║
║        ▼                                                                 ║
║   [ Zero-Trust Middleware ] ──► [ Kafka / Redpanda Producer ]           ║
║                                          │                               ║
║                                 ┌────────▼────────┐                     ║
║                                 │  Kafka Consumer  │                     ║
║                                 └────────┬────────┘                     ║
║                                          ▼                               ║
║               [ Feature Pipeline PIX ] ──► [ LSTM AIDS Score ]          ║
║                        │                          │                     ║
║                         └────────────┬────────────┘                     ║
║                                      ▼                                   ║
║                          [ SELS Hash-Chain Ledger ]                     ║
║                                      │                                   ║
║          ┌───────────────────────────┼───────────────────────┐           ║
║          ▼                           ▼                       ▼           ║
║  [ WebSocket Broadcast ]   [ Telegram/WhatsApp Alert ]  [ Prometheus ]  ║
║  [ Sovereign AI Platform ] [ Grafana Dashboard ]        [ TimescaleDB ] ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 🏗️ Arquitetura em Tempo Real

```mermaid
flowchart LR
    A["📱 Transação PIX\nSintética / Real"] --> ZT

    subgraph ZT ["🔐 Zero-Trust Layer"]
        direction TB
        ZT1["x-api-key\nx-service-id\nx-signature"]
    end

    ZT --> KP

    subgraph STREAM ["⚡ Kafka Streaming · Redpanda"]
        direction TB
        KP["Producer\nPIX Events"] --> KC["Consumer\nRealtime Pipeline"]
    end

    KC --> FE

    subgraph ML ["🤖 ML Pipeline"]
        direction TB
        FE["Feature Engineering\nPIX Especializado"] --> LS["LSTM AIDS\nPyTorch Score"]
        LS --> RS["Risk Rules\nEngine"]
        RS --> ES["Ensemble\nFraud Decision"]
    end

    ES --> SELS["🔗 SELS\nHash-Chain Ledger"]
    SELS --> WS["🔌 WebSocket\n/ws/pix Broadcast"]
    SELS --> AL["🚨 Alertas\nTelegram · WhatsApp"]
    SELS --> OB

    subgraph OB ["📊 Observability"]
        direction TB
        PR["Prometheus\nMetrics"] --> GR["Grafana\nDashboards"]
        TS[("TimescaleDB\nTime-Series")]
    end

    ES --> SOV["🛡️ Sovereign AI\nSecurity Platform"]

    style ZT fill:#001a0d,stroke:#00e676,color:#fff
    style STREAM fill:#1a0000,stroke:#FF4343,color:#fff
    style ML fill:#0d001a,stroke:#AB47BC,color:#fff
    style OB fill:#1a1000,stroke:#FFA726,color:#fff
```

---

## 🛠️ Stack Tecnológico

```
╔══════════════════════════════════════════════════════════════════════╗
║  CAMADA               TECNOLOGIAS                                    ║
╠══════════════════════════════════════════════════════════════════════╣
║  API & Streaming      FastAPI · Uvicorn · WebSocket                  ║
║                       Kafka (Redpanda) Producer/Consumer             ║
╠══════════════════════════════════════════════════════════════════════╣
║  Machine Learning     PyTorch LSTM (AIDS model)                      ║
║                       Feature Pipeline PIX especializado             ║
║                       Feature Store · Scaler JSON                    ║
╠══════════════════════════════════════════════════════════════════════╣
║  Storage              TimescaleDB (PostgreSQL time-series)           ║
║                       SELS — Secure Event Ledger (hash-chain)        ║
╠══════════════════════════════════════════════════════════════════════╣
║  Segurança            Zero-Trust Middleware (API Key + Service ID)   ║
║                       SELS Hash-Chain · Assinatura opcional          ║
║                       LGPD Compliance · Eventos anonimizados         ║
╠══════════════════════════════════════════════════════════════════════╣
║  Alertas              Telegram Bot API                               ║
║                       WhatsApp Business API                          ║
╠══════════════════════════════════════════════════════════════════════╣
║  Observabilidade      Prometheus · Grafana Dashboards                ║
║                       Latência p99 · Throughput · Fraud Rate         ║
╠══════════════════════════════════════════════════════════════════════╣
║  Infraestrutura       Terraform · AWS sa-east-1 (Brasil)             ║
║                       Docker · Docker Compose                        ║
╠══════════════════════════════════════════════════════════════════════╣
║  Integração           Sovereign AI Security Platform (webhook)       ║
║                       Fraud-Master-Bank (base reutilizada)           ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 📂 Estrutura do Projeto

<details>
<summary><b>🗂️ Expandir estrutura completa</b></summary>

```
PIX-Fraud-RealTime/
│
├── 🧠 src/
│   ├── Backend/               # Infraestrutura base (Fraud-Master-Bank)
│   ├── db/                    # Modelos de banco e migrações
│   │
│   ├── pix/                   # ★ Módulo PIX especializado
│   │   ├── api/               # Routers FastAPI PIX
│   │   ├── mock/              # Mock de transações PIX sintéticas (padrões BR)
│   │   ├── features/          # Feature engineering PIX
│   │   ├── feature_store/     # Cache de features para scoring <1s
│   │   ├── ml/
│   │   │   ├── aids_lstm.py   # Arquitetura LSTM AIDS (PyTorch)
│   │   │   └── train_lstm.py  # Treinamento + export do checkpoint .pt
│   │   ├── security/          # Zero-Trust middleware + SELS hash-chain
│   │   ├── services/          # Processamento, scoring, alertas, métricas
│   │   ├── streaming/         # Kafka Producer/Consumer PIX
│   │   └── ws/                # WebSocket broadcast de decisões PIX
│   │
│   └── sovereign/             # Integração Sovereign AI Security Platform
│
├── 🤖 models/
│   └── aids_scaler.json       # Scaler serializado do modelo LSTM
│
├── 📊 prometheus/             # Configuração Prometheus (scrape configs)
├── 📈 grafana/
│   ├── dashboards/            # Dashboards JSON pré-provisionados
│   └── provisioning/          # Auto-provisionamento Grafana
│
├── ☁️ infrastructure/
│   └── terraform/             # IaC AWS sa-east-1 (módulo mínimo)
│
├── 🐳 docker/                 # Dockerfiles por serviço
├── 📓 notebooks/              # Análise exploratória e experimentos
├── 🧪 tests/                  # pytest (inclui validação de latência <1s)
├── ⚙️ config/                 # Configurações por ambiente
│
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
└── .env.example
```

</details>

---

## 🔧 Módulos Principais

<details>
<summary><b>📡 src/pix/streaming — Kafka Producer/Consumer</b></summary>

Pipeline de streaming em tempo real com Kafka (Redpanda):

- **Producer**: publica eventos PIX sintéticos ou reais no tópico Kafka com metadados de risco
- **Consumer**: consome o tópico e aciona o pipeline de features + scoring
- Suporte a cenários de carga configuráveis: `transactions_per_second`, `duration_seconds`, `fraud_ratio`

</details>

<details>
<summary><b>⚙️ src/pix/features — Feature Engineering PIX</b></summary>

Features especializadas para o domínio PIX brasileiro:

| Feature | Descrição |
|---|---|
| `device_trust_score` | Score de confiança do dispositivo |
| `failed_auth_count_24h` | Autenticações falhas nas últimas 24h |
| `is_new_beneficiary` | Flag de novo beneficiário |
| `velocity_1h` | Volume de transações na última hora |
| `amount_zscore` | Z-score do valor vs. histórico do pagador |
| `hour_of_day` / `day_of_week` | Sazonalidade comportamental |
| `geo_risk_score` | Risco geográfico (cidade/estado) |

</details>

<details>
<summary><b>🔗 src/pix/security — Zero-Trust + SELS</b></summary>

**Zero-Trust Middleware:** toda requisição PIX exige:

```http
x-api-key:     <chave de serviço>
x-service-id:  <identificador do serviço>
x-signature:   <assinatura HMAC opcional>
```

**SELS (Secure Event Ledger System):** cada decisão de fraude gera um registro imutável via hash-chain:

```
event_n.hash = SHA256(event_n.payload + event_{n-1}.hash)
```

Auditável via `GET /api/v1/pix/sels/verify`.

</details>

<details>
<summary><b>🛡️ src/sovereign — Sovereign AI Integration</b></summary>

Quando fraude é detectada, o módulo envia um evento anonimizado para a Sovereign AI Security Platform com:

- Perfil de compliance BR/LGPD
- Score e reason codes sem dados pessoais
- Timestamp e hash SELS para correlação forense

Configure via `.env`: `SOVEREIGN_PLATFORM_WEBHOOK` e `SOVEREIGN_PLATFORM_TOKEN`.

</details>

---

## 🚀 Quick Start

### Pré-requisitos

```bash
Docker Desktop  >= 24.x
docker compose  >= 2.x
Python          >= 3.11    # para execução local
```

### ⚡ Stack Completa com Docker

<table>
<tr>
<th>🐧 Linux / macOS</th>
<th>🪟 Windows (PowerShell)</th>
</tr>
<tr>
<td>

```bash
# 1. Clone
git clone https://github.com/maykonlincolnusa/\
PIX-Fraud-RealTime.git
cd PIX-Fraud-RealTime

# 2. Variáveis de ambiente
cp .env.example .env
# Configure Telegram, WhatsApp e Sovereign

# 3. Subir stack completa
docker compose up -d --build
```

</td>
<td>

```powershell
# 1. Clone
git clone https://github.com/maykonlincolnusa/`
PIX-Fraud-RealTime.git
cd PIX-Fraud-RealTime

# 2. Variáveis de ambiente
Copy-Item .env.example .env
# Configure Telegram, WhatsApp e Sovereign

# 3. Subir stack completa
docker compose up -d --build
```

</td>
</tr>
</table>

---

## 🌐 Serviços & Portas

| Serviço | URL / Endereço | Descrição |
|---|---|---|
| ⚡ **API REST** | http://localhost:8000 | FastAPI principal |
| 📄 **Swagger UI** | http://localhost:8000/docs | Documentação interativa |
| 🔌 **WebSocket PIX** | `ws://localhost:8000/ws/pix` | Broadcast realtime de decisões |
| 📈 **Prometheus** | http://localhost:9090 | Métricas brutas |
| 📊 **Grafana** | http://localhost:3000 | Dashboards (`admin/admin`) |
| 🗄️ **TimescaleDB** | `localhost:5432` | Série temporal de eventos |
| 🔴 **Redpanda** | `localhost:9092` | Kafka-compatible broker |

---

## 📡 Endpoints PIX

> Todos os endpoints `POST /api/v1/pix/*` exigem headers Zero-Trust obrigatórios.

| Método | Endpoint | Descrição |
|---|---|---|
| `POST` | `/api/v1/pix/score` | Score de fraude online (<1s) |
| `POST` | `/api/v1/pix/mock/publish` | Publicar stream sintético no Kafka |
| `GET` | `/api/v1/pix/sels/verify` | Verificar integridade do SELS hash-chain |
| `GET` | `/api/v1/pix/alerts` | Listar alertas de fraude PIX |
| `GET` | `/ws/pix` | WebSocket — broadcast realtime |
| `GET` | `/health` | Health check |
| `GET` | `/metrics` | Prometheus metrics |

### Exemplo — Score Online

```bash
curl -X POST http://localhost:8000/api/v1/pix/score \
  -H "Content-Type: application/json" \
  -H "x-api-key: local-dev-key" \
  -H "x-service-id: ops-console" \
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
  "transaction_id":  "PIX-20250318-0042a7",
  "fraud_score":     0.91,
  "decision":        "BLOCK",
  "latency_ms":      87,
  "reason_codes":    ["RC-NEW-BENEFICIARY", "RC-HIGH-VELOCITY", "RC-LOW-DEVICE-TRUST"],
  "sels_hash":       "a3f8c2d1e9b47...",
  "alert_dispatched": true,
  "timestamp":       "2025-03-18T14:22:03Z"
}
```

### Exemplo — Publicar Stream Sintético

```bash
curl -X POST http://localhost:8000/api/v1/pix/mock/publish \
  -H "x-api-key: local-dev-key" \
  -H "x-service-id: ops-console" \
  -H "Content-Type: application/json" \
  -d '{
    "transactions_per_second": 20,
    "duration_seconds":        60,
    "fraud_ratio":             0.12
  }'
```

---

## 🤖 Modelo LSTM AIDS

```
╔══════════════════════════════════════════════════════════════════════╗
║  LSTM AIDS (Anomaly Intrusion Detection System) · PyTorch            ║
╠══════════════════════════════════════════════════════════════════════╣
║  Arquitetura    LSTM bidirecional + camada densa de classificação    ║
║  Entrada        Sequência de features PIX normalizadas (scaler JSON) ║
║  Saída          Probabilidade de fraude [0.0 – 1.0]                 ║
║  Threshold      Configurável via .env (default: 0.72)               ║
║  Latência       <50ms de inferência (excluindo feature pipeline)     ║
╚══════════════════════════════════════════════════════════════════════╝
```

**Treinar novo checkpoint:**

```bash
# Local
python -m src.pix.ml.train_lstm

# Artefatos gerados
# models/aids_lstm.pt          ← checkpoint PyTorch
# models/aids_scaler.json      ← parâmetros de normalização
```

---

## 🔗 SELS — Ledger Imutável

O **Secure Event Ledger System** garante cadeia de custódia forense para cada decisão de fraude:

```
╔══════════════════════════════════════════════════════════════════════╗
║  SELS HASH-CHAIN                                                     ║
╠══════════════════════════════════════════════════════════════════════╣
║  Algoritmo      SHA-256 encadeado (hash_n = SHA256(payload + h_{n-1})║
║  Storage        data/sels_ledger.jsonl  (append-only local)          ║
║                 Tabela SQL: sels_events  (PostgreSQL)                ║
║  Verificação    GET /api/v1/pix/sels/verify                          ║
║  Auditoria      Cada evento: timestamp · decision · hash · score     ║
╚══════════════════════════════════════════════════════════════════════╝
```

```mermaid
graph LR
    E0["Genesis Block\nhash_0 = SHA256(seed)"]
    E1["Evento #1\nfraud_score=0.91\nhash_1 = SHA256(e1+h0)"]
    E2["Evento #2\nfraud_score=0.23\nhash_2 = SHA256(e2+h1)"]
    E3["Evento #N\nhash_N = SHA256(eN+h_{N-1})"]

    E0 --> E1 --> E2 --> E3

    style E0 fill:#001a0d,stroke:#00e676,color:#fff
    style E1 fill:#001a0d,stroke:#00e676,color:#fff
    style E2 fill:#001a0d,stroke:#00e676,color:#fff
    style E3 fill:#001a0d,stroke:#00e676,color:#fff
```

---

## 🔐 Zero-Trust Security

```
╔══════════════════════════════════════════════════════════════════════╗
║  ZERO-TRUST MIDDLEWARE · HEADERS OBRIGATÓRIOS                        ║
╠══════════════════════════════════════════════════════════════════════╣
║  x-api-key        Chave de acesso por serviço                        ║
║  x-service-id     Identificador único do serviço chamante            ║
║  x-signature      Assinatura HMAC opcional (quando habilitado)       ║
╠══════════════════════════════════════════════════════════════════════╣
║  PRINCÍPIOS       Never trust, always verify                         ║
║                   Least privilege por service-id                     ║
║                   Audit trail SELS para cada decisão                 ║
║  COMPLIANCE       LGPD: eventos anonimizados antes do envio externo  ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

## 🚨 Alertas em Tempo Real

Configure no `.env` para receber alertas instantâneos quando fraude é detectada:

```bash
# Telegram
TELEGRAM_BOT_TOKEN=<token-do-bot>
TELEGRAM_CHAT_ID=<id-do-chat>

# WhatsApp Business API
WHATSAPP_API_URL=<url-da-api>
WHATSAPP_TOKEN=<token>
WHATSAPP_TO=<numero-destino>
```

**Payload de alerta enviado:**

```
🚨 FRAUDE PIX DETECTADA
━━━━━━━━━━━━━━━━━━━━━━
Score:    0.91 (HIGH RISK)
Decisão:  BLOCK
Motivos:  RC-NEW-BENEFICIARY · RC-HIGH-VELOCITY
SELS:     a3f8c2d1...
Latência: 87ms
Hora:     2025-03-18 14:22:03
```

---

## 📊 Observabilidade

```
╔══════════════════════════════════════════════════════════════════════╗
║  MÉTRICAS PROMETHEUS                                                 ║
╠══════════════════════════════════════════════════════════════════════╣
║  pix_fraud_score_histogram   Distribuição de scores em tempo real    ║
║  pix_decision_total          Contador: BLOCK · ALLOW · REVIEW        ║
║  pix_latency_p99_ms          Latência p99 do pipeline completo       ║
║  pix_throughput_tps          Transações por segundo processadas      ║
║  pix_kafka_lag               Lag do consumer Kafka                   ║
║  sels_events_total           Total de eventos no ledger SELS         ║
╚══════════════════════════════════════════════════════════════════════╝
```

Grafana pré-provisionado com dashboards em `grafana/dashboards/` — zero configuração manual após `docker compose up`.

---

## 🛡️ Integração Sovereign AI

Ao detectar fraude, o módulo `src/sovereign` envia evento anonimizado para a **Sovereign AI Security Platform**:

```bash
# .env
SOVEREIGN_PLATFORM_WEBHOOK=https://sovereign.example.com/ingest
SOVEREIGN_PLATFORM_TOKEN=<token>
```

O payload respeita LGPD: nenhum dado pessoal é transmitido — apenas score, reason codes, hash SELS e compliance profile `BR/LGPD`.

---

## ☁️ Infraestrutura AWS

<details>
<summary><b>🌩️ Deploy Terraform · sa-east-1 (Brasil)</b></summary>

```bash
cd infrastructure/terraform

# Copiar variáveis
cp terraform.tfvars.example terraform.tfvars
# Edite: region, VPC CIDR, instâncias, etc.

# Inicializar e aplicar
terraform init
terraform plan
terraform apply
```

Região padrão: **`sa-east-1` (São Paulo)** — menor latência para clientes brasileiros e conformidade com LGPD de armazenamento de dados no Brasil.

</details>

---

## 🧪 Testes

```bash
# Suíte completa
pytest

# Com cobertura
pytest --cov=src --cov-report=html

# Validação de latência <1s (teste crítico)
pytest tests/test_pix_latency.py -v
```

> O teste de latência valida que o pipeline completo — desde a requisição até a resposta com score — é concluído em **menos de 1 segundo** sob carga normal.

---

## 📄 Licença

```
MIT License · Copyright (c) 2025 Maykon Lincoln
Uso comercial permitido com preservação do aviso de copyright.
```

---

## 👤 Autor

<p align="center">
  <a href="https://github.com/maykonlincolnusa">
    <img src="https://img.shields.io/badge/GitHub-maykonlincolnusa-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
  <img src="https://img.shields.io/badge/AWS-Solutions%20Architect-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white"/>
  <img src="https://img.shields.io/badge/CISSP-Certified-003087?style=for-the-badge&logo=isc2&logoColor=white"/>
  <img src="https://img.shields.io/badge/GCP-Data%20Engineer-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white"/>
  <img src="https://img.shields.io/badge/CKA-Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white"/>
</p>

<p align="center">
  <b>Senior Systems Engineer & AI Architect</b><br/>
  Enterprise AI/ML · Cybersecurity · Real-Time Systems · Cloud Infrastructure
</p>

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00a86b,50:003322,100:000d0a&height=120&section=footer&text=PIX%20Fraud%20RealTime&fontSize=22&fontColor=ffffff&fontAlignY=65&animation=fadeIn" alt="Footer Wave"/>
</p>

<p align="center">
  <sub>Decisão em &lt;1s · Ledger imutável · Zero-Trust nativo · LGPD compliant</sub>
</p>
