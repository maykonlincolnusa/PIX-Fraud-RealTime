const apiBase = `${window.location.origin}/api/v1`;

const pixForm = document.getElementById("pixForm");
const streamForm = document.getElementById("streamForm");
const pixResult = document.getElementById("pixResult");
const pixFeed = document.getElementById("pixFeed");
const apiStatus = document.getElementById("apiStatus");
const wsStatus = document.getElementById("wsStatus");
const processedCount = document.getElementById("processedCount");
const fraudCount = document.getElementById("fraudCount");
const fraudRate = document.getElementById("fraudRate");
const avgLatency = document.getElementById("avgLatency");
const lastUpdate = document.getElementById("lastUpdate");

const headers = {
  "Content-Type": "application/json",
  "x-api-key": "local-dev-key",
  "x-service-id": "ops-console",
};

function addFeedItem(item) {
  const li = document.createElement("li");
  li.innerHTML = `<strong>${item.is_fraud ? "FRAUDE" : "OK"}</strong>
    <span>E2E: ${item.end_to_end_id}</span>
    <span>Valor: R$ ${item.amount.toFixed(2)}</span>
    <span>Score: ${(item.score * 100).toFixed(2)}% | Latencia: ${item.latency_ms.toFixed(2)} ms</span>
    <span>Motivos: ${(item.reasons || []).join(", ") || "-"}</span>`;

  if (item.is_fraud) {
    li.style.borderColor = "#ffb5a1";
    li.style.background = "#fff2ee";
  }

  pixFeed.prepend(li);
  while (pixFeed.children.length > 12) {
    pixFeed.removeChild(pixFeed.lastChild);
  }
}

async function checkHealth() {
  try {
    const res = await fetch(`${window.location.origin}/health`);
    apiStatus.textContent = res.ok ? "online" : "offline";
    apiStatus.style.background = res.ok ? "#d0f0f2" : "#ffe8d2";
  } catch {
    apiStatus.textContent = "offline";
    apiStatus.style.background = "#ffe8d2";
  }
}

async function refreshMetrics() {
  try {
    const res = await fetch(`${apiBase}/pix/metrics`, { headers });
    if (!res.ok) return;

    const metrics = await res.json();
    processedCount.textContent = metrics.processed_transactions;
    fraudCount.textContent = metrics.fraud_detected;
    fraudRate.textContent = `${(metrics.fraud_rate * 100).toFixed(2)}%`;
    avgLatency.textContent = `${metrics.average_latency_ms.toFixed(2)} ms`;
    lastUpdate.textContent = new Date(metrics.last_updated).toLocaleTimeString();
  } catch {
    // no-op
  }
}

pixForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  pixResult.textContent = "processando...";

  const formData = new FormData(pixForm);
  const payload = {
    payer_id: formData.get("payer_id"),
    payee_id: formData.get("payee_id"),
    amount: Number(formData.get("amount")),
    city: formData.get("city") || "Sao Paulo",
    state: "SP",
    channel: "mobile",
    pix_key_type: "cpf",
    device_id: "device_web",
    is_new_beneficiary: formData.get("is_new_beneficiary") === "true",
    device_trust_score: Number(formData.get("device_trust_score")),
  };

  try {
    const res = await fetch(`${apiBase}/pix/score`, {
      method: "POST",
      headers,
      body: JSON.stringify(payload),
    });

    const data = await res.json();
    if (!res.ok) {
      pixResult.textContent = `erro: ${data.detail || res.statusText}`;
      return;
    }

    pixResult.textContent = `score ${(data.score * 100).toFixed(2)}% (${data.is_fraud ? "fraude" : "ok"})`;

    addFeedItem({
      end_to_end_id: data.end_to_end_id,
      amount: payload.amount,
      score: data.score,
      is_fraud: data.is_fraud,
      latency_ms: data.latency_ms,
      reasons: data.reasons,
    });

    await refreshMetrics();
  } catch {
    pixResult.textContent = "falha ao processar";
  }
});

streamForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(streamForm);
  const payload = {
    transactions_per_second: Number(formData.get("tps")),
    duration_seconds: Number(formData.get("duration")),
    fraud_ratio: Number(formData.get("fraud_ratio")),
  };

  try {
    const res = await fetch(`${apiBase}/pix/mock/publish`, {
      method: "POST",
      headers,
      body: JSON.stringify(payload),
    });

    const data = await res.json();
    if (!res.ok) {
      pixResult.textContent = `erro no streaming: ${data.detail || res.statusText}`;
      return;
    }

    pixResult.textContent = "streaming iniciado no Kafka";
  } catch {
    pixResult.textContent = "falha ao publicar no Kafka";
  }
});

function connectPixWebSocket() {
  const ws = new WebSocket(`ws://${window.location.host}/ws/pix`);

  ws.addEventListener("open", () => {
    wsStatus.textContent = "connected";
    wsStatus.style.background = "#d0f0f2";
  });

  ws.addEventListener("close", () => {
    wsStatus.textContent = "disconnected";
    wsStatus.style.background = "#ffe8d2";
    setTimeout(connectPixWebSocket, 1500);
  });

  ws.addEventListener("message", async (event) => {
    const item = JSON.parse(event.data);
    addFeedItem(item);
    await refreshMetrics();
  });
}

checkHealth();
refreshMetrics();
connectPixWebSocket();
setInterval(refreshMetrics, 5000);
