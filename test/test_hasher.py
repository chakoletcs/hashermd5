""""This is the test module developed to test the various scenarios where the main code has to behave correctly"""
from project.hashermd5 import Hasher
import hashlib
import pytest

class TestHasher:
    def test_hasher_with_numeric_values(self):
        with pytest.raises(TypeError):
            obj=Hasher(15)
    def test_harsher_with_string_values(self):
        obj1=Hasher("shantanu")
        assert obj1.hashermd5() == "2e9cc0cc73d64cd2bcdc602eaa8f0759"
    def test_hasher_with_dict_values_number(self):
        with pytest.raises(ValueError):
            obj=Hasher({"key1":123})


