"""Warm white and beige theme with small floral accents for the Streamlit app."""

CSS = """
<style>
:root {
  /* Neutral base: warm white and beige */
  --paper: #faf6ef;
  --card: #fffdf9;
  --beige: #f3ece1;
  --line: #e6dccd;
  --ink: #2f2a26;
  --muted: #6f655b;
  /* Small colorful accents */
  --rose: #b03a5b;
  --rose-soft: #f2c4d2;
  --lavender: #b39ddb;
  --sage: #8fae8b;
  --gold: #d9a441;
  --stripe: linear-gradient(90deg, #e57399, #f4a6c0 25%, #b39ddb 50%, #8fae8b 75%, #e6b450);
}

.stApp { background: var(--paper); }

/* Falling petals */
.petals { position: fixed; inset: 0; pointer-events: none; overflow: hidden; z-index: 0; }
.petals span {
  position: absolute; top: -10vh; opacity: .22;
  animation: fall linear infinite;
}
@keyframes fall {
  0%   { transform: translate(0, 0) rotate(0deg); }
  50%  { transform: translate(40px, 55vh) rotate(180deg); }
  100% { transform: translate(-20px, 115vh) rotate(360deg); }
}
@media (prefers-reduced-motion: reduce) { .petals { display: none; } }

/* Header */
.hero {
  position: relative; z-index: 1;
  text-align: center; padding: 1.6rem 1rem 1.2rem; margin-bottom: 1rem;
  border-radius: 20px; overflow: hidden;
  background: var(--card); border: 1px solid var(--line);
  box-shadow: 0 6px 20px rgba(47,42,38,.06);
}
.hero::before { content: ""; position: absolute; inset: 0 0 auto 0; height: 5px; background: var(--stripe); }
.hero h1 {
  margin: 0; font-size: 2.6rem; color: var(--ink); letter-spacing: .5px;
  font-family: Georgia, "Times New Roman", serif;
}
.hero p { margin: .35rem 0 0; color: var(--muted); font-size: 1.05rem; }

.section-title {
  font-family: Georgia, serif; font-size: 1.4rem; color: var(--rose);
  margin: .6rem 0 .1rem;
}
.section-sub { color: var(--muted); margin-bottom: .8rem; }

/* Featured cards */
[class*="st-key-featcard"], [class*="st-key-card-"] {
  background: var(--card);
  border-radius: 16px; padding: 1rem .9rem .9rem;
  border: 1px solid var(--line); border-top: 4px solid var(--accent, var(--rose-soft));
  box-shadow: 0 3px 12px rgba(47,42,38,.05);
  transition: transform .25s ease, box-shadow .25s ease;
  height: 100%;
}
[class*="st-key-featcard"]:hover, [class*="st-key-card-"]:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 22px rgba(47,42,38,.10);
}
.st-key-featcard-0 { --accent: #e57399; }
.st-key-featcard-1 { --accent: #b39ddb; }
.st-key-featcard-2 { --accent: #f4a6c0; }
.st-key-featcard-3 { --accent: #8fae8b; }
.st-key-featcard-4 { --accent: #e6b450; }
.card-flower { font-size: 1.8rem; line-height: 1; }
.card-name { font-weight: 700; font-family: Georgia, serif; font-size: 1.05rem; margin: .3rem 0 .15rem; }
.card-meta { color: var(--muted); font-size: .85rem; margin-bottom: .4rem; }
.card-teaser { font-size: .92rem; color: var(--ink); }

.stButton > button {
  border-radius: 999px; border: 1px solid var(--line);
  background: var(--card);
  color: var(--rose); font-weight: 600;
  transition: transform .15s ease, box-shadow .15s ease;
}
.stButton > button:hover {
  transform: scale(1.02); color: #fff; border-color: var(--rose);
  background: var(--rose);
  box-shadow: 0 4px 12px rgba(176,58,91,.22);
}

/* Chat bubbles */
.chat { position: relative; z-index: 1; display: flex; flex-direction: column; gap: .9rem; margin: 1rem 0 1.5rem; }
.row { display: flex; align-items: flex-end; gap: .55rem; animation: bloom .35s ease-out both; }
.row.user { flex-direction: row-reverse; }
.chat .row, .hero { scroll-margin-top: 4.5rem; }
.avatar {
  flex: 0 0 auto; width: 2.4rem; height: 2.4rem; border-radius: 50%;
  display: grid; place-items: center; font-size: 1.3rem;
  background: var(--card); border: 1px solid var(--line); box-shadow: 0 2px 6px rgba(47,42,38,.08);
}
.bubble {
  max-width: min(75%, 680px); padding: .8rem 1.05rem; line-height: 1.5;
  border-radius: 18px; box-shadow: 0 2px 10px rgba(47,42,38,.05);
  word-wrap: break-word;
}
.row.user .bubble {
  color: var(--ink); border-bottom-right-radius: 6px;
  background: var(--beige); border: 1px solid var(--line); border-right: 3px solid var(--rose-soft);
}
.row.bot .bubble {
  color: var(--ink); border-bottom-left-radius: 6px;
  background: var(--card); border: 1px solid var(--line); border-left: 3px solid var(--sage);
}
.typing span {
  display: inline-block; width: .5rem; height: .5rem; margin: 0 .12rem; border-radius: 50%;
  background: var(--rose-soft); animation: pulse 1s infinite ease-in-out;
}
.typing span:nth-child(2) { animation-delay: .15s; background: var(--lavender); }
.typing span:nth-child(3) { animation-delay: .3s; background: var(--sage); }
@keyframes pulse { 0%, 100% { transform: scale(.6); opacity: .5; } 50% { transform: scale(1); opacity: 1; } }
@keyframes bloom { from { opacity: 0; transform: translateY(10px) scale(.97); } to { opacity: 1; transform: none; } }

.empty {
  text-align: center; color: var(--muted); padding: 1.2rem; border-radius: 16px;
  border: 1.5px dashed var(--line); background: var(--card);
}

[data-testid="stChatInput"] textarea { font-size: 1rem; }
[data-testid="stChatInput"] > div {
  border-radius: 999px !important; border: 1.5px solid var(--line) !important;
  background: var(--card) !important; box-shadow: 0 4px 14px rgba(47,42,38,.06);
}
hr { border-color: var(--line) !important; }

/* Prominent figure cards get a gold edge and a badge */
[class*="st-key-card-prom-"] { --accent: var(--gold); }
[class*="st-key-card-find-"] { --accent: var(--rose-soft); }
.badge {
  display: inline-block; font-size: .72rem; font-weight: 700; letter-spacing: .3px;
  padding: .12rem .55rem; border-radius: 999px; margin-bottom: .3rem;
  color: #7a5200; background: #fdeec8; border: 1px solid #f1d38b;
}
.card-tagline { font-size: .9rem; color: var(--ink); margin-bottom: .5rem; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] { gap: .4rem; flex-wrap: wrap; }
.stTabs [data-baseweb="tab"] {
  border-radius: 999px; padding: .35rem 1rem; background: var(--card);
  border: 1px solid var(--line);
}
.stTabs [aria-selected="true"] { background: var(--beige); border-color: var(--rose-soft); color: var(--rose); }
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none; }

.result-count { color: var(--muted); margin: .3rem 0 .8rem; font-size: .95rem; }

/* Sources under each answer */
.sources {
  margin-top: .7rem; padding-top: .55rem; border-top: 1px dashed var(--line);
  font-size: .8rem; color: var(--muted);
}
.sources-title { font-weight: 700; color: var(--rose); margin-bottom: .2rem; letter-spacing: .3px; }
.sources ol { margin: 0; padding-left: 1.1rem; }
.sources li { margin: .1rem 0; }
.sources a { color: var(--rose); }

/* Profile dialog */
.profile-meta { color: var(--muted); margin: -.3rem 0 .8rem; }
.profile-burial {
  background: var(--beige); border-left: 4px solid var(--gold); border-radius: 10px;
  padding: .6rem .8rem; margin: .4rem 0 1rem; font-size: .92rem;
}
.timeline { border-left: 3px solid var(--rose-soft); margin: .3rem 0 1rem .4rem; padding-left: 1rem; }
.timeline div { margin: .35rem 0; }
.timeline b { color: var(--rose); }
.cite { font-size: .72rem; color: var(--muted); vertical-align: super; }

/* Hide the zero-height helper frame used for auto-scroll */
.st-key-autoscroll { position: absolute !important; height: 0 !important; width: 0 !important; overflow: hidden; }
</style>
"""
