# Moomin DVDs — Live Marketplace Tracker (Notion-style)

## Shareable URL
Deploy this folder with **GitHub Pages** or **Netlify**.

### GitHub Pages quick deploy
1. Create a GitHub repo (e.g. `moomin-dvd-tracker`)
2. Upload `index.html`, `data/`, `.github/`, `scripts/`
3. Repo → Settings → Pages → Deploy from branch → `main` → `/ (root)`
4. Your shareable URL: `https://<user>.github.io/<repo>/`

## Daily refresh (optional)
`.github/workflows/daily-refresh.yml` runs once per day and can write `data/live-picks.json`.
Current script is conservative and does NOT scrape marketplaces.

## Edit sources
Open `data/sources.json` and add:
- more countries
- more local big classifieds (Tori/OLX/Marktplaats/…)
- antikvariaatit / used-media shops
- eBay/Amazon/Vinted search URLs

Tip: include multiple name variants per country (e.g., Croatia uses both **Mumini** and **Moomin**).
