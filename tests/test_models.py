import pytest
import sys
print(sys.path)
import re
import datetime
from ..generator.config import * # provides values to use in tests like `num_tags` et al
from ..generator.primitives import Key,Value,Tag,Field,Timestamp


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

def test_one_tag_tagset():
    tag_key = Key()
    tag_value = Value()
    tag = Tag(key=tag_key, val=tag_value)
    tagset = Tagset([tag])
    assert len(tagset.__dict__) > 1

def test_multi_tag_tagset():
    num_tags = 3
    tags = []
    for t in range(num_tags):
        tags.append(Tag())
    tagset = Tagset(tags)
    assert tagset.tags[0] != tagset.tags[1]
    assert len(tagset.tags) == num_tags
    assert repr(tagset)

def test_only_ints_fieldset():
    int_fields = 5
    fields = []
    for t in range(int_fields):
        fields.append(Field(key=Key(isfield=True))) # Field() defaults `vtype` to 'int'
    fieldset = Fieldset(fields)
    assert fieldset.fields[0] != fieldset.fields[1]
    assert re.search("tag_", fieldset.text) == None
    assert len(re.findall(",", fieldset.text)) == int_fields-1

def test_mixed_types_fieldset():
    # int_fields, float_fields, str_fields, bool_fields = 1, 2, 1, 1
    fields = []
    key = Key(isfield=True)
    for i in range(int_fields):
        key = Key(isfield=True)
        field = Field(key=key)
        fields.append(field)
    for f in range(float_fields):
        key = Key(isfield=True)
        val = Value(vtype='float')
        field = Field(key, val)
        fields.append(field)
    for s in range(str_fields):
        key = Key(isfield=True)
        val = Value(vtype='str')
        field = Field(key, val)
        fields.append(field)
    for b in range(bool_fields):
        key = Key(isfield=True)
        val = Value(vtype='bool')
        field = Field(key, val)
        fields.append(field)
    
    fieldset = Fieldset(fields)
    assert len(re.findall(",", fieldset.text)) == 4 # num fields defined

def test_line_constructor_2tags_5fields_mix_types():
    tags = []
    for t in range(num_tags):
        key = Key(length=tag_key_length)
        val = Value(length=tag_value_length)
        tags.append(Tag(key,val))

    fields = []
    key = Key(isfield=True)
    for i in range(int_fields):
        key = Key(isfield=True)
        field = Field(key=key)
        fields.append(field)
    for f in range(float_fields):
        key = Key(isfield=True)
        val = Value(vtype='float')
        field = Field(key, val)
        fields.append(field)
    for s in range(str_fields):
        key = Key(isfield=True)
        val = Value(vtype='str')
        field = Field(key, val)
        fields.append(field)
    for b in range(bool_fields):
        key = Key(isfield=True)
        val = Value(vtype='bool')
        field = Field(key, val)
        fields.append(field)
    
    tagset = Tagset(tags)
    fieldset = Fieldset(fields)

    line = Line(measurement=measurement,
                tagset=tagset,
                fieldset=fieldset,
                timestamp=Timestamp(precision=time_precision))

    assert line
    assert line.measurement == 'measurement'
    assert len(re.findall(",", line.tagset.text)) == num_tags
    
    return line # for use in interactive testing

# def test_batch_constructor():
#     All keys and values are different per line
#     b = Batch() # initalize defaults
#     assert [line == prev_line 
#     pass
#     Keep all Tags and Field keys the same
#     Keep all Tags the same
