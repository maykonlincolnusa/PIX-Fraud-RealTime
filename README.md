# PIX-Fraud-RealTime

Deteccao de fraude PIX em tempo real (<1s) como extensao direta do `Fraud-Master-Bank`.

## Stack
- FastAPI + WebSocket
- Kafka (Redpanda)
- TimescaleDB (PostgreSQL)
- PyTorch LSTM (AIDS) + regras de risco
- Prometheus + Grafana
- Alertas Telegram + WhatsApp API
- Zero-Trust basico + SELS (Secure Event Ledger System) para log imutavel
- Terraform minimo (AWS `sa-east-1`)

## O que foi reutilizado do projeto base
- Estrutura de `src/Backend`, `services`, `pipelines`, `db`, `tests`, Dockerfiles
- Endpoints legados de transacoes/alertas/entidades/grafo
- Feature pipeline e scoring pipeline existentes, agora com modulo PIX especializado

## Novos modulos principais
- `src/pix/mock`: mock completo de transacoes PIX sinteticas com padroes brasileiros
- `src/pix/streaming`: produtor/consumidor Kafka para fluxo realtime
- `src/pix/ml`: modelo LSTM AIDS (PyTorch) + treinamento e scaler
- `src/pix/services`: processamento, scoring, alertas, metricas, integracao soberana
- `src/pix/security`: Zero-Trust middleware + SELS hash-chain
- `src/pix/ws`: broadcast realtime de decisoes PIX
- `src/sovereign`: modulo de integracao com Sovereign AI Security Platform

## Estrutura
```text
PIX-Fraud-RealTime/
  src/
    Backend/
    db/
    pix/
      api/
      mock/
      features/
      feature_store/
      ml/
      security/
      services/
      streaming/
      ws/
    sovereign/
  models/
  prometheus/
  grafana/
    dashboards/
    provisioning/
  infrastructure/
    terraform/
  docker/
  docker-compose.yml
```

## Subida rapida com Docker
```bash
docker compose up -d --build
```

Servicos:
- API: `http://localhost:8000`
- Swagger: `http://localhost:8000/docs`
- WebSocket PIX: `ws://localhost:8000/ws/pix`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000` (`admin/admin`)

## Endpoints PIX
Todos os endpoints `POST /api/v1/pix/*` exigem headers Zero-Trust:
- `x-api-key`
- `x-service-id`
- opcional `x-signature` (quando habilitado)

### Score online
`POST /api/v1/pix/score`

Exemplo:
```bash
curl -X POST http://localhost:8000/api/v1/pix/score \
  -H "Content-Type: application/json" \
  -H "x-api-key: local-dev-key" \
  -H "x-service-id: ops-console" \
  -d '{
    "payer_id":"payer_1001",
    "payee_id":"payee_9001",
    "amount":23500,
    "city":"Sao Paulo",
    "state":"SP",
    "is_new_beneficiary":true,
    "device_trust_score":0.31,
    "failed_auth_count_24h":4
  }'
```

### Publicar stream sintetico em Kafka
`POST /api/v1/pix/mock/publish`

```json
{
  "transactions_per_second": 20,
  "duration_seconds": 60,
  "fraud_ratio": 0.12
}
```

## Modelo LSTM AIDS
- Arquivos: `src/pix/ml/aids_lstm.py`, `src/pix/ml/train_lstm.py`, `models/aids_scaler.json`
- Para gerar novo checkpoint `.pt`:
```bash
python -m src.pix.ml.train_lstm
```

## SELS (log imutavel)
- Ledger local: `data/sels_ledger.jsonl`
- Tabela SQL: `sels_events`
- Verificacao da cadeia: `GET /api/v1/pix/sels/verify`

## Alertas
Configurar no `.env`:
- `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`
- `WHATSAPP_API_URL`, `WHATSAPP_TOKEN`, `WHATSAPP_TO`

## Integracao Sovereign AI Security Platform
Configurar no `.env`:
- `SOVEREIGN_PLATFORM_WEBHOOK`
- `SOVEREIGN_PLATFORM_TOKEN`

Quando fraude e detectada, o modulo envia evento anonimizado e compliance profile BR/LGPD.

## Terraform minimo (Brasil)
Pasta: `infrastructure/terraform`

```bash
cd infrastructure/terraform
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform plan
terraform apply
```

## Testes
```bash
pytest
```

Inclui teste do endpoint PIX com validacao de latencia `< 1s`.
