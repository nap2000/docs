#!/bin/sh

if [ -f ".venv/bin/activate" ]; then
  . ".venv/bin/activate"
else
  echo "Missing .venv. Create it with: python3 -m venv .venv" >&2
  exit 1
fi

# The expression tables are generated from the spec the server checks expressions with
if ! python3 tools/expression_tables.py --check; then
  python3 tools/expression_tables.py || exit 1
  echo "Expression tables updated from form-expressions.json, commit them with the docs" >&2
fi

mkdir -p _build/html
make html
tar -zcf docs.tgz --no-xattrs _build/html
