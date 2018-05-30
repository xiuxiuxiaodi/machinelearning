#-*-encoding=utf-8-*-
#invite peopel for the Kaggle party
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

#bring in the six packs
df_train=pd.read_csv('h:/train.csv')

#check the decoration
df.train.columns

