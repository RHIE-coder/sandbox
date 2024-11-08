python3 -m venv .venv
chmod 744 .venv/bin/activate
source .venv/bin/activate
pip install poetry
poetry install --no-root
playwright install