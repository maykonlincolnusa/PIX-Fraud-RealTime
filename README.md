<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>PIX Fraud RealTime — README Preview</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

  :root {
    --bg:        #090e0b;
    --bg2:       #0d1610;
    --bg3:       #111c14;
    --border:    #1a3d22;
    --green:     #00e676;
    --green2:    #00c853;
    --green3:    #69f0ae;
    --red:       #ff4343;
    --amber:     #ffa726;
    --purple:    #ab47bc;
    --blue:      #42a5f5;
    --muted:     #4a7a55;
    --text:      #d4f5d4;
    --text2:     #8fbc8f;
    --white:     #f0fff0;
  }

  * { margin:0; padding:0; box-sizing:border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Space Grotesk', sans-serif;
    font-size: 15px;
    line-height: 1.7;
    min-height: 100vh;
  }

  /* ── SCANLINE OVERLAY ── */
  body::before {
    content:'';
    position:fixed; inset:0;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0,230,118,0.015) 2px,
      rgba(0,230,118,0.015) 4px
    );
    pointer-events:none; z-index:0;
  }

  .wrap { max-width: 900px; margin:0 auto; padding: 0 24px 80px; position:relative; z-index:1; }

  /* ── HERO ── */
  .hero {
    position: relative;
    text-align: center;
    padding: 64px 24px 48px;
    overflow: hidden;
  }
  .hero::before {
    content:'';
    position:absolute; inset:0;
    background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(0,230,118,0.12) 0%, transparent 70%);
    pointer-events:none;
  }
  .hero-tag {
    display:inline-block;
    font-family:'JetBrains Mono',monospace;
    font-size:11px;
    color: var(--green);
    border: 1px solid var(--border);
    padding: 4px 14px;
    border-radius: 2px;
    letter-spacing: 3px;
    text-transform:uppercase;
    margin-bottom: 24px;
    background: rgba(0,230,118,0.05);
    animation: pulse 3s ease-in-out infinite;
  }
  @keyframes pulse {
    0%,100%{box-shadow:0 0 8px rgba(0,230,118,0.15);}
    50%{box-shadow:0 0 20px rgba(0,230,118,0.4), 0 0 40px rgba(0,230,118,0.1);}
  }
  .hero h1 {
    font-size: clamp(36px, 7vw, 64px);
    font-weight: 700;
    color: var(--white);
    letter-spacing: -1px;
    line-height: 1.05;
    margin-bottom: 8px;
  }
  .hero h1 span { color: var(--green); }
  .hero-sub {
    font-size: 15px;
    color: var(--text2);
    letter-spacing: 1px;
    margin-bottom: 32px;
    font-family:'JetBrains Mono',monospace;
  }
  .hero-sub strong { color: var(--green3); }

  /* latency badge */
  .latency-badge {
    display:inline-flex; align-items:center; gap:10px;
    background: rgba(0,230,118,0.08);
    border: 1px solid rgba(0,230,118,0.3);
    border-radius: 4px;
    padding: 10px 24px;
    font-family:'JetBrains Mono',monospace;
    font-size:13px;
    color: var(--green);
    margin-bottom: 40px;
  }
  .latency-dot {
    width:8px; height:8px; border-radius:50%;
    background: var(--green);
    box-shadow: 0 0 12px var(--green);
    animation: blink 1.2s ease-in-out infinite;
  }
  @keyframes blink { 0%,100%{opacity:1;} 50%{opacity:0.2;} }

  /* ── BADGES ── */
  .badges {
    display: flex; flex-wrap:wrap; gap:8px;
    justify-content:center;
    margin-bottom: 56px;
  }
  .badge {
    display:inline-flex; align-items:center; gap:6px;
    padding: 5px 12px;
    border-radius: 3px;
    font-family:'JetBrains Mono',monospace;
    font-size:11px;
    font-weight:600;
    letter-spacing:0.5px;
    border: 1px solid;
    transition: all 0.2s;
    cursor:default;
  }
  .badge:hover { transform:translateY(-2px); filter:brightness(1.2); }
  .badge-dot { width:6px;height:6px;border-radius:50%; }
  .b-green  { color:#00e676; border-color:rgba(0,230,118,0.3); background:rgba(0,230,118,0.06); }
  .b-teal   { color:#00bcd4; border-color:rgba(0,188,212,0.3); background:rgba(0,188,212,0.06); }
  .b-red    { color:#ff4343; border-color:rgba(255,67,67,0.3);  background:rgba(255,67,67,0.06); }
  .b-orange { color:#ffa726; border-color:rgba(255,167,38,0.3); background:rgba(255,167,38,0.06); }
  .b-purple { color:#ce93d8; border-color:rgba(206,147,216,0.3);background:rgba(206,147,216,0.06); }
  .b-blue   { color:#42a5f5; border-color:rgba(66,165,245,0.3); background:rgba(66,165,245,0.06); }
  .b-amber  { color:#ffeb3b; border-color:rgba(255,235,59,0.3); background:rgba(255,235,59,0.06); }
  .b-pink   { color:#f48fb1; border-color:rgba(244,143,177,0.3);background:rgba(244,143,177,0.06); }

  /* ── DIVIDER ── */
  .divider {
    height:1px;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
    margin: 40px 0;
  }

  /* ── SECTION TITLE ── */
  .sec-title {
    display:flex; align-items:center; gap:12px;
    margin-bottom: 24px;
  }
  .sec-title .icon { font-size:22px; }
  .sec-title h2 {
    font-size: 20px;
    font-weight:700;
    color: var(--white);
    letter-spacing:-0.3px;
  }
  .sec-title .line {
    flex:1; height:1px;
    background: linear-gradient(90deg, var(--border), transparent);
  }

  /* ── OVERVIEW GRID ── */
  .overview-text {
    color: var(--text2);
    font-size:15px;
    line-height:1.8;
    margin-bottom: 28px;
  }
  .overview-text strong { color: var(--green3); }

  /* ── ASCII BOX ── */
  .ascii-box {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius:4px;
    padding: 20px 24px;
    font-family:'JetBrains Mono',monospace;
    font-size:12px;
    line-height:1.7;
    color: var(--text2);
    overflow-x:auto;
    margin-bottom:8px;
    position:relative;
  }
  .ascii-box::before {
    content:'ARCHITECTURE';
    position:absolute; top:-1px; right:16px;
    font-size:9px; letter-spacing:2px;
    color: var(--muted);
    background:var(--bg); padding:0 8px;
  }
  .ascii-box .hi { color: var(--green); }
  .ascii-box .hi2 { color: var(--green3); }
  .ascii-box .dim { color: var(--muted); }

  /* ── FLOW DIAGRAM ── */
  .flow {
    display: flex;
    flex-direction: column;
    gap: 0;
    margin: 24px 0;
  }
  .flow-row {
    display:flex; align-items:stretch; gap:0;
  }
  .flow-node {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius:6px;
    padding: 12px 18px;
    text-align:center;
    font-size:12px;
    min-width:130px;
    position:relative;
  }
  .flow-node .label {
    font-family:'JetBrains Mono',monospace;
    font-size:10px;
    letter-spacing:1px;
    text-transform:uppercase;
    margin-bottom:4px;
  }
  .flow-node .val { font-size:13px; font-weight:600; color:var(--white); }
  .fn-green { border-color:rgba(0,230,118,0.4); background:rgba(0,230,118,0.05); }
  .fn-green .label { color:var(--green); }
  .fn-red   { border-color:rgba(255,67,67,0.4);  background:rgba(255,67,67,0.05); }
  .fn-red .label { color:var(--red); }
  .fn-purple{ border-color:rgba(206,147,216,0.4);background:rgba(206,147,216,0.05); }
  .fn-purple .label { color:var(--purple); }
  .fn-amber { border-color:rgba(255,167,38,0.4); background:rgba(255,167,38,0.05); }
  .fn-amber .label { color:var(--amber); }
  .flow-arrow {
    display:flex; align-items:center; justify-content:center;
    color: var(--muted); font-size:18px; padding: 0 8px;
    font-family:'JetBrains Mono',monospace;
  }

  /* ── PIPELINE VISUAL ── */
  .pipeline {
    display:flex; align-items:center; flex-wrap:wrap; gap:0;
    background: var(--bg2); border: 1px solid var(--border);
    border-radius:6px; padding: 20px;
    margin:24px 0; overflow-x:auto;
  }
  .pipe-step {
    display:flex; flex-direction:column; align-items:center;
    gap:6px; min-width:90px;
  }
  .pipe-icon {
    width:44px; height:44px; border-radius:8px;
    display:flex; align-items:center; justify-content:center;
    font-size:20px; border: 1px solid;
  }
  .pipe-label {
    font-size:10px; text-align:center;
    font-family:'JetBrains Mono',monospace;
    letter-spacing:0.5px; line-height:1.3;
    color: var(--text2);
  }
  .pipe-arrow {
    color: var(--muted); font-size:20px;
    padding: 0 4px; padding-bottom:18px;
    font-family:'JetBrains Mono',monospace;
  }

  /* ── STACK TABLE ── */
  .stack-table {
    width:100%;
    border-collapse:collapse;
    font-size:13px;
    margin-bottom:8px;
  }
  .stack-table th {
    text-align:left; padding:10px 14px;
    font-family:'JetBrains Mono',monospace;
    font-size:10px; letter-spacing:2px;
    text-transform:uppercase; color:var(--muted);
    border-bottom: 1px solid var(--border);
  }
  .stack-table td {
    padding: 10px 14px;
    border-bottom: 1px solid rgba(26,61,34,0.4);
    vertical-align:top;
  }
  .stack-table tr:last-child td { border-bottom:none; }
  .stack-table tr:hover td { background: rgba(0,230,118,0.03); }
  .stack-table .layer { color:var(--green3); font-weight:600; font-family:'JetBrains Mono',monospace; font-size:12px; }
  .stack-table .techs { color:var(--text2); }
  .stack-table .techs span {
    display:inline-block; background:rgba(0,230,118,0.06);
    border:1px solid rgba(0,230,118,0.15); border-radius:2px;
    padding:1px 7px; margin:2px 3px 2px 0;
    font-family:'JetBrains Mono',monospace; font-size:11px;
    color:var(--text); transition:all 0.2s;
  }
  .stack-table .techs span:hover { background:rgba(0,230,118,0.12); border-color:rgba(0,230,118,0.4); }

  /* ── SERVICES TABLE ── */
  .services-grid {
    display:grid; grid-template-columns: repeat(auto-fill,minmax(240px,1fr));
    gap:12px; margin: 24px 0;
  }
  .service-card {
    background:var(--bg2); border:1px solid var(--border);
    border-radius:6px; padding:16px;
    display:flex; flex-direction:column; gap:6px;
    transition:all 0.2s;
  }
  .service-card:hover { border-color:rgba(0,230,118,0.4); transform:translateY(-2px); }
  .service-card .sc-name { font-weight:700; color:var(--white); font-size:14px; }
  .service-card .sc-url {
    font-family:'JetBrains Mono',monospace; font-size:11px;
    color:var(--green); background:rgba(0,230,118,0.06);
    padding:3px 8px; border-radius:2px; width:fit-content;
  }
  .service-card .sc-desc { font-size:12px; color:var(--text2); }

  /* ── CODE BLOCK ── */
  .code-block {
    background: #060d08;
    border: 1px solid var(--border);
    border-radius:4px;
    padding: 18px 20px;
    font-family:'JetBrains Mono',monospace;
    font-size:12px;
    line-height:1.8;
    overflow-x:auto;
    position:relative;
    margin:16px 0;
  }
  .code-block::before {
    content: attr(data-lang);
    position:absolute; top:8px; right:12px;
    font-size:9px; letter-spacing:2px; text-transform:uppercase;
    color: var(--muted);
  }
  .code-block .cmd { color: var(--green3); }
  .code-block .key { color: #f48fb1; }
  .code-block .val { color: #ffe082; }
  .code-block .cmt { color: var(--muted); }
  .code-block .str { color: #a5d6a7; }

  /* ── JSON RESPONSE ── */
  .json-block {
    background:#060d08; border:1px solid var(--border);
    border-radius:4px; padding:18px 20px;
    font-family:'JetBrains Mono',monospace; font-size:12px;
    line-height:1.9; overflow-x:auto; margin:16px 0;
  }
  .json-block .jk { color:#f48fb1; }
  .json-block .jv { color:#ffe082; }
  .json-block .js { color:#a5d6a7; }
  .json-block .jb { color:#80cbc4; }
  .json-block .jn { color:#ef9a9a; }

  /* ── SELS CHAIN ── */
  .sels-chain {
    display:flex; align-items:center; flex-wrap:wrap; gap:0;
    margin:24px 0; overflow-x:auto;
  }
  .sels-block {
    background:rgba(0,230,118,0.04);
    border:1px solid rgba(0,230,118,0.25);
    border-radius:6px; padding:14px 16px;
    font-family:'JetBrains Mono',monospace;
    font-size:11px; min-width:160px;
    transition:all 0.2s;
  }
  .sels-block:hover { background:rgba(0,230,118,0.08); border-color:rgba(0,230,118,0.5); }
  .sels-block .sb-title { color:var(--green); font-size:10px; letter-spacing:1px; margin-bottom:6px; }
  .sels-block .sb-score { color:var(--white); font-size:13px; font-weight:600; }
  .sels-block .sb-hash { color:var(--muted); font-size:10px; margin-top:4px; }
  .sels-arrow { color:var(--green); font-size:20px; padding:0 10px; opacity:0.5; }

  /* ── ALERT BOX ── */
  .alert-preview {
    background:#060d08; border:1px solid rgba(255,67,67,0.3);
    border-radius:6px; padding:20px 24px;
    font-family:'JetBrains Mono',monospace; font-size:13px;
    line-height:2; color:var(--text2);
    position:relative; margin:16px 0;
    box-shadow: 0 0 30px rgba(255,67,67,0.05);
  }
  .alert-preview::before {
    content:'TELEGRAM / WHATSAPP';
    position:absolute; top:10px; right:14px;
    font-size:9px; letter-spacing:2px; color:rgba(255,67,67,0.5);
  }
  .alert-preview .al-head { color:#ff4343; font-size:15px; font-weight:700; margin-bottom:4px; }
  .alert-preview .al-line { display:flex; gap:12px; }
  .alert-preview .al-key { color:var(--muted); min-width:80px; }
  .alert-preview .al-val { color:var(--white); }
  .alert-preview .al-red { color:#ff4343; font-weight:700; }
  .alert-preview .al-green { color:var(--green); }
  .alert-preview .al-sep { color:var(--muted); margin:6px 0; letter-spacing:2px; }

  /* ── ZERO TRUST ── */
  .zt-grid {
    display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:24px 0;
  }
  @media(max-width:600px){ .zt-grid{grid-template-columns:1fr;} }
  .zt-card {
    background:var(--bg2); border:1px solid var(--border);
    border-radius:6px; padding:18px;
  }
  .zt-card .zt-title {
    font-family:'JetBrains Mono',monospace;
    font-size:11px; letter-spacing:2px;
    text-transform:uppercase; color:var(--green);
    margin-bottom:14px; display:flex; align-items:center; gap:8px;
  }
  .zt-card .zt-item {
    display:flex; align-items:flex-start; gap:10px;
    margin-bottom:10px; font-size:13px;
  }
  .zt-card .zt-key {
    font-family:'JetBrains Mono',monospace; font-size:11px;
    color:#f48fb1; background:rgba(244,143,177,0.06);
    border:1px solid rgba(244,143,177,0.2);
    border-radius:2px; padding:2px 8px;
    white-space:nowrap; margin-top:2px;
  }
  .zt-card .zt-desc { color:var(--text2); font-size:13px; }

  /* ── METRICS ── */
  .metrics-grid {
    display:grid; grid-template-columns:repeat(auto-fill,minmax(180px,1fr));
    gap:12px; margin:24px 0;
  }
  .metric-card {
    background:var(--bg2); border:1px solid var(--border);
    border-radius:6px; padding:16px;
    transition:all 0.2s;
  }
  .metric-card:hover { border-color:rgba(0,230,118,0.35); }
  .metric-card .mc-metric {
    font-family:'JetBrains Mono',monospace; font-size:11px;
    color:var(--green); margin-bottom:6px;
  }
  .metric-card .mc-desc { font-size:12px; color:var(--text2); }

  /* ── STRUCT TREE ── */
  .tree {
    background:var(--bg2); border:1px solid var(--border);
    border-radius:4px; padding:20px 24px;
    font-family:'JetBrains Mono',monospace; font-size:12px;
    line-height:1.9; overflow-x:auto;
  }
  .tree .td { color:var(--text2); }
  .tree .tf { color:var(--green3); }
  .tree .ts { color:#f48fb1; }
  .tree .tc { color:var(--muted); font-size:11px; }

  /* ── QUICK START ── */
  .qs-grid {
    display:grid; grid-template-columns:1fr 1fr; gap:16px; margin:24px 0;
  }
  @media(max-width:600px){ .qs-grid{grid-template-columns:1fr;} }
  .qs-card {
    background:var(--bg2); border:1px solid var(--border);
    border-radius:6px; overflow:hidden;
  }
  .qs-card .qs-head {
    background:rgba(0,230,118,0.05);
    padding:10px 16px;
    font-size:12px; font-weight:600;
    color:var(--green3);
    border-bottom:1px solid var(--border);
  }
  .qs-card .qs-body {
    padding:16px; font-family:'JetBrains Mono',monospace;
    font-size:11px; line-height:1.9; color:var(--text2);
  }
  .qs-card .qs-body .cmd { color:var(--green); }
  .qs-card .qs-body .cmt { color:var(--muted); }

  /* ── ENDPOINT TABLE ── */
  .ep-table { width:100%; border-collapse:collapse; font-size:13px; margin:20px 0; }
  .ep-table th {
    text-align:left; padding:9px 14px;
    font-family:'JetBrains Mono',monospace;
    font-size:10px; letter-spacing:2px; text-transform:uppercase;
    color:var(--muted); border-bottom:1px solid var(--border);
  }
  .ep-table td { padding:9px 14px; border-bottom:1px solid rgba(26,61,34,0.4); }
  .ep-table tr:last-child td { border-bottom:none; }
  .ep-table tr:hover td { background:rgba(0,230,118,0.03); }
  .method {
    font-family:'JetBrains Mono',monospace; font-size:11px;
    font-weight:700; padding:2px 8px; border-radius:2px;
    border:1px solid; white-space:nowrap;
  }
  .m-post { color:#69f0ae; border-color:rgba(105,240,174,0.35); background:rgba(105,240,174,0.06); }
  .m-get  { color:#42a5f5; border-color:rgba(66,165,245,0.35);  background:rgba(66,165,245,0.06); }
  .m-ws   { color:#ffd740; border-color:rgba(255,215,64,0.35);  background:rgba(255,215,64,0.06); }
  .ep-path { font-family:'JetBrains Mono',monospace; font-size:12px; color:var(--text); }
  .ep-desc { color:var(--text2); font-size:13px; }

  /* ── LSTM BOX ── */
  .lstm-spec {
    background:var(--bg2); border:1px solid rgba(206,147,216,0.3);
    border-radius:6px; padding:20px 24px; margin:20px 0;
  }
  .lstm-spec .ls-row {
    display:flex; align-items:baseline; gap:16px;
    padding:8px 0; border-bottom:1px solid rgba(206,147,216,0.1);
    font-size:13px;
  }
  .lstm-spec .ls-row:last-child { border-bottom:none; }
  .lstm-spec .ls-key {
    font-family:'JetBrains Mono',monospace; font-size:11px;
    color:#ce93d8; min-width:130px;
  }
  .lstm-spec .ls-val { color:var(--text2); }
  .lstm-spec .ls-val strong { color:var(--green); }

  /* ── FOOTER ── */
  .footer {
    margin-top:60px; padding:32px 0;
    border-top:1px solid var(--border);
    text-align:center;
  }
  .footer .author-name {
    font-size:18px; font-weight:700;
    color:var(--white); margin-bottom:6px;
  }
  .footer .author-sub {
    font-size:13px; color:var(--text2); margin-bottom:20px;
  }
  .footer .cert-badges {
    display:flex; flex-wrap:wrap; gap:8px; justify-content:center;
    margin-bottom:24px;
  }
  .footer-copy {
    font-family:'JetBrains Mono',monospace; font-size:11px;
    color:var(--muted); letter-spacing:1px;
  }

  /* ── COLLAPSIBLE ── */
  details {
    background:var(--bg2); border:1px solid var(--border);
    border-radius:6px; margin:8px 0;
    overflow:hidden;
  }
  summary {
    padding:14px 18px; cursor:pointer;
    font-size:14px; font-weight:600; color:var(--white);
    list-style:none;
    display:flex; align-items:center; gap:10px;
  }
  summary::-webkit-details-marker { display:none; }
  summary::before {
    content:'▶';
    font-size:10px; color:var(--green);
    transition:transform 0.2s;
  }
  details[open] summary::before { transform:rotate(90deg); }
  summary:hover { background:rgba(0,230,118,0.04); }
  .details-body { padding:16px 18px 18px; border-top:1px solid var(--border); }

  /* ── SECTION ── */
  section { margin-bottom: 52px; }

  /* ── DISCLAIMER ── */
  .disclaimer {
    background:rgba(255,167,38,0.06);
    border:1px solid rgba(255,167,38,0.25);
    border-radius:6px; padding:14px 18px;
    font-size:13px; color:var(--text2);
    margin-bottom:40px;
    display:flex; gap:12px; align-items:flex-start;
  }
  .disclaimer .disc-icon { font-size:18px; flex-shrink:0; }
  .disclaimer strong { color:var(--amber); }
</style>
</head>
<body>
<div class="wrap">

  <!-- ── HERO ── -->
  <div class="hero">
    <div class="hero-tag">⚡ Real-Time Fraud Detection · v1.0</div>
    <h1>PIX Fraud <span>RealTime</span></h1>
    <div class="hero-sub">Detection for Brazilian PIX Payments · <strong>&lt; 1 second latency</strong></div>
    <div class="latency-badge">
      <div class="latency-dot"></div>
      Pipeline Decision · p99 &lt; 1s · AWS sa-east-1
    </div>
    <div class="badges">
      <span class="badge b-green"><span class="badge-dot" style="background:#00e676"></span>FastAPI · WebSocket</span>
      <span class="badge b-red"><span class="badge-dot" style="background:#ff4343"></span>Kafka · Redpanda</span>
      <span class="badge b-orange"><span class="badge-dot" style="background:#ffa726"></span>PyTorch · LSTM AIDS</span>
      <span class="badge b-amber"><span class="badge-dot" style="background:#fdb515"></span>TimescaleDB</span>
      <span class="badge b-orange"><span class="badge-dot" style="background:#e6522c"></span>Prometheus</span>
      <span class="badge b-orange"><span class="badge-dot" style="background:#f46800"></span>Grafana</span>
      <span class="badge b-green"><span class="badge-dot" style="background:#00c853"></span>Zero-Trust</span>
      <span class="badge b-blue"><span class="badge-dot" style="background:#1565c0"></span>SELS Ledger</span>
      <span class="badge b-purple"><span class="badge-dot" style="background:#7b1fa2"></span>LGPD Compliant</span>
      <span class="badge b-purple"><span class="badge-dot" style="background:#7b42bc"></span>Terraform</span>
      <span class="badge b-blue"><span class="badge-dot" style="background:#26a5e4"></span>Telegram Alerts</span>
      <span class="badge b-green"><span class="badge-dot" style="background:#25d366"></span>WhatsApp Alerts</span>
      <span class="badge b-blue"><span class="badge-dot" style="background:#3776ab"></span>Python 82%</span>
      <span class="badge b-amber"><span class="badge-dot" style="background:#ffd600"></span>MIT License</span>
    </div>
  </div>

  <div class="disclaimer">
    <div class="disc-icon">⚠️</div>
    <div>Esta plataforma utiliza <strong>exclusivamente dados públicos e sintéticos</strong>. É uma extensão direta do <strong>Fraud-Master-Bank</strong>, adicionando um módulo PIX especializado para o contexto regulatório brasileiro — BACEN + LGPD.</div>
  </div>

  <!-- ── OVERVIEW ── -->
  <section>
    <div class="sec-title">
      <span class="icon">🟢</span>
      <h2>Visão Geral</h2>
      <div class="line"></div>
    </div>
    <p class="overview-text">
      Plataforma de detecção de fraudes em transações PIX com latência <strong>inferior a 1 segundo</strong>, construída sobre streaming Kafka/Redpanda, modelo <strong>LSTM AIDS em PyTorch</strong>, zero-trust middleware e um ledger de auditoria imutável baseado em hash-chain (SELS). Pensada para times de prevenção a fraudes, compliance e forensic analytics no ecossistema financeiro brasileiro.
    </p>
    <div class="ascii-box">
<span class="hi">╔══════════════════════════════════════════════════════════════════════════╗</span>
<span class="hi">║</span>                      <span class="hi2">PIX FRAUD REALTIME</span> <span class="dim">· FLUXO PRINCIPAL</span>                    <span class="hi">║</span>
<span class="hi">╠══════════════════════════════════════════════════════════════════════════╣</span>
<span class="hi">║</span>  <span class="dim">Transação PIX</span>                                                            <span class="hi">║</span>
<span class="hi">║</span>       <span class="hi">│</span>                                                                      <span class="hi">║</span>
<span class="hi">║</span>       <span class="hi">▼</span>                                                                      <span class="hi">║</span>
<span class="hi">║</span>  <span class="hi2">[ Zero-Trust Middleware ]</span> <span class="dim">──►</span> <span class="hi2">[ Kafka / Redpanda Producer ]</span>               <span class="hi">║</span>
<span class="hi">║</span>                                         <span class="hi">│</span>                                    <span class="hi">║</span>
<span class="hi">║</span>                                <span class="hi">┌────────▼────────┐</span>                          <span class="hi">║</span>
<span class="hi">║</span>                                <span class="hi">│  Kafka Consumer  │</span>                          <span class="hi">║</span>
<span class="hi">║</span>                                <span class="hi">└────────┬────────┘</span>                          <span class="hi">║</span>
<span class="hi">║</span>                                         <span class="hi">▼</span>                                    <span class="hi">║</span>
<span class="hi">║</span>            <span class="hi2">[ Feature Pipeline PIX ]</span> <span class="dim">──►</span> <span class="hi2">[ LSTM AIDS Score ]</span>               <span class="hi">║</span>
<span class="hi">║</span>                                         <span class="hi">▼</span>                                    <span class="hi">║</span>
<span class="hi">║</span>                          <span class="hi2">[ SELS Hash-Chain Ledger ]</span>                         <span class="hi">║</span>
<span class="hi">║</span>             <span class="hi">┌───────────────────────────┼──────────────────────┐</span>            <span class="hi">║</span>
<span class="hi">║</span>             <span class="hi">▼</span>                           <span class="hi">▼</span>                      <span class="hi">▼</span>            <span class="hi">║</span>
<span class="hi">║</span>  <span class="hi2">[ WebSocket /ws/pix ]</span>  <span class="hi2">[ Telegram/WhatsApp ]</span>  <span class="hi2">[ Prometheus ]</span>             <span class="hi">║</span>
<span class="hi">╚══════════════════════════════════════════════════════════════════════════╝</span>
    </div>
  </section>

  <!-- ── PIPELINE VISUAL ── -->
  <section>
    <div class="sec-title">
      <span class="icon">⚡</span>
      <h2>Pipeline em Tempo Real</h2>
      <div class="line"></div>
    </div>
    <div class="pipeline">
      <div class="pipe-step">
        <div class="pipe-icon fn-green" style="border-color:rgba(0,230,118,0.4)">📱</div>
        <div class="pipe-label">Transação<br/>PIX</div>
      </div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-step">
        <div class="pipe-icon fn-green" style="border-color:rgba(0,230,118,0.4)">🔐</div>
        <div class="pipe-label">Zero-Trust<br/>Middleware</div>
      </div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-step">
        <div class="pipe-icon fn-red" style="border-color:rgba(255,67,67,0.4)">📡</div>
        <div class="pipe-label">Kafka<br/>Redpanda</div>
      </div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-step">
        <div class="pipe-icon" style="border-color:rgba(66,165,245,0.4);background:rgba(66,165,245,0.05)">⚙️</div>
        <div class="pipe-label">Feature<br/>Engineering</div>
      </div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-step">
        <div class="pipe-icon fn-purple" style="border-color:rgba(206,147,216,0.4)">🧠</div>
        <div class="pipe-label">LSTM AIDS<br/>PyTorch</div>
      </div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-step">
        <div class="pipe-icon fn-amber" style="border-color:rgba(255,167,38,0.4)">🔗</div>
        <div class="pipe-label">SELS<br/>Ledger</div>
      </div>
      <div class="pipe-arrow">→</div>
      <div class="pipe-step">
        <div class="pipe-icon fn-green" style="border-color:rgba(0,230,118,0.4)">🚨</div>
        <div class="pipe-label">Alerta<br/>+ Decision</div>
      </div>
    </div>
  </section>

  <!-- ── STACK ── -->
  <section>
    <div class="sec-title">
      <span class="icon">🛠️</span>
      <h2>Stack Tecnológico</h2>
      <div class="line"></div>
    </div>
    <table class="stack-table">
      <thead><tr><th>Camada</th><th>Tecnologias</th></tr></thead>
      <tbody>
        <tr><td class="layer">API & Streaming</td><td class="techs"><span>FastAPI</span><span>Uvicorn</span><span>WebSocket</span><span>Kafka</span><span>Redpanda</span></td></tr>
        <tr><td class="layer">Machine Learning</td><td class="techs"><span>PyTorch</span><span>LSTM AIDS</span><span>Feature Store</span><span>Scaler JSON</span></td></tr>
        <tr><td class="layer">Storage</td><td class="techs"><span>TimescaleDB</span><span>PostgreSQL</span><span>SELS Hash-Chain</span></td></tr>
        <tr><td class="layer">Segurança</td><td class="techs"><span>Zero-Trust</span><span>HMAC Signature</span><span>LGPD</span><span>SELS Ledger</span></td></tr>
        <tr><td class="layer">Alertas</td><td class="techs"><span>Telegram Bot API</span><span>WhatsApp Business</span></td></tr>
        <tr><td class="layer">Observabilidade</td><td class="techs"><span>Prometheus</span><span>Grafana</span><span>Dashboards JSON</span></td></tr>
        <tr><td class="layer">Infraestrutura</td><td class="techs"><span>Terraform</span><span>AWS sa-east-1</span><span>Docker</span><span>Docker Compose</span></td></tr>
        <tr><td class="layer">Integração</td><td class="techs"><span>Sovereign AI Platform</span><span>Fraud-Master-Bank</span></td></tr>
      </tbody>
    </table>
  </section>

  <!-- ── ESTRUTURA ── -->
  <section>
    <div class="sec-title">
      <span class="icon">📂</span>
      <h2>Estrutura do Projeto</h2>
      <div class="line"></div>
    </div>
    <details open>
      <summary>Expandir estrutura completa</summary>
      <div class="details-body">
        <div class="tree">
<span class="tf">PIX-Fraud-RealTime/</span>
<span class="td">│</span>
<span class="td">├── 🧠 </span><span class="tf">src/</span>
<span class="td">│   ├── </span><span class="td">Backend/</span>            <span class="tc">  # Infraestrutura base (Fraud-Master-Bank)</span>
<span class="td">│   ├── </span><span class="td">db/</span>                 <span class="tc">  # Modelos de banco e migrações</span>
<span class="td">│   ├── </span><span class="tf">pix/</span>                <span class="tc">  # ★ Módulo PIX especializado</span>
<span class="td">│   │   ├── </span><span class="td">api/</span>            <span class="tc">  # Routers FastAPI PIX</span>
<span class="td">│   │   ├── </span><span class="td">mock/</span>           <span class="tc">  # Mock transações PIX sintéticas (padrões BR)</span>
<span class="td">│   │   ├── </span><span class="td">features/</span>       <span class="tc">  # Feature engineering PIX</span>
<span class="td">│   │   ├── </span><span class="td">feature_store/</span>  <span class="tc">  # Cache de features para scoring &lt;1s</span>
<span class="td">│   │   ├── </span><span class="tf">ml/</span>
<span class="td">│   │   │   ├── </span><span class="ts">aids_lstm.py</span>   <span class="tc"># Arquitetura LSTM AIDS (PyTorch)</span>
<span class="td">│   │   │   └── </span><span class="ts">train_lstm.py</span>  <span class="tc"># Treinamento + export checkpoint .pt</span>
<span class="td">│   │   ├── </span><span class="td">security/</span>       <span class="tc">  # Zero-Trust middleware + SELS</span>
<span class="td">│   │   ├── </span><span class="td">services/</span>       <span class="tc">  # Processamento, scoring, alertas</span>
<span class="td">│   │   ├── </span><span class="td">streaming/</span>      <span class="tc">  # Kafka Producer/Consumer</span>
<span class="td">│   │   └── </span><span class="td">ws/</span>             <span class="tc">  # WebSocket broadcast</span>
<span class="td">│   └── </span><span class="td">sovereign/</span>          <span class="tc">  # Integração Sovereign AI Platform</span>
<span class="td">│</span>
<span class="td">├── 🤖 </span><span class="tf">models/</span>
<span class="td">│   └── </span><span class="ts">aids_scaler.json</span>    <span class="tc">  # Scaler serializado do LSTM</span>
<span class="td">├── 📊 </span><span class="td">prometheus/</span>          <span class="tc">  # Scrape configs</span>
<span class="td">├── 📈 </span><span class="tf">grafana/</span>
<span class="td">│   ├── </span><span class="td">dashboards/</span>          <span class="tc">  # JSONs pré-provisionados</span>
<span class="td">│   └── </span><span class="td">provisioning/</span>        <span class="tc">  # Auto-provisionamento</span>
<span class="td">├── ☁️  </span><span class="td">infrastructure/terraform/</span>  <span class="tc"> # IaC AWS sa-east-1</span>
<span class="td">├── 🐳 </span><span class="td">docker/</span>
<span class="td">├── 📓 </span><span class="td">notebooks/</span>
<span class="td">├── 🧪 </span><span class="td">tests/</span>
<span class="td">├── </span><span class="ts">docker-compose.yml</span>
<span class="td">├── </span><span class="ts">requirements.txt</span>
<span class="td">└── </span><span class="ts">.env.example</span>
        </div>
      </div>
    </details>
  </section>

  <!-- ── QUICK START ── -->
  <section>
    <div class="sec-title">
      <span class="icon">🚀</span>
      <h2>Quick Start</h2>
      <div class="line"></div>
    </div>
    <div class="qs-grid">
      <div class="qs-card">
        <div class="qs-head">🐧 Linux / macOS</div>
        <div class="qs-body">
<span class="cmt"># 1. Clone</span>
<span class="cmd">git clone</span> https://github.com/maykonlincolnusa/PIX-Fraud-RealTime.git
<span class="cmd">cd</span> PIX-Fraud-RealTime

<span class="cmt"># 2. Variáveis de ambiente</span>
<span class="cmd">cp</span> .env.example .env

<span class="cmt"># 3. Subir stack</span>
<span class="cmd">docker compose up -d --build</span>
        </div>
      </div>
      <div class="qs-card">
        <div class="qs-head">🪟 Windows (PowerShell)</div>
        <div class="qs-body">
<span class="cmt"># 1. Clone</span>
<span class="cmd">git clone</span> https://github.com/maykonlincolnusa/PIX-Fraud-RealTime.git
<span class="cmd">cd</span> PIX-Fraud-RealTime

<span class="cmt"># 2. Variáveis de ambiente</span>
<span class="cmd">Copy-Item</span> .env.example .env

<span class="cmt"># 3. Subir stack</span>
<span class="cmd">docker compose up -d --build</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ── SERVICES ── -->
  <section>
    <div class="sec-title">
      <span class="icon">🌐</span>
      <h2>Serviços & Portas</h2>
      <div class="line"></div>
    </div>
    <div class="services-grid">
      <div class="service-card">
        <div class="sc-name">⚡ API REST</div>
        <div class="sc-url">http://localhost:8000</div>
        <div class="sc-desc">FastAPI principal</div>
      </div>
      <div class="service-card">
        <div class="sc-name">📄 Swagger UI</div>
        <div class="sc-url">http://localhost:8000/docs</div>
        <div class="sc-desc">Documentação interativa</div>
      </div>
      <div class="service-card">
        <div class="sc-name">🔌 WebSocket PIX</div>
        <div class="sc-url">ws://localhost:8000/ws/pix</div>
        <div class="sc-desc">Broadcast realtime de decisões</div>
      </div>
      <div class="service-card">
        <div class="sc-name">📈 Prometheus</div>
        <div class="sc-url">http://localhost:9090</div>
        <div class="sc-desc">Métricas brutas</div>
      </div>
      <div class="service-card">
        <div class="sc-name">📊 Grafana</div>
        <div class="sc-url">http://localhost:3000</div>
        <div class="sc-desc">Dashboards · admin/admin</div>
      </div>
      <div class="service-card">
        <div class="sc-name">🔴 Redpanda</div>
        <div class="sc-url">localhost:9092</div>
        <div class="sc-desc">Kafka-compatible broker</div>
      </div>
    </div>
  </section>

  <!-- ── ENDPOINTS ── -->
  <section>
    <div class="sec-title">
      <span class="icon">📡</span>
      <h2>Endpoints PIX</h2>
      <div class="line"></div>
    </div>
    <table class="ep-table">
      <thead><tr><th>Método</th><th>Endpoint</th><th>Descrição</th></tr></thead>
      <tbody>
        <tr><td><span class="method m-post">POST</span></td><td class="ep-path">/api/v1/pix/score</td><td class="ep-desc">Score de fraude online (&lt;1s)</td></tr>
        <tr><td><span class="method m-post">POST</span></td><td class="ep-path">/api/v1/pix/mock/publish</td><td class="ep-desc">Stream sintético no Kafka</td></tr>
        <tr><td><span class="method m-get">GET</span></td><td class="ep-path">/api/v1/pix/sels/verify</td><td class="ep-desc">Verificar integridade do ledger</td></tr>
        <tr><td><span class="method m-get">GET</span></td><td class="ep-path">/api/v1/pix/alerts</td><td class="ep-desc">Listar alertas de fraude PIX</td></tr>
        <tr><td><span class="method m-ws">WS</span></td><td class="ep-path">/ws/pix</td><td class="ep-desc">WebSocket — broadcast realtime</td></tr>
        <tr><td><span class="method m-get">GET</span></td><td class="ep-path">/health</td><td class="ep-desc">Health check</td></tr>
        <tr><td><span class="method m-get">GET</span></td><td class="ep-path">/metrics</td><td class="ep-desc">Prometheus metrics</td></tr>
      </tbody>
    </table>

    <details>
      <summary>📋 Exemplo — Score Online</summary>
      <div class="details-body">
        <div class="code-block" data-lang="bash">
<span class="cmd">curl</span> <span class="key">-X POST</span> http://localhost:8000/api/v1/pix/score \
  <span class="key">-H</span> <span class="str">"Content-Type: application/json"</span> \
  <span class="key">-H</span> <span class="str">"x-api-key: local-dev-key"</span> \
  <span class="key">-H</span> <span class="str">"x-service-id: ops-console"</span> \
  <span class="key">-d</span> <span class="str">'{
    "payer_id":              "payer_1001",
    "payee_id":              "payee_9001",
    "amount":                23500,
    "city":                  "Sao Paulo",
    "state":                 "SP",
    "is_new_beneficiary":    true,
    "device_trust_score":    0.31,
    "failed_auth_count_24h": 4
  }'</span>
        </div>
        <div class="json-block">
{
  <span class="jk">"transaction_id"</span>:   <span class="js">"PIX-20250318-0042a7"</span>,
  <span class="jk">"fraud_score"</span>:      <span class="jn">0.91</span>,
  <span class="jk">"decision"</span>:         <span class="js">"BLOCK"</span>,
  <span class="jk">"latency_ms"</span>:       <span class="jn">87</span>,
  <span class="jk">"reason_codes"</span>:     <span class="jb">[</span><span class="js">"RC-NEW-BENEFICIARY"</span>, <span class="js">"RC-HIGH-VELOCITY"</span>, <span class="js">"RC-LOW-DEVICE-TRUST"</span><span class="jb">]</span>,
  <span class="jk">"sels_hash"</span>:        <span class="js">"a3f8c2d1e9b47f..."</span>,
  <span class="jk">"alert_dispatched"</span>: <span class="jb">true</span>,
  <span class="jk">"timestamp"</span>:        <span class="js">"2025-03-18T14:22:03Z"</span>
}
        </div>
      </div>
    </details>
    <details>
      <summary>📋 Exemplo — Stream Sintético Kafka</summary>
      <div class="details-body">
        <div class="code-block" data-lang="bash">
<span class="cmd">curl</span> <span class="key">-X POST</span> http://localhost:8000/api/v1/pix/mock/publish \
  <span class="key">-H</span> <span class="str">"x-api-key: local-dev-key"</span> \
  <span class="key">-H</span> <span class="str">"x-service-id: ops-console"</span> \
  <span class="key">-H</span> <span class="str">"Content-Type: application/json"</span> \
  <span class="key">-d</span> <span class="str">'{
    "transactions_per_second": 20,
    "duration_seconds":        60,
    "fraud_ratio":             0.12
  }'</span>
        </div>
      </div>
    </details>
  </section>

  <!-- ── LSTM ── -->
  <section>
    <div class="sec-title">
      <span class="icon">🤖</span>
      <h2>Modelo LSTM AIDS</h2>
      <div class="line"></div>
    </div>
    <div class="lstm-spec">
      <div class="ls-row"><div class="ls-key">Arquitetura</div><div class="ls-val">LSTM bidirecional + camada densa de classificação</div></div>
      <div class="ls-row"><div class="ls-key">Entrada</div><div class="ls-val">Sequência de features PIX normalizadas via Scaler JSON</div></div>
      <div class="ls-row"><div class="ls-key">Saída</div><div class="ls-val">Probabilidade de fraude <strong>[0.0 – 1.0]</strong></div></div>
      <div class="ls-row"><div class="ls-key">Threshold</div><div class="ls-val">Configurável via <code>.env</code> · default <strong>0.72</strong></div></div>
      <div class="ls-row"><div class="ls-key">Latência</div><div class="ls-val"><strong>&lt;50ms</strong> de inferência pura</div></div>
      <div class="ls-row"><div class="ls-key">Artefatos</div><div class="ls-val"><code>models/aids_lstm.pt</code> · <code>models/aids_scaler.json</code></div></div>
    </div>
    <div class="code-block" data-lang="bash">
<span class="cmt"># Treinar novo checkpoint</span>
<span class="cmd">python -m</span> src.pix.ml.train_lstm
    </div>
  </section>

  <!-- ── SELS ── -->
  <section>
    <div class="sec-title">
      <span class="icon">🔗</span>
      <h2>SELS — Ledger Imutável</h2>
      <div class="line"></div>
    </div>
    <p class="overview-text">
      O <strong>Secure Event Ledger System</strong> garante cadeia de custódia forense para cada decisão de fraude via SHA-256 encadeado. Cada novo evento incorpora o hash do evento anterior — tornando adulteração retroativa matematicamente detectável.
    </p>
    <div class="sels-chain">
      <div class="sels-block">
        <div class="sb-title">GENESIS BLOCK</div>
        <div class="sb-score">hash_0 = SHA256(seed)</div>
        <div class="sb-hash">▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒</div>
      </div>
      <div class="sels-arrow">→</div>
      <div class="sels-block">
        <div class="sb-title">EVENTO #1</div>
        <div class="sb-score">fraud_score: 0.91</div>
        <div class="sb-hash">h1=SHA256(e1+h0)</div>
      </div>
      <div class="sels-arrow">→</div>
      <div class="sels-block">
        <div class="sb-title">EVENTO #2</div>
        <div class="sb-score">fraud_score: 0.23</div>
        <div class="sb-hash">h2=SHA256(e2+h1)</div>
      </div>
      <div class="sels-arrow">→</div>
      <div class="sels-block">
        <div class="sb-title">EVENTO #N</div>
        <div class="sb-score">fraud_score: ...</div>
        <div class="sb-hash">hN=SHA256(eN+hN-1)</div>
      </div>
    </div>
    <p style="font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--muted);margin-top:8px;">
      Verificação: <span style="color:var(--green)">GET /api/v1/pix/sels/verify</span> · Storage: <span style="color:var(--green)">data/sels_ledger.jsonl</span> + tabela SQL <span style="color:var(--green)">sels_events</span>
    </p>
  </section>

  <!-- ── ZERO TRUST ── -->
  <section>
    <div class="sec-title">
      <span class="icon">🔐</span>
      <h2>Zero-Trust Security</h2>
      <div class="line"></div>
    </div>
    <div class="zt-grid">
      <div class="zt-card">
        <div class="zt-title">🔑 Headers Obrigatórios</div>
        <div class="zt-item"><div class="zt-key">x-api-key</div><div class="zt-desc">Chave de acesso por serviço</div></div>
        <div class="zt-item"><div class="zt-key">x-service-id</div><div class="zt-desc">Identificador único do serviço chamante</div></div>
        <div class="zt-item"><div class="zt-key">x-signature</div><div class="zt-desc">Assinatura HMAC opcional (quando habilitada)</div></div>
      </div>
      <div class="zt-card">
        <div class="zt-title">🛡️ Princípios</div>
        <div class="zt-item" style="flex-direction:column;gap:6px">
          <div style="color:var(--text2);font-size:13px">● <strong style="color:var(--white)">Never trust, always verify</strong></div>
          <div style="color:var(--text2);font-size:13px">● Least privilege por service-id</div>
          <div style="color:var(--text2);font-size:13px">● Audit trail SELS para cada decisão</div>
          <div style="color:var(--text2);font-size:13px">● LGPD: eventos anonimizados antes do envio externo</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── ALERTS ── -->
  <section>
    <div class="sec-title">
      <span class="icon">🚨</span>
      <h2>Alertas em Tempo Real</h2>
      <div class="line"></div>
    </div>
    <div class="alert-preview">
      <div class="al-head">🚨 FRAUDE PIX DETECTADA</div>
      <div class="al-sep">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</div>
      <div class="al-line"><div class="al-key">Score</div><div class="al-val al-red">0.91 · HIGH RISK</div></div>
      <div class="al-line"><div class="al-key">Decisão</div><div class="al-val al-red">BLOCK</div></div>
      <div class="al-line"><div class="al-key">Motivos</div><div class="al-val">RC-NEW-BENEFICIARY · RC-HIGH-VELOCITY</div></div>
      <div class="al-line"><div class="al-key">SELS</div><div class="al-val al-green">a3f8c2d1e9b47f...</div></div>
      <div class="al-line"><div class="al-key">Latência</div><div class="al-val al-green">87ms ✓</div></div>
      <div class="al-line"><div class="al-key">Hora</div><div class="al-val">2025-03-18 14:22:03</div></div>
    </div>
  </section>

  <!-- ── METRICS ── -->
  <section>
    <div class="sec-title">
      <span class="icon">📊</span>
      <h2>Observabilidade</h2>
      <div class="line"></div>
    </div>
    <div class="metrics-grid">
      <div class="metric-card"><div class="mc-metric">pix_fraud_score_histogram</div><div class="mc-desc">Distribuição de scores em tempo real</div></div>
      <div class="metric-card"><div class="mc-metric">pix_decision_total</div><div class="mc-desc">Contador: BLOCK · ALLOW · REVIEW</div></div>
      <div class="metric-card"><div class="mc-metric">pix_latency_p99_ms</div><div class="mc-desc">Latência p99 do pipeline completo</div></div>
      <div class="metric-card"><div class="mc-metric">pix_throughput_tps</div><div class="mc-desc">Transações por segundo</div></div>
      <div class="metric-card"><div class="mc-metric">pix_kafka_lag</div><div class="mc-desc">Lag do consumer Kafka</div></div>
      <div class="metric-card"><div class="mc-metric">sels_events_total</div><div class="mc-desc">Total de eventos no ledger SELS</div></div>
    </div>
  </section>

  <!-- ── TESTES ── -->
  <section>
    <div class="sec-title">
      <span class="icon">🧪</span>
      <h2>Testes</h2>
      <div class="line"></div>
    </div>
    <div class="code-block" data-lang="bash">
<span class="cmt"># Suíte completa</span>
<span class="cmd">pytest</span>

<span class="cmt"># Com cobertura</span>
<span class="cmd">pytest</span> <span class="key">--cov=src --cov-report=html</span>

<span class="cmt"># Validação de latência &lt;1s (teste crítico)</span>
<span class="cmd">pytest</span> tests/test_pix_latency.py <span class="key">-v</span>
    </div>
  </section>

  <!-- ── FOOTER ── -->
  <div class="divider"></div>
  <div class="footer">
    <div class="author-name">Maykon Lincoln</div>
    <div class="author-sub">Senior Systems Engineer & AI Architect · Enterprise AI/ML · Cybersecurity · Real-Time Systems</div>
    <div class="cert-badges">
      <span class="badge b-orange"><span class="badge-dot" style="background:#ff9900"></span>AWS Solutions Architect</span>
      <span class="badge b-blue"><span class="badge-dot" style="background:#003087"></span>CISSP</span>
      <span class="badge b-blue"><span class="badge-dot" style="background:#4285f4"></span>GCP Data Engineer</span>
      <span class="badge b-blue"><span class="badge-dot" style="background:#326ce5"></span>CKA Kubernetes</span>
    </div>
    <div class="footer-copy">MIT License · Copyright © 2025 Maykon Lincoln · Decisão em &lt;1s · Ledger imutável · LGPD compliant</div>
  </div>

</div>
</body>
</html>
