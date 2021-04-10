import argparse
from generator import helpers, primitives
from generator.line import Line
from generator.sets import Tagset, Fieldset
from generator.primitives import Key, Value, Timestamp, Tag, Field 
import runconfig as cfg


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a batch of Line Protocol points of a specified shape")
    parser.add_argument('measurement', type=str)
    parser.add_argument('--sample_interval', type=int, default=10)
    parser.add_argument('--batch_size', type=int, default=10)
    parser.add_argument('--num_tags', type=int, default=3)
    parser.add_argument('--int_fields', type=int, default=2)
    parser.add_argument('--float_fields', type=int, default=1)
    parser.add_argument('--str_fields', type=int, default=1)
    parser.add_argument('--bool_fields', type=int, default=1)
    parser.add_argument('--tag_key_length', type=int, default=8)
    parser.add_argument('--tag_value_length', type=int, default=10)  
    parser.add_argument('--field_key_length', type=int, default=8)
    parser.add_argument('--int_value_length', type=int, default=4)
    parser.add_argument('--float_value_length', type=int, default=4)
    parser.add_argument('--str_value_length', type=int, default=8)
    parser.add_argument('--bool_value_length', type=int, default=4)
    parser.add_argument('--time_precision', type=str, choices = ['s','S','ms','MS','us','US','ns','NS'], default='s')
    parser.add_argument('--keep_series_session', action='store_true', help="Keep Tag/Field keys constant for each line in all batches; only relevant when `--loop` is True")
    parser.add_argument('--keep_series_batch', action='store_true', help="Superset of `--keep_keys_batch`; keeps Tag values constant as well")
    parser.add_argument('--loop', action='store_true', help="If True, script runs in infinit loop; used with Telegraf `execd` input plugin")
    parser.add_argument('--merge_lines', action='store_true', help="If True, Fields sharing a metaseries will be on the same line for a given timestamp")

    kwargs = vars(parser.parse_args())

    int_fields = kwargs["int_fields"]
    float_fields = kwargs["float_fields"]
    str_fields = kwargs["str_fields"]
    bool_fields = kwargs["bool_fields"]
    total_fields = int_fields + float_fields + str_fields + bool_fields
    num_lines = kwargs["batch_size"] or cfg.batch_size
    meas = kwargs["measurement"] or cfg.measurement
    precision = kwargs["time_precision"] or cfg.time_precision
    interval = kwargs["sample_interval"] or cfg.sample_interval
    num_tags = kwargs["num_tags" or cfg.num_tags]

    if kwargs["loop"]:
        if kwargs["keep_series_session"]:
            # Create keys outside of loop
            tagsets = [Tagset(num_tags=num_tags) for i in range(num_lines)]
            fieldsets = [Fieldset() for i in range(num_lines)]
            while True:
                lines = []
                timestamp = Timestamp(precision=precision)
                for tset, fset in zip(tagsets, fieldsets):
                    line = Line(measurement=meas, tagset=tset, fieldset=fset, timestamp=timestamp)
                    lines.append(line)

                print(lines)

                time.sleep(interval)
        # else:
        #     while True:
        #         lines = []
        #         timestamp = Timestamp(precision=precision)
        #         for i in range(num_lines):
        #             line = Line(measurement=meas, Tagset(num_tags)

            

            # else:
            #     # Create

