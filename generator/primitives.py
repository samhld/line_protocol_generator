from generator.helpers import *


class Key:
    def __init__(self, length=5, isfield=False):
        """
        Parameters
        ----------
        length: number of chars
        isfield: whether Value is a Field -- determines whether 'tag_` is prepended
        """
        self.length = length
        self.isfield = isfield
        self.text = self._gen_text()
        
    def _gen_text(self):
        if self.isfield:
            return create_string(self.length)
        else:
            return "tag_"+create_string(self.length)[:-4]

class Value:
    def __init__(self, length=5, vtype='str'):
        """
        Parameters
        ----------
        length: number of chars
        vtype: the primitive type of Value; can also be ['int'|'float'|'bool']; used to determine return of repr
        """
        self.length = length
        self.vtype = vtype
        self.text = str(self._gen_text())

    def _gen_text(self):
        if self.vtype == 'str':
            val = '"'+create_string(self.length)+'"'
        elif self.vtype == 'int':
            val = str(create_int(self.length))+'i'
        elif self.vtype == 'float':
            val = round(random.uniform(10,99), self.length-2)
        elif self.vtype == 'bool':
            val = random.choice([True,False])
        else:
            raise ValueError(f"{self.vtype} is not a supported type")
                    
        return val

class Tag:
    def __init__(self, key=None, val=None):
        self.key = key or Key()
        self.val = val or Value()
        self.text = f"{self.key.text}={self.val.text}"

class Field:
    def __init__(self, key=None, val=None):
        self.key = key or Key()
        self.val = val or Value(vtype='int')
        self.text = f"{self.key.text}={self.val.text}"
    
class Timestamp:
    def __init__(self, precision: str='s'):
        self.precision = precision
        self.text = str(create_timestamp(self.precision))

class Measurement:
    pass # Currently generated at runtime of script so need for further functionality for now
