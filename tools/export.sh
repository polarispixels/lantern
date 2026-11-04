#!/usr/bin/env bash
# Rebuild the web version of the game into site/.
# GitHub Actions can't run PICO-8 (it's a licensed binary), so the export is
# committed. Run this before committing any change to lantern.p8.
set -euo pipefail
cd "$(dirname "$0")/.."
PICO8="${PICO8:-/home/rgris/tools/pico-8/pico8}"

(cd site && "$PICO8" ../lantern.p8 -export index.html)

# The default shell calls every game "PICO-8 Cartridge" and has no icon.
sed -i 's|<title>PICO-8 Cartridge</title>|<title>Lantern</title>\n<link rel="icon" type="image/png" sizes="32x32" href="icon-32.png">\n<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">\n<link rel="apple-touch-icon" href="icon-192.png">|' site/index.html

# Lets the deploy workflow refuse an export that's older than the cart.
sha256sum lantern.p8 > site/cart.sha256
echo "exported site/index.html and site/index.js"
