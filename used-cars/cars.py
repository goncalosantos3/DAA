import sklearn as skl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

cars = pd.read_csv('cars.csv')

# Coluna target para último lugar
cars = cars.reindex(columns = [col for col in cars.columns if col != 'Price'] + ['Price'])

################################# Exploração #####################################

# primeiras 5 entradas
print(cars.head())

# Colunas
print("\n\nColunas do dataset:")
print(cars.columns)

# Descrição geral dos dados
print("\n\nDescrição geral dos dados:")
print(cars.describe())

# Distribuição geral do target
plt.hist(cars['Price'], bins = 20) 
plt.show()

# Relação entre várias features e o target (Price)
## Relação entre "Company Name" com "Price"
print("\n\nRelação entre a empresa com a média dos preços:")
print(cars.groupby(by=['Company Name'])['Price'].mean())
sns.barplot(x='Company Name', y='Price', data=cars)
plt.show()

## Relação entre "Company Name" e "Model Name" com "Price"
print("\n\nRelação entre a empresa e o modelo com a média dos preços:")
print(cars.groupby(by=['Company Name', 'Model Name'])['Price'].mean())

## Relação entre "Mileage" com "Price"
print("\n\nRelação entre 'Mileage' com a média dos preços:")
print(cars.groupby(by=['Mileage'])['Price'].mean())

# Matriz de Correlação
corr_matrix = cars.corr(numeric_only=True)
sns.heatmap(corr_matrix, vmin=-1, vmax=1, square=True, annot=True)
plt.show()