import runconfig as cfg
from primitives import *
from sets import *

class Batch:
    # class attrs to refer to if needed
    # size, measurement_length, key_length = 10
    def __init__(self, measurement=None, 
                       tagset=None, 
                       fieldset=None, 
                       timestamp=None, 
                       **kwargs):
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
        # self.lines               = tagset or self._gen_tagset()
        self.tagset              = tagset or self._gen_tagset()

    def _gen_tagset(self, **kwargs):
        tags = []
        for i in range(num_tags):
            k = Key(length=kwargs["tag_key_length"])
            v = Value(length=kwargs["tag_value_length"])
            tag = Tag(k,v)
            tags.append(tag)
        tagset = Tagset(tags)
        
        return tagset

    def _gen_fieldset(self, fields=None, **kwargs):
        
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

    def _gen_line(self, measurement=None, tags=None, tagset=None, fields=None, fieldset=None, **kwargs):
        
        if fieldset:
            line = Line(measurement=self.measurement, 
                    tagset=Tagset(**kwargs),
                    fieldset=Fieldset(**kwargs),
                    timestamp=self.time_precision)