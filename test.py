import pytest
import subprocess
from os import path


def test_path():
    mc_filename=path.join(path.curdir, "..")

    print(mc_filename)
    assert True