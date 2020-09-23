""""This is the test module developed to test the various scenarios"""
from project.hashermd5 import Hasher
import pytest

class TestHasherForString:
    """"test class for testing string as a value"""
    def test_harsher_with_string_values(self):
        """module for testing string"""
        obj1=Hasher("shantanu")
        assert obj1.hashermd5() == "2e9cc0cc73d64cd2bcdc602eaa8f0759"
    def test_hasher_with_numeric_values(self):
        """module for testing numeric"""
        with pytest.raises(TypeError):
            Hasher(15)

class TestHasherForDict:
    """"test class for testing dict as a value"""
    def test_harsher_with_dict_values_string(self):
        """module for testing string"""
        obj1=Hasher({"key1":"a","key2":"b"})
        assert obj1.hashermd5()["key1"] == "0cc175b9c0f1b6a831c399e269772661"
    def test_hasher_with_dict_values_number(self):
        """module for testing numeric"""
        with pytest.raises(ValueError):
            Hasher({"key1":123})
    def test_harsher_with_dict_values_mixed(self):
        """module for testing mixed values"""
        with pytest.raises(ValueError):
            Hasher({"key1":"a","key2":1})

class TestHasherForList:
    """test class for testing list as a value"""
    def test_hasher_with_list_values_strings(self):
        """module for testing string"""
        obj1=Hasher(["shantanu","a","b"])
        assert obj1.hashermd5() == ["2e9cc0cc73d64cd2bcdc602eaa8f0759",
                                    "0cc175b9c0f1b6a831c399e269772661",
                                    "92eb5ffee6ae2fec3ad71c777531578f"]
    def test_hasher_with_list_values_number(self):
        """module for testing numeric"""
        with pytest.raises(ValueError):
            Hasher([1,2,3])
    def test_hasher_with_list_mixed_values(self):
        """module for testing mixed values"""
        with pytest.raises(ValueError):
            Hasher(["shantanu",1,"b"])

class TestHasherForTuple:
    """test class for testing tuple as a value"""
    def test_hasher_with_tuple_string(self):
        """module for testing string"""
        obj1=Hasher(("a","b","shantanu"))
        assert obj1.hashermd5() == ("0cc175b9c0f1b6a831c399e269772661",
                                    "92eb5ffee6ae2fec3ad71c777531578f",
                                    "2e9cc0cc73d64cd2bcdc602eaa8f0759")
    def test_hasher_with_tuple_numeric(self):
        """module for testing numeric value"""
        with pytest.raises(ValueError):
            Hasher((1,2,3))
    def test_hasher_with_tuple_mixed(self):
        """module for testing mixed value"""
        with pytest.raises(ValueError):
            Hasher(("shantanu","a",1))
