""""This is the test module developed to test the various scenarios where the main code has to behave correctly"""
from project.hashermd5 import Hasher
import pytest

class TestHasherForString:
    def test_harsher_with_string_values(self):
        obj1=Hasher("shantanu")
        assert obj1.hashermd5() == "2e9cc0cc73d64cd2bcdc602eaa8f0759"
    def test_hasher_with_numeric_values(self):
        with pytest.raises(TypeError):
            obj=Hasher(15)

class TestHasherForDict:
    def test_harsher_with_dict_values_string(self):
        obj1=Hasher({"key1":"a","key2":"b"})
        assert obj1.hashermd5()["key1"] == "0cc175b9c0f1b6a831c399e269772661"
    def test_hasher_with_dict_values_number(self):
        with pytest.raises(ValueError):
            Hasher({"key1":123})
    def test_harsher_with_dict_values_mixed(self):
        with pytest.raises(ValueError):
            Hasher({"key1":"a","key2":1})

class TestHasherForList:
    def test_hasher_with_list_values_strings(self):
        obj1=Hasher(["shantanu","a","b"])
        assert obj1.hashermd5() == ["2e9cc0cc73d64cd2bcdc602eaa8f0759","0cc175b9c0f1b6a831c399e269772661","92eb5ffee6ae2fec3ad71c777531578f"]
    def test_hasher_with_list_values_number(self):
        with pytest.raises(ValueError):
            Hasher([1,2,3])
    def test_hasher_with_list_mixed_values(self):
        with pytest.raises(ValueError):
            Hasher(["shantanu",1,"b"])

class TestHasherForTuple:
    def test_hasher_with_tuple_string(self):
        obj1=Hasher(("a","b","shantanu"))
        assert obj1.hashermd5() == ("0cc175b9c0f1b6a831c399e269772661","92eb5ffee6ae2fec3ad71c777531578f","2e9cc0cc73d64cd2bcdc602eaa8f0759")
    def test_hasher_with_tuple_numeric(self):
        with pytest.raises(ValueError):
            obj1=Hasher((1,2,3))
    def test_hasher_with_tuple_mixed(self):
        with pytest.raises(ValueError):
            obj1=Hasher(("shantanu","a",1))




