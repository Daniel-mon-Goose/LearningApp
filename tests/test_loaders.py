from files.loader import LoaderInterface, CSVLoader
import pytest


def test_raises_exception_on_abstract_instance():
    with pytest.raises(TypeError):
        LoaderInterface()


def test_raises_exception_on_property_setter():
    with pytest.raises(AttributeError):
        CSVLoader('').vocabulary = ''


def test_raises_exception_wrong_format():
    with pytest.raises(ValueError):
        vc = CSVLoader("test.txt").vocabulary


def test_csv_container():
    loader = CSVLoader("test.csv")

    assert loader.vocabulary == {
        'who': ('are', 'you'),
        'a': ('b', 'c')
    }
