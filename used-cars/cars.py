import sklearn as skl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

cars = pd.read_csv('cars.csv')

print(cars.columns)

cars.info()