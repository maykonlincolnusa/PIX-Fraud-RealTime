# PIX-Fraud-RealTime Architecture

```mermaid
graph LR
  A[PIX Mock API / Banking Channels] --> B[Kafka Redpanda Topic pix.transactions]
  B --> C[PIX Worker Consumer]
  C --> D[Feature Store - TimescaleDB]
  C --> E[AIDS LSTM Scoring + Rules]
  E --> F[SELS Immutable Ledger]
  E --> G[Alerts Telegram/WhatsApp]
  E --> H[Sovereign AI Security Platform]
  C --> I[WebSocket /ws/pix]
  C --> J[Prometheus Metrics]
  J --> K[Grafana Dashboard]
```

## Latency target
- End-to-end scoring path: `< 1s`
- Rule-based scoring and feature retrieval optimized for 24h lookback window indexes.

## Security baseline
- Zero-trust headers (`x-api-key`, `x-service-id`, optional `x-signature` HMAC).
- Immutable ledger (`SELS`) with hash chaining and database persistence.
- Data residency profile: Brazil (`sa-east-1` Terraform default).
