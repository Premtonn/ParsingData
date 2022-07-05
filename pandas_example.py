import pandas as pd
import numpy as np
import pyodbc

data = pd.read_csv('ex2.csv', delimiter=';')

df = pd.DataFrame(data)

df = df.fillna(0)


# for col in df.columns:
#   print(col[0])

df.drop([1, 2], axis=0, inplace=True)
df.drop('T', axis=1, inplace=True)

"""df.rename(columns={'Unnamed: 17': '41', 'Unnamed: 18': '42', 'Unnamed: 19': '43', 'Unnamed: 20': '44', 'Unnamed: 21': '45',
                   'Unnamed: 22': '46', 'Unnamed: 23': '47', 'Unnamed: 24': '48', 'Unnamed: 25': '49', 'Unnamed: 26': '50',
                   'Unnamed: 27': '51',  'Unnamed: 28': '52'}, inplace=True)"""

df['26'].values[0] = '26'
df['25'] = np.where((df['26'].astype(int) == 25), df['27'], 'NaN')

df['29'].values[0] = '29'
df['26'] = np.where((df['29'].astype(int) == 26), df['30'], 'NaN')

df['28'] = np.where((df['26'] == 'NaN'), df['27'], 'NaN')

df['29'] = np.where((df['29'] == '29'), df['30'], 'NaN')

df['30'] = np.where((df['32'] == '30'), df['33'], 'NaN')

df['31'] = np.where((df['35'] == '31'), df['36'], 'NaN')

df['32'] = np.where((df['38'] == '32'), df['39'], 'NaN')

df['33'] = np.where((df['41'].astype(int) == 33.0), df['42'], 'NaN')

df['34'] = np.where((df['44'].astype(int) == 34.0), df['45'], 'NaN')

df['35'] = np.where((df['47'].astype(int) == 35.0), df['48'], 'NaN')

df['36'] = np.where((df['50'].astype(int) == 36.0), df['51'], 'NaN')

df['38']


df.drop(['37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52'], axis=1, inplace=True)
df.drop([0], axis=0, inplace=True)

df.rename(columns={'25': 'Int_Temperature', '26': 'Int_Humidity', '27': 'Int_Coin_cell_voltage',
                   '28': 'Temperature', '29': 'Battery_Voltage', '30': 'Ultra_Depth', '31': 'Velocity',
                   '32': 'RSSI', '33': 'Signal_Speed', '34': 'Unnamed', '35': 'Depth_Pressure', '36': 'Barometric_Reference',
                   '37': 'Signal_Strength', '38': 'Provider', '39': 'Cellular_technology', '40': 'Roaming'}, inplace=True)
df.to_csv('data11.csv', sep=";")

conn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=MIC-BCEN-K05\SQLEXPRESS,54342;"
            "Database=datalogger;"
            "UID=user2;"
            "PWD=Premtazmo1234;")
conn = pyodbc.connect(conn_str)

cursor = conn.cursor()

cursor.execute('''
		CREATE TABLE data (
			Int_Temperature nvarchar(50),
			Int_Humidity nvarchar(50),
			Int_Coin_cell_voltage nvarchar(50),
			Temperature nvarchar(50),
			Battery_Voltage nvarchar(50),
			Ultra_Depth nvarchar(50),
			Velocity nvarchar(50),
			RSSI nvarchar(50),
			Signal_Speed nvarchar(50),
			Unnamed nvarchar(50),
			Depth_Pressure nvarchar(50),
			Barometric_Reference nvarchar(50),
			Signal_Strength nvarchar(50),
			Provider nvarchar(50),
			Cellular_technology nvarchar(50),
			Roaming nvarchar(50)
			)
               ''')

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO data (Int_Temperature, Int_Humidity, Int_Coin_cell_voltage, Temperature, Battery_Voltage,
                Ultra_Depth, Velocity, RSSI, Signal_Speed, Unnamed, Depth_Pressure, Barometric_Reference, Signal_Strength,
                Provider, Cellular_technology, Roaming)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                row.Int_Temperature,
                row.Int_Humidity,
                row.Int_Coin_cell_voltage,
                row.Temperature,
                row.Battery_Voltage,
                row.Ultra_Depth,
                row.Velocity,
                row.RSSI,
                row.Signal_Speed,
                row.Unnamed,
                row.Depth_Pressure,
                row.Barometric_Reference,
                row.Signal_Strength,
                row.Provider,
                row.Cellular_technology,
                row.Roaming
                )
conn.commit()


