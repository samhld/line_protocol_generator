import datetime
import random
from generator.helpers import *

class Key:
    def __init__(self, length=5, inherited='', isfield=False):
        """
        Parameters
        ----------
        length: number of chars
        inherited: holds a value passed to it from the calling function; used when values are to be determinstic
        vtype: the primitive type of Value; can also be ['int'|'float'|'bool']; used to determine return of repr
        """
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
        if self.isfield:
            return str(self.repr)
        else:
            return 'tag_'+str(self.repr)[:-4]


class Value:
    def __init__(self, length=5, inherited='', vtype='str'):
        """
        Parameters
        ----------
        length: number of chars
        inherited: holds a value passed to it from the calling function; used when values are to be determinstic
        isfield: whether Value is a Field
        vtype: the primitive type of Value; can also be ['int'|'float'|'bool']; used to determine return of repr
        """
        self.length = length
        self.inherited = inherited
        # self.isfield = isfield
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
        return str(self.repr)+'i' if self.vtype == 'int' else str(self.repr)


class Tag:
    def __init__(self, key=None, val=None):
        self.key = key or Key()
        self.val = val or Value()
    
    def __repr__(self):
        return f"{self.key}={self.val}"


class Field:
    def __init__(self, key=None, val=None):
        self.key = key or Key()
        self.val = val or Value(vtype='int')
    
    def __repr__(self):
        return f"{self.key}={self.val}"

class Timestamp:
    def __init__(self, precision: str='s'):
        self.precision = precision
        self.repr = create_timestamp(self.precision)
    
    def __repr__(self):
        return str(self.repr)

class Measurement:
    pass

class Tagset:
    def __init__(self, tags):
        self.tags = tags
        self.repr = self._generate()

    def _generate(self):
        return ''.join([f",{tag}" for tag in self.tags])

    def __repr__(self):
        return repr(self.repr)

class Fieldset:
    pass

class Line:
    def __init__(self, measurement: Measurement=None, 
                       tagset: Tagset=None, 
                       fieldset: Fieldset=None, 
                       timestamp: Timestamp=None,
                       **kwargs):
        self.measurement = measurement if measurement else Batch.length
        self.tagset = tagset
        self.fieldset = fieldset
        self.timestamp = timestamp


    def _generate(self):
        if self.measurement:
            measurement = self.measurement
            return measurement
        else:
            return create_string(length)

class Batch:
    # class attrs to refer to if needed
    # size, measurement_length, key_length = 10
    def __init__(self, **kwargs):
        """
        Initialize what is needed to initialize lines
        """
        self.size                = kwargs["batch_size"]
        self.time_precision      = kwargs["time_precision"]
        self.measurement         = kwargs["measurement"]
        self.num_tags            = kwargs["num_tags"]
        self.tag_key_length      = kwargs["tag_key_length"]
        self.tag_value_length    = kwargs["tag_value_length"]
        self.int_fields          = kwargs["int_fields"]
        self.float_fields        = kwargs["float_fields"]
        self.str_fields          = kwargs["str_fields"]
        self.bool_fields         = kwargs["bool_fields"]
        self.keep_series_batch   = kwargs["keep_series_batch"] # if True, Measurement,Tagset Fieldset stay constant in batch instance
        self.keep_series_session = kwargs["keep_series_batch"] # if True, Measurement,Tagset Fieldset stay constant in batch instance
        self.keep_time           = kwargs["keep_time"] # if True, timestamp will remain constant on every line in batch
        self.lines               = []

    def _generate_tagset():
        return Tagset(**kwargs)

    def _generate_line():
        return Line(measurement=self.measurement, 
                    tagset=Tagset(**kwargs),
                    fieldset=Fieldset(**kwargs),
                    timestamp=self.time_precision)

    def generate(self):
        lines = []
        if self.keep_series_key:
            for i in range(self.size):
                lines.append(_generate_line())
        else:
            pass


