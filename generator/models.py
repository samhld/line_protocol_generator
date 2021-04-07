import datetime
import random
from generator.helpers import *

class Key:
    def __init__(self, length: int=5, inherited: str='', isfield: bool=False):
        self.length = length
        self.inherited = inherited
        self.isfield = isfield
        self.repr = self._generate()

    def _generate(self):
        if self.inherited:
            return self.inherited
        else:
            return create_string(self.length) 

    def __repr__(self):
        return str(self.repr)

class Value:
    def __init__(self, length: int=5, inherited: str='', isfield: bool=False, vtype: str='str'):
        """
        Parameters
        ----------
        length: number of chars
        inherited: holds a value passed to it from the calling function; used when values are to be determinstic
        field: whether Value is a Field
        vtype: the primitive type of Value; can also be ['int'|'float'|'bool']; used to determine return of repr
        """
        self.length = length
        self.inherited = inherited
        self.isfield = isfield
        self.vtype = vtype
        self.repr = self._generate()

    def _generate(self):
        if self.inherited:
            return self.inherited
        else:
            if self.vtype == 'str':
                val = create_string(self.length)
            elif self.vtype == 'int':
                val = create_int(self.length)
            elif self.vtype == 'float':
                val = round(random.uniform(10,99), self.length-2)
            elif self.vtype == 'bool':
                val = random.choice([True,False])
            else:
                raise ValueError(f"{self.vtype} is not a supported type")
                        
            return val

    def __repr__(self):
        return str(self.repr)

class Tag(Key, Value):
    def __init__(self, key: Key, val: Value):
        self.key = repr(key)
        self.val = repr(val)
    
    def __repr__(self):
        return f"{self.key}={self.val}"

class Tagset:
    def __init__(self, tags):
        self.tags = tags
        # self.string = 

    def _generate(self):
        pass

    def __repr__(self):
        pass
