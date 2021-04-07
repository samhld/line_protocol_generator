import datetime
import random
from helpers import *

class Key:
    def __init__(self, length: int=5, inherited: str='', field: bool=False):
        self.length = length
        self.inherited = inherited

    def _generate(self, length, inherited):
        if self.inherited:
            return self.inherited
        else:
            return create_string(length)    

    def __repr__(self):
        return str(self._generate(self.length, self.inherited))

class Value:
    def __init__(self, length: int=5, inherited: str='', field: bool=False, vtype: str='str'):
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
        self.field = field
        self.vtype = vtype

    def _generate(self):
        if self.vtype == 'str':
            val = create_string(self.length)
        elif self.vtype == 'int':
            val = create_int(self.length)
        elif self.vtype == 'float':
            val = round(random.uniform(10,99), self.length-2)
        elif self.vtype == 'bool':
            val = random.choice([True,False])
        return val
        # else:
        #     raise ValueError

    def __repr__(self):
        val = self._generate()
        return str(val)