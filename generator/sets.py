
import re
import generator.runconfig as cfg
from generator.primitives import *

class Tagset:
    def __init__(self, tags=None, num_tags=0):
        self.tags = tags or []
        # self.text = "".join([f",{tag.text}" for tag in self.tags])
        self.keys = [tag.key for tag in self.tags]
        self.values = [tag.val for tag in self.tags]

    def append(self, tag):
        self.tags.append(tag)

    def add_tag(self, tag: Tag=None, key_len=cfg.tag_key_length, val_len=cfg.tag_value_length):
        if tag:
            self.append(tag)
        else:
            key = Key(length=key_len)
            val = Value(length=val_len)
            self.append(Tag(key, val))
    
    def __str__(self):
        return "".join([f",{tag}" for tag in self.tags])


class Fieldset:
    def __init__(self, fields=None, field_key_length=8, field_value_length=10,
                       int_fields=0, float_fields=0, str_fields=0, bool_fields=0, **kwargs):
        self.fields = fields or []
        # self.text = ''.join([f"{field.text}," for field in self.fields])[:-1]
        self.keys = [field.key for field in self.fields]
        self.values = [field.val for field in self.fields]
        self.int_fields = int_fields
        self.float_fields = float_fields
        self.str_fields = str_fields
        self.bool_fields = bool_fields
        self._total = self.int_fields + self.float_fields + self.str_fields + self.bool_fields
        self.int_keys_slice = slice(0, self.int_fields)
        self.float_keys_slice = slice(self.int_fields, (self.int_fields + self.float_fields))
        self.str_keys_slice = slice((self._total - self.bool_fields), (self._total - self.bool_fields))
        self.bool_fields_slice = slice((self._total - self.bool_fields), self._total)

    def append(self, field):
        self.fields.append(field)

    def add_key(self, key_len):
        pass

    def add_value(self, val_len):
        pass

    def add_int(self, field: Field=None, key_len=cfg.field_key_length, val_len=cfg.int_value_length):
        if field:
            print("Nonetype")
            self.append(field)
        else:
            key = Key(isfield=True, length=key_len)
            val = Value(vtype='int', length=val_len)
            self.append(Field(key, val))

    def add_float(self, field: Field=None, key_len=cfg.field_key_length, val_len=cfg.float_value_length):
        if field:
            self.append(field)
        else:    
            key = Key(isfield=True, length=key_len)
            val = Value(vtype='float', length=val_len)
            self.append(Field(key, val))
    
    def add_str(self, field: Field=None, key_len=cfg.field_key_length, val_len=cfg.str_value_length):
        if field:
            self.append(field)
        else:
            key = Key(isfield=True, length=key_len)
            val = Value(vtype='str', length=val_len)
            self.append(Field(key, val))

    def add_bool(self, field: Field=None, key_len=cfg.field_key_length, val_len=cfg.bool_value_length):
        if field:
            self.append(field)
        else:
            key = Key(isfield=True, length=key_len)
            val = Value(vtype='bool', length=val_len)
            self.append(Field(key, val))

    def __str__(self):
        return ''.join([f"{field}," for field in self.fields])[:-1]
