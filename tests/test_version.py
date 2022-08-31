import pytest
import semtemver


def test_version():
    assert semtemver.__version__ is not None
