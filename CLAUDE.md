# Lantern

A PICO-8 arcade game, built as a proof of concept for learning and fun.

## Concept

A tiny miner digs down a mine shaft one screen at a time. His lamp oil drains
all the time, and as it runs low the circle of light around him shrinks until
the screen is nearly dark. Gems give points, and they're worth more the deeper
you go. Oil cans refill the lamp. The tension: dig deeper for better gems, or
stay near the oil.

## MVP scope (nothing more until the user asks)

1. A 128x128 screen shaft made of 8x8 tiles. Dirt can be dug, rock cannot.
   Each screen is procedurally generated, and falling off the bottom
   generates the next one.
2. A miner that walks, falls with gravity, and digs left, right, or down.
3. An oil meter that drains over time, plus darkness: only a circle around
   the miner is visible, and it shrinks as oil drops.
4. Gems (worth more deeper) and oil cans buried in the dirt.
5. One enemy: a bat that flies back and forth and costs oil on contact.
6. A HUD showing depth, score, and oil. At zero oil, show "lamp out" with the
   final depth and score, then restart on a button press.
7. Controls: arrow keys move/aim, X digs in the facing direction.

## Cart structure

Everything lives in one text-format cart, `lantern.p8`:

- `__lua__`: all game code, kept readable and heavily commented, because the
  user is learning PICO-8 from it. Sections, in order: constants, init/reset,
  level generation, update (player, bats, popups), draw (world, darkness,
  HUD, game over), and small helpers.
- `__gfx__`: placeholder 8x8 sprites. The sprite number *is* the tile id:
  - 0 empty, 1 dirt, 2 rock, 3/4/5 gems (green/blue/red), 6 oil can
  - 7-8 miner walk frames, 9-10 bat flap frames, 11 miner aiming down
- `__sfx__`: 0 dig, 1 gem, 2 oil, 3 bat hit, 4 lamp out, 5 rock clunk.
- The map is generated at runtime with `mset`, so the `__map__` section is
  unused. The play area is map cells (0,0)-(15,14), drawn 8px down to leave
  room for the HUD.

Conventions:
- Standard `_init` / `_update` (30 fps) / `_draw` callbacks.
- Write all Lua in lowercase. PICO-8 shows uppercase letters as glyphs.
- Stay well under the 8192-token limit. Check with `ctrl+p` in the code
  editor, or the token count at the bottom right.
- Level generation never lets a rock touch another rock horizontally or
  diagonally (vertical stacks are fine). That guarantees the miner can never
  be boxed in, so don't break it when tweaking generation.

## Workflow

- The user play-tests in the Windows build of PICO-8: drag `lantern.p8` onto
  the PICO-8 window to load it, then type `run`. Inside PICO-8, `ctrl+r`
  reloads and runs after the file changes on disk.
- Claude cannot play the game. The Linux build in WSL
  (`/home/rgris/tools/pico-8/pico8`, also `pico8` on the login-shell PATH)
  can be used to check that the cart loads, and to export with
  `tools/export.sh`.
- The user reports back on how it plays. Tune constants at the top of the
  `__lua__` section first, before restructuring anything.
- Stray exports in the repo root (`.html`, `.js`, binaries) are git-ignored.

## Deployment

- **Play:** https://polarispixels.github.io/lantern/
- **Docs:** https://polarispixels.github.io/lantern/docs/ (source:
  `site/docs/index.html`)
- **Repo:** https://github.com/polarispixels/lantern (deploys to GitHub Pages on
  push to `main`)
- GitHub Actions can't run PICO-8, so the export in `site/` is committed. After
  changing `lantern.p8`, run `tools/export.sh` and commit `site/` with the cart.
  The deploy fails if `site/cart.sha256` doesn't match the cart.
- If the tuning values or tile table change, update the docs page too.
