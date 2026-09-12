from pathlib import Path
import json
import re

ROOT = Path(__file__).parent

PATTERN = re.compile(r"^Day \d+ Part \d+ \d{4}\.py$")

def getStars(year: int) -> int:
    folder = ROOT / f"AOC {year}"

    if not folder.exists():
        return 0

    files = [
        file.name
        for file in folder.iterdir()
        if file.is_file()
    ]

    matching = [
        name
        for name in files
        if PATTERN.fullmatch(name)
    ]

    count = len(matching)

    # AoC 2015-2024 have 50 stars.
    # AoC 2025 onwards has 24 stars (12 days).
    maxStars = 50 if year <= 2024 else 24
    finalDay = 25 if year <= 2024 else 12

    # Account for your repository convention where the final
    # day's Part 1 can represent completion of the day.
    lastFile = f"Day {finalDay} Part 1 {year}.py"

    if count == maxStars - 1 and lastFile in files:
        count = maxStars

    return count

def main():
    years = range(2015, 2026)

    progress = {
        str(year): getStars(year)
        for year in years
    }

    output = ROOT / "aoc-progress.json"

    output.write_text(
        json.dumps(progress, indent=4) + "\n",
        encoding="utf-8"
    )

    print(json.dumps(progress, indent=4))

if __name__ == "__main__":
    main()