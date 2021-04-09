import config

class Line:
    def __init__(self, measurement=None, 
                       tagset=None, 
                       fieldset=None, 
                       timestamp=None,
                       **kwargs):
        self.measurement = measurement
        self.tagset = tagset
        self.fieldset = fieldset
        self.timestamp = timestamp
        self.text = f"{self.measurement}{self.tagset.text} {self.fieldset.text} {self.timestamp.text}"   


def gen_line(measurement=None, tags=None, tagset=None, fields=None, fieldset=None, **kwargs):
    
    if fieldset:
        line = Line(measurement=self.measurement, 
                tagset=Tagset(**kwargs),
                fieldset=Fieldset(**kwargs),
                timestamp=self.time_precision)

# def generate(self):
#     lines = []
#     if self.keep_series_key:
#         for i in range(self.size):
#             lines.append(_generate_line())
#     else:
#         pass
