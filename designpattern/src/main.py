from dataclasses import dataclass
import typer
from typing import Annotated


def main(
    name: Annotated[str, typer.Argument(metavar="NNNNNN", help="who to greet")],
    lastname: Annotated[str, typer.Option(prompt="Please tell me your last name")],
):
    """
    hhhh llll oooo eee 
    """
    print(f"Hello {name} {lastname}")

if __name__ == "__main__":
    typer.run(main)