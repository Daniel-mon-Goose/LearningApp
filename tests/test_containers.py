from packs.containers import CSVContainer, CommonContainer
import csv
import pytest


def test_raises_exception_on_abstract_instance():
    with pytest.raises(TypeError):
        CommonContainer()


def test_csv_container():
    with open("test.csv", "r") as f:
        reader = csv.reader(f)
        container = CSVContainer()
        container.load_data(reader)
        assert container.data == {
            'who': ('are', 'you'),
            'a': ('b', 'c')
        }
