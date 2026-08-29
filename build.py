#!/usr/bin/env python3
"""
Mustang Codeworks LLC - static site generator.

Everything you normally edit lives in the CONFIG and APPS blocks below.
Change those, run `python3 build.py`, and the whole site regenerates into public/.

    python3 build.py

Cloudflare Pages setup:
    Framework preset ....... None
    Build command .......... (leave empty)
    Build output directory . public

Commit the generated public/ folder so Cloudflare needs no build step at all.
"""

import os
import shutil
from datetime import date

# --------------------------------------------------------------------------
# CONFIG - edit these
# --------------------------------------------------------------------------

SITE = {
    "company":   "Mustang Codeworks LLC",
    "short":     "Mustang Codeworks",
    "domain":    "mustangcodeworks.com",
    "url":       "https://mustangcodeworks.com",
    "tagline":   "Build. Automate. Innovate.",
    "email_support": "support@mustangcodeworks.com",
    "email_privacy": "privacy@mustangcodeworks.com",
    "email_hello":   "hello@mustangcodeworks.com",
    "state":     "Arizona",
    "updated":   date.today().strftime("%B %-d, %Y"),
    "github":    "https://github.com/allenca21",
    "linkedin":  "",   # add your LinkedIn URL
}

# --------------------------------------------------------------------------
# APPS - one entry per product. Fill in the store URLs when you have them.
# `collects` drives the privacy policy. Be accurate: it must match the
# privacy labels you declare in App Store Connect and Play Console.
# --------------------------------------------------------------------------

APPS = [
    {
        "slug": "whats-the-call-baseball",
        "name": "What's the Call? Baseball",
        "family": "What's the Call?",
        "tagline": "Know the rule before the play happens.",
        "blurb": "Scenario-based rules training for baseball umpires, coaches, "
                 "players and parents. Quizzes, rule interpretation chapters, and "
                 "Live Call for in-game situations.",
        "ios_url": "",
        "play_url": "",
        "status": "Live on iOS &middot; Android in progress",
        "collects": ["purchase", "diagnostics"],
        "faq": [
            ("I paid for Pro but it isn't unlocking.",
             "Open Settings and tap Restore Purchases. Purchases are tied to the "
             "store account that bought them, so make sure you're signed in with "
             "the same Apple Account or Google account."),
            ("Which rule set do you use?",
             "Little League rules, updated each season. Rule interpretation "
             "chapters cite the specific rule number so you can check the source."),
            ("Can I use it without a connection?",
             "Yes. Quizzes and rule content work fully offline once downloaded."),
        ],
    },
    {
        "slug": "whats-the-call-softball",
        "name": "What's the Call? Softball",
        "family": "What's the Call?",
        "tagline": "Softball rules, drilled until they're instinct.",
        "blurb": "The softball edition of the What's the Call? rules trainer, with "
                 "its own scenario library and rule interpretation chapters.",
        "ios_url": "",
        "play_url": "",
        "status": "Live on iOS &middot; Android in progress",
        "collects": ["purchase", "diagnostics"],
        "faq": [
            ("I paid for Pro but it isn't unlocking.",
             "Open Settings and tap Restore Purchases, signed in with the store "
             "account that made the original purchase."),
            ("Can I use it without a connection?",
             "Yes. Quizzes and rule content work fully offline once downloaded."),
        ],
    },
    {
        "slug": "whats-the-call-fast-pitch",
        "name": "What's the Call? Fast Pitch",
        "family": "What's the Call?",
        "tagline": "Fast pitch situations, called correctly.",
        "blurb": "Fast pitch rules training built on the same scenario engine, "
                 "tuned to the situations that actually come up on the field.",
        "ios_url": "",
        "play_url": "",
        "status": "Live on iOS &middot; Android in progress",
        "collects": ["purchase", "diagnostics"],
        "faq": [
            ("I paid for Pro but it isn't unlocking.",
             "Open Settings and tap Restore Purchases, signed in with the store "
             "account that made the original purchase."),
            ("Can I use it without a connection?",
             "Yes. Quizzes and rule content work fully offline once downloaded."),
        ],
    },
    {
        "slug": "whats-the-call-flag-football",
        "name": "What's the Call? Flag Football",
        "family": "What's the Call?",
        "tagline": "Flag football rules without the arguments.",
        "blurb": "Rules training for flag football officials, coaches and parents, "
                 "covering the calls that decide games.",
        "ios_url": "",
        "play_url": "",
        "status": "Live on iOS &middot; Android in progress",
        "collects": ["purchase", "diagnostics"],
        "faq": [
            ("I paid for Pro but it isn't unlocking.",
             "Open Settings and tap Restore Purchases, signed in with the store "
             "account that made the original purchase. If a recent purchase failed "
             "to unlock, email support and include your receipt."),
            ("Can I use it without a connection?",
             "Yes. Quizzes and rule content work fully offline once downloaded."),
        ],
    },
    {
        "slug": "voltforge",
        "name": "VoltForge",
        "family": None,
        "tagline": "Field calculations for working electricians.",
        "blurb": "A jobsite reference and calculator built for electricians. "
                 "Transformer sizing with wiring diagrams, load calculations, "
                 "and a launchpad that gets you to the number fast.",
        "ios_url": "",
        "play_url": "",
        "status": "Live on iOS and Google Play",
        "collects": ["purchase", "diagnostics"],
        "faq": [
            ("Are the calculations code-compliant?",
             "VoltForge is a reference tool, not a substitute for the current NEC "
             "or your local amendments. Always verify against the code edition "
             "your jurisdiction has adopted."),
            ("Does it work offline?",
             "Yes. Every calculator runs on-device with no connection required."),
            ("Can I use it in dark conditions?",
             "Yes. Settings has a light and dark theme; dark is easier in a panel "
             "room or after sunset."),
        ],
    },
    {
        "slug": "trace",
        "name": "Trace",
        "family": None,
        "tagline": "See what's tracking you.",
        "blurb": "A privacy tool for everyday people. Background Bluetooth tracker "
                 "detection, a direction finder for locating a tracker near you, "
                 "network exposure checks, and a built-in speed test.",
        "ios_url": "",
        "play_url": "",
        "status": "Live on iOS and Google Play &middot; v1.1.0",
        "collects": ["purchase", "diagnostics"],
        "permissions": [
            ("Bluetooth", "Required to scan for nearby trackers. Scan results are "
                          "processed on your device and are not transmitted to us."),
            ("Location", "iOS and Android both require location permission for any "
                         "app that scans for Bluetooth devices. Trace uses it only "
                         "to enable scanning. Your location is not collected, "
                         "stored, or transmitted."),
            ("Local network", "Used by the network exposure check and speed test to "
                              "read the properties of the Wi-Fi network you're on."),
        ],
        "faq": [
            ("Does Trace send my scan results anywhere?",
             "No. Bluetooth scanning and analysis happen entirely on your device. "
             "Tracker detections are not uploaded."),
            ("Why does Trace need location permission?",
             "Both iOS and Android require location permission for any app that "
             "scans for Bluetooth devices - it's a platform rule, not a Trace "
             "requirement. Trace does not collect or transmit your location."),
            ("The direction finder isn't pointing anywhere.",
             "Signal strength direction finding needs you to move. Walk slowly in "
             "one direction for several seconds and watch whether the signal "
             "strengthens or weakens. Concrete, metal and water all distort it."),
            ("I found a tracker. What should I do?",
             "If you believe you are being followed, contact local law enforcement. "
             "Trace can tell you a device is present; it cannot tell you who owns it."),
        ],
    },
]

# Data categories used in the privacy policies.
COLLECT_LABELS = {
    "purchase":    ("Purchase and subscription status",
                    "Whether you hold an active subscription or purchase, so the "
                    "app can unlock the features you paid for. Handled by Apple, "
                    "Google, and our subscription provider. We never see your "
                    "payment card details."),
    "diagnostics": ("Crash and performance diagnostics",
                    "Anonymous crash reports and basic performance data, used only "
                    "to find and fix defects. Not linked to your identity."),
    "email":       ("Email address",
                    "Only if you write to us for support. Used to answer you, and "
                    "kept no longer than needed to resolve your question."),
}

# --------------------------------------------------------------------------
# Templates
# --------------------------------------------------------------------------

CSS = """
/* Mustang Codeworks LLC - site styles */

:root {
  --electric:  #007AFF;
  --cyber:     #00D1FF;
  --steel:     #C0C6D4;
  --charcoal:  #0A0A0A;

  --bg:        #0A0C0E;
  --bg-raised: #14181C;
  --bg-sunken: #06080A;
  --text:      #EAEEF4;
  --text-dim:  #97A1B0;
  --line:      #232A32;
  --accent:    #2E90FF;
  --accent-dim:#1C6FD0;

  --f-display: "Saira", "Arial Narrow", Arial, sans-serif;
  --f-body:    "IBM Plex Sans", system-ui, -apple-system, sans-serif;
  --f-mono:    "IBM Plex Mono", ui-monospace, Menlo, monospace;

  --measure: 68ch;
  --gutter: 24px;
  --maxw: 1080px;
}

@media (prefers-color-scheme: light) {
  :root:not([data-theme="dark"]) {
    --bg:        #FFFFFF;
    --bg-raised: #F4F6F9;
    --bg-sunken: #EDF0F4;
    --text:      #0D1116;
    --text-dim:  #545E6B;
    --line:      #DDE2E9;
    --accent:    #0064DA;
    --accent-dim:#004CA8;
  }
}

:root[data-theme="light"] {
  --bg:        #FFFFFF;
  --bg-raised: #F4F6F9;
  --bg-sunken: #EDF0F4;
  --text:      #0D1116;
  --text-dim:  #545E6B;
  --line:      #DDE2E9;
  --accent:    #0064DA;
  --accent-dim:#004CA8;
}

* { box-sizing: border-box; }

html { scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  * { transition: none !important; animation: none !important; }
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: var(--f-body);
  font-size: 17px;
  line-height: 1.62;
  -webkit-font-smoothing: antialiased;
}

.wrap { max-width: var(--maxw); margin: 0 auto; padding: 0 var(--gutter); }
.narrow { max-width: 760px; }

a { color: var(--accent); text-underline-offset: 3px; }
a:hover { color: var(--cyber); }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; border-radius: 2px; }

/* ---------- header ---------- */

.site-head {
  border-bottom: 1px solid var(--line);
  background: var(--bg);
  position: sticky; top: 0; z-index: 50;
}
.site-head .wrap {
  display: flex; align-items: center; justify-content: space-between;
  gap: 24px; min-height: 68px;
}
.brand { display: flex; align-items: center; gap: 12px; text-decoration: none; color: var(--text); }
.brand img { height: 34px; width: auto; display: block; }
.brand-fallback {
  font-family: var(--f-display);
  font-weight: 700; font-size: 17px; letter-spacing: .06em; text-transform: uppercase;
}
.brand-fallback span { color: var(--accent); }
.nav { display: flex; gap: 26px; align-items: center; flex-wrap: wrap; }
.nav a {
  font-family: var(--f-display);
  font-size: 13px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase;
  color: var(--text-dim); text-decoration: none;
}
.nav a:hover, .nav a[aria-current="page"] { color: var(--text); }

/* ---------- hero ---------- */

.hero { padding: 92px 0 72px; border-bottom: 1px solid var(--line); background: var(--bg-sunken); }
.eyebrow {
  font-family: var(--f-mono); font-size: 11.5px; letter-spacing: .22em;
  text-transform: uppercase; color: var(--accent); margin: 0 0 20px;
}
h1 {
  font-family: var(--f-display); font-weight: 700;
  font-size: clamp(38px, 6vw, 62px); line-height: 1.02; letter-spacing: -.02em;
  text-wrap: balance; margin: 0 0 20px;
}
.lede { font-size: 19px; line-height: 1.55; color: var(--text-dim); max-width: 60ch; margin: 0; }

/* ---------- sections ---------- */

section { padding: 72px 0; border-bottom: 1px solid var(--line); }
section:last-of-type { border-bottom: none; }

h2 {
  font-family: var(--f-display); font-weight: 700;
  font-size: clamp(25px, 3.4vw, 33px); letter-spacing: -.012em; line-height: 1.15;
  text-wrap: balance; margin: 0 0 14px;
}
h3 {
  font-family: var(--f-display); font-weight: 600;
  font-size: 19px; letter-spacing: -.005em; margin: 34px 0 8px;
}
p { max-width: var(--measure); }
.section-note { color: var(--text-dim); max-width: 62ch; margin: 0 0 36px; }

/* ---------- two-track split ---------- */

.split-band { padding: 0; }
.split { display: grid; grid-template-columns: 1fr 1fr; }
.track { padding: 60px 46px; }
.track:first-child { padding-left: 0; }
.track:last-child { padding-right: 0; border-left: 1px solid var(--line); }
.track h2 { margin-bottom: 10px; }
.track p { color: var(--text-dim); margin: 0 0 22px; }
.track ul { margin: 0 0 26px; padding: 0; list-style: none; }
.track li {
  padding: 8px 0 8px 22px; position: relative;
  border-top: 1px solid var(--line); font-size: 15.5px;
}
.track li:first-child { border-top: none; }
.track li::before {
  content: "\\203A"; position: absolute; left: 2px; top: 8px;
  color: var(--accent); font-weight: 700;
}

/* ---------- buttons ---------- */

.btn {
  display: inline-flex; align-items: center; gap: 9px;
  font-family: var(--f-display); font-weight: 600;
  font-size: 13px; letter-spacing: .09em; text-transform: uppercase;
  padding: 12px 22px; border-radius: 3px; text-decoration: none;
  border: 1px solid var(--accent); color: var(--accent);
  max-width: 100%; overflow-wrap: anywhere;
  transition: background-color .14s ease, color .14s ease;
}
.btn:hover { background: var(--accent); color: #fff; }
.btn-solid { background: var(--accent); color: #fff; }
.btn-solid:hover { background: var(--accent-dim); border-color: var(--accent-dim); color: #fff; }
.btn-row { display: flex; flex-wrap: wrap; gap: 12px; }

/* ---------- app cards ---------- */

.apps { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(310px, 100%), 1fr)); gap: 20px; }
.card {
  background: var(--bg-raised); border: 1px solid var(--line);
  border-radius: 6px; padding: 26px; display: flex; flex-direction: column;
}
.card-top { display: flex; gap: 16px; align-items: flex-start; margin-bottom: 14px; }
.card-icon {
  width: 56px; height: 56px; border-radius: 13px; flex-shrink: 0;
  background: var(--bg-sunken); border: 1px solid var(--line);
  object-fit: cover; display: block;
}
.card h3 { margin: 0 0 3px; font-size: 18px; }
.card .kicker {
  font-family: var(--f-mono); font-size: 11px; letter-spacing: .1em;
  text-transform: uppercase; color: var(--accent);
}
.card p { font-size: 15px; color: var(--text-dim); margin: 0 0 18px; flex-grow: 1; }
.card .status {
  font-family: var(--f-mono); font-size: 11.5px; color: var(--text-dim);
  padding-top: 14px; margin-top: auto; border-top: 1px solid var(--line);
}
.store-row { display: flex; flex-wrap: wrap; gap: 9px; margin-bottom: 4px; }
.store {
  font-family: var(--f-display); font-size: 12px; font-weight: 600;
  letter-spacing: .07em; text-transform: uppercase;
  padding: 8px 14px; border: 1px solid var(--line); border-radius: 3px;
  color: var(--text); text-decoration: none;
}
.store:hover { border-color: var(--accent); color: var(--accent); }
.store[aria-disabled="true"] { opacity: .38; pointer-events: none; }
.card-links { display: flex; gap: 16px; margin-top: 14px; font-size: 13.5px; }

/* ---------- prose (privacy / support) ---------- */

.prose { padding: 60px 0 84px; }
.prose h1 { font-size: clamp(30px, 4.6vw, 42px); margin-bottom: 10px; }
.prose .updated {
  font-family: var(--f-mono); font-size: 12.5px; color: var(--text-dim);
  margin: 0 0 40px; padding-bottom: 22px; border-bottom: 1px solid var(--line);
}
.prose p, .prose li { max-width: var(--measure); }
.prose ul { padding-left: 20px; }
.prose li { margin-bottom: 9px; }
.prose h2 { font-size: 23px; margin-top: 44px; }
.prose h3 { font-size: 17.5px; }
.dl { margin: 0; }
.dl dt {
  font-family: var(--f-display); font-weight: 600; font-size: 16.5px;
  margin-top: 24px; margin-bottom: 5px;
}
.dl dd { margin: 0; color: var(--text-dim); max-width: var(--measure); }

.faq { list-style: none; padding: 0; margin: 0; }
.faq > li { border-top: 1px solid var(--line); padding: 22px 0; margin: 0; max-width: none; }
.faq > li:first-child { border-top: none; }
.faq h3 { margin: 0 0 6px; }
.faq p { margin: 0; color: var(--text-dim); }

.callout {
  border-left: 3px solid var(--accent); background: var(--bg-raised);
  padding: 18px 22px; margin: 30px 0; max-width: var(--measure);
}
.callout p { margin: 0; }

/* ---------- footer ---------- */

.site-foot {
  border-top: 1px solid var(--line); background: var(--bg-sunken);
  padding: 46px 0 56px; margin-top: 0;
}
.foot-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 32px; }
.foot-grid h4 {
  font-family: var(--f-mono); font-size: 11px; letter-spacing: .16em;
  text-transform: uppercase; color: var(--text-dim); margin: 0 0 14px; font-weight: 500;
}
.foot-grid ul { list-style: none; margin: 0; padding: 0; }
.foot-grid li { margin-bottom: 8px; font-size: 14.5px; overflow-wrap: anywhere; }
.foot-grid a { color: var(--text-dim); text-decoration: none; }
.foot-grid a:hover { color: var(--accent); }
.colophon {
  margin-top: 40px; padding-top: 22px; border-top: 1px solid var(--line);
  font-family: var(--f-mono); font-size: 12px; color: var(--text-dim);
  display: flex; flex-wrap: wrap; gap: 8px 20px; justify-content: space-between;
}

@media (max-width: 760px) {
  body { font-size: 16px; }
  .split { grid-template-columns: 1fr; }
  .track { padding: 40px 0; }
  .track:last-child { border-left: none; border-top: 1px solid var(--line); }
  .hero { padding: 62px 0 52px; }
  section { padding: 54px 0; }
  .site-head .wrap { flex-wrap: wrap; padding-top: 12px; padding-bottom: 12px; }
  .nav { gap: 18px; }
}
"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:image" content="{site_url}/assets/img/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0A0C0E">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{root}assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="{root}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Saira:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{root}assets/css/site.css">
</head>
<body>

<header class="site-head">
  <div class="wrap">
    <a class="brand" href="{root}index.html">
      <img src="{root}assets/img/logo-horizontal.svg" alt="{company}"
           onerror="this.style.display='none';this.nextElementSibling.style.display='block';">
      <span class="brand-fallback" style="display:none;">Mustang <span>Codeworks</span></span>
    </a>
    <nav class="nav">
      <a href="{root}apps/index.html"{nav_apps}>Apps</a>
      <a href="{root}consulting/index.html"{nav_consulting}>Consulting</a>
      <a href="{root}support/index.html"{nav_support}>Support</a>
      <a href="{root}privacy/index.html"{nav_privacy}>Privacy</a>
    </nav>
  </div>
</header>
"""

FOOT = """
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <h4>Products</h4>
        <ul>{foot_apps}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="{root}consulting/index.html">Consulting</a></li>
          <li><a href="{root}apps/index.html">All apps</a></li>
          <li><a href="mailto:{email_hello}">{email_hello}</a></li>
        </ul>
      </div>
      <div>
        <h4>Legal &amp; help</h4>
        <ul>
          <li><a href="{root}support/index.html">Support</a></li>
          <li><a href="{root}privacy/index.html">Privacy policies</a></li>
          <li><a href="mailto:{email_support}">{email_support}</a></li>
        </ul>
      </div>
    </div>
    <div class="colophon">
      <span>&copy; {year} {company}. An {state} limited liability company.</span>
      <span>{tagline}</span>
    </div>
  </div>
</footer>

</body>
</html>
"""


def page(path_depth, title, desc, url, body, nav=None):
    root = "../" * path_depth
    navmap = {k: "" for k in ("apps", "consulting", "support", "privacy")}
    if nav:
        navmap[nav] = ' aria-current="page"'
    foot_apps = "".join(
        '<li><a href="{r}apps/index.html#{s}">{n}</a></li>'.format(
            r=root, s=a["slug"], n=a["name"])
        for a in APPS
    )
    head = HEAD.format(
        title=title, desc=desc, url=url, site_url=SITE["url"], root=root,
        company=SITE["company"],
        nav_apps=navmap["apps"], nav_consulting=navmap["consulting"],
        nav_support=navmap["support"], nav_privacy=navmap["privacy"],
    )
    foot = FOOT.format(
        root=root, foot_apps=foot_apps, year=date.today().year,
        company=SITE["company"], state=SITE["state"], tagline=SITE["tagline"],
        email_hello=SITE["email_hello"], email_support=SITE["email_support"],
    )
    return head + body + foot


def store_buttons(app):
    out = []
    if app["ios_url"]:
        out.append('<a class="store" href="{}">App Store</a>'.format(app["ios_url"]))
    else:
        out.append('<a class="store" aria-disabled="true" href="#">App Store &mdash; soon</a>')
    if app["play_url"]:
        out.append('<a class="store" href="{}">Google Play</a>'.format(app["play_url"]))
    else:
        out.append('<a class="store" aria-disabled="true" href="#">Google Play &mdash; soon</a>')
    return '<div class="store-row">' + "".join(out) + "</div>"


def app_card(app, root):
    return """
    <article class="card" id="{slug}">
      <div class="card-top">
        <img class="card-icon" src="{root}assets/img/icon-{slug}.png" alt=""
             onerror="this.style.visibility='hidden';">
        <div>
          {kicker}
          <h3>{name}</h3>
        </div>
      </div>
      <p>{blurb}</p>
      {stores}
      <div class="card-links">
        <a href="{root}support/{slug}.html">Support</a>
        <a href="{root}privacy/{slug}.html">Privacy</a>
      </div>
      <div class="status">{status}</div>
    </article>""".format(
        slug=app["slug"], name=app["name"], blurb=app["blurb"],
        status=app["status"], stores=store_buttons(app), root=root,
        kicker='<div class="kicker">{}</div>'.format(app["family"]) if app["family"] else "",
    )


# --------------------------------------------------------------------------
# Page builders
# --------------------------------------------------------------------------

def build_home():
    cards = "".join(app_card(a, "") for a in APPS[:3])
    body = """
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">{tagline}</p>
    <h1>Software built by someone who had to use it first.</h1>
    <p class="lede">Mustang Codeworks builds mobile applications and provides
    cybersecurity and software consulting. Six apps shipped across iOS and Android,
    and twenty-six years of Navy C4I and defensive cyber operations behind them.</p>
  </div>
</section>

<section class="split-band">
  <div class="wrap">
<div class="split">
  <div class="track">
    <h2>Apps</h2>
    <p>Tools for people doing a specific job, built because the job needed them.</p>
    <ul>
      <li>What&rsquo;s the Call? &mdash; sports rules training, four titles</li>
      <li>VoltForge &mdash; electrician field calculator</li>
      <li>Trace &mdash; consumer privacy and tracker detection</li>
    </ul>
    <div class="btn-row"><a class="btn" href="apps/index.html">See all apps</a></div>
  </div>
  <div class="track">
    <h2>Consulting</h2>
    <p>Cyber operations planning, application security, and full-lifecycle mobile
    development for teams that need a builder, not a briefing.</p>
    <ul>
      <li>Cyber operations planning &amp; DCO</li>
      <li>Application and mobile security review</li>
      <li>End-to-end mobile delivery, design through store release</li>
    </ul>
    <div class="btn-row"><a class="btn" href="consulting/index.html">How I work</a></div>
  </div>
</div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2>Recent work</h2>
    <p class="section-note">A sample. Every app below is live, maintained, and
    supported by the person who wrote it.</p>
    <div class="apps">{cards}</div>
    <div class="btn-row" style="margin-top:28px;">
      <a class="btn" href="apps/index.html">All six apps</a>
    </div>
  </div>
</section>
""".format(tagline=SITE["tagline"], cards=cards)
    return page(0, "{} — {}".format(SITE["short"], SITE["tagline"]),
                "Mobile applications and cybersecurity consulting. Six apps live on "
                "iOS and Android, backed by 26 years of Navy C4I and cyber operations.",
                SITE["url"] + "/", body)


def build_apps():
    cards = "".join(app_card(a, "../") for a in APPS)
    body = """
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Products</p>
    <h1>Apps</h1>
    <p class="lede">Six applications across iOS and Android. Each one has a support
    page and its own privacy policy, linked from its card.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="apps">{cards}</div>
  </div>
</section>
""".format(cards=cards)
    return page(1, "Apps — " + SITE["short"],
                "All apps from Mustang Codeworks: What's the Call?, VoltForge, and Trace.",
                SITE["url"] + "/apps/", body, nav="apps")


def build_consulting():
    body = """
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Consulting</p>
    <h1>Twenty-six years of operations, then six apps in six months.</h1>
    <p class="lede">I spent fourteen years enlisted before commissioning, retired as
    a Lieutenant Commander, and built C4I and defensive cyber capability for the
    fleet. Now I build software. Both halves inform the work.</p>
  </div>
</section>

<section>
  <div class="wrap narrow">
    <h2>What I do</h2>
    <dl class="dl">
      <dt>Cyber operations planning</dt>
      <dd>Defensive cyber operations, CPT support, and the planning work that turns
      an intent into an executable operation. Active TS clearance.</dd>

      <dt>Application &amp; mobile security</dt>
      <dd>Security review of mobile applications and their backends, from someone
      who ships production apps rather than only auditing them.</dd>

      <dt>Full-lifecycle mobile delivery</dt>
      <dd>Design, build, subscription integration, store submission, and the
      post-launch maintenance nobody warns you about. Six apps, two platforms.</dd>

      <dt>Process and reporting tooling</dt>
      <dd>Internal tools that remove repetitive work &mdash; SharePoint and Power BI
      tracking systems, message parsers, reporting automation.</dd>
    </dl>

    <h2>Background</h2>
    <p>Master&rsquo;s in Cybersecurity. Career Navy: fourteen years enlisted, then
    commissioned, retiring as a LCDR with a background in C4I leadership and
    defensive cyber operations. Active Top Secret clearance.</p>

    <h2>Get in touch</h2>
    <p>Availability, rates, and scope are all conversations. The fastest way to
    start one is email.</p>
    <div class="btn-row">
      <a class="btn btn-solid" href="mailto:{email}">{email}</a>
    </div>
  </div>
</section>
""".format(email=SITE["email_hello"])
    return page(1, "Consulting — " + SITE["short"],
                "Cyber operations planning, application security, and full-lifecycle "
                "mobile development. Active TS clearance.",
                SITE["url"] + "/consulting/", body, nav="consulting")


def build_support_index():
    items = "".join(
        '<li><a href="{s}.html">{n}</a></li>'.format(s=a["slug"], n=a["name"])
        for a in APPS)
    body = """
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Help</p>
    <h1>Support</h1>
    <p class="lede">Pick your app below, or write to us directly. A real person
    answers &mdash; usually within two business days.</p>
  </div>
</section>

<section>
  <div class="wrap narrow">
    <h2>By app</h2>
    <ul>{items}</ul>

    <h2>Email us</h2>
    <p>Include your device model, OS version, the app name, and what you expected to
    happen versus what did. If it involves a purchase, include the store receipt.
    That gets it fixed on the first reply instead of the third.</p>
    <div class="btn-row">
      <a class="btn btn-solid" href="mailto:{email}">{email}</a>
    </div>
  </div>
</section>
""".format(items=items, email=SITE["email_support"])
    return page(1, "Support — " + SITE["short"],
                "Support for all Mustang Codeworks apps.",
                SITE["url"] + "/support/", body, nav="support")


def build_support_page(app):
    faq = "".join(
        "<li><h3>{q}</h3><p>{a}</p></li>".format(q=q, a=a)
        for q, a in app["faq"])
    body = """
<div class="wrap narrow prose">
  <p class="eyebrow">Support</p>
  <h1>{name}</h1>
  <p class="updated">{status} &nbsp;&middot;&nbsp; Updated {updated}</p>

  <p>{blurb}</p>

  <h2>Common questions</h2>
  <ul class="faq">{faq}</ul>

  <h2>Still stuck?</h2>
  <p>Email <a href="mailto:{email}">{email}</a> with your device model, OS version,
  and what happened. Purchase problems go faster if you attach the store receipt.
  We answer within two business days.</p>

  <div class="callout">
    <p><strong>Privacy:</strong> see the <a href="../privacy/{slug}.html">{name}
    privacy policy</a> for exactly what this app does and does not collect.</p>
  </div>
</div>
""".format(name=app["name"], status=app["status"], blurb=app["blurb"],
           faq=faq, email=SITE["email_support"], slug=app["slug"],
           updated=SITE["updated"])
    return page(1, "{} Support — {}".format(app["name"], SITE["short"]),
                "Support and frequently asked questions for {}.".format(app["name"]),
                "{}/support/{}.html".format(SITE["url"], app["slug"]),
                body, nav="support")


def build_privacy_index():
    items = "".join(
        '<li><a href="{s}.html">{n}</a></li>'.format(s=a["slug"], n=a["name"])
        for a in APPS)
    body = """
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">Legal</p>
    <h1>Privacy</h1>
    <p class="lede">Each app has its own policy, because each app handles different
    things. The short version is the same across all of them: we collect as little
    as possible, and we do not sell anything about you.</p>
  </div>
</section>

<section>
  <div class="wrap narrow">
    <h2>Policies by app</h2>
    <ul>{items}</ul>

    <h2>The short version</h2>
    <ul>
      <li>We do not sell or share your personal information.</li>
      <li>We do not use third-party advertising or tracking SDKs.</li>
      <li>Purchases are handled by Apple and Google. We never see your card details.</li>
      <li>App content works on your device; we pull as little to our servers as we can.</li>
    </ul>

    <h2>Questions</h2>
    <p>Write to <a href="mailto:{email}">{email}</a>.</p>
  </div>
</section>
""".format(items=items, email=SITE["email_privacy"])
    return page(1, "Privacy — " + SITE["short"],
                "Privacy policies for all Mustang Codeworks apps.",
                SITE["url"] + "/privacy/", body, nav="privacy")


def build_privacy_page(app):
    collected = "".join(
        "<dt>{t}</dt><dd>{d}</dd>".format(t=COLLECT_LABELS[k][0], d=COLLECT_LABELS[k][1])
        for k in app["collects"])

    perms = ""
    if app.get("permissions"):
        rows = "".join("<dt>{t}</dt><dd>{d}</dd>".format(t=t, d=d)
                       for t, d in app["permissions"])
        perms = """
  <h2>Permissions this app requests</h2>
  <p>Each permission below exists for a specific feature. If you deny one, that
  feature stops working &mdash; nothing else changes.</p>
  <dl class="dl">{rows}</dl>
""".format(rows=rows)

    body = """
<div class="wrap narrow prose">
  <p class="eyebrow">Privacy policy</p>
  <h1>{name}</h1>
  <p class="updated">Last updated {updated}</p>

  <p>This policy explains what {name} collects, why, and what we do with it.
  {name} is published by {company}, {state}, United States.</p>

  <div class="callout">
    <p><strong>In one sentence:</strong> {name} collects the minimum needed to work
    and to fix defects, does not sell or share your personal information, and
    contains no third-party advertising or tracking SDKs.</p>
  </div>

  <h2>What we collect</h2>
  <dl class="dl">{collected}</dl>
{perms}
  <h2>What we do not collect</h2>
  <ul>
    <li>We do not collect your name, address, or contact details unless you email us.</li>
    <li>We do not collect or store your location.</li>
    <li>We do not build advertising profiles, and we do not use advertising SDKs.</li>
    <li>We do not sell, rent, or share personal information with data brokers.</li>
  </ul>

  <h2>Who processes data on our behalf</h2>
  <p>We use a small number of service providers to run the app. Each one only
  receives what it needs:</p>
  <ul>
    <li><strong>Apple and Google</strong> &mdash; app distribution and payment processing.</li>
    <li><strong>RevenueCat</strong> &mdash; subscription and purchase status.</li>
    <li><strong>Supabase</strong> &mdash; content delivery for in-app material.</li>
  </ul>

  <h2>Children</h2>
  <p>{name} is not directed to children under 13, and we do not knowingly collect
  personal information from children. If you believe a child has provided us
  information, email us and we will delete it.</p>

  <h2>Your rights</h2>
  <p>Depending on where you live, you may have the right to request access to,
  correction of, or deletion of your personal information, and to object to certain
  processing. Because we hold so little, most requests are answered quickly. Write
  to <a href="mailto:{email}">{email}</a>.</p>

  <h2>Data retention</h2>
  <p>Diagnostic data is retained only as long as needed to diagnose and fix defects.
  Support emails are kept until your question is resolved and then deleted on a
  routine schedule.</p>

  <h2>Changes to this policy</h2>
  <p>If we change what we collect, we will update this page and the date at the top.
  Material changes will be noted in the app&rsquo;s release notes.</p>

  <h2>Contact</h2>
  <p>{company}<br>
  Email: <a href="mailto:{email}">{email}</a></p>
</div>
""".format(name=app["name"], company=SITE["company"], state=SITE["state"],
           collected=collected, perms=perms, email=SITE["email_privacy"],
           updated=SITE["updated"])
    return page(1, "{} Privacy Policy — {}".format(app["name"], SITE["short"]),
                "Privacy policy for {}.".format(app["name"]),
                "{}/privacy/{}.html".format(SITE["url"], app["slug"]),
                body, nav="privacy")


# --------------------------------------------------------------------------
# Write everything out
# --------------------------------------------------------------------------

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  " + os.path.relpath(path, OUT))


HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "public")

def main():
    # public/ is generated, but assets/img/ holds files you added by hand
    # (logo, favicon, app icons). Preserve them across rebuilds.
    img_dir = os.path.join(OUT, "assets", "img")
    keep = {}
    if os.path.isdir(img_dir):
        for name in os.listdir(img_dir):
            path = os.path.join(img_dir, name)
            if os.path.isfile(path) and name != "README.txt":
                with open(path, "rb") as f:
                    keep[name] = f.read()

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    print("Building into public/ ...")

    write(os.path.join(OUT, "index.html"), build_home())
    write(os.path.join(OUT, "apps", "index.html"), build_apps())
    write(os.path.join(OUT, "consulting", "index.html"), build_consulting())
    write(os.path.join(OUT, "support", "index.html"), build_support_index())
    write(os.path.join(OUT, "privacy", "index.html"), build_privacy_index())

    for app in APPS:
        write(os.path.join(OUT, "support", app["slug"] + ".html"), build_support_page(app))
        write(os.path.join(OUT, "privacy", app["slug"] + ".html"), build_privacy_page(app))

    write(os.path.join(OUT, "assets", "css", "site.css"), CSS.strip() + "\n")

    # Cloudflare Pages: security headers
    write(os.path.join(OUT, "_headers"), """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains

/assets/*
  Cache-Control: public, max-age=31536000, immutable
""")

    # Cloudflare Pages: tidy URLs and legacy paths
    write(os.path.join(OUT, "_redirects"), """# Short links you can print or hand out
/support/*   /support/:splat.html   200
/privacy/*   /privacy/:splat.html   200
/apps        /apps/index.html       301
""")

    write(os.path.join(OUT, "robots.txt"),
          "User-agent: *\nAllow: /\n\nSitemap: {}/sitemap.xml\n".format(SITE["url"]))

    urls = ["/", "/apps/", "/consulting/", "/support/", "/privacy/"]
    urls += ["/support/{}.html".format(a["slug"]) for a in APPS]
    urls += ["/privacy/{}.html".format(a["slug"]) for a in APPS]
    today = date.today().isoformat()
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sm += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        sm += "  <url><loc>{}{}</loc><lastmod>{}</lastmod></url>\n".format(
            SITE["url"], u, today)
    sm += "</urlset>\n"
    write(os.path.join(OUT, "sitemap.xml"), sm)

    # placeholder so the assets/img folder survives in git
    os.makedirs(os.path.join(OUT, "assets", "img"), exist_ok=True)
    write(os.path.join(OUT, "assets", "img", "README.txt"),
          "Drop these files here (see the project README for exact sizes):\n"
          "  logo-horizontal.svg\n  favicon.svg\n  favicon-32.png\n"
          "  apple-touch-icon.png\n  og-image.png\n"
          + "".join("  icon-{}.png\n".format(a["slug"]) for a in APPS))

    for name, blob in keep.items():
        with open(os.path.join(OUT, "assets", "img", name), "wb") as f:
            f.write(blob)
    if keep:
        print("  (kept {} image{} in assets/img/)".format(
            len(keep), "" if len(keep) == 1 else "s"))

    print("\nDone. {} pages.".format(5 + len(APPS) * 2))


if __name__ == "__main__":
    main()
