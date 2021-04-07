import pytest
from generator.models import Key,Value,Tag

def test_key_constructor():
    # Test Key class
    k = Key() # initialize defaults
    assert k.length == 5
    assert k.inherited == ''
    assert k.isfield == False
    k = Key(10) # custom length
    assert k.length == 10
    k = Key(10, 'tag1')
    assert k
    k = Key(length=10, inherited='cpu_usage')
    assert repr(k) == 'cpu_usage'

def test_value_constructor():
    v = Value() # initialize defaults
    assert v.length == 5
    assert v.inherited == ''
    assert v.isfield == False
    assert v.vtype == 'str'
    v = Value(10)
    assert v.length == 10
    assert repr(v) == v.repr
    v = Value(10, inherited='value')
    assert repr(v) == 'value'

    with pytest.raises(ValueError) as info:
        v = Value(vtype='long')
    assert 'long is not a supported type' == str(info.value)