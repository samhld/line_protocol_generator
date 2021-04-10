import runconfig as cfg
from sets import Tagset, Fieldset
from primitives import Timestamp


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
        return f"{self.measurement}{self.tagset} {self.fieldset} {self.timestamp}" 


def gen_line(measurement=None, tags=None, tagset=None, fields=None, fieldset=None, **kwargs):
    
    if fieldset and tagset:
        line = Line(measurement=measurement, tagset=Tagset(**kwargs),
                    fieldset=Fieldset(**kwargs), timestamp=time_precision)
        return line
    elif tags and fields:
        tagset = Tagset(tags)
        fieldset = Fieldset(fields)
        line = Line(measurement=measurement, tagset=Tagset(**kwargs),
                    fieldset=Fieldset(**kwargs), timestamp=time_precision)
        return line
    else:
        return Line()



# def generate(self):
#     lines = []
#     if self.keep_series_key:
#         for i in range(self.size):
#             lines.append(_generate_line())
#     else:
#         pass
