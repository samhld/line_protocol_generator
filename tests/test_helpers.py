import sys
print(sys.path)
import re
from ..generator.runconfig import * # many variables used in this file are defined in `config.py`
 # many classes used in this file are defined in `models.py`

def test_gen_tagset():
    text = gen_tagset().text
    assert gen_tagset().text != gen_tagset().text # default should genreate randomly
