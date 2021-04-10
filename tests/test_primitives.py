import pytest
import sys
sys.path.append(f"")
import re
import datetime
from generator.runconfig import * # provides values to use in tests like `num_tags` et al
from primitives import Key,Value,Tag,Field,Timestamp


def test_key_constructor():
    # Test Key class
    k = Key(10) # custom length
    assert k.length == 10

def test_value_constructor():
    v = Value(10)
    assert v.length == 10
    assert type(v.text) == str  
    with pytest.raises(ValueError) as info:
        v = Value(vtype='long')
    assert 'long is not a supported type' == str(info.value)

def test_tag_constructor():
    k, v = Key(), Value()
    t = Tag(key=k, val=v)
    assert t
    assert t.text.startswith('tag_') == True

def test_field_construtor():
    k, v = Key(isfield=True), Value(vtype='int')
    f = Field(key=k, val=v)
    assert f.text.endswith('i') == True
    k, v = Key(isfield=True), Value(vtype='float')
    f = Field(key=k, val=v)
    assert "." in f.text



