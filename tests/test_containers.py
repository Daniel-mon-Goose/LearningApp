from files.loader import LoaderInterface, CSVLoader
import pytest


def test_raises_exception_on_abstract_instance():
    with pytest.raises(TypeError):
        LoaderInterface()


def test_csv_container():
    loader = CSVLoader()
    data = loader.get_vocabulary("test.csv")
    assert data == {
        'who': ('are', 'you'),
        'a': ('b', 'c')
    }
