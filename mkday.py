#!/bin/env python3

import argparse
from datetime import datetime
from pathlib import Path
import shutil
from typing import Tuple
import os

import requests

import secret


def init_dir(year: int, day: int) -> Tuple[Path, bool]:
    """returns the created directory and whether it was new"""
    directory = Path(f"{year}")/f"day{day}"
    if os.path.exists(directory): # already exists
        return directory, False
    directory.mkdir(parents=True)
    shutil.copy("templates/template.py", directory / "solution.py")
    return directory, True


def download_input(year: int, day: int, user: str, directory: Path) -> None:
    """downloads input for day and year from user"""
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookie = secret.users[user]
    headers = {"Cookie": cookie}
    with requests.get(url, timeout=10, headers=headers) as res:
        # TODO: error handling
        input_file = directory / "input"
        input_file.touch()
        with input_file.open("wb") as fileh:
            for chunk in res.iter_content(chunk_size=128):
                fileh.write(chunk)


def main() -> None:
    now = datetime.now()

    parser = argparse.ArgumentParser(prog="AOC templater")
    parser.add_argument(
        "-y",
        "--year",
        required=False,
        help="which year",
        default=now.year,
        type=int,
    )
    parser.add_argument(
        "-d", "--day", required=False, help="which day", default=now.day, type=int
    )
    args = parser.parse_args()

    directory, new = init_dir(args.year, args.day)
    if not new:
        return
    download_input(args.year, args.day, user="default", directory=directory)


if __name__ == "__main__":
    main()
