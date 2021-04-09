

import runconfig as cfg

class Tagset:
    def __init__(self, tags=None):
        self.tags = tags
        self.text = ''.join([f",{tag.text}" for tag in self.tags])

def gen_tagset(keys=None, vals=None, tags=None):
    
    if tags:
        return Tagset(tags)
    elif keys and vals:
        tags = []
        for k,v in (keys, vals):
            tag = Tag(k, v)
            tags.append(tag)
        return Tagset(tags)
    else:
        tags = []
        for i in range(num_tags):
            k = Key(length=tag_key_length)
            v = Value(length=tag_value_length)
            tag = Tag(k,v)
            tags.append(tag)
        tagset = Tagset(tags)
        return tagset


class Fieldset:
    def __init__(self, fields=None):
        self.fields = fields
        self.text = ''.join([f"{field.text}," for field in self.fields])[:-1]


def gen_fieldset(fields=None, **kwargs):
    
    if fields:
        fieldset = Fieldset(fields)
        return fieldset   

    fields = []
    if int_fields:
        for i in range(int_fields):
            key = Key(isfield=True)
            field = Field(key=key)
            fields.append(field)
    if float_fields:
        for f in range(float_fields):
            key = Key(isfield=True)
            val = Value(vtype='float')
            field = Field(key, val)
            fields.append(field)
    if str_fields:
        for s in range(str_fields):
            key = Key(isfield=True)
            val = Value(vtype='str')
            field = Field(key, val)
            fields.append(field)
    if bool_fields:
        for b in range(bool_fields):
            key = Key(isfield=True)
            val = Value(vtype='bool')
            field = Field(key, val)
            fields.append(field)

    fieldset = Fieldset(fields)
    
    return fieldset