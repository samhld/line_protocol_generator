import argparse
from generator import models, helpers


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a batch of Line Protocol points of a specified shape")
    parser.add_argument('measurement', type=str)
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

    if kwargs["loop"]:
        if kwargs["keep_series_session"]:

            batch = models.Batch(**kwargs)
