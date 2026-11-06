import json
import os
from quiz_questions import QUIZ_QUESTIONS

with open(r"k:\podPorn\podcast_data.json", "r", encoding="utf-8") as f:
    podcast_data = json.load(f)

data_json_str = json.dumps(podcast_data, ensure_ascii=False)
quiz_json_str = json.dumps(QUIZ_QUESTIONS, ensure_ascii=False)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="cs" data-theme="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Optika & Strukturovaná kabeláž – Audio Podcast, Tahák & ABCD Test (140 otázek)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    /* ==========================================================================
       CALM, PLEASANT EDITORIAL DESIGN SYSTEM (LIGHT PAPER & SOFT GRAPHITE DARK)
       ========================================================================== */
    :root[data-theme="light"] {
      --bg-page: #f6f5f0;
      --bg-card: #ffffff;
      --bg-subtle: #efede6;
      --bg-hover: #eae7df;
      --bg-active-turn: #eef4ff;
      --border-color: #e4e1d8;
      --border-strong: #d0ccc0;
      --text-main: #1c1e21;
      --text-secondary: #4a4f55;
      --text-muted: #7a7f87;
      --accent-primary: #2563eb;
      --accent-primary-soft: rgba(37, 99, 235, 0.10);
      --accent-warm: #d97706;
      --accent-warm-soft: rgba(217, 119, 6, 0.10);
      --accent-green: #059669;
      --accent-green-soft: rgba(5, 150, 105, 0.12);
      --accent-rose: #e11d48;
      --accent-rose-soft: rgba(225, 29, 72, 0.10);
      --shadow-card: 0 4px 24px -4px rgba(24, 24, 27, 0.06), 0 1px 3px rgba(24, 24, 27, 0.04);
      --shadow-player: 0 16px 48px -8px rgba(24, 24, 27, 0.16), 0 2px 8px rgba(24, 24, 27, 0.08);
      --player-bg: rgba(255, 255, 255, 0.92);
      --diagram-bg: #faf9f5;
    }

    :root[data-theme="dark"] {
      --bg-page: #131418;
      --bg-card: #1b1d23;
      --bg-subtle: #23262e;
      --bg-hover: #2a2e38;
      --bg-active-turn: rgba(59, 130, 246, 0.13);
      --border-color: #2b2f3a;
      --border-strong: #3b404e;
      --text-main: #f3f4f6;
      --text-secondary: #c4c9d4;
      --text-muted: #858c9c;
      --accent-primary: #60a5fa;
      --accent-primary-soft: rgba(96, 165, 250, 0.14);
      --accent-warm: #fbbf24;
      --accent-warm-soft: rgba(251, 191, 36, 0.13);
      --accent-green: #34d399;
      --accent-green-soft: rgba(52, 211, 153, 0.14);
      --accent-rose: #fb7185;
      --accent-rose-soft: rgba(251, 113, 133, 0.14);
      --shadow-card: 0 8px 30px -6px rgba(0, 0, 0, 0.35);
      --shadow-player: 0 20px 50px -10px rgba(0, 0, 0, 0.65);
      --player-bg: rgba(27, 29, 35, 0.92);
      --diagram-bg: #15171c;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-page);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      line-height: 1.6;
      min-height: 100vh;
      padding-bottom: 135px;
      transition: background-color 0.25s ease, color 0.25s ease;
      -webkit-font-smoothing: antialiased;
    }

    ::-webkit-scrollbar { width: 7px; height: 7px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: var(--border-strong); border-radius: 99px; }

    /* ==========================================================================
       HEADER & TOP NAVIGATION
       ========================================================================== */
    .header-wrap {
      position: sticky;
      top: 0;
      z-index: 40;
      background: var(--player-bg);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-bottom: 1px solid var(--border-color);
    }

    .header-top {
      max-width: 1320px;
      margin: 0 auto;
      padding: 13px 28px 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
    }

    .title-area {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .logo-badge {
      width: 42px;
      height: 42px;
      border-radius: 12px;
      background: var(--accent-primary-soft);
      color: var(--accent-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 18px;
      border: 1px solid rgba(96, 165, 250, 0.25);
    }

    .app-title {
      font-size: 17.5px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text-main);
    }

    .app-subtitle {
      font-size: 12px;
      color: var(--text-muted);
      font-weight: 500;
    }

    /* MAIN VIEW TABS (PODCAST vs ABCD QUIZ) */
    .main-mode-tabs {
      display: inline-flex;
      background: var(--bg-subtle);
      padding: 4px;
      border-radius: 14px;
      border: 1px solid var(--border-strong);
      gap: 4px;
    }

    .mode-tab-btn {
      border: none;
      background: transparent;
      color: var(--text-secondary);
      font-family: inherit;
      font-size: 13.5px;
      font-weight: 700;
      padding: 8px 16px;
      border-radius: 10px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.18s ease;
    }
    .mode-tab-btn:hover {
      color: var(--text-main);
    }
    .mode-tab-btn.active {
      background: var(--accent-primary);
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.28);
    }
    .mode-tab-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      padding: 2px 7px;
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
    }

    .seg-btn {
      border: none;
      background: transparent;
      color: var(--text-secondary);
      font-family: inherit;
      font-size: 12px;
      font-weight: 600;
      padding: 6px 11px;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.16s ease;
    }
    .seg-btn:hover {
      color: var(--text-main);
    }
    .seg-btn.active {
      background: var(--bg-card);
      color: var(--accent-primary);
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
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
    .action-btn:hover {
      background: var(--bg-hover);
    }
    .action-btn.primary-soft {
      background: var(--accent-primary-soft);
      color: var(--accent-primary);
      border-color: rgba(96, 165, 250, 0.3);
    }
    .action-btn.rose-soft {
      background: var(--accent-rose-soft);
      color: var(--accent-rose);
      border-color: rgba(251, 113, 133, 0.3);
    }

    /* HORIZONTAL TOPIC NAVIGATION PILLS */
    .topic-bar {
      max-width: 1320px;
      margin: 0 auto;
      padding: 6px 28px 12px;
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
      font-size: 12.5px;
      font-weight: 600;
      padding: 6px 13px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.16s ease;
      display: inline-flex;
      align-items: center;
      gap: 7px;
    }
    .topic-pill:hover {
      background: var(--bg-hover);
      color: var(--text-main);
    }
    .topic-pill.active {
      background: var(--accent-primary);
      color: #ffffff;
      border-color: var(--accent-primary);
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.28);
    }
    .topic-pill .pill-time {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      opacity: 0.82;
    }

    /* ==========================================================================
       2-COLUMN SPACIOUS STUDY LAYOUT (PODCAST VIEW)
       ========================================================================== */
    .main-grid {
      max-width: 1320px;
      margin: 24px auto 0;
      padding: 0 28px;
      display: grid;
      grid-template-columns: 1.08fr 0.92fr;
      gap: 26px;
      align-items: start;
    }

    @media (max-width: 1024px) {
      .main-grid {
        grid-template-columns: 1fr;
        padding: 0 16px;
      }
      .header-top, .topic-bar, .quiz-workspace {
        padding-left: 16px !important;
        padding-right: 16px !important;
      }
    }

    .surface-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 22px;
      box-shadow: var(--shadow-card);
      overflow: hidden;
    }

    .sticky-col {
      position: sticky;
      top: 132px;
    }

    .card-head {
      padding: 18px 24px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
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

    /* LEFT COLUMN: STUDY NOTES & ORIGINAL DIAGRAMS */
    .study-content {
      padding: 24px;
      max-height: calc(100vh - 265px);
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }

    .q-heading {
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text-main);
      line-height: 1.35;
    }

    .note-block {
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 16px 18px;
      font-size: 14.5px;
      color: var(--text-secondary);
      line-height: 1.65;
    }
    .note-block strong {
      color: var(--text-main);
      font-weight: 700;
    }
    .note-block ul {
      margin-top: 8px;
      padding-left: 20px;
    }
    .note-block li {
      margin-bottom: 5px;
    }

    .callout-tip {
      background: var(--accent-green-soft);
      border: 1px solid rgba(16, 185, 129, 0.3);
      border-radius: 16px;
      padding: 15px 18px;
      font-size: 14px;
      color: var(--text-main);
    }
    .callout-tip strong {
      color: var(--accent-green);
    }

    .callout-warn {
      background: var(--accent-rose-soft);
      border: 1px solid rgba(244, 63, 94, 0.3);
      border-radius: 16px;
      padding: 15px 18px;
      font-size: 14px;
      color: var(--text-main);
    }
    .callout-warn strong {
      color: var(--accent-rose);
    }

    .formula-pill {
      font-family: 'JetBrains Mono', monospace;
      font-size: 14px;
      font-weight: 600;
      color: var(--accent-primary);
      background: var(--accent-primary-soft);
      border: 1px solid rgba(96, 165, 250, 0.25);
      padding: 10px 14px;
      border-radius: 12px;
      text-align: center;
      margin: 8px 0;
    }

    .figure-frame {
      background: var(--diagram-bg);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 16px;
      text-align: center;
    }
    .figure-frame img {
      max-width: 100%;
      height: auto;
      border-radius: 10px;
      display: block;
      margin: 0 auto;
    }
    .figure-frame svg {
      width: 100%;
      max-width: 100%;
      height: auto;
      display: block;
    }
    .figure-caption {
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 10px;
      text-align: left;
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
      padding: 10px 14px;
      border-bottom: 1px solid var(--border-color);
    }
    .clean-table td {
      padding: 9px 14px;
      border-bottom: 1px solid var(--border-color);
      color: var(--text-secondary);
    }
    .clean-table tr:last-child td { border-bottom: none; }

    /* RIGHT COLUMN: CONVERSATION TRANSCRIPT */
    .transcript-list {
      padding: 18px 20px;
      max-height: calc(100vh - 265px);
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 10px;
      scroll-behavior: smooth;
    }

    .dialogue-item {
      padding: 14px 18px;
      border-radius: 16px;
      background: transparent;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.18s ease;
    }
    .dialogue-item:hover {
      background: var(--bg-subtle);
    }
    .dialogue-item.active {
      background: var(--bg-active-turn);
      border-color: rgba(96, 165, 250, 0.35);
    }

    .dialogue-meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
    }

    .speaker-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      font-weight: 700;
    }
    .speaker-dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
    }
    .speaker-tomas { color: var(--accent-primary); }
    .speaker-tomas .speaker-dot { background: var(--accent-primary); }
    .speaker-klara { color: var(--accent-warm); }
    .speaker-klara .speaker-dot { background: var(--accent-warm); }

    .dialogue-timestamp {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11.5px;
      color: var(--text-muted);
    }

    .dialogue-body {
      font-size: 15px;
      color: var(--text-secondary);
      line-height: 1.65;
    }
    .dialogue-item.active .dialogue-body {
      color: var(--text-main);
    }
    .dialogue-body strong {
      color: var(--text-main);
      font-weight: 700;
    }

    /* ==========================================================================
       ABCD QUIZ WORKSPACE & PROGRESS DASHBOARD
       ========================================================================== */
    .quiz-workspace {
      max-width: 1120px;
      margin: 24px auto 0;
      padding: 0 28px;
      display: none;
      flex-direction: column;
      gap: 22px;
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

    .pct-hero {
      display: flex;
      align-items: center;
      gap: 18px;
    }

    .pct-big-circle {
      min-width: 88px;
      height: 68px;
      padding: 0 16px;
      border-radius: 18px;
      background: var(--accent-primary-soft);
      border: 1px solid rgba(96, 165, 250, 0.35);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    .pct-big-value {
      font-family: 'JetBrains Mono', monospace;
      font-size: 26px;
      font-weight: 800;
      color: var(--accent-primary);
      line-height: 1.1;
    }

    .pct-big-label {
      font-size: 10.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--text-muted);
    }

    .stats-pills {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }

    .stat-box {
      background: var(--bg-subtle);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 9px 15px;
      display: flex;
      flex-direction: column;
      min-width: 105px;
    }
    .stat-box-val {
      font-family: 'JetBrains Mono', monospace;
      font-size: 17px;
      font-weight: 800;
      color: var(--text-main);
    }
    .stat-box-lbl {
      font-size: 11.5px;
      color: var(--text-muted);
      font-weight: 600;
    }
    .stat-box.green .stat-box-val { color: var(--accent-green); }
    .stat-box.rose .stat-box-val { color: var(--accent-rose); }
    .stat-box.warm .stat-box-val { color: var(--accent-warm); }

    /* DUAL PROGRESS BAR (ACCURACY + COMPLETION) */
    .progress-bars-wrap {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .bar-label-row {
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-secondary);
    }

    .bar-track {
      width: 100%;
      height: 10px;
      background: var(--bg-subtle);
      border-radius: 999px;
      overflow: hidden;
      display: flex;
      border: 1px solid var(--border-color);
    }

    .bar-fill-correct {
      height: 100%;
      background: var(--accent-green);
      transition: width 0.3s ease;
    }
    .bar-fill-wrong {
      height: 100%;
      background: var(--accent-rose);
      transition: width 0.3s ease;
    }

    /* QUESTION CARD */
    .quiz-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 22px;
      padding: 28px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      gap: 20px;
      transition: border-color 0.2s ease;
    }
    .quiz-card.answered-correct {
      border-color: rgba(52, 211, 153, 0.45);
    }
    .quiz-card.answered-wrong {
      border-color: rgba(251, 113, 133, 0.45);
    }

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
      border: 1px solid rgba(96, 165, 250, 0.25);
    }

    .quiz-num-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12.5px;
      font-weight: 700;
      color: var(--text-muted);
    }

    .quiz-question-text {
      font-size: 19px;
      font-weight: 800;
      line-height: 1.42;
      color: var(--text-main);
      letter-spacing: -0.015em;
    }

    .options-grid {
      display: flex;
      flex-direction: column;
      gap: 11px;
    }

    .option-btn {
      width: 100%;
      text-align: left;
      background: var(--bg-subtle);
      border: 1.5px solid var(--border-color);
      border-radius: 16px;
      padding: 15px 18px;
      color: var(--text-main);
      font-family: inherit;
      font-size: 15px;
      font-weight: 600;
      line-height: 1.5;
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 14px;
      transition: all 0.15s ease;
    }
    .option-btn:hover:not(:disabled) {
      background: var(--bg-hover);
      border-color: var(--accent-primary);
      transform: translateX(2px);
    }
    .option-btn:disabled {
      cursor: default;
    }

    .opt-letter {
      flex-shrink: 0;
      width: 30px;
      height: 30px;
      border-radius: 9px;
      background: var(--bg-card);
      border: 1px solid var(--border-strong);
      color: var(--text-secondary);
      font-family: 'JetBrains Mono', monospace;
      font-size: 13.5px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-top: 1px;
    }

    .option-btn.correct-choice {
      background: var(--accent-green-soft);
      border-color: var(--accent-green);
      color: var(--text-main);
    }
    .option-btn.correct-choice .opt-letter {
      background: var(--accent-green);
      border-color: var(--accent-green);
      color: #ffffff;
    }

    .option-btn.wrong-choice {
      background: var(--accent-rose-soft);
      border-color: var(--accent-rose);
      color: var(--text-main);
    }
    .option-btn.wrong-choice .opt-letter {
      background: var(--accent-rose);
      border-color: var(--accent-rose);
      color: #ffffff;
    }

    .option-btn.dimmed-choice {
      opacity: 0.58;
    }

    .explanation-box {
      background: var(--bg-subtle);
      border-left: 4px solid var(--accent-primary);
      border-radius: 14px;
      padding: 16px 18px;
      font-size: 14.5px;
      color: var(--text-secondary);
      line-height: 1.6;
    }
    .explanation-box.is-correct {
      border-left-color: var(--accent-green);
    }
    .explanation-box.is-wrong {
      border-left-color: var(--accent-rose);
    }
    .explanation-box strong {
      color: var(--text-main);
    }

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
      background: var(--accent-primary);
      color: #ffffff;
      font-family: inherit;
      font-size: 14px;
      font-weight: 700;
      padding: 11px 22px;
      border-radius: 13px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(37, 99, 235, 0.28);
      transition: all 0.15s ease;
    }
    .next-q-cta:hover {
      filter: brightness(1.07);
      transform: translateY(-1px);
    }

    /* ==========================================================================
       FLOATING APPLE-STYLE BOTTOM AUDIO PLAYER PILL
       ========================================================================== */
    .player-bar-wrap {
      position: fixed;
      bottom: 16px;
      left: 0;
      right: 0;
      z-index: 50;
      padding: 0 20px;
      pointer-events: none;
    }

    .player-pill {
      pointer-events: auto;
      max-width: 980px;
      margin: 0 auto;
      background: var(--player-bg);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid var(--border-strong);
      border-radius: 24px;
      box-shadow: var(--shadow-player);
      padding: 11px 22px 13px;
      display: flex;
      flex-direction: column;
      gap: 9px;
    }

    .scrub-row {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .scrub-time {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      min-width: 44px;
    }
    .scrub-time.current {
      color: var(--accent-primary);
    }

    .range-bar {
      flex: 1;
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
      width: 15px;
      height: 15px;
      border-radius: 50%;
      background: var(--accent-primary);
      cursor: pointer;
      transition: transform 0.12s ease;
    }
    .range-bar::-webkit-slider-thumb:hover {
      transform: scale(1.2);
    }

    .player-controls-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }

    .now-playing-info {
      display: flex;
      align-items: center;
      gap: 10px;
      min-width: 210px;
    }

    .live-Tag {
      font-size: 11.5px;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 99px;
      background: var(--accent-primary-soft);
      color: var(--accent-primary);
    }

    .main-transport {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .icon-btn {
      border: 1px solid var(--border-color);
      background: var(--bg-subtle);
      color: var(--text-main);
      font-family: inherit;
      font-size: 12px;
      font-weight: 600;
      padding: 8px 13px;
      border-radius: 12px;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .icon-btn:hover {
      background: var(--bg-hover);
    }

    .play-cta {
      border: none;
      background: var(--accent-primary);
      color: #ffffff;
      font-family: inherit;
      font-size: 13.5px;
      font-weight: 700;
      padding: 9px 22px;
      border-radius: 14px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 16px rgba(37, 99, 235, 0.32);
      transition: all 0.16s ease;
    }
    .play-cta:hover {
      transform: translateY(-1px);
      filter: brightness(1.06);
    }
  </style>
</head>
<body>

  <!-- TOP NAVIGATION & MODE SWITCHER -->
  <header class="header-wrap">
    <div class="header-top">
      <div class="title-area">
        <div class="logo-badge">🎓</div>
        <div>
          <h1 class="app-title">Optika &amp; Strukturovaná kabeláž</h1>
          <div class="app-subtitle">Audio podcast, vizuální tahák z hodin &amp; tréninkový ABCD test (140 otázek)</div>
        </div>
      </div>

      <!-- TOP-LEVEL MODE SWITCHER: PODCAST vs ABCD QUIZ -->
      <div class="main-mode-tabs">
        <button id="tab-btn-podcast" class="mode-tab-btn active" onclick="setAppMode('podcast')">
          🎧 Podcast &amp; Tahák
        </button>
        <button id="tab-btn-quiz" class="mode-tab-btn" onclick="setAppMode('quiz')">
          📝 Test ABCD
          <span id="header-quiz-badge" class="mode-tab-badge">140 otázek</span>
        </button>
      </div>

      <div class="header-actions">
        <div id="voice-switcher-wrap" class="segmented-control" title="Přepnutí hlasů">
          <button id="eng-copilot" class="seg-btn active" onclick="switchEngine('copilot_v2')">
            ✨ Copilot V2 (Andrew &amp; Ava)
          </button>
          <button id="eng-cz" class="seg-btn" onclick="switchEngine('cz_studio')">
            🎙️ CZ Studio (Antonín &amp; Vlasta)
          </button>
        </div>

        <button id="theme-btn" class="action-btn" onclick="toggleTheme()">
          ☀️ Světlý režim
        </button>

        <a id="download-link" href="podcast_copilot_v2.mp3" download class="action-btn">
          ⬇ MP3
        </a>
      </div>
    </div>

    <!-- HORIZONTAL PILL BAR FOR PODCAST CHAPTERS -->
    <nav id="chapter-list" class="topic-bar"></nav>

    <!-- HORIZONTAL PILL BAR FOR QUIZ TOPICS (SHOWN IN QUIZ MODE) -->
    <nav id="quiz-topic-bar" class="topic-bar" style="display:none;"></nav>
  </header>

  <!-- ========================================================================
       VIEW 1: SPACIOUS 2-COLUMN PODCAST & STUDY SHEET WORKSPACE
       ======================================================================== -->
  <main id="podcast-workspace" class="main-grid">

    <!-- LEFT: STUDY SHEET & ORIGINAL DIAGRAMS FROM CLASS NOTES -->
    <section class="surface-card sticky-col">
      <div class="card-head">
        <div>
          <div id="active-q-badge" class="card-head-title">Tahák &amp; Nákresy k aktuální otázce</div>
          <div class="card-head-sub">Automaticky se přepíná podle toho, o čem se v podcastu mluví</div>
        </div>
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
          <button class="action-btn primary-soft" onclick="openQuizForCurrentTopic()">📝 Otestovat toto téma (ABCD)</button>
          <button class="action-btn" onclick="showAllDiagrams()">Zobrazit celý tahák</button>
        </div>
      </div>
      <div id="diagram-panel" class="study-content"></div>
    </section>

    <!-- RIGHT: SYNCHRONIZED DIALOGUE TRANSCRIPT -->
    <section class="surface-card">
      <div class="card-head">
        <div>
          <div class="card-head-title">Přepis rozhovoru (Tomáš &amp; Klára)</div>
          <div class="card-head-sub">Kliknutím na libovolný odstavec přeskočíš v audiu přímo na danou větu</div>
        </div>
        <label style="font-size:12px; font-weight:600; color:var(--text-secondary); display:flex; align-items:center; gap:6px; cursor:pointer;">
          <input type="checkbox" id="autoscroll-toggle" checked style="accent-color:var(--accent-primary);" />
          Auto-posun
        </label>
      </div>
      <div id="transcript-container" class="transcript-list"></div>
    </section>

  </main>

  <!-- ========================================================================
       VIEW 2: EXTENSIVE ABCD QUIZ WORKSPACE (140 QUESTIONS, EVERY FACT ≥3x)
       ======================================================================== -->
  <section id="quiz-workspace" class="quiz-workspace">

    <!-- LIVE PERCENTAGE SCORE DASHBOARD -->
    <div class="score-dashboard">
      <div class="score-top-row">
        <div class="pct-hero">
          <div id="pct-circle" class="pct-big-circle">
            <span id="quiz-pct-val" class="pct-big-value">0 %</span>
            <span class="pct-big-label">Úspěšnost</span>
          </div>
          <div>
            <div style="font-size:17px; font-weight:800; color:var(--text-main);">
              Průběžná úspěšnost v testu ABCD
            </div>
            <div id="quiz-status-subtitle" style="font-size:13px; color:var(--text-muted); font-weight:500;">
              Každá věc z testu i výpisu z hodin je zde procvičena alespoň 3× z různých úhlů pohledu.
            </div>
          </div>
        </div>

        <div class="stats-pills">
          <div class="stat-box green">
            <span id="stat-correct" class="stat-box-val">0</span>
            <span class="stat-box-lbl">✓ Správně</span>
          </div>
          <div class="stat-box rose">
            <span id="stat-wrong" class="stat-box-val">0</span>
            <span class="stat-box-lbl">✗ Špatně</span>
          </div>
          <div class="stat-box">
            <span id="stat-answered" class="stat-box-val">0 / 140</span>
            <span class="stat-box-lbl">Zodpovězeno</span>
          </div>
          <div class="stat-box warm">
            <span id="stat-streak" class="stat-box-val">0 🔥</span>
            <span class="stat-box-lbl">Série bez chyby</span>
          </div>
        </div>
      </div>

      <!-- PROGRESS BARS -->
      <div class="progress-bars-wrap">
        <div class="bar-label-row">
          <span id="bar-left-label">Poměr správných (zelená) a chybných (červená) odpovědí</span>
          <span id="bar-right-label">Dokončeno 0 % ze zvoleného okruhu</span>
        </div>
        <div class="bar-track">
          <div id="bar-correct" class="bar-fill-correct" style="width: 0%;"></div>
          <div id="bar-wrong" class="bar-fill-wrong" style="width: 0%;"></div>
        </div>
      </div>

      <!-- QUIZ CONTROLS ROW -->
      <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:10px; padding-top:4px;">
        <div class="segmented-control">
          <button id="qview-single" class="seg-btn active" onclick="setQuizViewMode('single')">
            🎯 Po jedné otázce (s klávesnicí A/B/C/D)
          </button>
          <button id="qview-list" class="seg-btn" onclick="setQuizViewMode('list')">
            📋 Všechny otázky pod sebou
          </button>
        </div>

        <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
          <button id="btn-filter-mistakes" class="action-btn rose-soft" onclick="filterOnlyMistakes()" style="display:none;">
            🔁 Procvičit jen chyby (<span id="mistake-count-btn">0</span>)
          </button>
          <button class="action-btn primary-soft" onclick="shuffleActiveQuiz()">
            🔀 Zamíchat otázky a možnosti
          </button>
          <button class="action-btn" onclick="resetQuizStats()">
            ♻️ Vynulovat skóre
          </button>
        </div>
      </div>
    </div>

    <!-- DYNAMIC QUIZ CONTENT CONTAINER -->
    <div id="quiz-cards-container" style="display:flex; flex-direction:column; gap:18px;"></div>

  </section>

  <!-- FLOATING BOTTOM PLAYER -->
  <div class="player-bar-wrap">
    <audio id="podcast-audio" src="podcast_copilot_v2.mp3" preload="metadata"></audio>
    <div class="player-pill">
      <div class="scrub-row">
        <span id="time-current" class="scrub-time current">00:00</span>
        <input id="seek-slider" type="range" class="range-bar" min="0" max="800" step="0.1" value="0" />
        <span id="time-total" class="scrub-time">00:00</span>
      </div>

      <div class="player-controls-row">
        <div class="now-playing-info">
          <span id="now-playing-speaker" class="live-Tag">Připraveno</span>
          <span id="now-playing-chapter" style="font-size:12.5px; color:var(--text-secondary); font-weight:600;">Klikni na Přehrát</span>
        </div>

        <div class="main-transport">
          <button class="icon-btn" onclick="skipReplica(-1)">⏮ Předchozí</button>
          <button class="icon-btn" onclick="seekRelative(-10)">-10 s</button>
          <button id="play-btn" class="play-cta" onclick="togglePlay()">
            <span id="play-icon">▶</span>
            <span id="play-label">Přehrát</span>
          </button>
          <button class="icon-btn" onclick="seekRelative(10)">+10 s</button>
          <button class="icon-btn" onclick="skipReplica(1)">Další ⏭</button>
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

    let activeEngine = RAW_DATA.default_engine || "copilot_v2";
    let currentTrack = RAW_DATA.tracks ? RAW_DATA.tracks[activeEngine] : RAW_DATA;
    let appMode = "podcast"; // 'podcast' | 'quiz'

    const CHAPTERS = [
      { id: "intro", badge: "Úvod", title: "Úvod" },
      { id: "opt-1", badge: "Optika 1", title: "1. Struktura a typy vláken" },
      { id: "opt-2", badge: "Optika 2", title: "2. Totální odraz, NA a útlum" },
      { id: "sk-8",  badge: "Otázka 8", title: "8. Normy v ČR" },
      { id: "sk-9",  badge: "Otázka 9", title: "9. UTP, FTP, STP & Rybí kost" },
      { id: "sk-10", badge: "Otázka 10", title: "10. Kroucené páry" },
      { id: "sk-11", badge: "Otázka 11", title: "11. Třídy linek & Frekvence" },
      { id: "sk-12", badge: "Otázka 12", title: "12. Přeslech FEXT" },
      { id: "sk-13", badge: "Otázka 13", title: "13. Subsystémy & Šňůry A,B,E" },
      { id: "sk-14", badge: "Otázka 14", title: "14. Pracovní plocha" },
      { id: "sk-15", badge: "Otázka 15", title: "15. Patří do generické SK?" },
      { id: "sk-16", badge: "Otázka 16", title: "16. Konektor RJ-45 Typ B" }
    ];

    const QUIZ_TOPICS = [
      { id: "all",   title: "Všechny otázky" },
      { id: "opt-1", title: "Optika 1: Vlákna & λ" },
      { id: "opt-2", title: "Optika 2: Odraz, NA & Útlum" },
      { id: "sk-8",  title: "Ot. 8: Normy v ČR" },
      { id: "sk-9",  title: "Ot. 9: UTP, FTP, STP & Kříž" },
      { id: "sk-10", title: "Ot. 10: Kroucené páry" },
      { id: "sk-11", title: "Ot. 11: Třídy A–Fa & Frekvence" },
      { id: "sk-12", title: "Ot. 12: Přeslech FEXT" },
      { id: "sk-13", title: "Ot. 13: Subsystémy & Šňůry A,B,E" },
      { id: "sk-14", title: "Ot. 14: Pracovní plocha (10 m²)" },
      { id: "sk-15", title: "Ot. 15: Patří do SK?" },
      { id: "sk-16", title: "Ot. 16: Konektor RJ-45 Typ B" }
    ];

    const DIAGRAMS = {
      "intro": `
        <div class="q-heading">Přehled testových okruhů (Optika &amp; Strukturovaná kabeláž)</div>
        <div class="note-block">
          V horní liště si můžeš kliknout na libovolnou otázku, nebo se přepnout do záložky <strong>📝 Test ABCD (140 otázek)</strong>, kde je každá věc procvičena minimálně 3× z různých úhlů pohledu.
        </div>
        <div class="callout-tip">
          <strong>Ovládání klávesnicí:</strong> V podcastu mezerník (Space) zastaví/spustí přehrávání. V testu ABCD můžeš odpovídat klávesami <strong>A, B, C, D</strong> (nebo <strong>1, 2, 3, 4</strong>) a přecházet na další otázku klávesou <strong>Enter</strong> nebo <strong>šipkou doprava</strong>.
        </div>
      `,
      "opt-1": `
        <div class="q-heading">1. Základní typy optických vláken, vlnové délky a struktura vlákna</div>
        <div class="figure-frame">
          <div class="figure-caption">Nákres do testu: Průřez optickým vláknem (4 vrstvy od středu ven)</div>
          <svg viewBox="0 0 460 205">
            <circle cx="105" cy="102" r="85" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
            <circle cx="105" cy="102" r="61" fill="#0f172a" stroke="#10b981" stroke-width="2" stroke-dasharray="4 2"/>
            <circle cx="105" cy="102" r="39" fill="#1e3a8a" fill-opacity="0.45" stroke="#38bdf8" stroke-width="2"/>
            <circle cx="105" cy="102" r="15" fill="#38bdf8" stroke="#e0f2fe" stroke-width="2"/>

            <line x1="105" y1="102" x2="215" y2="34" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="222" y="30" fill="#38bdf8" font-size="12" font-weight="bold">1. Jádro (Core) – vyšší index lomu n₁</text>
            <text x="222" y="46" fill="#94a3b8" font-size="11">Ø 9 µm (SM) | 50 nebo 62,5 µm (MM)</text>

            <line x1="136" y1="80" x2="215" y2="78" stroke="#60a5fa" stroke-width="1.5"/>
            <text x="222" y="74" fill="#60a5fa" font-size="12" font-weight="bold">2. Plášť (Cladding) – nižší index lomu n₂</text>
            <text x="222" y="90" fill="#94a3b8" font-size="11">Ø 125 µm (vždy stejný u SM i MM)</text>

            <line x1="156" y1="128" x2="215" y2="124" stroke="#10b981" stroke-width="1.5"/>
            <text x="222" y="120" fill="#10b981" font-size="12" font-weight="bold">3. Primární ochrana (Primary Coating)</text>
            <text x="222" y="136" fill="#94a3b8" font-size="11">Ø 250 µm (akrylátový lak)</text>

            <line x1="172" y1="158" x2="215" y2="168" stroke="#94a3b8" stroke-width="1.5"/>
            <text x="222" y="165" fill="#94a3b8" font-size="12" font-weight="bold">4. Sekundární ochrana (Buffer)</text>
            <text x="222" y="181" fill="#64748b" font-size="11">Ø 900 µm (plastová trubička)</text>
          </svg>
        </div>

        <div class="note-block">
          <strong>Základní typy optických vláken:</strong>
          <ul>
            <li><strong>Mnohovidová (Multimode – MM, jádro 50 nebo 62,5 µm):</strong> šíří se jimi více vidů najednou → vzniká <em>vidová (modální) disperze</em>. Dělí se na <strong>skoková (Step-Index)</strong> a <strong>gradientní (Graded-Index)</strong> s parabolickým profilem indexu lomu, který vyrovnává časy průchodu paprsků.</li>
            <li><strong>Jednovidová (Singlemode – SM, jádro 9 µm):</strong> šíří se jimi pouze <strong>1 přímý vid</strong> → nulová vidová disperze, přenos na desítky km.</li>
          </ul>
        </div>

        <table class="clean-table">
          <thead>
            <tr><th>Přenosové okno</th><th>Vlnová délka</th><th>Použití &amp; Typický útlum</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>1. okno</strong></td><td><strong>850 nm</strong></td><td>Mnohovidová (MM), útlum ~2,5–3 dB/km</td></tr>
            <tr><td><strong>2. okno</strong></td><td><strong>1300 nm (MM) / 1310 nm (SM)</strong></td><td>Nulová chromatická disperze, ~0,35–0,5 dB/km</td></tr>
            <tr><td><strong>3. okno</strong></td><td><strong>1550 nm</strong></td><td>Jednovidová (SM), nejnižší útlum <strong>~0,2 dB/km</strong></td></tr>
          </tbody>
        </table>
      `,
      "opt-2": `
        <div class="q-heading">2. Podmínka přenosu, index lomu, numerická apertura (NA) a vložný útlum</div>
        <div class="note-block">
          <strong>Základní podmínka přenosu světla:</strong> Jev <strong>totálního (úplného) vnitřního odrazu</strong> na rozhraní jádra a pláště. Musí platit:<br/>
          1. Index lomu jádra je větší než index lomu pláště: <strong>n₁ &gt; n₂</strong><br/>
          2. Úhel dopadu α je větší než mezní úhel α_m (kde <strong>sin α_m = n₂ / n₁</strong>).
        </div>

        <div class="note-block">
          <strong>Index lomu (n):</strong> Udává, kolikrát pomaleji se světlo šíří v daném prostředí oproti vakuu (c ≈ 3·10⁸ m/s):
          <div class="formula-pill">n = c / v</div>
        </div>

        <div class="callout-warn">
          <strong>Numerická apertura (NA) a maximální úhel navázání (θ_max):</strong>
          <div class="formula-pill">NA = sin(θ_max) = √(n₁² − n₂²)</div>
          • <strong>Souvisí NA s průměrem vlákna?</strong> <strong>NE!</strong> Ve vzorci průměr vůbec nefiguruje, NA závisí pouze na indexech lomu n₁ a n₂.<br/>
          • <strong>Jakou NA požadujeme?</strong> Jde o <strong>kompromis</strong>: pro snadné navázání světla ze zdroje chceme velkou NA, ale pro malou vidovou disperzi (velkou šířku pásma) potřebujeme malou NA.
        </div>

        <div class="note-block">
          <strong>Vložný útlum (Insertion Loss):</strong> Ztráta optického výkonu (v dB) vložením konektoru nebo sváru do trasy. Vzniká: 1) Fresnelovým odrazem na vzduchové mezeře, 2) geometrickým přesazením jader (osovým/úhlovým), 3) nečistotami nebo rozdílným průměrem/NA spojovaných vláken.
        </div>
      `,
      "sk-8": `
        <div class="q-heading">8. Podle jakých norem můžeme v ČR vytvořit strukturovanou kabeláž?</div>
        <div class="callout-tip">
          <strong>Přesná odpověď z tvého výpisu z hodin:</strong><br/>
          Podle norem <strong>ČSN EN 50173 a ČSN EN 50174</strong> (jde o české převzetí evropské normy EN).
        </div>
        <div class="note-block">
          • <strong>ČSN EN 50173</strong> – návrh a parametry univerzální strukturované kabeláže<br/>
          • <strong>ČSN EN 50174</strong> – instalace a budování informačních kabeláží<br/>
          • Vycházejí z mezinárodní normy <strong>ISO/IEC 11801</strong> (v USA <strong>TIA/EIA-568</strong>).
        </div>
      `,
      "sk-9": `
        <div class="q-heading">9. Popište kabel STP a UTP (vč. FTP a rybí kosti). Do které kategorie UTP?</div>
        <div class="figure-frame">
          <div class="figure-caption">Originální obrázek z tvého výpisu z hodin (STP vs. UTP)</div>
          <img src="assets/image1.png" alt="STP a UTP kabel z hodin" />
        </div>
        <div class="note-block">
          <strong>UTP = Unshielded Twisted Pair (Nestíněná kroucená dvojlinka)</strong>
          <ul>
            <li>Nemá kovové stínění, skládá se ze <strong>4 párů (8 žil/vodičů)</strong> vzájemně zkroucených</li>
            <li>Barvy vidíme vlastním okem, levnější a jednodušší na instalaci</li>
            <li><strong>Využití: v kategorii 6 (třída E)</strong></li>
          </ul>
        </div>
        <div class="note-block">
          <strong>FTP = Foiled Twisted Pair (Kompromis mezi UTP a STP)</strong>
          <ul>
            <li>Kroucená dvojlinka s <strong>celkovým stíněním z hliníkové fólie kolem všech 4 párů dohromady</strong> (jednotlivé páry stíněné nejsou).</li>
          </ul>
        </div>
        <div class="note-block">
          <strong>STP = Shielded Twisted Pair (Stíněná kroucená dvojlinka)</strong>
          <ul>
            <li>Stejná struktura jako UTP, ale <strong>každý pár je samostatně stíněný</strong></li>
            <li><strong>Využití: v kategorii 6a a výš (třída Ea a výš)</strong></li>
          </ul>
        </div>
        <div class="callout-tip">
          <strong>Plastový kříž („rybí kost“):</strong> Typický pro <strong>kategorii 6</strong> – uvnitř kabelu mechanicky odděluje jednotlivé páry, aby nešly moc k sobě!
        </div>
      `,
      "sk-10": `
        <div class="q-heading">10. Proč používáme technologii kroucených párů?</div>
        <div class="note-block">
          <strong>Přesné body z tvých hodin:</strong>
          <ul>
            <li>Kroucené páry používáme proto, abychom <strong>omezili elektromagnetické rušení a přeslechy</strong> mezi jednotlivými vodiči a páry – díky tomu zajišťujeme spolehlivější přenos dat.</li>
            <li><strong>Každý ze 4 párů má jinou hustotu zákrutů</strong>, aby se omezily přeslechy a rušení mezi sousedními páry.</li>
            <li>V každém páru se přenáší signál pomocí dvou vodičů:
              <ul>
                <li>jeden vodič přenáší <strong>kladnou polaritu signálu (+U)</strong>,</li>
                <li>druhý vodič přenáší <strong>opačnou polaritu signálu (−U)</strong>,</li>
                <li><strong>přijímač vyhodnocuje rozdíl napětí mezi vodiči</strong> (soufázové rušení se tím odečte).</li>
              </ul>
            </li>
          </ul>
        </div>
      `,
      "sk-11": `
        <div class="q-heading">11. Které normy definují třídy linek? Vyjmenujte třídy linek a frekvenční rozsahy</div>
        <div class="note-block">
          • <strong>ČSN EN 50173</strong> – evropská norma pro univerzální kabeláž<br/>
          • <strong>ISO/IEC 11801</strong> – mezinárodní norma pro univerzální kabeláž:<br/>
          &nbsp;&nbsp;– <strong>ISO</strong> = <em>International Organization for Standardization</em> (Mezinárodní organizace pro normalizaci)<br/>
          &nbsp;&nbsp;– <strong>IEC</strong> = <em>International Electrotechnical Commission</em> (Mezinárodní elektrotechnická komise)<br/>
          • U optiky se frekvence světla běžně udává v <strong>THz</strong>.
        </div>
        <div class="figure-frame">
          <div class="figure-caption">Originální tabulka tříd linek a frekvenčních rozsahů z tvých hodin</div>
          <img src="assets/image3.png" alt="Tabulka tříd linek z hodin" />
        </div>
      `,
      "sk-12": `
        <div class="q-heading">12. Co je to FEXT? Jaký útlum FEXT požadujeme?</div>
        <div class="note-block">
          • <strong>FEXT = Far-End Crosstalk</strong> – <strong>přeslech na vzdáleném konci kabelu</strong>.<br/>
          • Jde o nežádoucí rušení, kdy signál z jednoho páru ovlivňuje jiný pár a rušení se měří na <strong>opačném konci kabelu</strong>, než kde signál vzniká.<br/>
          • Útlum přeslechu (v dB) udává míru potlačení nežádoucího signálu rušení. Čím vyšší útlum přeslechu v dB, tím kvalitnější kabeláž a menší vzájemné rušení párů.
        </div>
        <div class="callout-warn">
          <strong>Ke zkoušce si zapamatuj:</strong><br/>
          U FEXT požadujeme <strong>co nejvyšší hodnotu útlumu v decibelech (dB)</strong>, aby bylo rušení mezi páry co nejmenší!
        </div>
      `,
      "sk-13": `
        <div class="q-heading">13. Tři základní subsystémy generické kabeláže a maximální délky kabelů</div>
        <div class="note-block">
          <strong>3 základní subsystémy a jejich délky z hodin:</strong>
          <ul>
            <li><strong>1. Subsystém páteřní kabeláže areálu:</strong> <strong>optika, max. délka 1500 m</strong>, spojuje <strong>CD</strong> (Campus Distributor – rozvaděč areálu) → <strong>BD</strong> (Building Distributor).</li>
            <li><strong>2. Subsystém páteřní kabeláže budovy:</strong> <strong>optika, max. délka 500 m</strong>, spojuje <strong>BD</strong> → <strong>FD</strong> (Floor Distributor – patrový rozvaděč).</li>
            <li><strong>3. Subsystém horizontální kabeláže:</strong> <strong>metalické kabely, max. délka 90 m</strong>, spojuje <strong>FD</strong> → <strong>TO</strong> (telekomunikační zásuvka).</li>
          </ul>
        </div>
        <div class="figure-frame">
          <div class="figure-caption">Originální schéma subsystémů generické kabeláže z tvých hodin</div>
          <img src="assets/image6.png" alt="Schéma CD BD FD CP TO z hodin" style="background:#fff; padding:8px;" />
        </div>
        <div class="figure-frame">
          <div class="figure-caption">Přídavné šňůry A, B, E – souhrnná tabulka z hodin</div>
          <img src="assets/image7.png" alt="Tabulka přídavných šňůr A B E" />
        </div>
        <div class="callout-tip">
          <strong>Pravidlo 90 + 10 = 100 m:</strong> Horizontální pevný spoj má max. <strong>90 m</strong> a celý kanál včetně přídavných šňůr má <strong>90 + 10 = 100 m</strong>, protože musí platit <strong>A + B + E ≤ 10 m</strong>!
        </div>
      `,
      "sk-14": `
        <div class="q-heading">14 &amp; 15. Pracovní plocha a zda patří její kabely do generické SK</div>
        <div class="note-block">
          <strong>14. Co je to pracovní plocha, kolik portů a jejich vlastnosti:</strong>
          <ul>
            <li>Prostor, kde uživatelé pracují s koncovými zařízeními (PC, tiskárna, IP kamera atd.).</li>
            <li><strong>Začíná telekomunikační zásuvkou (TO)</strong>, zahrnuje propojovací kabel k zařízení (<strong>max. 5 m</strong>) a samotné koncové zařízení.</li>
            <li>Na <strong>1 pracovní plochu (10 m²)</strong> se zpravidla přidělují <strong>2 zásuvky (nebo 1 dvojzásuvka)</strong>.</li>
            <li>Tyto zásuvky musí odpovídat kategorii kabeláže (Cat 6, 6a atd.).</li>
          </ul>
        </div>
        <div class="callout-warn">
          <strong>15. Patří kabely pracovní plochy do generické strukturované kabeláže?</strong><br/>
          <strong>NE!</strong> Kabeláž pracovní plochy (přídavné šňůry od zásuvky ke koncovému zařízení) <strong>není součástí generické SK</strong>. Strukturovaná kabeláž končí na zásuvce (TO), která do SK ještě patří!
        </div>
      `,
      "sk-16": `
        <div class="q-heading">16. Popište zapojení konektorů pro zásuvku typu B (T568B)</div>
        <div class="callout-tip">
          <strong>Pomůcka z hodin:</strong> Typ B je v Evropě. 1 pin = 1 vodič = 1 barva = 1 drátek.<br/>
          <strong>Zelené piny jsou „rozházené“ (nejsou u sebe) – piny 3 a 6!</strong> Ostatní jsou vedle sebe: oranžová 1,2 – modrá 4,5 – hnědá 7,8.
        </div>
        <div style="display:grid; grid-template-columns: 1.2fr 0.8fr; gap:12px; align-items:center;">
          <div class="figure-frame">
            <div class="figure-caption">T568A vs. T568B</div>
            <img src="assets/image8.jpeg" alt="T568A a T568B zapojení" />
          </div>
          <div class="figure-frame">
            <div class="figure-caption">Pořadí barev T568B</div>
            <img src="assets/image9.png" alt="Pořadí barev pinů 1 až 8" />
          </div>
        </div>
      `
    };
    DIAGRAMS["sk-15"] = DIAGRAMS["sk-14"];

    const audio = document.getElementById("podcast-audio");
    const seekSlider = document.getElementById("seek-slider");
    const timeCurrent = document.getElementById("time-current");
    const timeTotal = document.getElementById("time-total");
    const playIcon = document.getElementById("play-icon");
    const playLabel = document.getElementById("play-label");
    const chapterListEl = document.getElementById("chapter-list");
    const transcriptEl = document.getElementById("transcript-container");
    const diagramPanel = document.getElementById("diagram-panel");
    const activeQBadge = document.getElementById("active-q-badge");
    const nowPlayingSpeaker = document.getElementById("now-playing-speaker");
    const nowPlayingChapter = document.getElementById("now-playing-chapter");
    const autoscrollToggle = document.getElementById("autoscroll-toggle");
    const downloadLink = document.getElementById("download-link");
    const themeBtn = document.getElementById("theme-btn");

    let currentSegmentIndex = -1;
    let currentQuestionId = "";

    /* =========================================================================
       MODE SWITCHING (PODCAST & TAHÁK vs TEST ABCD)
       ========================================================================= */
    function setAppMode(mode) {
      appMode = mode;
      const isQuiz = mode === "quiz";
      document.getElementById("tab-btn-podcast").classList.toggle("active", !isQuiz);
      document.getElementById("tab-btn-quiz").classList.toggle("active", isQuiz);

      document.getElementById("podcast-workspace").style.display = isQuiz ? "none" : "grid";
      document.getElementById("chapter-list").style.display = isQuiz ? "none" : "flex";

      document.getElementById("quiz-workspace").style.display = isQuiz ? "flex" : "none";
      document.getElementById("quiz-topic-bar").style.display = isQuiz ? "flex" : "none";

      if (isQuiz) {
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
      currentSingleIndex = 0;
      rebuildActiveQuestionList();
      setAppMode("quiz");
      window.scrollTo({ top: 0, behavior: "smooth" });
    }

    function toggleTheme() {
      const root = document.documentElement;
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      themeBtn.textContent = next === "dark" ? "☀️ Světlý režim" : "🌙 Tmavý režim";
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
        btn.className = "topic-pill" + (ch.id === currentQuestionId ? " active" : "");
        btn.onclick = () => {
          updateDiagram(ch.id);
          audio.currentTime = startSec + 0.05;
          audio.play();
        };
        btn.innerHTML = `
          <span>${ch.title}</span>
          <span class="pill-time">${formatTime(startSec)}</span>
        `;
        chapterListEl.appendChild(btn);
      });

      currentTrack.segments.forEach((seg, idx) => {
        const div = document.createElement("div");
        div.id = `seg-${idx}`;
        const isTomas = seg.speaker === "Tomáš";
        div.className = "dialogue-item";
        div.onclick = () => {
          audio.currentTime = seg.start + 0.05;
          audio.play();
        };
        const chObj = CHAPTERS.find(c => c.id === seg.question_id);
        div.innerHTML = `
          <div class="dialogue-meta">
            <span class="speaker-badge ${isTomas ? 'speaker-tomas' : 'speaker-klara'}">
              <span class="speaker-dot"></span>
              ${seg.speaker}
              <span style="font-weight:500; color:var(--text-muted); font-size:12px;">• ${chObj ? chObj.badge : ''}</span>
            </span>
            <span class="dialogue-timestamp">${formatTime(seg.start)}</span>
          </div>
          <div class="dialogue-body">${formatText(seg.display)}</div>
        `;
        transcriptEl.appendChild(div);
      });

      seekSlider.max = currentTrack.total_duration;
      timeTotal.textContent = formatTime(currentTrack.total_duration);
    }

    function switchEngine(engineKey) {
      if (!RAW_DATA.tracks || !RAW_DATA.tracks[engineKey]) return;
      const wasPlaying = !audio.paused;
      const savedSegIdx = currentSegmentIndex >= 0 ? currentSegmentIndex : 0;

      activeEngine = engineKey;
      currentTrack = RAW_DATA.tracks[engineKey];

      document.getElementById("eng-copilot").classList.toggle("active", engineKey === "copilot_v2");
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
        activeQBadge.textContent = `${chObj.title} – Tahák & Schéma`;
      }
      diagramPanel.innerHTML = DIAGRAMS[qId] || DIAGRAMS["intro"];

      CHAPTERS.forEach(ch => {
        const el = document.getElementById(`chap-btn-${ch.id}`);
        if (el) el.classList.toggle("active", ch.id === qId);
      });
    }

    function showAllDiagrams() {
      currentQuestionId = "all";
      activeQBadge.textContent = "Kompletní tahák všech otázek (Optika 1–2 & Kabeláž 8–16)";
      diagramPanel.innerHTML = ["opt-1", "opt-2", "sk-8", "sk-9", "sk-10", "sk-11", "sk-12", "sk-13", "sk-14", "sk-16"]
        .map(k => `<div style="padding-bottom:24px; border-bottom:1px solid var(--border-color); margin-bottom:16px; display:flex; flex-direction:column; gap:14px;">${DIAGRAMS[k]}</div>`)
        .join("");
    }

    /* =========================================================================
       ABCD QUIZ ENGINE (140 QUESTIONS, OPTION SHUFFLING, LIVE PERCENTAGE)
       ========================================================================= */
    let quizFilterTopic = "all";
    let quizViewMode = "single"; // 'single' | 'list'
    let onlyMistakesMode = false;
    let currentSingleIndex = 0;
    let currentStreak = 0;

    // Map questionId -> { chosenIndex, isCorrect, shuffledOptions: [{text, isCorrect}] }
    let quizState = {};
    let activeQuestionList = [];

    function createShuffledOptions(qObj) {
      const items = qObj.options.map((text, idx) => ({
        text: text,
        isCorrect: idx === qObj.ans
      }));
      // Fisher-Yates shuffle so correct option is evenly distributed across A, B, C, D
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

      // Restore saved answers from localStorage if available
      try {
        const saved = localStorage.getItem("podporn_quiz_v1");
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
          if (quizState[k].answered) {
            answeredOnly[k] = quizState[k];
          }
        });
        localStorage.setItem("podporn_quiz_v1", JSON.stringify({
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
      }
      activeQuestionList = pool;
      if (currentSingleIndex >= activeQuestionList.length) {
        currentSingleIndex = 0;
      }
    }

    function selectQuizTopic(topicId) {
      quizFilterTopic = topicId;
      onlyMistakesMode = false;
      currentSingleIndex = 0;
      rebuildActiveQuestionList();
      // Jump to first unanswered question in that topic if available
      const firstUnanswered = activeQuestionList.findIndex(q => !quizState[q.id].answered);
      if (firstUnanswered !== -1) currentSingleIndex = firstUnanswered;
      renderQuizTopicBar();
      renderQuizDashboardAndCards();
    }

    function setQuizViewMode(mode) {
      quizViewMode = mode;
      document.getElementById("qview-single").classList.toggle("active", mode === "single");
      document.getElementById("qview-list").classList.toggle("active", mode === "list");
      renderQuizDashboardAndCards();
    }

    function filterOnlyMistakes() {
      onlyMistakesMode = !onlyMistakesMode;
      currentSingleIndex = 0;
      rebuildActiveQuestionList();
      renderQuizTopicBar();
      renderQuizDashboardAndCards();
    }

    function shuffleActiveQuiz() {
      // Re-shuffle unanswered question options and shuffle activeQuestionList order
      RAW_QUIZ.forEach(q => {
        if (!quizState[q.id].answered) {
          quizState[q.id].shuffledOptions = createShuffledOptions(q);
        }
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
      RAW_QUIZ.forEach(q => {
        quizState[q.id] = {
          answered: false,
          chosenIndex: -1,
          isCorrect: false,
          shuffledOptions: createShuffledOptions(q)
        };
      });
      try { localStorage.removeItem("podporn_quiz_v1"); } catch (e) {}
      currentSingleIndex = 0;
      rebuildActiveQuestionList();
      updateHeaderQuizBadge();
      renderQuizTopicBar();
      renderQuizDashboardAndCards();
    }

    function getTopicStats(topicId) {
      const subset = topicId === "all" ? RAW_QUIZ : RAW_QUIZ.filter(q => q.topic === topicId);
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
      const pct = answered > 0 ? Math.round((correct / answered) * 100) : null;
      return { total: subset.length, answered, correct, wrong, pct };
    }

    function updateHeaderQuizBadge() {
      const allSt = getTopicStats("all");
      const badgeEl = document.getElementById("header-quiz-badge");
      if (allSt.answered === 0) {
        badgeEl.textContent = `${allSt.total} otázek`;
      } else {
        badgeEl.textContent = `${allSt.pct} % (${allSt.answered}/${allSt.total})`;
      }
    }

    function renderQuizTopicBar() {
      const bar = document.getElementById("quiz-topic-bar");
      bar.innerHTML = "";

      QUIZ_TOPICS.forEach(tp => {
        const st = getTopicStats(tp.id);
        const btn = document.createElement("button");
        const isActive = (quizFilterTopic === tp.id && !onlyMistakesMode);
        btn.className = "topic-pill" + (isActive ? " active" : "");
        btn.onclick = () => selectQuizTopic(tp.id);

        const pctText = st.pct !== null ? `${st.pct}%` : `${st.total}`;
        btn.innerHTML = `
          <span>${tp.title}</span>
          <span class="pill-time">${pctText}</span>
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

      if (st.isCorrect) {
        currentStreak++;
      } else {
        currentStreak = 0;
      }

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

    function buildQuestionCardHTML(qObj, idxInList, totalInList) {
      const st = quizState[qObj.id];
      const letters = ["A", "B", "C", "D"];
      let cardStateClass = "";
      if (st.answered) {
        cardStateClass = st.isCorrect ? "answered-correct" : "answered-wrong";
      }

      const optionsHTML = st.shuffledOptions.map((opt, oIdx) => {
        let btnClass = "option-btn";
        if (st.answered) {
          if (opt.isCorrect) {
            btnClass += " correct-choice";
          } else if (oIdx === st.chosenIndex && !opt.isCorrect) {
            btnClass += " wrong-choice";
          } else {
            btnClass += " dimmed-choice";
          }
        }
        const disabledAttr = st.answered ? "disabled" : "";
        return `
          <button class="${btnClass}" ${disabledAttr} onclick="answerQuestion(${qObj.id}, ${oIdx})">
            <span class="opt-letter">${letters[oIdx]}</span>
            <span style="flex:1;">${opt.text}</span>
          </button>
        `;
      }).join("");

      let explanationHTML = "";
      if (st.answered) {
        const statusTitle = st.isCorrect
          ? "✅ Správná odpověď!"
          : "❌ Pozor, tady byla chyba!";
        const expClass = st.isCorrect ? "explanation-box is-correct" : "explanation-box is-wrong";
        explanationHTML = `
          <div class="${expClass}">
            <div style="font-weight:800; margin-bottom:4px; color:${st.isCorrect ? 'var(--accent-green)' : 'var(--accent-rose)'};">
              ${statusTitle}
            </div>
            <div><strong>Vysvětlení k testu:</strong> ${qObj.exp}</div>
          </div>
        `;
      }

      let navFooterHTML = "";
      if (quizViewMode === "single") {
        const prevDisabled = idxInList <= 0 ? "disabled style='opacity:0.45; cursor:default;'" : "";
        const nextLabel = idxInList < totalInList - 1 ? "Další otázka →" : "Zpět na 1. otázku ↺";
        navFooterHTML = `
          <div class="quiz-nav-footer">
            <div style="display:flex; gap:8px; flex-wrap:wrap;">
              <button class="action-btn" ${prevDisabled} onclick="stepSingleQuestion(-1)">← Předchozí</button>
              ${st.answered ? `<button class="action-btn" onclick="retrySingleQuestion(${qObj.id})">🔄 Zkusit tuto otázku znovu (zamíchat A–D)</button>` : ""}
            </div>
            <button class="next-q-cta" onclick="stepSingleQuestion(1)">
              ${nextLabel}
            </button>
          </div>
        `;
      } else if (st.answered) {
        navFooterHTML = `
          <div style="display:flex; justify-content:flex-end;">
            <button class="action-btn" onclick="retrySingleQuestion(${qObj.id})">🔄 Zkusit tuto otázku znovu</button>
          </div>
        `;
      }

      return `
        <article class="quiz-card ${cardStateClass}" id="qcard-${qObj.id}">
          <div class="quiz-card-top">
            <span class="quiz-topic-tag">${qObj.topic_label}</span>
            <span class="quiz-num-tag">Otázka ${idxInList + 1} z ${totalInList} (#${qObj.id})</span>
          </div>
          <div class="quiz-question-text">${qObj.q}</div>
          <div class="options-grid">
            ${optionsHTML}
          </div>
          ${explanationHTML}
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

      const pctValEl = document.getElementById("quiz-pct-val");
      const pctCircleEl = document.getElementById("pct-circle");

      if (scopeStats.answered === 0) {
        pctValEl.textContent = "— %";
        pctValEl.style.color = "var(--accent-primary)";
        pctCircleEl.style.background = "var(--accent-primary-soft)";
      } else {
        pctValEl.textContent = `${scopeStats.pct} %`;
        if (scopeStats.pct >= 80) {
          pctValEl.style.color = "var(--accent-green)";
          pctCircleEl.style.background = "var(--accent-green-soft)";
        } else if (scopeStats.pct >= 50) {
          pctValEl.style.color = "var(--accent-warm)";
          pctCircleEl.style.background = "var(--accent-warm-soft)";
        } else {
          pctValEl.style.color = "var(--accent-rose)";
          pctCircleEl.style.background = "var(--accent-rose-soft)";
        }
      }

      document.getElementById("stat-correct").textContent = scopeStats.correct;
      document.getElementById("stat-wrong").textContent = scopeStats.wrong;
      document.getElementById("stat-answered").textContent = `${scopeStats.answered} / ${scopeStats.total}`;
      document.getElementById("stat-streak").textContent = `${currentStreak} 🔥`;

      // Progress bars
      const correctWidth = scopeStats.total > 0 ? (scopeStats.correct / scopeStats.total) * 100 : 0;
      const wrongWidth = scopeStats.total > 0 ? (scopeStats.wrong / scopeStats.total) * 100 : 0;
      document.getElementById("bar-correct").style.width = `${correctWidth}%`;
      document.getElementById("bar-wrong").style.width = `${wrongWidth}%`;

      const completionPct = scopeStats.total > 0 ? Math.round((scopeStats.answered / scopeStats.total) * 100) : 0;
      document.getElementById("bar-left-label").textContent =
        scopeStats.answered > 0
          ? `Úspěšnost zodpovězených: ${scopeStats.pct} % (${scopeStats.correct} správně, ${scopeStats.wrong} špatně)`
          : "Zatím nebyla zodpovězena žádná otázka v tomto okruhu";
      document.getElementById("bar-right-label").textContent =
        `Projito ${completionPct} % okruhu (${scopeStats.answered} z ${scopeStats.total} otázek)`;

      // Mistake filter button
      const mistakeBtn = document.getElementById("btn-filter-mistakes");
      const mistakeCntEl = document.getElementById("mistake-count-btn");
      if (allStats.wrong > 0 || onlyMistakesMode) {
        mistakeBtn.style.display = "inline-flex";
        mistakeCntEl.textContent = allStats.wrong;
        mistakeBtn.innerHTML = onlyMistakesMode
          ? `✕ Zrušit filtr chyb (zobrazit vše)`
          : `🔁 Procvičit jen chyby (${allStats.wrong})`;
      } else {
        mistakeBtn.style.display = "none";
      }

      // Render cards
      const container = document.getElementById("quiz-cards-container");
      if (activeQuestionList.length === 0) {
        container.innerHTML = `
          <div class="quiz-card" style="text-align:center; padding:40px 24px;">
            <div style="font-size:22px; font-weight:800; color:var(--accent-green);">🎉 Žádné chybné otázky k opakování!</div>
            <div style="color:var(--text-secondary); margin-top:6px;">Všechny zodpovězené otázky v tomto výběru máš správně.</div>
            <div style="margin-top:14px;">
              <button class="next-q-cta" onclick="selectQuizTopic('all')">Zobrazit všechny otázky (140)</button>
            </div>
          </div>
        `;
        return;
      }

      if (quizViewMode === "single") {
        const qObj = activeQuestionList[currentSingleIndex];
        container.innerHTML = buildQuestionCardHTML(qObj, currentSingleIndex, activeQuestionList.length);
      } else {
        container.innerHTML = activeQuestionList
          .map((qObj, idx) => buildQuestionCardHTML(qObj, idx, activeQuestionList.length))
          .join("");
      }
    }

    /* =========================================================================
       INITIALIZATION & AUDIO / KEYBOARD LISTENERS
       ========================================================================= */
    renderUIForTrack();
    updateDiagram("opt-1");
    initQuizData();

    function togglePlay() {
      if (audio.paused) audio.play();
      else audio.pause();
    }

    audio.addEventListener("play", () => {
      playIcon.textContent = "⏸";
      playLabel.textContent = "Pozastavit";
    });

    audio.addEventListener("pause", () => {
      playIcon.textContent = "▶";
      playLabel.textContent = "Přehrát";
    });

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

      // Quiz mode keyboard shortcuts (A/B/C/D or 1/2/3/4 + Enter/Arrows)
      if (appMode === "quiz" && quizViewMode === "single" && activeQuestionList.length > 0) {
        const curQ = activeQuestionList[currentSingleIndex];
        const keyUpper = e.key.toUpperCase();
        if (["1", "A"].includes(keyUpper)) {
          e.preventDefault();
          answerQuestion(curQ.id, 0);
          return;
        }
        if (["2", "B"].includes(keyUpper)) {
          e.preventDefault();
          answerQuestion(curQ.id, 1);
          return;
        }
        if (["3", "C"].includes(keyUpper)) {
          e.preventDefault();
          answerQuestion(curQ.id, 2);
          return;
        }
        if (["4", "D"].includes(keyUpper)) {
          e.preventDefault();
          answerQuestion(curQ.id, 3);
          return;
        }
        if (e.code === "Enter" || e.code === "ArrowRight") {
          e.preventDefault();
          stepSingleQuestion(1);
          return;
        }
        if (e.code === "ArrowLeft") {
          e.preventDefault();
          stepSingleQuestion(-1);
          return;
        }
      }

      if (e.code === "Space") {
        e.preventDefault();
        togglePlay();
      } else if (e.code === "ArrowRight") {
        seekRelative(10);
      } else if (e.code === "ArrowLeft") {
        seekRelative(-10);
      }
    });
  </script>
</body>
</html>
"""

final_html = (
    HTML_TEMPLATE
    .replace("__PODCAST_DATA_JSON__", data_json_str)
    .replace("__QUIZ_QUESTIONS_JSON__", quiz_json_str)
)

with open(r"k:\podPorn\index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Successfully built k:\\podPorn\\index.html with {len(QUIZ_QUESTIONS)} ABCD questions!")
