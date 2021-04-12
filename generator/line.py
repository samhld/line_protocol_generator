import generator.runconfig as cfg
from generator.sets import Tagset, Fieldset
from generator.primitives import Timestamp


class Line:
    def __init__(self, measurement=None, tags=None, fields=None, 
                       tagset=None, fieldset=None, timestamp=None, 
                       series_key=None, **kwargs):

        self.measurement = measurement
        # self.tags = tags
        # self.fields = fields
        self.tagset = tagset
        self.fieldset = fieldset
        self.timestamp = timestamp
        # self.text = _gen_text(gen_line(measurement=measurement, )) 
    
    def __str__(self):

        if self.timestamp:
            return f"{self.measurement}{self.tagset or ''} {self.fieldset} {self.timestamp}"
        else:
            return f"{self.measurement}{self.tagset or ''} {self.fieldset}"