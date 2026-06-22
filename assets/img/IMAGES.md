# Adding your own photos

The site works right now without any photos — every image slot shows a
tasteful placeholder icon until a real file is dropped in at the exact path
below. Recommended size: roughly 1600×1200px (4:3) for property photos and
1200×800px (16:11) for local-guide cards, JPG format, keep each under ~500KB
so the site stays fast.

## Property photos (use your own Airbnb listing photos)

**Traumeri Casita** → `assets/img/casita/`
- `exterior.jpg`
- `living-room.jpg`
- `hot-tub.jpg`
- `bedroom.jpg`
- `kitchen.jpg`

**Traumeri Casa** → `assets/img/casa/`
- `exterior.jpg`
- `living-room.jpg`
- `hot-tub.jpg`
- `bedroom.jpg`
- `kitchen.jpg`

## Local guide photos (optional — generic Sedona scenery)

These live under `assets/img/sedona/<category>/<slug>.jpg`. Run this from
the repo root to print the exact list anytime:

```
grep -ho 'assets/img/sedona/[a-z/-]*\.jpg' casita/index.html | sort -u
```

Categories: `dining/`, `hikes/`, `spiritual/`, `poi/`, `drives/`, `shopping/`.
Each card's exact expected filename is a lowercase, hyphenated version of its
title (e.g. "Devil's Bridge" → `devils-bridge.jpg`). You don't have to fill
all of these in — cards without a matching file just keep their placeholder.
