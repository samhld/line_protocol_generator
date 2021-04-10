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
        return f"{self.measurement}{self.tagset} {self.fieldset} {self.timestamp}" 

    @classmethod
    def gen_line(cls, measurement=None, timestamp=None, tagset=None, fieldset=None, tags=None, fields=None, **kwargs):
        
        if not timestamp:
            timestamp = Timestamp(precision=kwargs["time_precision"])
        if fieldset and tagset:
            line = Line(measurement=measurement, tagset=Tagset(**kwargs),
                        fieldset=Fieldset(**kwargs), timestamp=timestamp)
            return cls(line)
        elif tags and fields:
            tagset = Tagset(tags)
            fieldset = Fieldset(fields)
            line = Line(measurement=measurement, tagset=Tagset(**kwargs),
                        fieldset=Fieldset(**kwargs), timestamp=timestamp)
            return cls(line)
        else:
            if kwargs["num_tags"]:
                tset = Tagset()
                for t in range(kwargs["num_tags"]):
                    tset.add_tag(key_len=kwargs["tag_key_length"], val_len=kwargs["tag_value_length"])

            fset = Fieldset()

            if kwargs["int_fields"]:
                for i in range(kwargs["int_fields"]):
                    fset.add_int(key_len=kwargs["field_key_length"], val_len=kwargs["int_value_length"])
            if kwargs["float_fields"]:
                for i in range(kwargs["float_fields"]):
                    fset.add_float(key_len=kwargs["field_key_length"], val_len=kwargs["float_value_length"])
            if kwargs["str_fields"]:
                for i in range(kwargs["str_fields"]):
                    fset.add_str(key_len=kwargs["field_key_length"], val_len=kwargs["str_value_length"])
            if kwargs["bool_fields"]:
                for i in range(kwargs["bool_fields"]):
                    fset.add_bool(key_len=kwargs["field_key_length"], val_len=kwargs["bool_value_length"])
            
            line = Line(measurement=measurement, tagset=tset,
                        fieldset=fset, timestamp=timestamp)
            return cls(line)



# def generate(self):
#     lines = []
#     if self.keep_series_key:
#         for i in range(self.size):
#             lines.append(_generate_line())
#     else:
#         pass
