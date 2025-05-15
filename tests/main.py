import pytest

def text():

    return "test"

def testText():

    assert text() == "test"
