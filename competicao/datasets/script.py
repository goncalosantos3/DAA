import csv
import re

###################################  TREINO  ####################################

out = open('treino.csv', 'w')
writer = csv.writer(out)
# Cabeçalho
writer.writerow(['Data', 'Hora', 'Normal (kWh)', 'Horario Economico (kWh)', 
                 'Autoconsumo (kWh)', 'Injeçao na rede (kWh)',
                 'dt', 'dt_iso', 'city_name', 'temp', 'feels_like', 'temp_min',
                 'temp_max', 'pressure', 'sea_level', 'grnd_level', 'humidity', 
                 'wind_speed', 'rain_1h', 'clouds_all', 'weather_description'])

e1 = open('energia_202109-202112.csv', 'r')
m1 = open('meteo_202109-202112.csv', 'r')

ce1 = []
cm1 = []

for row in csv.reader(e1):
    ce1.append(row)

for row in csv.reader(m1):
    cm1.append(row)

for i in range(1, len(cm1)):
    match = False
    for j in range(1, len(ce1)):
        datam = re.search(r'\d+\-\d+\-\d+', cm1[i][1]).group()
        horam = re.search(r'\d+:\d+:\d+', cm1[i][1]).group()

        # Entrada presente em ambos os datasets
        if ce1[j][0] == datam and ce1[j][1] == horam[:2]:
            match = True
            writer.writerow(ce1[j] + cm1[i])
    
    if match == False:
        writer.writerow(['','','','','',''] + cm1[i])

e1.close()
m1.close()

e2 = open('energia_202201-202212.csv', 'r')
m2 = open('meteo_202201-202212.csv', 'r')

ce2 = []
cm2 = []

for row in csv.reader(e2):
    ce2.append(row)

for row in csv.reader(m2):
    cm2.append(row)

for i in range(1, len(cm2)):
    match = False
    for j in range(1, len(ce2)):
        datam = re.search(r'\d+\-\d+\-\d+', cm2[i][1]).group()
        horam = re.search(r'\d+:\d+:\d+', cm2[i][1]).group()

        # Entrada presente em ambos os datasets
        if ce2[j][0] == datam and ce2[j][1] == horam[:2]:
            match = True
            writer.writerow(ce2[j] + cm2[i])
    
    if match == False:
        writer.writerow(['','','','','',''] + cm2[i])

e2.close()
m2.close()
out.close()

###################################  TESTE  ####################################

out = open('teste.csv', 'w')
writer = csv.writer(out)
# Cabeçalho
writer.writerow(['Data', 'Hora', 'Normal (kWh)', 'Horario Economico (kWh)', 
                 'Autoconsumo (kWh)',
                 'dt', 'dt_iso', 'city_name', 'temp', 'feels_like', 'temp_min',
                 'temp_max', 'pressure', 'sea_level', 'grnd_level', 'humidity', 
                 'wind_speed', 'rain_1h', 'clouds_all', 'weather_description'])

e3 = open('energia_202301-202304.csv', 'r')
m3 = open('meteo_202301-202304.csv', 'r')

ce3 = []
cm3 = []

for row in csv.reader(e3):
    ce3.append(row)

for row in csv.reader(m3):
    cm3.append(row)

for i in range(1, len(ce3)):
    match = False
    for j in range(1, len(cm3)):
        datam = re.search(r'\d+\-\d+\-\d+', cm3[j][1]).group()
        horam = re.search(r'\d+:\d+:\d+', cm3[j][1]).group()

        # Entrada presente em ambos os datasets
        if ce3[i][0] == datam and ce3[i][1] == horam[:2]:
            match = True
            writer.writerow(ce3[i] + cm3[j])
    
    if match == False:
        writer.writerow(['','','','','',''] + ce3[i])

e3.close()
m3.close()
out.close()