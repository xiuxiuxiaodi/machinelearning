import numpy as np

import matplotlib

import json
import pandas as pd

test='''{"a":1,"b":2}
{"a":3,"b":4}'''
#df=pd.read_json(test,orient='records') doesn't work, expects []

l=[ json.loads(l) for l in test.splitlines()]
df=pd.DataFrame(l)
print l
print df
