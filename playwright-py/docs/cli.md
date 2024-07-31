# Python environments in VS Code

```sh
python3 -m venv .venv
chmod 744 ./.venv/bin/activate
source ./.venv/bin/activate
```

https://code.visualstudio.com/docs/python/environments

# Download Package Manager Tools based on pyproject.toml

```sh
pip install poetry
poetry install --no-root
```

# Install Playwright and Pytest with Plugin

```sh
pip install pytest-playwright
or
poetry add pytest-playwright
```

# Run E2E Test

```sh
pytest --headed --browser chromium --browser firefox --browser webkit
PWDEBUG=1 pytest -s
```

# Report

```sh
pip install pytest-html
pytest -s -v  --headed --browser chromium --browser firefox --browser webkit --html=pwreport.html
```

# Parallelism

```sh
# install dependency
pip install pytest-xdist
# use the --numprocesses flag
pytest --numprocesses auto
```

# requirements.txt

```sh
# exports
pip freeze > requirements.txt
# imports
pip install -r requirements.txt
```