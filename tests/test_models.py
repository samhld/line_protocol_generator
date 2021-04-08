import pytest
import re
from generator.models import Key,Value,Tag,Field,Tagset,Fieldset

def create_test_line(**kwargs):
    tag_keys = [Key(length=kwargs["tag_key_length"], inherited=kwargs["inherited"]) for key in keys]
    tag_values = Value(lenght=kwargs[""] )


def test_key_constructor():
    # Test Key class
    k = Key() # initialize defaults
    assert (k.length, k.inherited) == (5, '')
    k = Key(10) # custom length
    assert k.length == 10
    k = Key(10, 'tag1')
    assert k
    k = Key(length=10, inherited='cpu_usage')
    assert repr(k) == 'tag_cpu_u' # trims last 4 chars to allow `tag_`

def test_value_constructor():
    v = Value() # initialize defaults
    assert (v.length, v.inherited, v.vtype) == (5, '', 'str')
    v = Value(10)
    assert v.length == 10
    assert repr(v) == v.repr
    v = Value(10, inherited='value')
    assert repr(v) == 'value'

    with pytest.raises(ValueError) as info:
        v = Value(vtype='long')
    assert 'long is not a supported type' == str(info.value)

def test_tag_constructor():
    k, v = Key(), Value()
    t = Tag(key=k, val=v)
    assert t
    assert repr(t).startswith('tag_') == True
    k, v = Key(inherited='hosthost'), Value()
    t = Tag(key=k, val=v)
    assert 'host' in repr(t)


def test_measrement_constructor():
    pass

def test_field_construtor():
    k, v = Key(), Value(vtype='int')
    f = Field(key=k, val=v)
    assert repr(f).endswith('i') == True
    v = Value(vtype='float', inherited='asdf')
    f = Field(key=k, val=v)
    assert 'asdf' in repr(f)

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
    assert re.search("tag_", repr(fieldset)) == None
    assert len(re.findall(",", repr(fieldset))) == int_fields

def test_mixed_types_fieldset():
    int_fields, float_fields, str_fields, bool_fields = 1, 2, 1, 1
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
    assert len(re.findall(",", repr(fieldset))) == 5 # num fields defined











# def test_fieldset_constructor():
#     pass

# def test_line_constructor():
#     pass

# def test_batch_constructor():
    # All keys and values are different per line
    # b = Batch() # initalize defaults
    # assert [line == prev_line 
    pass
    # Keep all Tags and Field keys the same
    # Keep all Tags the same
