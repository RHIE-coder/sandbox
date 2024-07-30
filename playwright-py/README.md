```sh
python -m venv venv
```

## Python environments in VS Code

https://code.visualstudio.com/docs/python/environments

```sh
pytest --headed --browser chromium --browser firefox --browser webkit
```

## Report

```sh
pip install pytest-html

pytest -s -v  --headed --browser chromium --browser firefox --browser webkit --html=pwreport.html
```

## Debug Mode

```sh
PWDEBUG=1 pytest -s
```