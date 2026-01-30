#!/bin/sh

if [ -f ".venv/bin/activate" ]; then
  . ".venv/bin/activate"
else
  echo "Missing .venv. Create it with: python3 -m venv .venv" >&2
  exit 1
fi

mkdir -p _build/html
make html
tar -zcf docs.tgz _build/html
