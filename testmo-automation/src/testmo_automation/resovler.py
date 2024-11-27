from pathlib import Path

def upward_searching(*, from_path=None, to_find, until_reach=None):
    reached_rootpath = False

    if to_find is None:
        raise ReferenceError(f"'to_find' argument is not defined")
    to_find = Path(to_find)

    if from_path is None:
        from_path = "."
    from_path = Path(from_path)

    if until_reach is None:
        until_reach = "/"
    until_reach = Path(until_reach)

    current_path = Path(from_path).resolve()

    while not reached_rootpath:
        findpath = current_path / to_find
        if findpath.exists():
            return findpath

        if findpath == until_reach:
            reached_rootpath = True

        current_path = current_path.parent

    raise LookupError(f"{to_find} not found before reaching {until_reach}")

def get_project_path():
    pyproject_path = upward_searching(from_path=Path("."), to_find="pyproject.toml")
    return pyproject_path.parent