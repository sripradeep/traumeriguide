# Traumeri Sedona Guest Guides

A self-hosted guest guide for **Traumeri Casita** and **Traumeri Casa** in
Sedona, AZ — built to replace/extend the Touch Stay guides, styled after
guide.grapevinestays.com, with an expanded local guide covering Sedona
dining, hikes, spiritual/vortex sites, points of interest, scenic drives,
and shopping.

```
traumeriguide/
├── index.html              ← landing page (links to both guides)
├── casita/index.html        ← full Traumeri Casita guide
├── casa/index.html          ← full Traumeri Casa guide
├── assets/
│   ├── css/style.css
│   ├── js/main.js
│   └── img/                 ← add your own photos here (see IMAGES.md)
├── content_data.py          ← all text content, in one place — edit this,
│                              not the HTML, to change copy
└── build.py                 ← regenerates the 3 HTML files from content_data.py
```

## Editing content

Don't hand-edit the HTML files — they're generated. Instead:

1. Edit `content_data.py` (restaurant descriptions, hikes, WiFi password,
   check-in time, anything text-based).
2. Run `python3 build.py` to regenerate `index.html`, `casita/index.html`,
   and `casa/index.html`.
3. Commit and push (see below).

## Adding photos

See `assets/img/IMAGES.md` for the exact filenames the pages expect. The
site renders fine with no photos at all (clean placeholders), so you can
publish now and add real photos whenever you have them — just re-upload to
the same path and refresh.

## Publishing to GitHub Pages

Your repo **github.com/sripradeep/traumeriguide** is already created and
empty. From a terminal, inside this `traumeriguide` folder:

```bash
git init
git branch -M main
git remote add origin https://github.com/sripradeep/traumeriguide.git
git add .
git commit -m "Initial Traumeri Sedona guest guides"
git push -u origin main
```

Then on GitHub:

1. Go to **github.com/sripradeep/traumeriguide → Settings → Pages**.
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Branch: **main**, folder: **/ (root)** → **Save**.
4. GitHub will publish at **https://sripradeep.github.io/traumeriguide/**
   within a minute or two (refresh the Pages settings page to get the live
   link, or check the **Actions** tab for the build status).

To use a custom domain (e.g. `guide.traumeristays.com`) instead, add a
`CNAME` file to this folder containing just that domain, then point a CNAME
DNS record at `sripradeep.github.io` — GitHub's Pages docs walk through the
exact DNS values.

## Updating later

Any time you change `content_data.py`:

```bash
python3 build.py
git add .
git commit -m "Update guide content"
git push
```

GitHub Pages redeploys automatically within a minute of the push.
