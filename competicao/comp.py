import sklearn as skl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

e1 = pd.read_csv('datasets/energia_202109-202112.csv', encoding='latin-1')

print(e1.columns)