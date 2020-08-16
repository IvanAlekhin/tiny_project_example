import sys
import os
import pytest

from src.scripts import ShipFinder

BASE_DIR = os.path.join(sys.path[0], 'tests/input_examples')


def test1():
    file_path = os.path.join(BASE_DIR, '1.txt')
    s = ShipFinder(file_path, 'INFO')
    assert s.count_ships() == 5


def test2():
    file_path = os.path.join(BASE_DIR, '2.txt')
    s = ShipFinder(file_path, 'INFO')
    assert s.count_ships() == 1


def test3():
    file_path = os.path.join(BASE_DIR, '3.txt')
    s = ShipFinder(file_path, 'INFO')
    assert s.count_ships() == 0


def test4():
    file_path = os.path.join(BASE_DIR, '4.txt')
    s = ShipFinder(file_path, 'INFO')
    assert s.count_ships() == 10


def test5():
    file_path = os.path.join(BASE_DIR, '5.txt')
    s = ShipFinder(file_path, 'INFO')
    assert s.count_ships() == 1


def test6_heavy():
    file_path = os.path.join(BASE_DIR, '6.txt')
    s = ShipFinder(file_path, 'INFO')
    assert s.count_ships() == 2


def test7_empty_file():
    file_path = os.path.join(BASE_DIR, '7.txt')
    s = ShipFinder(file_path, 'INFO')
    assert s.count_ships() == 0


def test8_ship_bad_location():
    file_path = os.path.join(BASE_DIR, '8.txt')
    s = ShipFinder(file_path, 'INFO')
    with pytest.raises(ValueError):
        s.count_ships()


def test9_file_lines():
    file_path = os.path.join(BASE_DIR, '9.txt')
    s = ShipFinder(file_path, 'INFO')
    with pytest.raises(ValueError):
        s.count_ships()


def test_file_existance():
    file_path = os.path.join(BASE_DIR, 'non_existent_file.txt')
    s = ShipFinder(file_path, 'INFO')
    with pytest.raises(FileNotFoundError):
        s.count_ships()
