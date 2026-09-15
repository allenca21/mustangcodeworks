# mustangcodeworks.com

Static site for Mustang Codeworks. Company pages, an app directory with store
links, and the per-app **support** and **privacy** pages that Apple and Google
require for every listing.

No framework, no build step at deploy time, no dependencies. Just HTML and CSS.

---

## Deploy to Cloudflare Pages

1. Create a GitHub repo and push this folder.

   ```bash
   git init
   git add .
   git commit -m "Initial site"
   git branch -M main
   git remote add origin git@github.com:allenca21/mustangcodeworks.git
   git push -u origin main
   ```

2. In the Cloudflare dashboard: **Workers & Pages → Create → Pages → Connect to Git**,
   pick the repo, then set:

   | Setting | Value |
   |---|---|
   | Framework preset | **None** |
   | Build command | *(leave empty)* |
   | Build output directory | `public` |

3. **Custom domains → Set up a domain →** `mustangcodeworks.com`, and add `www` too.
   Cloudflare handles DNS and the SSL certificate automatically since the domain is
   already on your account.

Every `git push` to `main` redeploys in about thirty seconds. Pull requests get
their own preview URL.

---

## Editing the site

Everything you'd normally change lives at the top of `build.py`:

- **`SITE`** — company details and the three email addresses.
- **`APPS`** — one entry per product. This single list drives the app cards, the
  store buttons, the footer, the sitemap, and both the support and privacy pages.

After editing:

```bash
python3 build.py
```

That regenerates `public/`. Commit both `build.py` and `public/`.

To preview locally before pushing:

```bash
cd public && python3 -m http.server 8000
```

Then open http://localhost:8000.

**Adding a seventh app** is one new dict in `APPS` — you get its card, support page,
privacy policy, footer entry, and sitemap row for free.

---

## Store links

Every app currently shows a greyed-out "App Store — soon" button, because the URLs
are blank. Fill in `ios_url` and `play_url` in `APPS` and the buttons go live.

Find them at:
- **App Store** — App Store Connect → your app → the marketing URL, or just the
  public listing URL.
- **Google Play** — Play Console → your app → the store listing URL.

---

## Images to add

Drop these into `public/assets/img/`. The site degrades gracefully if any are
missing — the logo falls back to a styled text wordmark, and app icons hide
themselves — so you can deploy today and add art later.

| File | Size | Notes |
|---|---|---|
| `logo-horizontal.svg` | vector | Header lockup. Use the **white-on-dark** variant. |
| `favicon.svg` | vector | See the note below about small sizes. |
| `favicon-32.png` | 32×32 | Fallback for older browsers. |
| `apple-touch-icon.png` | 180×180 | iOS home screen. |
| `og-image.png` | 1200×630 | Link preview card for social and iMessage. |
| `icon-<slug>.png` | 180×180 | One per app; slugs are listed in `assets/img/README.txt`. |

### About the favicon

The full logo has a lot of mane detail. At 32×32 — and especially at the 16×16 the
browser tab actually uses — that detail turns to mush. Make the favicon from a
**simplified** element instead: either the `</>` glyph alone, or a flat single-colour
horse-head silhouette with the interior detail removed. Test it at actual size in a
browser tab before committing to it.

---

## What's in here

```
build.py              Site generator. Edit SITE and APPS at the top.
public/               Generated output — this is what Cloudflare serves.
  index.html          Home: apps and consulting as two equal paths
  apps/               All six apps with store links
  consulting/         Services and background
  support/            Index + one page per app
  privacy/            Index + one policy per app
  assets/css/         Single stylesheet
  assets/img/         Your logo and icons go here
  _headers            Security headers + asset caching
  _redirects          Tidy URLs (/support/trace works without .html)
  robots.txt
  sitemap.xml
```

---

## Before you publish: read the privacy policies

The privacy policies are **drafts written from what the apps appear to do** — they
are not legal advice, and I am not a lawyer. Each one must be checked against what
your apps actually do before it goes live, because:

- Apple and Google both require your policy to match the privacy labels you declare
  in App Store Connect and Play Console. A mismatch is a review rejection, and a
  false declaration is worse than a rejection.
- The draft lists **RevenueCat** and **Supabase** as processors. Remove any you
  don't actually use in that app, and add any you do.
- **Trace needs the closest read.** It's a privacy product, so its policy is part of
  the product promise. The draft states that Bluetooth scan results stay on-device
  and that location is never collected or transmitted — verify both claims against
  the code before you publish them.
- If you have EU or UK users, GDPR wants a stated legal basis for each purpose. If
  you have California users, CCPA wants specific disclosures. Neither is in this
  draft.

The `collects` list in each `APPS` entry drives the "What we collect" section, so
correcting the policy usually means correcting that list and rebuilding.
