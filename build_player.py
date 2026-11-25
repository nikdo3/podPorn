import json
import os
from quiz_questions import QUIZ_QUESTIONS

with open(r"k:\podPorn\podcast_data.json", "r", encoding="utf-8") as f:
    podcast_data = json.load(f)

with open(r"k:\podPorn\google_keep_tahak.txt", "r", encoding="utf-8") as f:
    keep_raw = f.read()

split_marker = "===================================================================="
if split_marker in keep_raw:
    parts = keep_raw.split(split_marker)
    keep_full = parts[0].strip()
    keep_pocket = parts[-1].strip()
else:
    keep_full = keep_raw.strip()
    keep_pocket = keep_raw.strip()

data_json_str = json.dumps(podcast_data, ensure_ascii=False)
quiz_json_str = json.dumps(QUIZ_QUESTIONS, ensure_ascii=False)
keep_json_str = json.dumps({"full": keep_full, "pocket": keep_pocket}, ensure_ascii=False)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="cs" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Satelitní komunikace & Oběžné dráhy – Orbital Study Studio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    /* ==========================================================================
       ORBITAL TELEMETRY & EDITORIAL STUDY STUDIO DESIGN SYSTEM
       ========================================================================== */
    :root[data-theme="dark"] {
      --bg-page: #0b0e14;
      --bg-glow: radial-gradient(ellipse 80% 50% at 50% -10%, rgba(56, 189, 248, 0.12), transparent);
      --bg-card: #121722;
      --bg-subtle: #181f2e;
      --bg-hover: #1f283b;
      --bg-active-turn: rgba(56, 189, 248, 0.11);
      --border-color: #232c3f;
      --border-strong: #33415c;
      --text-main: #f1f5f9;
      --text-secondary: #cbd5e1;
      --text-muted: #7c8ba1;
      --accent-primary: #38bdf8;
      --accent-primary-solid: #0284c7;
      --accent-primary-soft: rgba(56, 189, 248, 0.14);
      --accent-warm: #f59e0b;
      --accent-warm-soft: rgba(245, 158, 11, 0.14);
      --accent-green: #10b981;
      --accent-green-soft: rgba(16, 185, 129, 0.14);
      --accent-rose: #f43f5e;
      --accent-rose-soft: rgba(244, 63, 94, 0.14);
      --accent-purple: #c084fc;
      --accent-purple-soft: rgba(168, 85, 247, 0.12);
      --shadow-card: 0 12px 32px -8px rgba(0, 0, 0, 0.48);
      --shadow-player: 0 20px 52px -10px rgba(0, 0, 0, 0.72);
      --glass-bg: rgba(18, 23, 34, 0.88);
      --figure-pad: #ffffff;
      --uncertainty-stripe: repeating-linear-gradient(
        45deg,
        rgba(245, 158, 11, 0.36),
        rgba(245, 158, 11, 0.36) 6px,
        rgba(245, 158, 11, 0.14) 6px,
        rgba(245, 158, 11, 0.14) 12px
      );
    }

    :root[data-theme="light"] {
      --bg-page: #f4f6fa;
      --bg-glow: radial-gradient(ellipse 80% 45% at 50% -10%, rgba(2, 132, 199, 0.08), transparent);
      --bg-card: #ffffff;
      --bg-subtle: #eef2f7;
      --bg-hover: #e4eaf3;
      --bg-active-turn: #e0f2fe;
      --border-color: #dce3ee;
      --border-strong: #c2cde0;
      --text-main: #0f172a;
      --text-secondary: #334155;
      --text-muted: #64748b;
      --accent-primary: #0284c7;
      --accent-primary-solid: #0284c7;
      --accent-primary-soft: rgba(2, 132, 199, 0.10);
      --accent-warm: #d97706;
      --accent-warm-soft: rgba(217, 119, 6, 0.12);
      --accent-green: #059669;
      --accent-green-soft: rgba(5, 150, 105, 0.12);
      --accent-rose: #e11d48;
      --accent-rose-soft: rgba(225, 29, 72, 0.10);
      --accent-purple: #7c3aed;
      --accent-purple-soft: rgba(124, 58, 237, 0.10);
      --shadow-card: 0 6px 24px -6px rgba(15, 23, 42, 0.08), 0 1px 3px rgba(15, 23, 42, 0.04);
      --shadow-player: 0 16px 46px -8px rgba(15, 23, 42, 0.18), 0 2px 8px rgba(15, 23, 42, 0.06);
      --glass-bg: rgba(255, 255, 255, 0.90);
      --figure-pad: #ffffff;
      --uncertainty-stripe: repeating-linear-gradient(
        45deg,
        rgba(217, 119, 6, 0.30),
        rgba(217, 119, 6, 0.30) 6px,
        rgba(217, 119, 6, 0.12) 6px,
        rgba(217, 119, 6, 0.12) 12px
      );
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg-page);
      background-image: var(--bg-glow);
      background-attachment: fixed;
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.62;
      min-height: 100vh;
      padding-bottom: 132px;
      transition: background-color 0.25s ease, color 0.25s ease;
      -webkit-font-smoothing: antialiased;
    }

    h1, h2, h3, .q-heading, .app-title {
      font-family: 'Space Grotesk', 'Plus Jakarta Sans', sans-serif;
    }

    ::-webkit-scrollbar { width: 7px; height: 7px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: var(--border-strong); border-radius: 99px; }

    .svg-ico {
      width: 15px;
      height: 15px;
      flex-shrink: 0;
      display: inline-block;
      vertical-align: middle;
    }

    /* ==========================================================================
       STICKY GLASS TOPBAR
       ========================================================================== */
    .header-wrap {
      position: sticky;
      top: 0;
      z-index: 40;
      background: var(--glass-bg);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--border-color);
    }

    .header-top {
      max-width: 1420px;
      margin: 0 auto;
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }

    .title-area {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .logo-badge {
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: var(--accent-primary-soft);
      color: var(--accent-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid rgba(56, 189, 248, 0.28);
    }

    .app-title {
      font-size: 17px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--text-main);
    }

    .app-subtitle {
      font-size: 11.5px;
      color: var(--text-muted);
      font-weight: 500;
    }

    /* MODE TABS */
    .main-mode-tabs {
      display: inline-flex;
      background: var(--bg-subtle);
      padding: 4px;
      border-radius: 13px;
      border: 1px solid var(--border-color);
      gap: 4px;
      flex-wrap: wrap;
    }

    .mode-tab-btn {
      border: none;
      background: transparent;
      color: var(--text-secondary);
      font-family: inherit;
      font-size: 12.5px;
      font-weight: 700;
      padding: 7px 13px;
      border-radius: 9px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.18s ease;
    }
    .mode-tab-btn:hover { color: var(--text-main); }
    .mode-tab-btn.active {
      background: var(--accent-primary-solid);
      color: #ffffff;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.30);
    }
    .mode-tab-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      padding: 1px 7px;
      border-radius: 99px;
      background: rgba(255, 255, 255, 0.18);
      color: inherit;
    }
    .mode-tab-btn:not(.active) .mode-tab-badge {
      background: var(--bg-card);
      color: var(--accent-primary);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .segmented-control {
      display: inline-flex;
      background: var(--bg-subtle);
      padding: 3px;
      border-radius: 11px;
      border: 1px solid var(--border-color);
      gap: 3px;
      flex-wrap: wrap;
    }

    .seg-btn {
      border: none;
      background: transparent;
      color: var(--text-secondary);
      font-family: inherit;
      font-size: 11.5px;
      font-weight: 600;
      padding: 6px 10px;
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.16s ease;
    }
    .seg-btn:hover { color: var(--text-main); }
    .seg-btn.active {
      background: var(--bg-card);
      color: var(--accent-primary);
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.12);
    }

    .action-btn {
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-main);
      font-family: inherit;
      font-size: 12px;
      font-weight: 600;
      padding: 7px 12px;
      border-radius: 10px;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }
    .action-btn:hover { background: var(--bg-hover); border-color: var(--border-strong); }
    .action-btn.primary-soft {
      background: var(--accent-primary-soft);
      color: var(--accent-primary);
      border-color: rgba(56, 189, 248, 0.30);
    }
    .action-btn.warm-soft {
      background: var(--accent-warm-soft);
      color: var(--accent-warm);
      border-color: rgba(245, 158, 11, 0.35);
    }
    .action-btn.rose-soft {
      background: var(--accent-rose-soft);
      color: var(--accent-rose);
      border-color: rgba(244, 63, 94, 0.32);
    }

    /* QUIZ TOPIC PILL BAR */
    .topic-bar {
      max-width: 1420px;
      margin: 0 auto;
      padding: 6px 24px 11px;
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      scrollbar-width: none;
    }
    .topic-bar::-webkit-scrollbar { display: none; }

    .topic-pill {
      flex-shrink: 0;
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-secondary);
      font-family: inherit;
      font-size: 12px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.16s ease;
      display: inline-flex;
      align-items: center;
      gap: 7px;
    }
    .topic-pill:hover { background: var(--bg-hover); color: var(--text-main); }
    .topic-pill.active {
      background: var(--accent-primary-solid);
      color: #ffffff;
      border-color: var(--accent-primary-solid);
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.28);
    }
    .topic-pill .pill-time {
      font-family: 'JetBrains Mono', monospace;
      font-size: 10.5px;
      opacity: 0.85;
    }

    /* ==========================================================================
       3-COLUMN STUDY & PODCAST STUDIO LAYOUT
       ========================================================================== */
    .studio-grid {
      max-width: 1420px;
      margin: 22px auto 0;
      padding: 0 24px;
      display: grid;
      grid-template-columns: 245px minmax(0, 1fr) 375px;
      gap: 22px;
      align-items: start;
    }

    @media (max-width: 1220px) {
      .studio-grid {
        grid-template-columns: minmax(0, 1fr) 340px;
      }
      .chapter-rail {
        grid-column: 1 / -1;
        position: static !important;
      }
      .rail-list {
        flex-direction: row !important;
        overflow-x: auto;
        padding-bottom: 6px;
      }
      .rail-item {
        flex-shrink: 0;
      }
    }

    @media (max-width: 880px) {
      body[data-mode="quiz"],
      body[data-mode="matrix"] {
        padding-bottom: 24px;
      }
      body[data-mode="quiz"] .player-bar-wrap,
      body[data-mode="matrix"] .player-bar-wrap,
      body[data-mode="quiz"] #voice-switcher-wrap,
      body[data-mode="matrix"] #voice-switcher-wrap,
      body[data-mode="quiz"] #download-link,
      body[data-mode="matrix"] #download-link {
        display: none !important;
      }
      .header-wrap {
        position: static;
      }
      .header-top {
        padding: 10px 14px 8px;
        gap: 10px;
      }
      .app-subtitle {
        display: none;
      }
      .main-mode-tabs {
        width: 100%;
      }
      .mode-tab-btn {
        flex: 1 1 auto;
        justify-content: center;
        padding: 8px 10px;
        font-size: 12px;
      }
      .studio-grid {
        grid-template-columns: 1fr;
        padding: 0 14px;
        margin-top: 14px;
      }
      .header-top, .topic-bar, .quiz-workspace {
        padding-left: 14px !important;
        padding-right: 14px !important;
      }
      .quiz-workspace {
        margin-top: 14px;
      }
      .dialogue-col {
        position: static !important;
      }
      .clean-table {
        display: block;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
      }
      .player-bar-wrap {
        bottom: 8px;
        padding: 0 10px;
      }
      .player-pill {
        padding: 9px 13px;
        border-radius: 18px;
      }
      .now-playing-info {
        min-width: 0;
        width: 100%;
      }
      .main-transport {
        width: 100%;
        justify-content: space-between;
      }
    }

    @media (max-width: 640px) {
      .score-dashboard {
        padding: 16px;
        border-radius: 18px;
        gap: 14px;
      }
      .stats-pills {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        width: 100%;
      }
      .stat-box {
        min-width: 0;
      }
      .quiz-card {
        padding: 16px 15px;
        border-radius: 18px;
        gap: 14px;
      }
      .quiz-question-text {
        font-size: 16px;
      }
      .option-btn {
        padding: 12px 13px;
        font-size: 13.5px;
        gap: 10px;
      }
      .kbd-hint {
        display: none;
      }
      .study-content {
        padding: 16px;
      }
      .card-head {
        padding: 14px 16px;
      }
    }

    .surface-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      box-shadow: var(--shadow-card);
      overflow: hidden;
    }

    /* LEFT CHAPTER RAIL */
    .chapter-rail {
      position: sticky;
      top: 84px;
      padding: 14px;
    }

    .rail-heading {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      padding: 4px 10px 10px;
    }

    .rail-list {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .rail-item {
      width: 100%;
      border: 1px solid transparent;
      background: transparent;
      color: var(--text-secondary);
      font-family: inherit;
      font-size: 12.5px;
      font-weight: 600;
      padding: 9px 11px;
      border-radius: 12px;
      cursor: pointer;
      text-align: left;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      transition: all 0.15s ease;
    }
    .rail-item:hover {
      background: var(--bg-subtle);
      color: var(--text-main);
    }
    .rail-item.active {
      background: var(--accent-primary-soft);
      border-color: rgba(56, 189, 248, 0.30);
      color: var(--accent-primary);
      font-weight: 700;
    }
    .rail-time {
      font-family: 'JetBrains Mono', monospace;
      font-size: 10.5px;
      color: var(--text-muted);
      flex-shrink: 0;
    }
    .rail-item.active .rail-time { color: var(--accent-primary); }

    /* CENTER STUDY SHEET (NATURAL DOCUMENT SCROLL) */
    .card-head {
      padding: 16px 22px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }

    .card-head-title {
      font-size: 14px;
      font-weight: 700;
      color: var(--text-main);
    }

    .card-head-sub {
      font-size: 12px;
      color: var(--text-muted);
    }

    .study-content {
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }

    .q-heading {
      font-size: 21px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--text-main);
      line-height: 1.32;
    }

    .note-block {
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      border-radius: 15px;
      padding: 15px 18px;
      font-size: 14.5px;
      color: var(--text-secondary);
      line-height: 1.65;
    }
    .note-block strong { color: var(--text-main); font-weight: 700; }
    .note-block ul { margin-top: 8px; padding-left: 20px; }
    .note-block li { margin-bottom: 5px; }

    .callout-tip {
      background: var(--accent-green-soft);
      border: 1px solid rgba(16, 185, 129, 0.30);
      border-radius: 15px;
      padding: 14px 18px;
      font-size: 14px;
      color: var(--text-main);
    }
    .callout-tip strong { color: var(--accent-green); }

    .callout-warn {
      background: var(--accent-warm-soft);
      border: 1px solid rgba(245, 158, 11, 0.35);
      border-radius: 15px;
      padding: 14px 18px;
      font-size: 14px;
      color: var(--text-main);
    }
    .callout-warn strong { color: var(--accent-warm); }

    .formula-pill {
      font-family: 'JetBrains Mono', monospace;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--accent-primary);
      background: var(--accent-primary-soft);
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 9px 14px;
      border-radius: 11px;
      text-align: center;
      margin: 8px 0;
    }

    .figure-frame {
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 14px;
    }
    .figure-caption {
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 10px;
    }
    .figure-pad {
      background: var(--figure-pad);
      border-radius: 11px;
      padding: 10px;
      overflow: hidden;
    }
    .figure-pad img {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
    }
    .figure-frame svg {
      width: 100%;
      height: auto;
      display: block;
    }

    .clean-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
      border-radius: 14px;
      overflow: hidden;
      border: 1px solid var(--border-color);
    }
    .clean-table th {
      background: var(--bg-subtle);
      color: var(--text-main);
      font-weight: 700;
      text-align: left;
      padding: 10px 13px;
      border-bottom: 1px solid var(--border-color);
    }
    .clean-table td {
      padding: 9px 13px;
      border-bottom: 1px solid var(--border-color);
      color: var(--text-secondary);
    }
    .clean-table tr:last-child td { border-bottom: none; }

    /* RIGHT STICKY LIVE DIALOGUE */
    .dialogue-col {
      position: sticky;
      top: 84px;
    }

    .transcript-list {
      padding: 14px;
      max-height: calc(100vh - 255px);
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
      scroll-behavior: smooth;
    }

    .dialogue-item {
      padding: 12px 14px;
      border-radius: 14px;
      background: transparent;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.16s ease;
    }
    .dialogue-item:hover { background: var(--bg-subtle); }
    .dialogue-item.active {
      background: var(--bg-active-turn);
      border-color: rgba(56, 189, 248, 0.35);
    }

    .dialogue-meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 5px;
    }

    .speaker-badge {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      font-size: 12.5px;
      font-weight: 700;
    }
    .speaker-dot { width: 8px; height: 8px; border-radius: 50%; }
    .speaker-marek { color: var(--accent-primary); }
    .speaker-marek .speaker-dot { background: var(--accent-primary); }
    .speaker-tereza { color: var(--accent-warm); }
    .speaker-tereza .speaker-dot { background: var(--accent-warm); }

    .eq-bars {
      display: none;
      align-items: flex-end;
      gap: 2px;
      height: 11px;
      margin-left: 4px;
    }
    .dialogue-item.active .eq-bars { display: inline-flex; }
    .eq-bars span {
      width: 2.5px;
      background: currentColor;
      border-radius: 2px;
      animation: eqBounce 0.9s ease-in-out infinite alternate;
    }
    .eq-bars span:nth-child(2) { animation-delay: 0.2s; }
    .eq-bars span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes eqBounce {
      0% { height: 3px; }
      100% { height: 11px; }
    }

    .dialogue-timestamp {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--text-muted);
    }

    .dialogue-body {
      font-size: 13.5px;
      color: var(--text-secondary);
      line-height: 1.58;
    }
    .dialogue-item.active .dialogue-body { color: var(--text-main); }
    .dialogue-body strong { color: var(--text-main); font-weight: 700; }

    /* ==========================================================================
       ABCD QUIZ & RADIAL PROBABILITY / UNCERTAINTY DASHBOARD
       ========================================================================== */
    .quiz-workspace {
      max-width: 1180px;
      margin: 22px auto 0;
      padding: 0 24px;
      display: none;
      flex-direction: column;
      gap: 20px;
    }

    .score-dashboard {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 22px;
      padding: 22px 26px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      gap: 18px;
    }

    .score-top-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 18px;
    }

    .gauges-hero {
      display: flex;
      align-items: center;
      gap: 18px;
      flex-wrap: wrap;
    }

    .radial-gauge {
      position: relative;
      width: 82px;
      height: 82px;
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .radial-gauge svg {
      transform: rotate(-90deg);
      width: 82px;
      height: 82px;
    }
    .radial-track {
      fill: none;
      stroke: var(--bg-subtle);
      stroke-width: 7;
    }
    .radial-fill {
      fill: none;
      stroke-width: 7;
      stroke-linecap: round;
      transition: stroke-dashoffset 0.35s ease, stroke 0.25s ease;
    }
    .radial-center {
      position: absolute;
      inset: 0;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
    }
    .radial-val {
      font-family: 'JetBrains Mono', monospace;
      font-size: 16.5px;
      font-weight: 800;
      line-height: 1.05;
    }
    .radial-lbl {
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--text-muted);
      margin-top: 2px;
    }

    .stats-pills {
      display: flex;
      align-items: center;
      gap: 9px;
      flex-wrap: wrap;
    }

    .stat-box {
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 9px 14px;
      display: flex;
      flex-direction: column;
      min-width: 102px;
    }
    .stat-box-val {
      font-family: 'JetBrains Mono', monospace;
      font-size: 16px;
      font-weight: 800;
      color: var(--text-main);
    }
    .stat-box-lbl {
      font-size: 11px;
      color: var(--text-muted);
      font-weight: 600;
    }
    .stat-box.green .stat-box-val { color: var(--accent-green); }
    .stat-box.rose .stat-box-val { color: var(--accent-rose); }
    .stat-box.warm .stat-box-val { color: var(--accent-warm); }

    /* TRI-STATE BAR */
    .progress-bars-wrap { display: flex; flex-direction: column; gap: 8px; }
    .bar-label-row {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-secondary);
    }
    .bar-track {
      width: 100%;
      height: 11px;
      background: var(--bg-subtle);
      border-radius: 999px;
      overflow: hidden;
      display: flex;
      border: 1px solid var(--border-color);
    }
    .bar-fill-correct { height: 100%; background: var(--accent-green); transition: width 0.3s ease; }
    .bar-fill-uncertainty { height: 100%; background: var(--uncertainty-stripe); transition: width 0.3s ease; }
    .bar-fill-wrong { height: 100%; background: var(--accent-rose); transition: width 0.3s ease; }

    .legend-inline {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
      font-size: 11.5px;
      color: var(--text-muted);
      font-weight: 600;
    }
    .legend-dot {
      display: inline-block;
      width: 10px;
      height: 10px;
      border-radius: 3px;
      margin-right: 5px;
      vertical-align: middle;
    }
    .legend-dot.green { background: var(--accent-green); }
    .legend-dot.uncertainty { background: var(--uncertainty-stripe); border: 1px solid var(--accent-warm); }
    .legend-dot.rose { background: var(--accent-rose); }

    /* PER-CHAPTER PROBABILITY MATRIX */
    .exam-prob-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(min(100%, 320px), 1fr));
      gap: 18px;
    }

    .exam-q-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 20px;
      padding: 20px 22px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      gap: 14px;
      transition: border-color 0.16s ease;
    }
    .exam-q-card:hover { border-color: var(--border-strong); }

    .exam-q-head {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 12px;
    }
    .exam-q-title { font-size: 15.5px; font-weight: 700; color: var(--text-main); line-height: 1.32; }
    .exam-q-sub { font-size: 12px; color: var(--text-muted); margin-top: 3px; font-weight: 500; }

    .chance-badge-col { display: flex; flex-direction: column; align-items: flex-end; flex-shrink: 0; }
    .chance-pill-main {
      font-family: 'JetBrains Mono', monospace;
      font-size: 17px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 10px;
      line-height: 1.2;
    }
    .chance-pill-sub { font-size: 10.5px; font-weight: 700; color: var(--text-muted); margin-top: 3px; }

    .metrics-3col {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      border-radius: 13px;
      padding: 9px 10px;
      text-align: center;
    }
    .m3-val { font-family: 'JetBrains Mono', monospace; font-size: 13.5px; font-weight: 800; }
    .m3-lbl { font-size: 10.5px; color: var(--text-muted); font-weight: 600; }

    .subq-chips-wrap { display: flex; flex-wrap: wrap; gap: 6px; }
    .subq-chip {
      border: 1px solid var(--border-color);
      background: var(--bg-subtle);
      color: var(--text-secondary);
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.14s ease;
    }
    .subq-chip:hover { transform: translateY(-1px); border-color: var(--accent-primary); }
    .subq-chip.st-correct { background: var(--accent-green-soft); color: var(--accent-green); border-color: rgba(16, 185, 129, 0.4); }
    .subq-chip.st-wrong { background: var(--accent-rose-soft); color: var(--accent-rose); border-color: rgba(244, 63, 94, 0.4); }
    .subq-chip.st-unanswered { background: var(--accent-warm-soft); color: var(--accent-warm); border-color: rgba(245, 158, 11, 0.35); }

    .exam-q-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-top: auto;
      padding-top: 8px;
      border-top: 1px solid var(--border-color);
    }

    /* QUESTION CARD */
    .quiz-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 22px;
      padding: 26px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      gap: 18px;
      transition: border-color 0.2s ease;
    }
    .quiz-card.answered-correct { border-color: rgba(16, 185, 129, 0.45); }
    .quiz-card.answered-wrong { border-color: rgba(244, 63, 94, 0.45); }

    .quiz-card-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }

    .quiz-topic-tag {
      font-size: 12px;
      font-weight: 700;
      padding: 5px 12px;
      border-radius: 99px;
      background: var(--accent-primary-soft);
      color: var(--accent-primary);
      border: 1px solid rgba(56, 189, 248, 0.25);
    }

    .quiz-num-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }

    .q-prob-pill {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 9px;
      border-radius: 99px;
    }
    .q-prob-pill.uncertain { background: var(--accent-warm-soft); color: var(--accent-warm); border: 1px solid rgba(245, 158, 11, 0.35); }
    .q-prob-pill.certain-ok { background: var(--accent-green-soft); color: var(--accent-green); border: 1px solid rgba(16, 185, 129, 0.35); }
    .q-prob-pill.certain-bad { background: var(--accent-rose-soft); color: var(--accent-rose); border: 1px solid rgba(244, 63, 94, 0.35); }

    .quiz-question-text {
      font-size: 18.5px;
      font-weight: 700;
      line-height: 1.42;
      color: var(--text-main);
      letter-spacing: -0.015em;
    }

    .options-grid { display: flex; flex-direction: column; gap: 10px; }

    .option-btn {
      width: 100%;
      text-align: left;
      background: var(--bg-subtle);
      border: 1.5px solid var(--border-color);
      border-radius: 15px;
      padding: 14px 17px;
      color: var(--text-main);
      font-family: inherit;
      font-size: 14.5px;
      font-weight: 600;
      line-height: 1.5;
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 13px;
      transition: all 0.15s ease;
    }
    .option-btn:hover:not(:disabled) {
      background: var(--bg-hover);
      border-color: var(--accent-primary);
      transform: translateX(2px);
    }
    .option-btn:disabled { cursor: default; }

    .opt-letter {
      flex-shrink: 0;
      width: 28px;
      height: 28px;
      border-radius: 8px;
      background: var(--bg-card);
      border: 1px solid var(--border-strong);
      color: var(--text-secondary);
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-top: 1px;
    }

    .option-btn.correct-choice { background: var(--accent-green-soft); border-color: var(--accent-green); }
    .option-btn.correct-choice .opt-letter { background: var(--accent-green); border-color: var(--accent-green); color: #ffffff; }
    .option-btn.wrong-choice { background: var(--accent-rose-soft); border-color: var(--accent-rose); }
    .option-btn.wrong-choice .opt-letter { background: var(--accent-rose); border-color: var(--accent-rose); color: #ffffff; }
    .option-btn.dimmed-choice { opacity: 0.56; }

    .explanation-box {
      background: var(--bg-subtle);
      border-left: 4px solid var(--accent-primary);
      border-radius: 13px;
      padding: 14px 17px;
      font-size: 14px;
      color: var(--text-secondary);
      line-height: 1.6;
    }
    .explanation-box.is-correct { border-left-color: var(--accent-green); }
    .explanation-box.is-wrong { border-left-color: var(--accent-rose); }
    .explanation-box strong { color: var(--text-main); }

    .quiz-nav-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      padding-top: 8px;
      border-top: 1px solid var(--border-color);
    }

    .next-q-cta {
      border: none;
      background: var(--accent-primary-solid);
      color: #ffffff;
      font-family: inherit;
      font-size: 13.5px;
      font-weight: 700;
      padding: 10px 20px;
      border-radius: 12px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.28);
      transition: all 0.15s ease;
    }
    .next-q-cta:hover { filter: brightness(1.08); transform: translateY(-1px); }

    .kbd-hint {
      font-family: 'JetBrains Mono', monospace;
      font-size: 10.5px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 6px;
      background: var(--bg-card);
      border: 1px solid var(--border-strong);
      color: var(--text-muted);
      line-height: 1.25;
      flex-shrink: 0;
      align-self: center;
      opacity: 0.82;
    }
    .next-q-cta .kbd-hint {
      background: rgba(255, 255, 255, 0.18);
      border-color: rgba(255, 255, 255, 0.34);
      color: #ffffff;
      opacity: 0.95;
    }
    @media (max-width: 540px) {
      .kbd-hint { display: none; }
    }

    /* ==========================================================================
       GOOGLE KEEP MODAL
       ========================================================================== */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      z-index: 80;
      background: rgba(5, 8, 15, 0.72);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .modal-backdrop.open { display: flex; }

    .modal-panel {
      width: 100%;
      max-width: 780px;
      max-height: 88vh;
      background: var(--bg-card);
      border: 1px solid var(--border-strong);
      border-radius: 22px;
      box-shadow: var(--shadow-player);
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }

    .modal-body {
      padding: 18px 22px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .keep-pre {
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 16px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12.2px;
      line-height: 1.55;
      color: var(--text-secondary);
      white-space: pre-wrap;
      max-height: 52vh;
      overflow-y: auto;
    }

    /* ==========================================================================
       FLOATING STUDIO AUDIO PLAYER BAR
       ========================================================================== */
    .player-bar-wrap {
      position: fixed;
      bottom: 14px;
      left: 0;
      right: 0;
      z-index: 50;
      padding: 0 18px;
      pointer-events: none;
    }

    .player-pill {
      pointer-events: auto;
      max-width: 1000px;
      margin: 0 auto;
      background: var(--glass-bg);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid var(--border-strong);
      border-radius: 22px;
      box-shadow: var(--shadow-player);
      padding: 10px 20px 12px;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .scrub-row { display: flex; align-items: center; gap: 12px; }
    .scrub-time {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      font-weight: 600;
      color: var(--text-muted);
      min-width: 42px;
    }
    .scrub-time.current { color: var(--accent-primary); }

    .seek-track-wrap {
      position: relative;
      flex: 1;
      display: flex;
      align-items: center;
      height: 18px;
    }

    .seek-markers {
      position: absolute;
      left: 7px;
      right: 7px;
      top: 50%;
      transform: translateY(-50%);
      height: 8px;
      pointer-events: none;
      z-index: 3;
    }

    .seek-tick {
      position: absolute;
      top: 0;
      width: 2px;
      height: 8px;
      border-radius: 2px;
      background: var(--text-muted);
      opacity: 0.55;
      transform: translateX(-50%);
    }

    .range-bar {
      position: relative;
      z-index: 2;
      width: 100%;
      -webkit-appearance: none;
      appearance: none;
      height: 6px;
      background: var(--bg-subtle);
      border-radius: 999px;
      outline: none;
      cursor: pointer;
    }
    .range-bar::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: var(--accent-primary);
      cursor: pointer;
      transition: transform 0.12s ease;
    }
    .range-bar::-webkit-slider-thumb:hover { transform: scale(1.2); }

    .player-controls-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }

    .now-playing-info {
      display: flex;
      align-items: center;
      gap: 9px;
      min-width: 210px;
    }

    .live-tag {
      font-size: 11px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 99px;
      background: var(--accent-primary-soft);
      color: var(--accent-primary);
    }

    .player-eq {
      display: inline-flex;
      align-items: flex-end;
      gap: 2.5px;
      height: 14px;
      padding: 0 2px;
      opacity: 0.32;
      transition: opacity 0.2s ease;
    }
    .player-eq span {
      width: 2.5px;
      height: 4px;
      border-radius: 2px;
      background: var(--accent-primary);
      transition: height 0.2s ease;
    }
    .player-pill.is-playing .player-eq {
      opacity: 1;
    }
    .player-pill.is-playing .player-eq span {
      animation: playerWave 0.78s ease-in-out infinite alternate;
    }
    .player-pill.is-playing .player-eq span:nth-child(2) { animation-delay: 0.16s; }
    .player-pill.is-playing .player-eq span:nth-child(3) { animation-delay: 0.34s; }
    .player-pill.is-playing .player-eq span:nth-child(4) { animation-delay: 0.12s; }
    .player-pill.is-playing .player-eq span:nth-child(5) { animation-delay: 0.28s; }
    @keyframes playerWave {
      0% { height: 3px; }
      100% { height: 14px; }
    }

    .main-transport { display: flex; align-items: center; gap: 7px; }

    .icon-btn {
      border: 1px solid var(--border-color);
      background: var(--bg-subtle);
      color: var(--text-main);
      font-family: inherit;
      font-size: 11.5px;
      font-weight: 600;
      padding: 7px 11px;
      border-radius: 10px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
    }
    .icon-btn:hover { background: var(--bg-hover); }

    .play-cta {
      border: none;
      background: var(--accent-primary-solid);
      color: #ffffff;
      font-family: inherit;
      font-size: 13px;
      font-weight: 700;
      padding: 8px 18px;
      border-radius: 12px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.34);
      transition: all 0.15s ease;
    }
    .play-cta:hover { transform: translateY(-1px); filter: brightness(1.08); }
  </style>
</head>
<body>

  <!-- STICKY GLASS TOPBAR -->
  <header class="header-wrap">
    <div class="header-top">
      <div class="title-area">
        <div class="logo-badge" aria-hidden="true">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="3"/>
            <ellipse cx="12" cy="12" rx="10" ry="4.5" transform="rotate(-28 12 12)"/>
            <circle cx="19.5" cy="7.5" r="1.4" fill="currentColor" stroke="none"/>
          </svg>
        </div>
        <div>
          <h1 class="app-title">Satelitní komunikace &amp; Oběžné dráhy</h1>
          <div class="app-subtitle">Skripta Oběžné dráhy + GiTySAT • Audio studio, 99 ABCD otázek &amp; Tahák</div>
        </div>
      </div>

      <!-- 3 MAIN VIEW MODES -->
      <div class="main-mode-tabs">
        <button id="tab-btn-podcast" class="mode-tab-btn active" onclick="setAppMode('podcast')">
          <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/></svg>
          <span>Studium &amp; Podcast</span>
        </button>
        <button id="tab-btn-quiz" class="mode-tab-btn" onclick="setAppMode('quiz')">
          <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
          <span>Test ABCD</span>
          <span id="header-quiz-badge" class="mode-tab-badge">Šance 0 %</span>
        </button>
        <button id="tab-btn-matrix" class="mode-tab-btn" onclick="setAppMode('matrix')">
          <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/></svg>
          <span>Šance po tématech</span>
          <span id="header-uncertainty-badge" class="mode-tab-badge">Nejistota 100 %</span>
        </button>
      </div>

      <div class="header-actions">
        <button class="action-btn primary-soft" onclick="openKeepModal()">
          <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          <span>Google Keep Tahák</span>
        </button>

        <div class="segmented-control" title="Výběr hlasového enginu">
          <button id="eng-eleven" class="seg-btn active" onclick="switchEngine('eleven_hd')">
            ElevenLabs HD (Brian &amp; Sarah)
          </button>
          <button id="eng-cz" class="seg-btn" onclick="switchEngine('cz_studio')">
            CZ Studio (Antonín &amp; Vlasta)
          </button>
        </div>

        <button id="theme-btn" class="action-btn" onclick="toggleTheme()">
          <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>
          <span>Světlý režim</span>
        </button>

        <a id="download-link" href="podcast_satelity_cz.mp3" download class="action-btn">
          <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          <span>MP3</span>
        </a>
      </div>
    </div>

    <!-- QUIZ TOPIC PILLS (SHOWN IN QUIZ & MATRIX MODES) -->
    <nav id="quiz-topic-bar" class="topic-bar" style="display:none;"></nav>
  </header>

  <!-- ========================================================================
       VIEW 1: 3-COLUMN ORBITAL STUDY STUDIO (CHAPTER RAIL + SHEET + DIALOGUE)
       ======================================================================== -->
  <main id="podcast-workspace" class="studio-grid">

    <!-- LEFT STICKY CHAPTER RAIL -->
    <aside class="surface-card chapter-rail">
      <div class="rail-heading">Kapitoly (1–9)</div>
      <div id="chapter-list" class="rail-list"></div>
    </aside>

    <!-- CENTER RICH VISUAL STUDY SHEET -->
    <section class="surface-card">
      <div class="card-head">
        <div>
          <div id="active-q-badge" class="card-head-title">Přehled &amp; Vizuální tahák</div>
          <div class="card-head-sub">Automaticky se synchronizuje s přehrávanou kapitolou podcastu</div>
        </div>
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="action-btn primary-soft" onclick="openQuizForCurrentTopic()">
            <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
            <span>Otestovat toto téma (ABCD)</span>
          </button>
          <button class="action-btn" onclick="showAllDiagrams()">
            <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
            <span>Zobrazit celý tahák</span>
          </button>
        </div>
      </div>
      <div id="diagram-panel" class="study-content"></div>
    </section>

    <!-- RIGHT STICKY LIVE DIALOGUE -->
    <section class="surface-card dialogue-col">
      <div class="card-head">
        <div>
          <div class="card-head-title">Rozhovor (Marek &amp; Tereza)</div>
          <div class="card-head-sub">Kliknutím na repliku přeskočíš přímo v audiu</div>
        </div>
        <label style="font-size:11.5px; font-weight:600; color:var(--text-secondary); display:flex; align-items:center; gap:6px; cursor:pointer;">
          <input type="checkbox" id="autoscroll-toggle" checked style="accent-color:var(--accent-primary);" />
          Auto-posun
        </label>
      </div>
      <div id="transcript-container" class="transcript-list"></div>
    </section>

  </main>

  <!-- ========================================================================
       VIEW 2 & 3: 99-QUESTION ABCD QUIZ + PROBABILITY & UNCERTAINTY STUDIO
       ======================================================================== -->
  <section id="quiz-workspace" class="quiz-workspace">

    <div class="score-dashboard">
      <div class="score-top-row">
        <div class="gauges-hero">
          <!-- RADIAL GAUGE 1: CONFIRMED CHANCE -->
          <div class="radial-gauge" title="Potvrzená šance = správně zodpovězené / všechny otázky v okruhu">
            <svg viewBox="0 0 82 82">
              <circle class="radial-track" cx="41" cy="41" r="34"/>
              <circle id="gauge-chance-ring" class="radial-fill" cx="41" cy="41" r="34" stroke="var(--accent-green)" stroke-dasharray="213.6" stroke-dashoffset="213.6"/>
            </svg>
            <div class="radial-center">
              <span id="quiz-pct-val" class="radial-val" style="color:var(--accent-green);">0 %</span>
              <span class="radial-lbl">Jistota</span>
            </div>
          </div>

          <!-- RADIAL GAUGE 2: UNCERTAINTY -->
          <div class="radial-gauge" title="Nejistota = podíl dosud nezodpovězených otázek">
            <svg viewBox="0 0 82 82">
              <circle class="radial-track" cx="41" cy="41" r="34"/>
              <circle id="gauge-unc-ring" class="radial-fill" cx="41" cy="41" r="34" stroke="var(--accent-warm)" stroke-dasharray="213.6" stroke-dashoffset="0"/>
            </svg>
            <div class="radial-center">
              <span id="quiz-unc-val" class="radial-val" style="color:var(--accent-warm);">100 %</span>
              <span class="radial-lbl">Nejistota</span>
            </div>
          </div>

          <div>
            <div id="dashboard-scope-title" style="font-size:16.5px; font-weight:700; color:var(--text-main);">
              Šance, že uděláš test (99 otázek)
            </div>
            <div style="font-size:12.5px; color:var(--text-secondary); font-weight:600; margin-top:3px;">
              Odhad se započtením nejistoty (tipování 25 % u nezodpovězených): <strong id="expected-chance-lbl" style="color:var(--accent-primary);">25 %</strong> • Interval: <strong id="interval-chance-lbl">0 % – 100 %</strong>
            </div>
          </div>
        </div>

        <div class="stats-pills">
          <div class="stat-box green">
            <span id="stat-correct" class="stat-box-val">0</span>
            <span class="stat-box-lbl">Potvrzeno (Správně)</span>
          </div>
          <div class="stat-box warm">
            <span id="stat-unanswered" class="stat-box-val">99</span>
            <span class="stat-box-lbl">Nejistota (Nezodp.)</span>
          </div>
          <div class="stat-box rose">
            <span id="stat-wrong" class="stat-box-val">0</span>
            <span class="stat-box-lbl">Chyby (Špatně)</span>
          </div>
          <div class="stat-box">
            <span id="stat-streak" class="stat-box-val">0</span>
            <span class="stat-box-lbl">Série bez chyby</span>
          </div>
        </div>
      </div>

      <!-- TRI-STATE PROGRESS BAR -->
      <div class="progress-bars-wrap">
        <div class="bar-label-row">
          <span id="bar-left-label">Rozložení jistoty a nejistoty ve zvoleném okruhu</span>
          <div class="legend-inline">
            <span><i class="legend-dot green"></i>Potvrzená jistota (<span id="leg-ok-pct">0%</span>)</span>
            <span><i class="legend-dot uncertainty"></i>Nejistota – nezodpovězeno (<span id="leg-unc-pct">100%</span>)</span>
            <span><i class="legend-dot rose"></i>Chybné (<span id="leg-bad-pct">0%</span>)</span>
          </div>
        </div>
        <div class="bar-track">
          <div id="bar-correct" class="bar-fill-correct" style="width: 0%;"></div>
          <div id="bar-uncertainty" class="bar-fill-uncertainty" style="width: 100%;"></div>
          <div id="bar-wrong" class="bar-fill-wrong" style="width: 0%;"></div>
        </div>
      </div>

      <!-- QUIZ CONTROLS -->
      <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px; padding-top:4px;">
        <div class="segmented-control">
          <button id="qview-single" class="seg-btn active" onclick="setQuizViewMode('single')">Po jedné otázce (A/B/C/D)</button>
          <button id="qview-list" class="seg-btn" onclick="setQuizViewMode('list')">Všechny pod sebou</button>
          <button id="qview-matrix" class="seg-btn" onclick="setQuizViewMode('matrix')">Šance po tématech</button>
        </div>

        <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
          <button id="btn-filter-unanswered" class="action-btn warm-soft" onclick="filterOnlyUnanswered()">
            <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
            <span id="btn-filter-unanswered-lbl">Procvičit jen nejistotu (99)</span>
          </button>
          <button id="btn-filter-mistakes" class="action-btn rose-soft" onclick="filterOnlyMistakes()" style="display:none;">
            <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>
            <span id="btn-filter-mistakes-lbl">Procvičit jen chyby (0)</span>
          </button>
          <button class="action-btn primary-soft" onclick="shuffleActiveQuiz()">
            <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 3 21 3 21 8"/><line x1="4" y1="20" x2="21" y2="3"/><polyline points="21 16 21 21 16 21"/><line x1="15" y1="15" x2="21" y2="21"/><line x1="4" y1="4" x2="9" y2="9"/></svg>
            <span>Zamíchat</span>
          </button>
          <button class="action-btn" onclick="resetQuizStats()">
            <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
            <span>Vynulovat</span>
          </button>
        </div>
      </div>
    </div>

    <div id="quiz-cards-container" style="display:flex; flex-direction:column; gap:18px;"></div>
  </section>

  <!-- GOOGLE KEEP MODAL -->
  <div id="keep-modal" class="modal-backdrop" onclick="if(event.target===this) closeKeepModal()">
    <div class="modal-panel">
      <div class="card-head">
        <div>
          <div class="card-head-title">Tahák připravený pro Google Keep</div>
          <div class="card-head-sub">Čistý formátovaný text s odrážkami – stačí kliknout na Kopírovat a vložit (Ctrl+V) do Keepu</div>
        </div>
        <button class="action-btn" onclick="closeKeepModal()">
          <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          <span>Zavřít</span>
        </button>
      </div>
      <div class="modal-body">
        <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px;">
          <div class="segmented-control">
            <button id="keep-tab-full" class="seg-btn active" onclick="switchKeepTab('full')">Kompletní tahák (9 kapitol)</button>
            <button id="keep-tab-pocket" class="seg-btn" onclick="switchKeepTab('pocket')">Kapesní rychlo-tahák (1 obrazovka)</button>
          </div>
          <button id="keep-copy-btn" class="next-q-cta" onclick="copyKeepText()">
            <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span id="keep-copy-label">Kopírovat do schránky</span>
          </button>
        </div>
        <pre id="keep-preview-box" class="keep-pre"></pre>
      </div>
    </div>
  </div>

  <!-- FLOATING STUDIO AUDIO PLAYER -->
  <div class="player-bar-wrap">
    <audio id="podcast-audio" src="podcast_satelity_cz.mp3" preload="metadata"></audio>
    <div id="player-pill" class="player-pill">
      <div class="scrub-row">
        <span id="time-current" class="scrub-time current">00:00</span>
        <div class="seek-track-wrap">
          <div id="seek-markers" class="seek-markers" aria-hidden="true"></div>
          <input id="seek-slider" type="range" class="range-bar" min="0" max="700" step="0.1" value="0" />
        </div>
        <span id="time-total" class="scrub-time">00:00</span>
      </div>

      <div class="player-controls-row">
        <div class="now-playing-info">
          <span id="player-eq" class="player-eq" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span></span>
          <span id="now-playing-speaker" class="live-tag">Připraveno</span>
          <span id="now-playing-chapter" style="font-size:12px; color:var(--text-secondary); font-weight:600;">Klikni na Přehrát</span>
        </div>

        <div class="main-transport">
          <button class="icon-btn" onclick="skipReplica(-1)" title="Předchozí replika">
            <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="19 20 9 12 19 4 19 20"/><line x1="5" y1="19" x2="5" y2="5"/></svg>
            <span>Předchozí</span>
          </button>
          <button class="icon-btn" onclick="seekRelative(-10)" title="Zpět o 10 sekund">
            <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
            <span>-10 s</span>
          </button>
          <button id="play-btn" class="play-cta" onclick="togglePlay()">
            <svg id="play-icon" class="svg-ico" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="6 4 20 12 6 20 6 4"/></svg>
            <span id="play-label">Přehrát</span>
          </button>
          <button class="icon-btn" onclick="seekRelative(10)" title="Vpřed o 10 sekund">
            <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/></svg>
            <span>+10 s</span>
          </button>
          <button class="icon-btn" onclick="skipReplica(1)" title="Další replika">
            <span>Další</span>
            <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 4 15 12 5 20 5 4"/><line x1="19" y1="5" x2="19" y2="19"/></svg>
          </button>
        </div>

        <div class="segmented-control">
          <button class="seg-btn speed-btn active" data-speed="1" onclick="setSpeed(1.0)">1×</button>
          <button class="seg-btn speed-btn" data-speed="1.15" onclick="setSpeed(1.15)">1.15×</button>
          <button class="seg-btn speed-btn" data-speed="1.25" onclick="setSpeed(1.25)">1.25×</button>
          <button class="seg-btn speed-btn" data-speed="1.5" onclick="setSpeed(1.5)">1.5×</button>
        </div>
      </div>
    </div>
  </div>

  <script>
    const RAW_DATA = __PODCAST_DATA_JSON__;
    const RAW_QUIZ = __QUIZ_QUESTIONS_JSON__;
    const KEEP_DATA = __KEEP_DATA_JSON__;

    let activeEngine = RAW_DATA.default_engine || "eleven_hd";
    let currentTrack = RAW_DATA.tracks ? RAW_DATA.tracks[activeEngine] : RAW_DATA;
    let appMode = "podcast";

    const CHAPTERS = [
      { id: "intro", badge: "Úvod", title: "Úvod do tématu" },
      { id: "sat-1", badge: "Kap. 1", title: "1. Orbitální mechanika & Kepler" },
      { id: "sat-2", badge: "Kap. 2", title: "2. Elementy & Orientace drah" },
      { id: "sat-3", badge: "Kap. 3", title: "3. LEO, MEO, GEO & Molnija/Tundra" },
      { id: "sat-4", badge: "Kap. 4", title: "4. Footprint, Latence, Doppler, FSPL" },
      { id: "sat-5", badge: "Kap. 5", title: "5. Konstelace Walker & Laser ISL" },
      { id: "sat-6", badge: "Kap. 6", title: "6. Kosmický segment & Pásma C–E" },
      { id: "sat-7", badge: "Kap. 7", title: "7. GEO sítě, Topologie & GiTy" },
      { id: "sat-8", badge: "Kap. 8", title: "8. O3b, OneWeb, Starlink, Amazon" },
      { id: "sat-9", badge: "Kap. 9", title: "9. Terminály, TRANSEC, ACM & Hybrid" }
    ];

    const QUIZ_TOPICS = [
      { id: "all",   title: "Všechny otázky", desc: "Kompletní soubor 99 otázek napříč všemi 9 kapitolami" },
      { id: "sat-1", title: "1. Mechanika & Kepler", desc: "Gravitace vs. dostředivá síla, v_c(h), úniková rychlost, 3 Keplerovy zákony a poruchy" },
      { id: "sat-2", title: "2. Elementy & Orientace", desc: "6 Keplerových elementů (a,e,i,Ω,ω,ν), prográdní/polární/retrográdní a SSO" },
      { id: "sat-3", title: "3. LEO / MEO / GEO / Speciální", desc: "Výšky, periody, Van Allenovy pásy, 4 podmínky GEO, GSO analema, Molnija vs. Tundra" },
      { id: "sat-4", title: "4. Spoj: Latence, Doppler, FSPL", desc: "Footprint vs. viditelnost, 119/239/500–650 ms, Dopplerův posuv a útlum FSPL" },
      { id: "sat-5", title: "5. Konstelace & Laser ISL", desc: "Spolehlivost P=1−(1−p)ᴺ, Walker Delta (360°) vs. Star (180°), ISL 1550 nm a 5G/6G NTN" },
      { id: "sat-6", title: "6. Kosmický segment & Pásma", desc: "Standardní vs. HTS, transpondéry (Bend pipe, Cross, OBS) a pásma C–E (22,23 GHz)" },
      { id: "sat-7", title: "7. GEO sítě & GiTySAT", desc: "Teleport v ČR, MPLS G-Net, NBÚ Tajné, Broadcast/SCPC/Star/MESH, Internet vs. Privátní" },
      { id: "sat-8", title: "8. Moderní konstelace", desc: "O3b mPOWER (MEO), OneWeb (MIR/CIR), Starlink, Amazon LEO a Telesat Lightspeed" },
      { id: "sat-9", title: "9. Terminály, Bezpečnost & Hybrid", desc: "Antény & modemy, TRANSEC/CSIR/FIPS, DVB-S2X ACM a hybridní síť GEO+LEO" }
    ];

    const DIAGRAMS = {
      "intro": `
        <div class="q-heading">Satelitní komunikace &amp; Oběžné dráhy – Přehled studia</div>
        <div class="note-block">
          Tahle stránka spojuje oba materiály ke zkoušce: <strong>skripta Oběžné dráhy &amp; Satelitní konstelace</strong> a prezentaci <strong>GiTySAT</strong>. Vše je rozdělené do <strong>9 přehledných kapitol</strong> bez zbytečného odvozování složitých vzorců.
        </div>
        <div class="callout-tip">
          <strong>Jak se rychle připravit:</strong><br/>
          1) Pusť si podcast v českém studiu (Marek &amp; Tereza) a sleduj schémata u jednotlivých kapitol.<br/>
          2) Přepni se do <strong>Test ABCD (99 otázek)</strong> – každá klíčová věc je tu 3× jinak.<br/>
          3) V záložce <strong>Šance po tématech</strong> sleduj u každé kapitoly potvrzenou šanci i zónu nejistoty.
        </div>
      `,
      "sat-1": `
        <div class="q-heading">1. Orbitální mechanika a Keplerovy zákony</div>
        <div class="figure-frame">
          <div class="figure-caption">Obr. 12 ze skript: Znázornění tří Keplerových zákonů pohybu družic</div>
          <div class="figure-pad"><img src="assets/obr12_kepler.png" alt="Tři Keplerovy zákony" /></div>
        </div>
        <div class="note-block">
          <strong>Rovnováha pohybu a rychlosti:</strong>
          <ul>
            <li><strong>Gravitační síla</strong> (F_g = μ·m / r², klesá s r²) poskytuje potřebnou <strong>dostředivou sílu</strong>.</li>
            <li><strong>Odstředivá síla</strong> není další skutečná síla – je to jen zdánlivá setrvačná síla v neinerciální soustavě rotující s družicí.</li>
            <li><strong>Klíčová intuice:</strong> Čím <strong>výš</strong> je kruhová dráha, tím <strong>POMALEJI</strong> družice letí (LEO ~7,6 km/s vs. GEO ~3,1 km/s) a tím <strong>DELŠÍ</strong> má oběžnou dobu.</li>
            <li><strong>Úniková rychlost</strong> je √2-krát větší než kruhová (u povrchu ~11,2 km/s → parabola e = 1; nad ní hyperbola e &gt; 1).</li>
          </ul>
        </div>
        <div class="callout-warn">
          <strong>3 Keplerovy zákony &amp; reálné poruchy:</strong><br/>
          • <strong>1. zákon:</strong> Dráha je elipsa se Zemí v jednom ohnisku (kruh je elipsa s e = 0).<br/>
          • <strong>2. zákon (ploch):</strong> Družice letí <strong>nejrychleji v perigeu</strong> (nejblíž Zemi) a <strong>nejpomaleji v apogeu</strong> (nejdál od Země).<br/>
          • <strong>3. zákon:</strong> T² ∝ a³ (druhá mocnina oběžné doby roste se třetí mocninou hlavní poloosy).<br/>
          • <strong>Reálné poruchy dráhy:</strong> zploštění Země (koeficient J₂), odpor zbytkové atmosféry (nízké LEO), gravitace Slunce a Měsíce, tlak slunečního záření.
        </div>
      `,
      "sat-2": `
        <div class="q-heading">2. Orbitální elementy a orientace drah</div>
        <div class="figure-frame">
          <div class="figure-caption">Obr. 14 ze skript: Rovníkové, polární, slunečně synchronní (SSO) a nakloněné dráhy</div>
          <div class="figure-pad"><img src="assets/obr14_orientace.png" alt="Orientace oběžných drah" /></div>
        </div>
        <table class="clean-table">
          <thead><tr><th>Keplerův element</th><th>Symbol</th><th>Co určuje</th></tr></thead>
          <tbody>
            <tr><td>Hlavní poloosa</td><td><strong>a</strong></td><td>Velikost oběžné dráhy</td></tr>
            <tr><td>Excentricita</td><td><strong>e</strong></td><td>Tvar dráhy (0 = kružnice, 0 &lt; e &lt; 1 = elipsa)</td></tr>
            <tr><td>Inklinace</td><td><strong>i</strong></td><td>Sklon roviny dráhy vůči rovníku (0° až 180°)</td></tr>
            <tr><td>RAAN (vzestupný uzel)</td><td><strong>Ω</strong></td><td>Natočení roviny dráhy kolem osy Země (u i = 0° nedefinováno)</td></tr>
            <tr><td>Argument perigea</td><td><strong>ω</strong></td><td>Poloha perigea uvnitř roviny dráhy (u e = 0 nedefinováno)</td></tr>
            <tr><td>Pravá anomálie</td><td><strong>ν</strong></td><td>Okamžitá poloha družice na dráze v čase</td></tr>
          </tbody>
        </table>
        <div class="note-block">
          <strong>Orientace podle inklinace i:</strong>
          <ul>
            <li><strong>Prográdní (0° ≤ i &lt; 90°):</strong> po směru rotace Země. <strong>Retrográdní (90° &lt; i ≤ 180°):</strong> proti rotaci Země.</li>
            <li><strong>Polární (i ≈ 90°):</strong> přelétá nad oběma póly → postupně nasnímá celý povrch Země (meteo, SAR, průzkum).</li>
            <li><strong>Slunečně synchronní SSO (i ≈ 97°–99°, 500–900 km):</strong> využívá zploštění Země (J₂) k precesi +0,9856°/den → přelétá ve <strong>stejný místní sluneční čas</strong> (optické snímkování, např. PlanetScope).</li>
          </ul>
        </div>
      `,
      "sat-3": `
        <div class="q-heading">3. Výškové rozdělení LEO, MEO, GEO a speciální dráhy</div>
        <div class="figure-frame">
          <div class="figure-caption">Obr. 13 ze skript: Porovnání výšek LEO, MEO a GEO</div>
          <div class="figure-pad"><img src="assets/obr13_leo_meo_geo.png" alt="LEO MEO GEO" /></div>
        </div>
        <table class="clean-table">
          <thead><tr><th>Dráha</th><th>Výška &amp; Oběh</th><th>RTT Latence</th><th>Pokrytí &amp; Příklady</th></tr></thead>
          <tbody>
            <tr><td><strong>LEO</strong></td><td>160–2 000 km<br/>90–130 min</td><td>20–50 ms<br/>(OneWeb ~100 ms)</td><td>Malé (~3,6 % na 500 km), stovky–tisíce družic, velký Doppler (Starlink, OneWeb, Iridium)</td></tr>
            <tr><td><strong>MEO</strong></td><td>2 000–35 786 km<br/>2–24 h</td><td>50–150 ms</td><td>Střední, desítky družic, Van Allenovy radiační pásy (GPS 20 200 km, Galileo, O3b 8 000 km)</td></tr>
            <tr><td><strong>GEO</strong></td><td>35 786 km<br/>23 h 56 min 4 s</td><td>500–650 ms</td><td>Až 42,4 % povrchu / družice (3 pokryjí většinu Země mimo póly), pevná anténa (Inmarsat, Astra)</td></tr>
          </tbody>
        </table>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap:14px;">
          <div class="figure-frame">
            <div class="figure-caption">Obr. 15: GEO vs. GSO (analema / osmička)</div>
            <div class="figure-pad"><img src="assets/obr15_geo_gso.png" alt="GEO a GSO" /></div>
          </div>
          <div class="figure-frame">
            <div class="figure-caption">Obr. 16: Molnija (12 h) vs. Tundra (24 h)</div>
            <div class="figure-pad"><img src="assets/obr16_molnija_tundra.png" alt="Molnija a Tundra" /></div>
          </div>
        </div>
        <div class="callout-tip">
          <strong>4 podmínky GEO:</strong> kruhová (e = 0) + rovníková (i = 0°) + prográdní + perioda = siderický den (23 h 56 min 4 s).<br/>
          <strong>Molnija &amp; Tundra (sklon i ≈ 63,4°):</strong> vysoce eliptické dráhy pro Arktidu a severní šířky – pomalý pohyb v apogeu zajistí 8+ h (Molnija, 12 h) až 12–16 h (Tundra, 24 h) pokrytí.
        </div>
      `,
      "sat-4": `
        <div class="q-heading">4. Vliv dráhy na rádiový spoj: Footprint, Latence, Doppler a FSPL</div>
        <div class="note-block">
          <strong>Footprint (stopa pokrytí) vs. Geometrická viditelnost:</strong>
          <ul>
            <li><strong>Geometrická viditelnost</strong> (elevace 0°) je jen teoretický výhled nad obzor.</li>
            <li><strong>Skutečný footprint</strong> je vždy menší – omezuje ho minimální elevační úhel (delší průchod atmosférou a stínění terénem při nízké elevaci), tvar svazku a výkonová bilance.</li>
          </ul>
        </div>
        <div class="note-block">
          <strong>Latence u GEO (rychlostí světla c ≈ 300 000 km/s):</strong>
          <ul>
            <li>1 úsek Země → GEO (35 786 km): <strong>~119 ms</strong></li>
            <li>Jednosměrně A → GEO → B (2 úseky): <strong>~239 ms</strong></li>
            <li>Minimální fyzikální RTT: <strong>~478 ms</strong> → Reálné síťové RTT v praxi: <strong>500–650 ms</strong>.</li>
          </ul>
        </div>
        <div class="callout-warn">
          <strong>Dopplerův posuv &amp; Útlum volného prostoru (FSPL):</strong><br/>
          • <strong>Dopplerův jev:</strong> Způsoben radiální složkou rychlosti (přibližování zvyšuje f, vzdalování snižuje f). U <strong>GEO</strong> je téměř nulový, u rychlého <strong>LEO</strong> dosahuje desítek až stovek kHz (nutná kompenzace).<br/>
          • <strong>FSPL:</strong> Roste se čtvercem vzdálenosti <strong>d²</strong> a čtvercem frekvence <strong>f²</strong>. Na 2 GHz je rozdíl LEO (550 km) vs. GEO kolem <strong>36 dB</strong> (~4 200×). Vyšší frekvence však umožňují větší anténní zisk při stejných rozměrech a širší pásmo (za cenu citlivosti na déšť).
        </div>
      `,
      "sat-5": `
        <div class="q-heading">5. Satelitní konstelace (Walker) &amp; Laserové ISL</div>
        <div class="figure-frame">
          <div class="figure-caption">Obr. 18 ze skript: Přímá komunikace přes mezidružicový spoj (ISL)</div>
          <div class="figure-pad"><img src="assets/obr18_isl.png" alt="Mezidružicový spoj ISL" /></div>
        </div>
        <div class="note-block">
          <strong>Architektury Walker &amp; Spolehlivost:</strong>
          <ul>
            <li><strong>Pravděpodobnost funkčnosti z N nezávislých družic:</strong> P = 1 − (1 − p)ᴺ (pro 5 družic s p = 0,9 vychází 99,999 %).</li>
            <li><strong>Walker Delta (i : T / P / F):</strong> orbitální roviny po <strong>360°</strong> (např. Galileo 56°:24/6/1 → 6 rovin po 4 družicích, rozestup 60°).</li>
            <li><strong>Walker Star:</strong> téměř polární dráhy rozložené v rozsahu <strong>180°</strong> → pokrývá i póly (např. <strong>Iridium</strong>: 66 družic v 6 rovinách, 780 km).</li>
          </ul>
        </div>
        <div class="callout-warn">
          <strong>Laserové ISL (λ = 1 550 nm) &amp; Bezpečnostní chyták:</strong><br/>
          • Přímé propojení družice ↔ družice bez mezilehlých pozemních bran (jednotky až desítky Gb/s, žádné vzájemné rušení, ale extrémní nároky na přesné míření a stabilizaci).<br/>
          • <strong>CHYTÁK:</strong> Úzký laserový svazek ztěžuje odposlech, ale <strong>sám o sobě nezaručuje kryptografickou bezpečnost</strong> – data je nutné šifrovat!<br/>
          • Moderní LEO konstelace se standardizují v 3GPP jako nepozemní sítě <strong>5G / 6G NTN</strong>.
        </div>
      `,
      "sat-6": `
        <div class="q-heading">6. Kosmický segment, Transpondéry a Kmitočtová pásma (GiTySAT)</div>
        <div class="figure-frame">
          <div class="figure-caption">Přehled satelitních kmitočtových pásem (C band až E band) z prezentace GiTySAT</div>
          <svg viewBox="0 0 760 190">
            <rect x="10" y="18" width="740" height="44" rx="10" fill="var(--bg-subtle)" stroke="var(--border-strong)"/>
            <rect x="18" y="26" width="84" height="28" rx="6" fill="#0284c7"/>
            <text x="60" y="44" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">C (4–8)</text>

            <rect x="108" y="26" width="84" height="28" rx="6" fill="#0d9488"/>
            <text x="150" y="44" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">X (8–12)</text>

            <rect x="198" y="26" width="96" height="28" rx="6" fill="#059669"/>
            <text x="246" y="44" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">Ku (11–18)</text>

            <rect x="300" y="26" width="110" height="28" rx="6" fill="#d97706"/>
            <text x="355" y="44" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">K (18–27)</text>

            <rect x="416" y="26" width="110" height="28" rx="6" fill="#2563eb"/>
            <text x="471" y="44" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">Ka (27–40)</text>

            <rect x="532" y="26" width="100" height="28" rx="6" fill="#7c3aed"/>
            <text x="582" y="44" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">V (40–75)</text>

            <rect x="638" y="26" width="104" height="28" rx="6" fill="#db2777"/>
            <text x="690" y="44" fill="#fff" font-size="11.5" font-weight="bold" text-anchor="middle">E (60–90 GHz)</text>

            <line x1="355" y1="54" x2="355" y2="86" stroke="var(--accent-warm)" stroke-width="2" stroke-dasharray="3 3"/>
            <rect x="200" y="86" width="310" height="40" rx="9" fill="var(--accent-warm-soft)" stroke="var(--accent-warm)"/>
            <text x="355" y="103" fill="var(--accent-warm)" font-size="11.5" font-weight="bold" text-anchor="middle">CHYTÁK: Útlum vodní párou při 22,23 GHz!</text>
            <text x="355" y="119" fill="var(--text-secondary)" font-size="10.5" text-anchor="middle">K band (18–27 GHz) má rezonanční absorpci atmosféry</text>

            <text x="60" y="160" fill="var(--text-secondary)" font-size="10.5" text-anchor="middle">Odolné dešti</text>
            <text x="150" y="160" fill="var(--text-secondary)" font-size="10.5" text-anchor="middle">Armáda / Radary</text>
            <text x="246" y="160" fill="var(--text-secondary)" font-size="10.5" text-anchor="middle">TV / VSAT / OneWeb</text>
            <text x="471" y="160" fill="var(--text-secondary)" font-size="10.5" text-anchor="middle">HTS / O3b / 5G</text>
            <text x="636" y="160" fill="var(--text-secondary)" font-size="10.5" text-anchor="middle">Experimentální / GW</text>
          </svg>
        </div>
        <div class="note-block">
          <strong>Typ družice &amp; Druhy transpondérů:</strong>
          <ul>
            <li><strong>Standardní družice</strong> (široký svazek) vs. <strong>HTS (High Throughput Satellite)</strong> – mnoho úzkých spot-beamů + opakované využití frekvencí = mnohonásobná kapacita.</li>
            <li><strong>Bend pipe:</strong> transparentní zesílení a posun frekvence (bez zpracování dat).</li>
            <li><strong>Cross type:</strong> křížové propojení mezi svazky/pásmy.</li>
            <li><strong>On-board switching:</strong> přepínání a směrování přímo na palubě družice.</li>
          </ul>
        </div>
      `,
      "sat-7": `
        <div class="q-heading">7. GEO sítě, Topologie a Služby GiTySAT</div>
        <div class="callout-tip">
          <strong>Společnost GiTy, a.s.:</strong> Vlastní satelitní teleport (HUB) v ČR, vlastní pozemní <strong>MPLS síť (G-Net)</strong> v ČR a SR, nepřetržité dohledové centrum 24/7/365 s garancí SLA a bezpečnostní <strong>certifikace NBÚ – Tajné</strong>.
        </div>
        <div class="figure-frame">
          <div class="figure-caption">4 topologické typy GEO satelitních sítí z prezentace GiTySAT</div>
          <svg viewBox="0 0 760 155">
            <rect x="10" y="12" width="175" height="130" rx="12" fill="var(--accent-primary-soft)" stroke="var(--border-strong)"/>
            <text x="97" y="34" fill="var(--accent-primary)" font-size="12" font-weight="bold" text-anchor="middle">1. Broadcast</text>
            <text x="97" y="56" fill="var(--text-secondary)" font-size="11" text-anchor="middle">Jednosměrná distribuce</text>
            <text x="97" y="74" fill="var(--text-secondary)" font-size="11" text-anchor="middle">dat k mnoha stanicím</text>
            <text x="97" y="112" fill="var(--text-main)" font-size="11" font-weight="bold" text-anchor="middle">HUB → SAT → N×RX</text>

            <rect x="198" y="12" width="175" height="130" rx="12" fill="var(--accent-green-soft)" stroke="var(--border-strong)"/>
            <text x="285" y="34" fill="var(--accent-green)" font-size="12" font-weight="bold" text-anchor="middle">2. Bod – Bod</text>
            <text x="285" y="56" fill="var(--text-secondary)" font-size="11" text-anchor="middle">Technologie SCPC</text>
            <text x="285" y="74" fill="var(--text-secondary)" font-size="11" text-anchor="middle">(vyhrazená nosná)</text>
            <text x="285" y="112" fill="var(--text-main)" font-size="11" font-weight="bold" text-anchor="middle">Modemy / IP routery</text>

            <rect x="386" y="12" width="175" height="130" rx="12" fill="var(--accent-warm-soft)" stroke="var(--border-strong)"/>
            <text x="473" y="34" fill="var(--accent-warm)" font-size="12" font-weight="bold" text-anchor="middle">3. Hvězdice (Star)</text>
            <text x="473" y="56" fill="var(--text-secondary)" font-size="11" text-anchor="middle">1× VSAT HUB, n× terminál</text>
            <text x="473" y="74" fill="var(--text-secondary)" font-size="11" text-anchor="middle">Asymetrický kanál</text>
            <text x="473" y="112" fill="var(--text-main)" font-size="11" font-weight="bold" text-anchor="middle">TDMA / FDMA</text>

            <rect x="574" y="12" width="175" height="130" rx="12" fill="var(--accent-purple-soft)" stroke="var(--border-strong)"/>
            <text x="661" y="34" fill="var(--accent-purple)" font-size="12" font-weight="bold" text-anchor="middle">4. MESH</text>
            <text x="661" y="56" fill="var(--text-secondary)" font-size="11" text-anchor="middle">Přímé spojení terminálů</text>
            <text x="661" y="74" fill="var(--text-secondary)" font-size="11" text-anchor="middle">jedním skokem</text>
            <text x="661" y="112" fill="var(--text-main)" font-size="11" font-weight="bold" text-anchor="middle">Bez 2× průchodu HUB</text>
          </svg>
        </div>
        <table class="clean-table">
          <thead><tr><th>Vlastnost</th><th>Internetová konfigurace</th><th>Privátní satelitní síť</th></tr></thead>
          <tbody>
            <tr><td><strong>Rozsah &amp; účel</strong></td><td>Velké množství terminálů, přístup do Internetu</td><td>Malé specifické sítě (pobočky ↔ centrála do MPLS)</td></tr>
            <tr><td><strong>Parametry</strong></td><td>Unifikované služby, FUP a agregace</td><td>Individuální služby, garantované QoS, přídavné šifrování</td></tr>
            <tr><td><strong>Dohled</strong></td><td>Omezené možnosti dohledu</td><td>Plný End-to-End dohled (SNMP) &amp; integrace služeb</td></tr>
          </tbody>
        </table>
      `,
      "sat-8": `
        <div class="q-heading">8. Moderní konstelace: O3b, OneWeb, Starlink, Amazon LEO, Telesat</div>
        <table class="clean-table">
          <thead><tr><th>Systém</th><th>Dráha &amp; Výška</th><th>RTT Latence</th><th>Pásma &amp; Klíčové parametry</th></tr></thead>
          <tbody>
            <tr><td><strong>SES O3b / mPOWER</strong></td><td>MEO (~8 000 km)<br/>20 / 13 družic</td><td>~150 ms</td><td>Ka-band, pokrytí ±50° šířky (ne póly), až 1,6 Gbps/beam</td></tr>
            <tr><td><strong>Eutelsat OneWeb</strong></td><td>LEO (~1 200 km)<br/>652 družic</td><td>~100 ms</td><td>Ka (GW) + Ku (terminál), &gt;40 GW, firemní MIR (150/30) i garantované <strong>CIR (40/8 Mbps)</strong></td></tr>
            <tr><td><strong>SpaceX Starlink</strong></td><td>LEO (550 km typ.)<br/>&gt;9 800 družic</td><td>25–50 ms</td><td>Ku/Ka/E-band + <strong>lasery ISL</strong>, 13km beamy; Mini/Standard/Enterprise/Performance</td></tr>
            <tr><td><strong>Amazon LEO</strong></td><td>LEO (590–630 km)<br/>plán 3 232 družic</td><td>nízká (LEO)</td><td>Ka uplink / K downlink + lasery, Nano/Pro/Ultra až 1 Gbps (start 2026/2Q 2027)</td></tr>
            <tr><td><strong>Telesat Lightspeed</strong></td><td>LEO (1 015 / 1 325 km)<br/>198 družic vč. pólů</td><td>nízká (LEO)</td><td>Ka-band + lasery, B2B/L2/letectví až 3 Gbps (start 2028)</td></tr>
          </tbody>
        </table>
        <div class="callout-tip">
          <strong>Technická vs. Komerční dostupnost (OneWeb):</strong> Technická dostupnost znamená, že oblast pokrývá signál z oběžné dráhy; komerční dostupnost navíc vyžaduje regulatorní/licenční povolení v daném státě.
        </div>
      `,
      "sat-9": `
        <div class="q-heading">9. Terminály, Zabezpečení (TRANSEC, CSIR), DVB-S2X ACM a Hybridní sítě</div>
        <div class="note-block">
          <strong>GEO terminál (ST Engineering / iDirect) &amp; Zabezpečení GiTySAT:</strong>
          <ul>
            <li><strong>Venkovní část:</strong> Anténa (fixní parabola 0,7–2,4 m, <em>Drive Away</em> na auto, <em>Quick Deploy</em>, přenosný <em>Manpack</em>) + RF jednotka (Ku, X, Ka nebo C).</li>
            <li><strong>Vnitřní část:</strong> VSAT terminál / modem (iDirect 950mp, 9530, Newtec MDM3315).</li>
            <li><strong>Bezpečnost:</strong> <strong>iDirect TRANSEC</strong> (skrytá aktivita kanálu, <strong>AES-256 na L2</strong>, certifikát <strong>X.509</strong>), <strong>Spread spectrum</strong>, <strong>FIPS 140-2 Level 3</strong> (kryptomoduly), <strong>CSIR</strong> (anti-jamming a potlačení rušení).</li>
            <li><strong>Trendy – DVB-S2X &amp; ACM:</strong> <em>Adaptive Coding and Modulation</em> dynamicky mění modulaci podle deště (Rx QPSK až <strong>256APSK</strong>, Tx BPSK až <strong>16QAM</strong>), aby spoj nespadl.</li>
          </ul>
        </div>
        <div class="figure-frame">
          <div class="figure-caption">Architektura hybridní sítě GiTySAT (GEO + LEO + Internet – Slide 25)</div>
          <svg viewBox="0 0 760 175">
            <rect x="14" y="45" width="125" height="85" rx="12" fill="var(--accent-primary-soft)" stroke="var(--accent-primary)"/>
            <text x="76" y="84" fill="var(--text-main)" font-size="13" font-weight="bold" text-anchor="middle">Pobočka</text>
            <text x="76" y="103" fill="var(--text-secondary)" font-size="10.5" text-anchor="middle">VSAT + LEO + FW</text>

            <rect x="615" y="45" width="130" height="85" rx="12" fill="var(--accent-green-soft)" stroke="var(--accent-green)"/>
            <text x="680" y="84" fill="var(--text-main)" font-size="13" font-weight="bold" text-anchor="middle">Centrála</text>
            <text x="680" y="103" fill="var(--text-secondary)" font-size="10.5" text-anchor="middle">MPLS G-Net</text>

            <!-- Red Critical GEO path -->
            <path d="M139 60 Q375 8 615 60" fill="none" stroke="var(--accent-rose)" stroke-width="3"/>
            <rect x="265" y="16" width="225" height="24" rx="6" fill="var(--bg-subtle)" stroke="var(--accent-rose)"/>
            <text x="377" y="32" fill="var(--accent-rose)" font-size="11" font-weight="bold" text-anchor="middle">Kritický provoz → GEO VSAT (HUB)</text>

            <!-- Blue Standard LEO path -->
            <line x1="139" y1="88" x2="615" y2="88" stroke="var(--accent-primary)" stroke-width="3"/>
            <rect x="255" y="75" width="245" height="24" rx="6" fill="var(--bg-subtle)" stroke="var(--accent-primary)"/>
            <text x="377" y="91" fill="var(--accent-primary)" font-size="11" font-weight="bold" text-anchor="middle">Standardní provoz → LEO + NNI do MPLS</text>

            <!-- Green Non-critical Internet path -->
            <path d="M139 116 Q375 166 560 135" fill="none" stroke="var(--accent-green)" stroke-width="2.5" stroke-dasharray="5 3"/>
            <rect x="250" y="132" width="255" height="24" rx="6" fill="var(--bg-subtle)" stroke="var(--accent-green)"/>
            <text x="377" y="148" fill="var(--accent-green)" font-size="11" font-weight="bold" text-anchor="middle">Nekritický provoz → Firewall → Internet</text>
          </svg>
        </div>
      `
    };

    const audio = document.getElementById("podcast-audio");
    const seekSlider = document.getElementById("seek-slider");
    const timeCurrent = document.getElementById("time-current");
    const timeTotal = document.getElementById("time-total");
    const playLabel = document.getElementById("play-label");
    const chapterListEl = document.getElementById("chapter-list");
    const transcriptEl = document.getElementById("transcript-container");
    const diagramPanel = document.getElementById("diagram-panel");
    const activeQBadge = document.getElementById("active-q-badge");
    const nowPlayingSpeaker = document.getElementById("now-playing-speaker");
    const nowPlayingChapter = document.getElementById("now-playing-chapter");
    const autoscrollToggle = document.getElementById("autoscroll-toggle");
    const downloadLink = document.getElementById("download-link");
    const playerPill = document.getElementById("player-pill");
    const playIcon = document.getElementById("play-icon");
    const seekMarkersEl = document.getElementById("seek-markers");

    let currentSegmentIndex = -1;
    let currentQuestionId = "";

    /* =========================================================================
       MODE SWITCHING
       ========================================================================= */
    function setAppMode(mode) {
      appMode = mode;
      document.body.dataset.mode = mode;
      const isPodcast = mode === "podcast";
      document.getElementById("tab-btn-podcast").classList.toggle("active", mode === "podcast");
      document.getElementById("tab-btn-quiz").classList.toggle("active", mode === "quiz");
      document.getElementById("tab-btn-matrix").classList.toggle("active", mode === "matrix");

      document.getElementById("podcast-workspace").style.display = isPodcast ? "grid" : "none";
      document.getElementById("quiz-workspace").style.display = isPodcast ? "none" : "flex";
      document.getElementById("quiz-topic-bar").style.display = isPodcast ? "none" : "flex";

      if (mode === "matrix") {
        quizViewMode = "matrix";
      } else if (mode === "quiz" && quizViewMode === "matrix") {
        quizViewMode = "single";
      }

      document.getElementById("qview-single").classList.toggle("active", quizViewMode === "single");
      document.getElementById("qview-list").classList.toggle("active", quizViewMode === "list");
      document.getElementById("qview-matrix").classList.toggle("active", quizViewMode === "matrix");

      if (!isPodcast) {
        renderQuizTopicBar();
        renderQuizDashboardAndCards();
      }
    }

    function openQuizForCurrentTopic() {
      const targetTopic = (currentQuestionId && currentQuestionId !== "intro" && currentQuestionId !== "all")
        ? currentQuestionId
        : "all";
      quizFilterTopic = targetTopic;
      onlyMistakesMode = false;
      onlyUnansweredMode = false;
      currentSingleIndex = 0;
      quizViewMode = "single";
      rebuildActiveQuestionList();
      setAppMode("quiz");
      window.scrollTo({ top: 0, behavior: "smooth" });
    }

    function openPodcastStudyForTopic(topicId) {
      setAppMode("podcast");
      updateDiagram(topicId);
      window.scrollTo({ top: 0, behavior: "smooth" });
    }

    function toggleTheme() {
      const root = document.documentElement;
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      const sunSvg = '<svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2"/><path d="M12 20v2"/><path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/><path d="M2 12h2"/><path d="M20 12h2"/><path d="m6.34 17.66-1.41 1.41"/><path d="m19.07 4.93-1.41 1.41"/></svg>';
      const moonSvg = '<svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>';
      document.getElementById("theme-btn").innerHTML = next === "dark"
        ? `${sunSvg}<span>Světlý režim</span>`
        : `${moonSvg}<span>Tmavý režim</span>`;
    }

    function formatTime(sec) {
      const m = Math.floor(sec / 60);
      const s = Math.floor(sec % 60);
      return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    }

    function formatText(text) {
      return text
        .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
        .replace(/\\n/g, '<br/>');
    }

    function renderUIForTrack() {
      chapterListEl.innerHTML = "";
      transcriptEl.innerHTML = "";

      const chapterStartMap = {};
      currentTrack.segments.forEach(seg => {
        if (!(seg.question_id in chapterStartMap)) {
          chapterStartMap[seg.question_id] = seg.start;
        }
      });

      CHAPTERS.forEach(ch => {
        const startSec = chapterStartMap[ch.id] || 0;
        const btn = document.createElement("button");
        btn.id = `chap-btn-${ch.id}`;
        btn.className = "rail-item" + (ch.id === currentQuestionId ? " active" : "");
        btn.onclick = () => {
          updateDiagram(ch.id);
          audio.currentTime = startSec + 0.05;
          audio.play();
        };
        btn.innerHTML = `
          <span>${ch.title}</span>
          <span class="rail-time">${formatTime(startSec)}</span>
        `;
        chapterListEl.appendChild(btn);
      });

      currentTrack.segments.forEach((seg, idx) => {
        const div = document.createElement("div");
        div.id = `seg-${idx}`;
        const isMarek = seg.speaker === "Marek";
        div.className = "dialogue-item";
        div.onclick = () => {
          audio.currentTime = seg.start + 0.05;
          audio.play();
        };
        const chObj = CHAPTERS.find(c => c.id === seg.question_id);
        div.innerHTML = `
          <div class="dialogue-meta">
            <span class="speaker-badge ${isMarek ? 'speaker-marek' : 'speaker-tereza'}">
              <span class="speaker-dot"></span>
              <span>${seg.speaker}</span>
              <span class="eq-bars" aria-hidden="true"><span></span><span></span><span></span></span>
              <span style="font-weight:500; color:var(--text-muted); font-size:11px;">${chObj ? chObj.badge : ''}</span>
            </span>
            <span class="dialogue-timestamp">${formatTime(seg.start)}</span>
          </div>
          <div class="dialogue-body">${formatText(seg.display)}</div>
        `;
        transcriptEl.appendChild(div);
      });

      seekSlider.max = currentTrack.total_duration;
      timeTotal.textContent = formatTime(currentTrack.total_duration);

      if (seekMarkersEl && currentTrack.total_duration > 0) {
        seekMarkersEl.innerHTML = "";
        CHAPTERS.forEach(ch => {
          const startSec = chapterStartMap[ch.id];
          if (typeof startSec === "number" && startSec > 1 && startSec < currentTrack.total_duration) {
            const tick = document.createElement("span");
            tick.className = "seek-tick";
            tick.style.left = `${(startSec / currentTrack.total_duration) * 100}%`;
            tick.title = `${ch.title} (${formatTime(startSec)})`;
            seekMarkersEl.appendChild(tick);
          }
        });
      }
    }

    function switchEngine(engineKey) {
      if (!RAW_DATA.tracks || !RAW_DATA.tracks[engineKey]) return;
      const wasPlaying = !audio.paused;
      const savedSegIdx = currentSegmentIndex >= 0 ? currentSegmentIndex : 0;

      activeEngine = engineKey;
      currentTrack = RAW_DATA.tracks[engineKey];

      document.getElementById("eng-eleven").classList.toggle("active", engineKey === "eleven_hd");
      document.getElementById("eng-cz").classList.toggle("active", engineKey === "cz_studio");

      audio.src = currentTrack.filename;
      downloadLink.href = currentTrack.filename;
      currentSegmentIndex = -1;
      renderUIForTrack();

      const targetSeg = currentTrack.segments[savedSegIdx] || currentTrack.segments[0];
      audio.currentTime = targetSeg ? targetSeg.start : 0;
      if (wasPlaying) audio.play();
    }

    function updateDiagram(qId) {
      if (qId === currentQuestionId) return;
      currentQuestionId = qId;
      const chObj = CHAPTERS.find(c => c.id === qId);
      if (chObj) {
        activeQBadge.textContent = `${chObj.title} – Vizuální tahák`;
      }
      diagramPanel.innerHTML = DIAGRAMS[qId] || DIAGRAMS["intro"];

      CHAPTERS.forEach(ch => {
        const el = document.getElementById(`chap-btn-${ch.id}`);
        if (el) el.classList.toggle("active", ch.id === qId);
      });
    }

    function showAllDiagrams() {
      currentQuestionId = "all";
      activeQBadge.textContent = "Kompletní tahák všech 9 kapitol";
      diagramPanel.innerHTML = ["sat-1","sat-2","sat-3","sat-4","sat-5","sat-6","sat-7","sat-8","sat-9"]
        .map(k => `<div style="padding-bottom:22px; border-bottom:1px solid var(--border-color); margin-bottom:14px; display:flex; flex-direction:column; gap:14px;">${DIAGRAMS[k]}</div>`)
        .join("");
    }

    /* =========================================================================
       GOOGLE KEEP MODAL
       ========================================================================= */
    let activeKeepTab = "full";
    function openKeepModal() {
      document.getElementById("keep-modal").classList.add("open");
      switchKeepTab(activeKeepTab);
    }
    function closeKeepModal() {
      document.getElementById("keep-modal").classList.remove("open");
    }
    function switchKeepTab(tab) {
      activeKeepTab = tab;
      document.getElementById("keep-tab-full").classList.toggle("active", tab === "full");
      document.getElementById("keep-tab-pocket").classList.toggle("active", tab === "pocket");
      document.getElementById("keep-preview-box").textContent = KEEP_DATA[tab] || "";
    }
    function copyKeepText() {
      const txt = KEEP_DATA[activeKeepTab] || "";
      const lbl = document.getElementById("keep-copy-label");
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(txt).then(() => {
          lbl.textContent = "Zkopírováno do schránky!";
          setTimeout(() => { lbl.textContent = "Kopírovat do schránky"; }, 2000);
        });
      } else {
        const ta = document.createElement("textarea");
        ta.value = txt;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand("copy");
        document.body.removeChild(ta);
        lbl.textContent = "Zkopírováno do schránky!";
        setTimeout(() => { lbl.textContent = "Kopírovat do schránky"; }, 2000);
      }
    }

    /* =========================================================================
       99-QUESTION ABCD QUIZ + PROBABILITY & UNCERTAINTY CALCULATOR
       ========================================================================= */
    let quizFilterTopic = "all";
    let quizViewMode = "single";
    let onlyMistakesMode = false;
    let onlyUnansweredMode = false;
    let currentSingleIndex = 0;
    let currentStreak = 0;

    let quizState = {};
    let activeQuestionList = [];

    function createShuffledOptions(qObj) {
      const items = qObj.options.map((text, idx) => ({
        text: text,
        isCorrect: idx === qObj.ans
      }));
      for (let i = items.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const tmp = items[i];
        items[i] = items[j];
        items[j] = tmp;
      }
      return items;
    }

    function initQuizData() {
      RAW_QUIZ.forEach(q => {
        quizState[q.id] = {
          answered: false,
          chosenIndex: -1,
          isCorrect: false,
          shuffledOptions: createShuffledOptions(q)
        };
      });

      try {
        const saved = localStorage.getItem("satelity_quiz_v1");
        if (saved) {
          const parsed = JSON.parse(saved);
          if (parsed && parsed.answers) {
            Object.keys(parsed.answers).forEach(idStr => {
              const qId = parseInt(idStr, 10);
              if (quizState[qId] && parsed.answers[idStr].shuffledOptions) {
                quizState[qId] = parsed.answers[idStr];
              }
            });
          }
          if (typeof parsed.streak === "number") {
            currentStreak = parsed.streak;
          }
        }
      } catch (e) {}

      rebuildActiveQuestionList();
      updateHeaderQuizBadge();
    }

    function saveQuizToStorage() {
      try {
        const answeredOnly = {};
        Object.keys(quizState).forEach(k => {
          if (quizState[k].answered) answeredOnly[k] = quizState[k];
        });
        localStorage.setItem("satelity_quiz_v1", JSON.stringify({
          answers: answeredOnly,
          streak: currentStreak
        }));
      } catch (e) {}
    }

    function rebuildActiveQuestionList() {
      let pool = RAW_QUIZ.slice();
      if (quizFilterTopic !== "all") {
        pool = pool.filter(q => q.topic === quizFilterTopic);
      }
      if (onlyMistakesMode) {
        pool = pool.filter(q => quizState[q.id] && quizState[q.id].answered && !quizState[q.id].isCorrect);
      } else if (onlyUnansweredMode) {
        pool = pool.filter(q => quizState[q.id] && !quizState[q.id].answered);
      }
      activeQuestionList = pool;
      if (currentSingleIndex >= activeQuestionList.length) currentSingleIndex = 0;
    }

    function selectQuizTopic(topicId) {
      quizFilterTopic = topicId;
      onlyMistakesMode = false;
      onlyUnansweredMode = false;
      currentSingleIndex = 0;
      rebuildActiveQuestionList();
      const firstUnanswered = activeQuestionList.findIndex(q => !quizState[q.id].answered);
      if (firstUnanswered !== -1) currentSingleIndex = firstUnanswered;
      renderQuizTopicBar();
      renderQuizDashboardAndCards();
    }

    function jumpToSpecificSubQuestion(topicId, qId) {
      quizFilterTopic = topicId;
      onlyMistakesMode = false;
      onlyUnansweredMode = false;
      quizViewMode = "single";
      appMode = "quiz";
      document.getElementById("tab-btn-podcast").classList.remove("active");
      document.getElementById("tab-btn-quiz").classList.add("active");
      document.getElementById("tab-btn-matrix").classList.remove("active");
      document.getElementById("qview-single").classList.add("active");
      document.getElementById("qview-list").classList.remove("active");
      document.getElementById("qview-matrix").classList.remove("active");

      rebuildActiveQuestionList();
      const idx = activeQuestionList.findIndex(q => q.id === qId);
      currentSingleIndex = idx !== -1 ? idx : 0;
      renderQuizTopicBar();
      renderQuizDashboardAndCards();
      window.scrollTo({ top: 0, behavior: "smooth" });
    }

    function setQuizViewMode(mode) {
      quizViewMode = mode;
      appMode = mode === "matrix" ? "matrix" : "quiz";
      document.getElementById("tab-btn-podcast").classList.remove("active");
      document.getElementById("tab-btn-quiz").classList.toggle("active", mode !== "matrix");
      document.getElementById("tab-btn-matrix").classList.toggle("active", mode === "matrix");

      document.getElementById("qview-single").classList.toggle("active", mode === "single");
      document.getElementById("qview-list").classList.toggle("active", mode === "list");
      document.getElementById("qview-matrix").classList.toggle("active", mode === "matrix");
      renderQuizDashboardAndCards();
    }

    function filterOnlyMistakes() {
      onlyMistakesMode = !onlyMistakesMode;
      if (onlyMistakesMode) {
        onlyUnansweredMode = false;
        if (quizViewMode === "matrix") setQuizViewMode("single");
      }
      currentSingleIndex = 0;
      rebuildActiveQuestionList();
      renderQuizTopicBar();
      renderQuizDashboardAndCards();
    }

    function filterOnlyUnanswered() {
      onlyUnansweredMode = !onlyUnansweredMode;
      if (onlyUnansweredMode) {
        onlyMistakesMode = false;
        if (quizViewMode === "matrix") setQuizViewMode("single");
      }
      currentSingleIndex = 0;
      rebuildActiveQuestionList();
      renderQuizTopicBar();
      renderQuizDashboardAndCards();
    }

    function shuffleActiveQuiz() {
      RAW_QUIZ.forEach(q => {
        if (!quizState[q.id].answered) quizState[q.id].shuffledOptions = createShuffledOptions(q);
      });
      for (let i = activeQuestionList.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const tmp = activeQuestionList[i];
        activeQuestionList[i] = activeQuestionList[j];
        activeQuestionList[j] = tmp;
      }
      currentSingleIndex = 0;
      renderQuizDashboardAndCards();
    }

    function resetQuizStats() {
      currentStreak = 0;
      onlyMistakesMode = false;
      onlyUnansweredMode = false;
      RAW_QUIZ.forEach(q => {
        quizState[q.id] = {
          answered: false,
          chosenIndex: -1,
          isCorrect: false,
          shuffledOptions: createShuffledOptions(q)
        };
      });
      try { localStorage.removeItem("satelity_quiz_v1"); } catch (e) {}
      currentSingleIndex = 0;
      rebuildActiveQuestionList();
      updateHeaderQuizBadge();
      renderQuizTopicBar();
      renderQuizDashboardAndCards();
    }

    function getTopicStats(topicId) {
      const subset = topicId === "all" ? RAW_QUIZ : RAW_QUIZ.filter(q => q.topic === topicId);
      const total = subset.length;
      let answered = 0;
      let correct = 0;
      let wrong = 0;
      subset.forEach(q => {
        const st = quizState[q.id];
        if (st && st.answered) {
          answered++;
          if (st.isCorrect) correct++;
          else wrong++;
        }
      });
      const unanswered = total - answered;
      const confirmedChancePct = total > 0 ? Math.round((correct / total) * 100) : 0;
      const uncertaintyPct = total > 0 ? Math.round((unanswered / total) * 100) : 0;
      const wrongPct = total > 0 ? Math.round((wrong / total) * 100) : 0;
      const expectedChancePct = total > 0 ? Math.round(((correct + 0.25 * unanswered) / total) * 100) : 0;
      const maxPotentialPct = total > 0 ? Math.round(((correct + unanswered) / total) * 100) : 0;

      return {
        total, answered, unanswered, correct, wrong,
        confirmedChancePct, uncertaintyPct, wrongPct, expectedChancePct, maxPotentialPct,
        subset
      };
    }

    function updateHeaderQuizBadge() {
      const allSt = getTopicStats("all");
      document.getElementById("header-quiz-badge").textContent = `Šance ${allSt.confirmedChancePct} %`;
      document.getElementById("header-uncertainty-badge").textContent = `Nejistota ${allSt.uncertaintyPct} %`;
    }

    function renderQuizTopicBar() {
      const bar = document.getElementById("quiz-topic-bar");
      bar.innerHTML = "";
      QUIZ_TOPICS.forEach(tp => {
        const st = getTopicStats(tp.id);
        const btn = document.createElement("button");
        const isActive = (quizFilterTopic === tp.id && !onlyMistakesMode && !onlyUnansweredMode);
        btn.className = "topic-pill" + (isActive ? " active" : "");
        btn.onclick = () => selectQuizTopic(tp.id);
        btn.innerHTML = `
          <span>${tp.title}</span>
          <span class="pill-time">${st.confirmedChancePct}% (±${st.uncertaintyPct}%)</span>
        `;
        bar.appendChild(btn);
      });
    }

    function answerQuestion(qId, optIdx) {
      const st = quizState[qId];
      if (!st || st.answered) return;
      const chosen = st.shuffledOptions[optIdx];
      st.answered = true;
      st.chosenIndex = optIdx;
      st.isCorrect = chosen.isCorrect;
      currentStreak = st.isCorrect ? currentStreak + 1 : 0;

      saveQuizToStorage();
      updateHeaderQuizBadge();
      renderQuizTopicBar();
      renderQuizDashboardAndCards();
    }

    function retrySingleQuestion(qId) {
      const qObj = RAW_QUIZ.find(q => q.id === qId);
      if (!qObj) return;
      quizState[qId] = {
        answered: false,
        chosenIndex: -1,
        isCorrect: false,
        shuffledOptions: createShuffledOptions(qObj)
      };
      saveQuizToStorage();
      updateHeaderQuizBadge();
      renderQuizTopicBar();
      renderQuizDashboardAndCards();
    }

    function buildExamQuestionProbabilityGridHTML() {
      const topicsToShow = quizFilterTopic === "all"
        ? QUIZ_TOPICS.filter(t => t.id !== "all")
        : QUIZ_TOPICS.filter(t => t.id === quizFilterTopic);

      const cardsHTML = topicsToShow.map(tp => {
        const st = getTopicStats(tp.id);
        const cWidth = st.total > 0 ? (st.correct / st.total) * 100 : 0;
        const uWidth = st.total > 0 ? (st.unanswered / st.total) * 100 : 0;
        const wWidth = st.total > 0 ? (st.wrong / st.total) * 100 : 0;

        let badgeColor = "var(--accent-primary)";
        let badgeBg = "var(--accent-primary-soft)";
        if (st.confirmedChancePct >= 75) {
          badgeColor = "var(--accent-green)";
          badgeBg = "var(--accent-green-soft)";
        } else if (st.confirmedChancePct >= 40) {
          badgeColor = "var(--accent-warm)";
          badgeBg = "var(--accent-warm-soft)";
        } else if (st.answered > 0) {
          badgeColor = "var(--accent-rose)";
          badgeBg = "var(--accent-rose-soft)";
        }

        const subChipsHTML = st.subset.map((qObj, idx) => {
          const qSt = quizState[qObj.id];
          let chipCls = "subq-chip st-unanswered";
          let icon = "?";
          if (qSt && qSt.answered) {
            chipCls = qSt.isCorrect ? "subq-chip st-correct" : "subq-chip st-wrong";
            icon = qSt.isCorrect ? "✓" : "✗";
          }
          const safeQ = qObj.q.replace(/"/g, "&quot;");
          return `
            <button class="${chipCls}" title="Podotázka #${qObj.id}: ${safeQ}" onclick="jumpToSpecificSubQuestion('${tp.id}', ${qObj.id})">
              <span>#${idx + 1}</span><span>${icon}</span>
            </button>
          `;
        }).join("");

        return `
          <div class="exam-q-card">
            <div class="exam-q-head">
              <div>
                <div class="exam-q-title">${tp.title}</div>
                <div class="exam-q-sub">${tp.desc}</div>
              </div>
              <div class="chance-badge-col">
                <div class="chance-pill-main" style="color:${badgeColor}; background:${badgeBg};">${st.confirmedChancePct} %</div>
                <div class="chance-pill-sub">Nejistota: ${st.uncertaintyPct} %</div>
              </div>
            </div>

            <div>
              <div style="display:flex; justify-content:space-between; font-size:11.5px; font-weight:700; color:var(--text-secondary); margin-bottom:5px;">
                <span>Odhad s nejistotou: <strong style="color:var(--accent-primary);">${st.expectedChancePct} %</strong></span>
                <span>Interval: ${st.confirmedChancePct} % – ${st.maxPotentialPct} %</span>
              </div>
              <div class="bar-track" style="height:9px;">
                <div class="bar-fill-correct" style="width:${cWidth}%;"></div>
                <div class="bar-fill-uncertainty" style="width:${uWidth}%;"></div>
                <div class="bar-fill-wrong" style="width:${wWidth}%;"></div>
              </div>
            </div>

            <div class="metrics-3col">
              <div>
                <div class="m3-val" style="color:var(--accent-green);">${st.correct} / ${st.total}</div>
                <div class="m3-lbl">Potvrzeno (${st.confirmedChancePct}%)</div>
              </div>
              <div>
                <div class="m3-val" style="color:var(--accent-warm);">${st.unanswered} / ${st.total}</div>
                <div class="m3-lbl">Nejistota (${st.uncertaintyPct}%)</div>
              </div>
              <div>
                <div class="m3-val" style="color:var(--accent-rose);">${st.wrong} / ${st.total}</div>
                <div class="m3-lbl">Chyby (${st.wrongPct}%)</div>
              </div>
            </div>

            <div>
              <div style="font-size:11px; font-weight:700; color:var(--text-muted); margin-bottom:6px;">
                Podotázky v okruhu (kliknutím skočíš na procvičení):
              </div>
              <div class="subq-chips-wrap">${subChipsHTML}</div>
            </div>

            <div class="exam-q-actions">
              <button class="action-btn" onclick="openPodcastStudyForTopic('${tp.id}')">
                <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                <span>Tahák &amp; Audio</span>
              </button>
              <button class="action-btn primary-soft" onclick="selectQuizTopic('${tp.id}'); setQuizViewMode('single');">
                <svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="6 4 20 12 6 20 6 4"/></svg>
                <span>Procvičit (${st.unanswered > 0 ? `zbývá ${st.unanswered}` : 'zopakovat'})</span>
              </button>
            </div>
          </div>
        `;
      }).join("");

      return `<div class="exam-prob-grid">${cardsHTML}</div>`;
    }

    function buildQuestionCardHTML(qObj, idxInList, totalInList) {
      const st = quizState[qObj.id];
      const topicStats = getTopicStats(qObj.topic);
      const letters = ["A", "B", "C", "D"];
      let cardStateClass = "";
      let qProbBadgeHTML = "";

      if (!st.answered) {
        qProbBadgeHTML = `<span class="q-prob-pill uncertain">Nejistota (tip 25 %)</span>`;
      } else if (st.isCorrect) {
        cardStateClass = "answered-correct";
        qProbBadgeHTML = `<span class="q-prob-pill certain-ok">Potvrzeno (100 %)</span>`;
      } else {
        cardStateClass = "answered-wrong";
        qProbBadgeHTML = `<span class="q-prob-pill certain-bad">Chyba (0 %)</span>`;
      }

      const optionsHTML = st.shuffledOptions.map((opt, oIdx) => {
        let btnClass = "option-btn";
        if (st.answered) {
          if (opt.isCorrect) btnClass += " correct-choice";
          else if (oIdx === st.chosenIndex && !opt.isCorrect) btnClass += " wrong-choice";
          else btnClass += " dimmed-choice";
        }
        const disabledAttr = st.answered ? "disabled" : "";
        const kbdHintHTML = (quizViewMode === "single" && !st.answered)
          ? `<kbd class="kbd-hint">${letters[oIdx]}</kbd>`
          : "";
        return `
          <button class="${btnClass}" ${disabledAttr} onclick="answerQuestion(${qObj.id}, ${oIdx})">
            <span class="opt-letter">${letters[oIdx]}</span>
            <span style="flex:1;">${opt.text}</span>
            ${kbdHintHTML}
          </button>
        `;
      }).join("");

      let explanationHTML = "";
      if (st.answered) {
        const statusTitle = st.isCorrect
          ? `Správně! Potvrzená šance tématu „${qObj.topic_label}“ je nyní ${topicStats.confirmedChancePct} % (nejistota ${topicStats.uncertaintyPct} %).`
          : `Chyba! Potvrzená šance tématu „${qObj.topic_label}“ je ${topicStats.confirmedChancePct} % (nejistota ${topicStats.uncertaintyPct} %).`;
        const expClass = st.isCorrect ? "explanation-box is-correct" : "explanation-box is-wrong";
        explanationHTML = `
          <div class="${expClass}">
            <div style="font-weight:700; margin-bottom:4px; color:${st.isCorrect ? 'var(--accent-green)' : 'var(--accent-rose)'};">${statusTitle}</div>
            <div><strong>Vysvětlení:</strong> ${qObj.exp}</div>
          </div>
        `;
      }

      const siblingChipsHTML = topicStats.subset.map((sibQ, sIdx) => {
        const sibSt = quizState[sibQ.id];
        let cls = "subq-chip st-unanswered";
        let sym = "?";
        if (sibSt && sibSt.answered) {
          cls = sibSt.isCorrect ? "subq-chip st-correct" : "subq-chip st-wrong";
          sym = sibSt.isCorrect ? "✓" : "✗";
        }
        const activeBorder = sibQ.id === qObj.id ? "outline: 2px solid var(--accent-primary); outline-offset: 1px;" : "";
        return `<button class="${cls}" style="${activeBorder}" onclick="jumpToSpecificSubQuestion('${qObj.topic}', ${sibQ.id})">#${sIdx + 1} ${sym}</button>`;
      }).join("");

      let navFooterHTML = "";
      const prevSvg = '<svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>';
      const nextSvg = '<svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>';
      const retrySvg = '<svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>';
      const chartSvg = '<svg class="svg-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/></svg>';
      if (quizViewMode === "single") {
        const prevDisabled = idxInList <= 0 ? "disabled style='opacity:0.45; cursor:default;'" : "";
        const isLast = idxInList >= totalInList - 1;
        const nextText = isLast ? "Zpět na 1. otázku" : "Další otázka";
        const nextIcon = isLast ? retrySvg : nextSvg;
        navFooterHTML = `
          <div class="quiz-nav-footer">
            <div style="display:flex; gap:8px; flex-wrap:wrap;">
              <button class="action-btn" ${prevDisabled} onclick="stepSingleQuestion(-1)">${prevSvg}<span>Předchozí</span></button>
              ${st.answered ? `<button class="action-btn" onclick="retrySingleQuestion(${qObj.id})">${retrySvg}<span>Zkusit znovu</span></button>` : ""}
              <button class="action-btn" onclick="setQuizViewMode('matrix')">${chartSvg}<span>Šance po tématech</span></button>
            </div>
            <button class="next-q-cta" onclick="stepSingleQuestion(1)">
              <span>${nextText}</span>
              ${nextIcon}
              <kbd class="kbd-hint">Enter</kbd>
            </button>
          </div>
        `;
      } else if (st.answered) {
        navFooterHTML = `
          <div style="display:flex; justify-content:flex-end;">
            <button class="action-btn" onclick="retrySingleQuestion(${qObj.id})">${retrySvg}<span>Zkusit znovu</span></button>
          </div>
        `;
      }

      return `
        <article class="quiz-card ${cardStateClass}" id="qcard-${qObj.id}">
          <div class="quiz-card-top">
            <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
              <span class="quiz-topic-tag">${qObj.topic_label}</span>
              <span style="font-size:12px; font-weight:700; color:var(--text-secondary);">
                Téma: <strong style="color:var(--accent-green);">${topicStats.confirmedChancePct} %</strong>
                <span style="color:var(--accent-warm);">(nejistota ${topicStats.uncertaintyPct} %)</span>
              </span>
            </div>
            <div class="quiz-num-tag">
              ${qProbBadgeHTML}
              <span>Otázka ${idxInList + 1} / ${totalInList}</span>
            </div>
          </div>

          <div class="quiz-question-text">${qObj.q}</div>
          <div class="options-grid">${optionsHTML}</div>
          ${explanationHTML}

          <div style="padding-top:6px; border-top:1px dashed var(--border-color); display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:8px;">
            <span style="font-size:11px; font-weight:700; color:var(--text-muted);">
              Podotázky tématu (${topicStats.correct}✓ / ${topicStats.unanswered}? / ${topicStats.wrong}✗):
            </span>
            <div class="subq-chips-wrap">${siblingChipsHTML}</div>
          </div>

          ${navFooterHTML}
        </article>
      `;
    }

    function stepSingleQuestion(delta) {
      if (activeQuestionList.length === 0) return;
      currentSingleIndex = (currentSingleIndex + delta + activeQuestionList.length) % activeQuestionList.length;
      renderQuizDashboardAndCards();
    }

    function renderQuizDashboardAndCards() {
      const scopeStats = getTopicStats(quizFilterTopic);
      const allStats = getTopicStats("all");
      const topicObj = QUIZ_TOPICS.find(t => t.id === quizFilterTopic) || QUIZ_TOPICS[0];

      document.getElementById("dashboard-scope-title").textContent =
        quizFilterTopic === "all"
          ? `Šance, že uděláš test – Všech ${scopeStats.total} otázek`
          : `Šance na téma: ${topicObj.title} (${scopeStats.total} podotázek)`;

      // Update SVG radial ring gauges (circumference = 2 * pi * 34 ≈ 213.6)
      const C = 213.6;
      const chanceRing = document.getElementById("gauge-chance-ring");
      const uncRing = document.getElementById("gauge-unc-ring");
      chanceRing.style.strokeDashoffset = C * (1 - scopeStats.confirmedChancePct / 100);
      uncRing.style.strokeDashoffset = C * (1 - scopeStats.uncertaintyPct / 100);

      document.getElementById("quiz-pct-val").textContent = `${scopeStats.confirmedChancePct} %`;
      document.getElementById("quiz-unc-val").textContent = `${scopeStats.uncertaintyPct} %`;

      document.getElementById("expected-chance-lbl").textContent = `${scopeStats.expectedChancePct} %`;
      document.getElementById("interval-chance-lbl").textContent = `${scopeStats.confirmedChancePct} % – ${scopeStats.maxPotentialPct} %`;

      document.getElementById("stat-correct").textContent = scopeStats.correct;
      document.getElementById("stat-unanswered").textContent = scopeStats.unanswered;
      document.getElementById("stat-wrong").textContent = scopeStats.wrong;
      document.getElementById("stat-streak").textContent = `${currentStreak}`;

      const correctWidth = scopeStats.total > 0 ? (scopeStats.correct / scopeStats.total) * 100 : 0;
      const uncertaintyWidth = scopeStats.total > 0 ? (scopeStats.unanswered / scopeStats.total) * 100 : 0;
      const wrongWidth = scopeStats.total > 0 ? (scopeStats.wrong / scopeStats.total) * 100 : 0;

      document.getElementById("bar-correct").style.width = `${correctWidth}%`;
      document.getElementById("bar-uncertainty").style.width = `${uncertaintyWidth}%`;
      document.getElementById("bar-wrong").style.width = `${wrongWidth}%`;

      document.getElementById("leg-ok-pct").textContent = `${scopeStats.confirmedChancePct}%`;
      document.getElementById("leg-unc-pct").textContent = `${scopeStats.uncertaintyPct}%`;
      document.getElementById("leg-bad-pct").textContent = `${scopeStats.wrongPct}%`;
      document.getElementById("bar-left-label").textContent =
        `Potvrzeno: ${scopeStats.confirmedChancePct} % • Nejistota: ${scopeStats.uncertaintyPct} % • Chyby: ${scopeStats.wrongPct} %`;

      const unansBtn = document.getElementById("btn-filter-unanswered");
      const unansLbl = document.getElementById("btn-filter-unanswered-lbl");
      if (scopeStats.unanswered > 0 || onlyUnansweredMode) {
        unansBtn.style.display = "inline-flex";
        unansLbl.textContent = onlyUnansweredMode
          ? "Zrušit filtr nejistoty"
          : `Procvičit jen nejistotu (${scopeStats.unanswered})`;
      } else {
        unansBtn.style.display = "none";
      }

      const mistakeBtn = document.getElementById("btn-filter-mistakes");
      const mistakeLbl = document.getElementById("btn-filter-mistakes-lbl");
      if (allStats.wrong > 0 || onlyMistakesMode) {
        mistakeBtn.style.display = "inline-flex";
        mistakeLbl.textContent = onlyMistakesMode
          ? "Zrušit filtr chyb"
          : `Procvičit jen chyby (${allStats.wrong})`;
      } else {
        mistakeBtn.style.display = "none";
      }

      const container = document.getElementById("quiz-cards-container");
      if (quizViewMode === "matrix") {
        container.innerHTML = buildExamQuestionProbabilityGridHTML();
        return;
      }

      if (activeQuestionList.length === 0) {
        container.innerHTML = `
          <div class="quiz-card" style="text-align:center; padding:38px 24px;">
            <div style="font-size:20px; font-weight:700; color:var(--accent-green);">V tomto filtru nezůstala žádná otázka!</div>
            <div style="color:var(--text-secondary); margin-top:6px;">Můžeš zkontrolovat celkový přehled šancí po tématech nebo zobrazit všech 99 otázek.</div>
            <div style="margin-top:14px; display:flex; gap:10px; justify-content:center; flex-wrap:wrap;">
              <button class="next-q-cta" onclick="setQuizViewMode('matrix')">Šance po tématech</button>
              <button class="action-btn" onclick="selectQuizTopic('all'); setQuizViewMode('single');">Všech 99 otázek</button>
            </div>
          </div>
        `;
        return;
      }

      if (quizViewMode === "single") {
        container.innerHTML = buildQuestionCardHTML(activeQuestionList[currentSingleIndex], currentSingleIndex, activeQuestionList.length);
      } else {
        container.innerHTML = activeQuestionList.map((qObj, idx) => buildQuestionCardHTML(qObj, idx, activeQuestionList.length)).join("");
      }
    }

    /* =========================================================================
       INIT & AUDIO / KEYBOARD LISTENERS
       ========================================================================= */
    renderUIForTrack();
    updateDiagram("sat-1");
    initQuizData();

    function togglePlay() {
      if (audio.paused) audio.play();
      else audio.pause();
    }

    function setPlayButtonState(isPlaying) {
      playLabel.textContent = isPlaying ? "Pozastavit" : "Přehrát";
      if (playerPill) playerPill.classList.toggle("is-playing", isPlaying);
      if (playIcon) {
        playIcon.innerHTML = isPlaying
          ? '<rect x="6" y="4" width="4" height="16" rx="1"/><rect x="14" y="4" width="4" height="16" rx="1"/>'
          : '<polygon points="6 4 20 12 6 20 6 4"/>';
      }
    }

    audio.addEventListener("play", () => setPlayButtonState(true));
    audio.addEventListener("pause", () => setPlayButtonState(false));
    audio.addEventListener("ended", () => setPlayButtonState(false));

    audio.addEventListener("timeupdate", () => {
      const t = audio.currentTime;
      seekSlider.value = t;
      timeCurrent.textContent = formatTime(t);

      let foundIdx = -1;
      for (let i = 0; i < currentTrack.segments.length; i++) {
        const s = currentTrack.segments[i];
        if (t >= s.start && t <= s.end + 0.25) {
          foundIdx = i;
          break;
        }
      }

      if (foundIdx !== -1 && foundIdx !== currentSegmentIndex) {
        if (currentSegmentIndex !== -1) {
          const prevEl = document.getElementById(`seg-${currentSegmentIndex}`);
          if (prevEl) prevEl.classList.remove("active");
        }
        currentSegmentIndex = foundIdx;
        const activeSeg = currentTrack.segments[foundIdx];
        const curEl = document.getElementById(`seg-${foundIdx}`);
        if (curEl) {
          curEl.classList.add("active");
          if (autoscrollToggle.checked && appMode === "podcast") {
            curEl.scrollIntoView({ behavior: "smooth", block: "center" });
          }
        }
        nowPlayingSpeaker.textContent = activeSeg.speaker;
        const chObj = CHAPTERS.find(c => c.id === activeSeg.question_id);
        nowPlayingChapter.textContent = chObj ? chObj.title : "";
        updateDiagram(activeSeg.question_id);
      }
    });

    seekSlider.addEventListener("input", () => {
      audio.currentTime = parseFloat(seekSlider.value);
    });

    function seekRelative(delta) {
      audio.currentTime = Math.max(0, Math.min(currentTrack.total_duration, audio.currentTime + delta));
    }

    function skipReplica(dir) {
      const nextIdx = Math.max(0, Math.min(currentTrack.segments.length - 1, (currentSegmentIndex === -1 ? 0 : currentSegmentIndex) + dir));
      audio.currentTime = currentTrack.segments[nextIdx].start + 0.05;
      audio.play();
    }

    function setSpeed(rate) {
      audio.playbackRate = rate;
      document.querySelectorAll(".speed-btn").forEach(btn => {
        btn.classList.toggle("active", parseFloat(btn.dataset.speed) === rate);
      });
    }

    window.addEventListener("keydown", (e) => {
      if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;

      if (appMode === "quiz" && quizViewMode === "single" && activeQuestionList.length > 0) {
        const curQ = activeQuestionList[currentSingleIndex];
        const keyUpper = e.key.toUpperCase();
        if (["1", "A"].includes(keyUpper)) { e.preventDefault(); answerQuestion(curQ.id, 0); return; }
        if (["2", "B"].includes(keyUpper)) { e.preventDefault(); answerQuestion(curQ.id, 1); return; }
        if (["3", "C"].includes(keyUpper)) { e.preventDefault(); answerQuestion(curQ.id, 2); return; }
        if (["4", "D"].includes(keyUpper)) { e.preventDefault(); answerQuestion(curQ.id, 3); return; }
        if (e.code === "Enter" || e.code === "ArrowRight") { e.preventDefault(); stepSingleQuestion(1); return; }
        if (e.code === "ArrowLeft") { e.preventDefault(); stepSingleQuestion(-1); return; }
      }

      if (e.code === "Space") { e.preventDefault(); togglePlay(); }
      else if (e.code === "ArrowRight") { seekRelative(10); }
      else if (e.code === "ArrowLeft") { seekRelative(-10); }
    });
  </script>
</body>
</html>
"""

final_html = (
    HTML_TEMPLATE
    .replace("__PODCAST_DATA_JSON__", data_json_str)
    .replace("__QUIZ_QUESTIONS_JSON__", quiz_json_str)
    .replace("__KEEP_DATA_JSON__", keep_json_str)
)

with open(r"k:\podPorn\index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Successfully built Orbital Studio k:\\podPorn\\index.html with {len(QUIZ_QUESTIONS)} questions!")
