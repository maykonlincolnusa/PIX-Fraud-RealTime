from __future__ import annotations

import json
from pathlib import Path

import numpy as np

try:
    import torch
    from torch import nn
except Exception as exc:  # pragma: no cover
    raise RuntimeError("PyTorch nao disponivel no ambiente.") from exc

from src.pix.ml.aids_lstm import AIDSLSTM
from src.pix.mock.generator import generate_pix_transactions
from src.pix.features.feature_builder import build_feature_sequence


def train_and_export(epochs: int = 4, seq_len: int = 12) -> None:
    transactions = generate_pix_transactions(total_transactions=4000, fraud_ratio=0.12, seed=11)

    by_payer: dict[str, list] = {}
    for tx in transactions:
        by_payer.setdefault(tx.payer_id, []).append(tx)

    X = []
    y = []
    for payer_txs in by_payer.values():
        history = []
        for tx in sorted(payer_txs, key=lambda item: item.timestamp):
            sequence, _ = build_feature_sequence(tx, history, seq_len=seq_len)
            X.append(sequence)
            y.append(1.0 if tx.metadata.get("synthetic_fraud") else 0.0)
            history.append(tx)

    data = np.array(X, dtype=np.float32)
    labels = np.array(y, dtype=np.float32)

    mean = data.mean(axis=(0, 1))
    std = data.std(axis=(0, 1)) + 1e-6
    norm_data = (data - mean) / std

    dataset_x = torch.tensor(norm_data)
    dataset_y = torch.tensor(labels).unsqueeze(1)

    model = AIDSLSTM(input_size=12, hidden_size=24, num_layers=1)
    criterion = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    model.train()
    for _ in range(epochs):
        optimizer.zero_grad()
        preds = model(dataset_x)
        loss = criterion(preds, dataset_y)
        loss.backward()
        optimizer.step()

    Path("models").mkdir(parents=True, exist_ok=True)
    torch.save({"state_dict": model.state_dict()}, "models/aids_lstm.pt")
    Path("models/aids_scaler.json").write_text(
        json.dumps({"mean": mean.tolist(), "std": std.tolist()}, indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    train_and_export()
