# Lantern

A tiny miner digs down a mine shaft one screen at a time. The lamp oil never
stops draining, and as it runs low the circle of light around the miner shrinks
until the screen is nearly dark. Gems are worth more the deeper you go, and oil
cans refill the lamp. So: dig deeper for better gems, or stay near the oil?

A proof of concept built in [PICO-8](https://www.lexaloffle.com/pico-8.php).

- **Play:** https://polarispixels.github.io/lantern/
- **Developer & agent docs:** https://polarispixels.github.io/lantern/docs/
- **Agent instructions:** [CLAUDE.md](CLAUDE.md)

## Controls

| Action | Keyboard | Phone |
| --- | --- | --- |
| Move / aim | Arrow keys | On-screen d-pad |
| Dig in the facing direction | X | On-screen X button |

## Working on it

All the code, art and sound live in one file, `lantern.p8`. Drag it onto the
PICO-8 window, type `run`, and use `ctrl+r` to reload after changes.

To publish, re-export and push to `main`:

```bash
tools/export.sh   # rebuilds site/index.html and site/index.js
```

GitHub Actions can't run PICO-8, so the export in `site/` is committed. The
deploy workflow publishes that folder, and fails if `lantern.p8` has changed
since the last export.
