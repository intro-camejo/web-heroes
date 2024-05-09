import csv
import os

DATA_FILE = os.path.join(os.environ.get("DATA_PATH", "../../data"), "characters.csv")


def _file_reader() -> list[str]:
    file = open(DATA_FILE)
    reader = csv.reader(file, delimiter = '\t')

    return reader


def _object_from_row(header: list[str], row: list[str]) -> dict[str, str]:
    return {header[i].lower(): row[i] for i in range(len(header))}


def get_all_characters():
    reader = _file_reader()

    header = next(reader)
    return list(map(lambda row: _object_from_row(header, row), reader))


def get_character_by_id(id: int):
    reader = _file_reader()

    header = next(reader)

    for row in reader:
        if str(row[0]) == str(id):
            return _object_from_row(header, row)

    return None
