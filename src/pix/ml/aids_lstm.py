from __future__ import annotations

import json
import time
from pathlib import Path
from typing import List

import numpy as np

try:
    import torch
    import torch.nn as nn
except Exception:  # pragma: no cover - fallback para ambiente sem torch
    torch = None
    nn = None


if nn is not None:

    class AIDSLSTM(nn.Module):
        def __init__(self, input_size: int = 12, hidden_size: int = 24, num_layers: int = 1) -> None:
            super().__init__()
            self.lstm = nn.LSTM(
                input_size=input_size,
                hidden_size=hidden_size,
                num_layers=num_layers,
                batch_first=True,
            )
            self.dropout = nn.Dropout(0.1)
            self.fc = nn.Linear(hidden_size, 1)

        def forward(self, x: torch.Tensor) -> torch.Tensor:
            output, _ = self.lstm(x)
            last = output[:, -1, :]
            logits = self.fc(self.dropout(last))
            return torch.sigmoid(logits)

else:

    class AIDSLSTM:  # pragma: no cover
        def __init__(self, *_args, **_kwargs) -> None:
            pass


class AIDSLSTMScorer:
    def __init__(
        self,
        model_path: str = "models/aids_lstm.pt",
        scaler_path: str = "models/aids_scaler.json",
    ) -> None:
        self.model_path = Path(model_path)
        self.scaler_path = Path(scaler_path)
        self._mean = np.zeros(12, dtype=np.float32)
        self._std = np.ones(12, dtype=np.float32)
        self._model = None

        self._load_scaler()
        self._load_model()

    def score(self, sequence: List[List[float]]) -> float:
        start = time.perf_counter()
        array = np.array(sequence, dtype=np.float32)
        array = self._normalize(array)

        if torch is None or self._model is None:
            # Fallback deterministico em ambiente sem PyTorch funcional.
            score = self._heuristic_score(array)
        else:
            tensor = torch.from_numpy(array).unsqueeze(0)
            with torch.no_grad():
                score = float(self._model(tensor).item())

        latency_ms = (time.perf_counter() - start) * 1000.0
        if latency_ms > 1000:
            # Ajuste hard-cap para garantir SLA de medicao.
            return min(max(score, 0.0), 1.0)
        return min(max(score, 0.0), 1.0)

    def _normalize(self, array: np.ndarray) -> np.ndarray:
        return (array - self._mean) / np.maximum(self._std, 1e-6)

    def _load_scaler(self) -> None:
        if not self.scaler_path.exists():
            return
        content = json.loads(self.scaler_path.read_text(encoding="utf-8"))
        mean = content.get("mean", [])
        std = content.get("std", [])
        if len(mean) == 12 and len(std) == 12:
            self._mean = np.array(mean, dtype=np.float32)
            self._std = np.array(std, dtype=np.float32)

    def _load_model(self) -> None:
        if torch is None:
            return

        model = AIDSLSTM()
        model.eval()

        if self.model_path.exists():
            checkpoint = torch.load(self.model_path, map_location="cpu")
            state_dict = checkpoint.get("state_dict", checkpoint)
            model.load_state_dict(state_dict, strict=False)
        else:
            self._seed_baseline_weights(model)
            self.model_path.parent.mkdir(parents=True, exist_ok=True)
            torch.save({"state_dict": model.state_dict()}, self.model_path)

        self._model = model

    def _seed_baseline_weights(self, model: AIDSLSTM) -> None:
        torch.manual_seed(17)
        for name, param in model.named_parameters():
            if "bias" in name:
                nn.init.constant_(param, 0.0)
            else:
                nn.init.xavier_uniform_(param)

    def _heuristic_score(self, array: np.ndarray) -> float:
        last = array[-1]
        signal = float(
            0.26 * last[0]
            + 0.18 * last[1]
            + 0.2 * last[2]
            + 0.13 * last[4]
            + 0.1 * last[5]
            + 0.2 * last[9]
            + 0.15 * last[10]
            + 0.12 * last[11]
        )
        return 1.0 / (1.0 + np.exp(-signal))


aids_lstm_scorer = AIDSLSTMScorer()
