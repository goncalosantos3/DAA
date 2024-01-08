import pandas as pd

allowed_nans = ['', '#N/A', '#N/A N/A', '#NA', '-1.#IND', '-1.#QNAN',
                '-NaN', '-nan', '1.#IND', '1.#QNAN', '<NA>', 'N/A', 'NA',
                'NULL', 'NaN', 'n/a', 'nan', 'null']

####################################### TREINO ################################################

pb = pd.read_csv('old/seaGrndPressureBraga.csv')
treino = pd.read_csv('treino.csv', na_values=allowed_nans, keep_default_na=False)

treino.drop(['sea_level', 'grnd_level'], inplace=True, axis=1)
treino.insert(14, "sea_level", list(pb['pressure_msl (hPa)']), True)
treino.insert(15, "grnd_level", list(pb['surface_pressure (hPa)']), True)

treino.to_csv('treino.csv', index=False)

####################################### TESTE #################################################

pb2023 = pd.read_csv('old/seaGrndPressureBraga2023.csv')
teste = pd.read_csv('teste.csv', na_values=allowed_nans, keep_default_na=False)

teste.drop(['sea_level', 'grnd_level'], inplace=True, axis=1)
teste.insert(13, "sea_level", list(pb2023['pressure_msl (hPa)']), True)
teste.insert(14, "grnd_level", list(pb2023['surface_pressure (hPa)']), True)

teste.to_csv('teste.csv', index=False)