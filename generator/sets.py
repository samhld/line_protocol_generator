
import re
from runconfig import *
from generator.primitives import *

class Tagset:
    def __init__(self, tags, num_tags=0):
        self.tags = tags
        self.text = "".join([f",{tag.text}" for tag in self.tags])
        self.keys = [tag.key.text for tag in tags]
        self.values = [tag.val.text for tag in tags]

    @classmethod
    def from_keys(cls, keys, num_tags, vals=None, tag_key_length=8, tag_value_length=10):
        tags = []
        for k in keys:
            tag = Tag(k, Value(length=tag_value_length))
            tags.append(tag)
        return cls(tags)

    @classmethod
    def from_nothing(cls, num_tags, tag_key_length, tag_value_length=10):
        tags = []
        for i in range(kwargs["num_tags"]):
            k = Key(length=tag_key_length)
            v = Value(length=tag_value_length)
            tag = Tag(k,v)
            tags.append(tag)
        return cls(tags)

class Fieldset:
    def __init__(self, fields=[], field_key_length=8, field_value_length=10,
                       int_fields=None, float_fields=None, str_fields=None, bool_fields=None, **kwargs):
        self.fields = fields if fields else []
        self.text = ''.join([f"{field.text}," for field in self.fields])[:-1]
        self.keys = [field.key.text for field in fields]
        self.values = [field.val.text for field in fields]
        self.int_fields = kwargs["int_fields"]
        self.float_fields = kwargs["float_fields"]
        self.str_fields = kwargs["str_fields"]
        self.bool_fields = kwargs["bool_fields"]
        self._total = self.int_fields + self.float_fields + self.str_fields + self.bool_fields
        self.int_keys_slice = slice(0, self.int_fields)
        self.float_keys_slice = slice(self.int_fields, (self.int_fields + fself.loat_fields))
        self.str_keys_slice = slice((self._total - self.bool_fields), (self._total - self.bool_fields))
        self.bool_fields_slice = slice((self._total - self.bool_fields), self._total)

    @staticmethod
    def gen_fields_of_type(vtype, keys=None, **kwargs):
        fields_by_type = []
        if keys:
            for k in range(len(keys)):
                val = Value(vtype=vtype)
                key = keys[k]
                field = Field(key, val)
                fields_by_type.append(field)
        else:
            key_count = eval(f"{vtype}_fields")
            for k in range(key_count):
                key = Key(isfield=True, length=kwargs["field_key_length"])
                val = Value(vtype=vtype, length=kwargs[f"{vtype}_fields"])
                field = Field(key, val)
                fields_by_type.append(field)

        return fields_by_type

    def add_ints(self, keys=[], **kwargs):
        int_fields = kwargs["int_fields"]
        klength = kwargs["field_key_length"]
        vlength = kwargs["int_value_length"]
        if int_fields:
            fields = []
            for i in range(int_fields):
                key = Key(length=klength, isfield=True)
                val = Value(length=vlength, vtype='int')
                field = Field(key, val)
                fields.append(field)
            print(self)
            self.fields.append(fields)
            return self
        else:
            return self

    def add_floats(self, keys=[], **kwargs):
        float_fields = kwargs["float_fields"]
        klength = kwargs["field_key_length"]
        vlength = kwargs["float_value_length"]
        if float_fields:
            fields = []
            for f in range(float_fields):
                key = Key(length=klength, isfield=True)
                val = Value(length=vlength, vtype='float')
                field = Field(key, val)
                fields.apend(field)
            return self.fields.append(fields)
        else:
            return self

    def add_strings(self, keys=[], **kwargs):
        str_fields = kwargs["str_fields"]
        klength = kwargs["field_key_length"]
        vlength = kwargs["str_value_length"]
        if str_fields:
            fields = []
            for i in range(str_fields):
                key = Key(length=klength, isfield=True)
                val = Value(length=vlength, vtype='str')
                field = Field(key, val)
                fields.apend(field)
            return self.fields.append(fields)
        else:
            return self

    def add_bools(self, keys=[], **kwargs):
        bool_fields = kwargs["bool_fields"]
        klength = kwargs["field_key_length"]
        vlength = kwargs["bool_value_length"]
        if bool_fields:
            fields = []
            for i in range(bool_fields):
                key = Key(length=klength, isfield=True)
                val = Value(length=vlength, vtype='bool')
                field = Field(key, val)
                fields.apend(field)
            return self.fields.append(fields)
        else:
            return self

    @classmethod
    def from_keys(cls, keys, **kwargs):
        int_fields = kwargs["int_fields"]
        float_fields = kwargs["float_fields"]
        str_fields = kwargs["str_fields"]
        bool_fields = kwargs["bool_fields"]

        _total = int_fields+float_fields+str_fields+bool_fields
        int_keys_slice = slice(0,int_fields)
        float_keys_slice = slice(int_fields,(int_fields+float_fields))
        str_keys_slice = slice((_total-bool_fields),(_total-bool_fields))
        bool_fields_slice = slice((_total-bool_fields),_total)
        

        fields = []
        if int_fields:
            fields.append(cls.gen_fields_of_type(vtype='int', keys=keys[int_keys_slice]))
        if float_fields:
            fields.append(cls.gen_fields_of_type(vtype='float', keys=keys[float_keys_slice]))
        if str_fields:
            fields.append(cls.gen_fields_of_type(vtype='float', keys=keys[str_keys_slice]))
        if bool_fields:
            fields.append(cls.gen_fields_of_type(vtype='float', keys=keys[bool_fields_slice]))
        
        return cls(fields)

    @classmethod
    def from_nothing(cls, **kwargs):
        int_fields = kwargs["int_fields"]
        float_fields = kwargs["float_fields"]
        str_fields = kwargs["str_fields"]
        bool_fields = kwargs["bool_fields"]

        _total = int_fields+float_fields+str_fields+bool_fields
        int_keys_slice = slice(0,int_fields)
        float_keys_slice = slice(int_fields,(kint_fields+float_fields))
        str_keys_slice = slice((_total-bool_fields),(_total-bool_fields))
        bool_fields_slice = slice((_total-bool_fields),_total)

        field_key_length = kwargs["field_key_length"]

        keys = [Key(length=field_key_length, isfield=True) for k in range(_total)]
        fields = []
        if int_fields:
            ints = cls.gen_fields_of_type(vtype='int', keys=keys[int_keys_slice])
            fields.append(ints)
        if float_fields:
            floats = cls.gen_fields_of_type(vtype='float', keys=keys[float_keys_slice])
            fields.append(floats)
        if str_fields:
            strs = cls.gen_fields_of_type(vtype='str', keys=keys[str_keys_slice])
            fields.append(strs)
        if bool_fields:
            bools = cls.gen_fields_of_type(vtype='bool', keys=keys[bool_keys_slice])
            fields.append(bools)

        return cls(fields)