from app.parse_file import count_rows
import unittest
import pytest

def test_count_lines(tmp_path):
    f = tmp_path / "test.csv"
    with open(f, "w") as file:
        file.write("age, name\n12, rrr")
    assert count_rows(f) == 1