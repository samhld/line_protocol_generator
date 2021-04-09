# All configuration parameters

measurement         = 'measurement'
batch_size          = 10
num_tags            = 3
int_fields          = 2
float_fields        = 1
str_fields          = 1
bool_fields         = 1
tag_key_length      = 8
tag_value_length    = 10
field_key_length    = 8
int_value_length    = 4
float_value_length  = 4
str_value_size      = 8
time_precision      = 's'
keep_series_batch   = False
keep_series_session = True
regular_sample      = True
sample_interval     = 5 if regular_sample else False
loop                = False

