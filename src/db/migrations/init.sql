CREATE EXTENSION IF NOT EXISTS timescaledb;

CREATE TABLE IF NOT EXISTS pix_transactions (
  transaction_id UUID PRIMARY KEY,
  end_to_end_id VARCHAR(40) UNIQUE NOT NULL,
  payer_id VARCHAR(128) NOT NULL,
  payee_id VARCHAR(128) NOT NULL,
  payer_bank VARCHAR(10) NOT NULL,
  payee_bank VARCHAR(10) NOT NULL,
  amount DOUBLE PRECISION NOT NULL,
  city VARCHAR(128) NOT NULL,
  state VARCHAR(8) NOT NULL,
  timestamp TIMESTAMP NOT NULL,
  pix_key_type VARCHAR(32) NOT NULL,
  channel VARCHAR(32) NOT NULL,
  device_id VARCHAR(128) NOT NULL,
  device_trust_score DOUBLE PRECISION NOT NULL DEFAULT 0.9,
  is_new_beneficiary BOOLEAN NOT NULL DEFAULT FALSE,
  failed_auth_count_24h INTEGER NOT NULL DEFAULT 0,
  metadata JSONB NOT NULL DEFAULT '{}'::jsonb
);

SELECT create_hypertable('pix_transactions', 'timestamp', if_not_exists => TRUE);

CREATE INDEX IF NOT EXISTS idx_pix_transactions_payer_ts
  ON pix_transactions (payer_id, timestamp DESC);

CREATE INDEX IF NOT EXISTS idx_pix_transactions_payee_ts
  ON pix_transactions (payee_id, timestamp DESC);

CREATE TABLE IF NOT EXISTS pix_fraud_decisions (
  transaction_id UUID PRIMARY KEY,
  end_to_end_id VARCHAR(40) NOT NULL,
  score DOUBLE PRECISION NOT NULL,
  lstm_score DOUBLE PRECISION NOT NULL,
  rules_score DOUBLE PRECISION NOT NULL,
  is_fraud BOOLEAN NOT NULL,
  latency_ms DOUBLE PRECISION NOT NULL,
  reasons JSONB NOT NULL DEFAULT '[]'::jsonb,
  created_at TIMESTAMP NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_pix_fraud_decisions_created
  ON pix_fraud_decisions (created_at DESC);

CREATE TABLE IF NOT EXISTS sels_events (
  event_id UUID PRIMARY KEY,
  event_type VARCHAR(64) NOT NULL,
  payload_hash VARCHAR(128) NOT NULL,
  prev_hash VARCHAR(128) NOT NULL,
  chain_hash VARCHAR(128) UNIQUE NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT now()
);
