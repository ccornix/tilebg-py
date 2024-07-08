#!/usr/bin/env sh

set -e

# Ensure working directory is the script directory
# https://stackoverflow.com/a/29835459
CDPATH='' cd -- "$(dirname -- "$0")"

for pyfile in ../src/tilebg/patterns/*.py; do
  bname="${pyfile##*/}"
  name="${bname%.py}"
  [ "$name" = __init__ ] && continue
  echo "Generating $name..."
  python -m tilebg "$name" > "$name.svg"
done
