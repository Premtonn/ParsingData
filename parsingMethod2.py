import pandas as pd
import numpy as np
import pyodbc

data = pd.read_csv("ex2.csv", delimiter=";")
df = pd.DataFrame(data)

df.rename(columns={'T': '24'}, inplace=True)

df = df.fillna(0)

df.drop([1, 2, 3], axis=0, inplace=True)

#Parsing the data
for column in df.columns[::3]:
    if (df[f'{column}'] == 'D').any():
        df['24'] = np.where((df[f'{column}'] == 'D'), df[f'{int(column)+1}'], 0)

#change the value to the right one, or remain how it was before, or it's changed to 0. two options.
for column in df.columns[2::3]:
    if (df[f'{column}'] == '25').any():
        df['25'] = np.where((df[f'{column}'] == '25'), df[f'{int(column)+1}'], 0)

    elif (df[f'{column}'] == '26').any():
        df['26'] = np.where((df[f'{column}'] == '26'), df[f'{int(column)+1}'], df['26'])

    elif (df[f'{column}'] == '27').any():
        df['27'] = np.where((df[f'{column}'] == '27'), df[f'{int(column)+1}'], df['27'])

    elif (df[f'{column}'] == '28').any():
        df['28'] = np.where((df[f'{column}'] == '28'), df[f'{int(column)+1}'], 0)

    elif (df[f'{column}'] == '29').any():
        df['29'] = np.where((df[f'{column}'] == '29'), df[f'{int(column)+1}'], df['29'])

    if (df[f'{column}'] == '29').any():
        df['29'] = np.where((df[f'{column}'] == '29'), df[f'{int(column)+1}'], 0)

    elif (df[f'{column}'] == '30').any():
        df['30'] = np.where((df[f'{column}'] == '30'), df[f'{int(column)+1}'], 0)

    elif (df[f'{column}'] == '31').any():
        df['31'] = np.where((df[f'{column}'] == '31'), df[f'{int(column)+1}'], 0)

    elif (df[f'{column}'] == '32').any():
        df['32'] = np.where((df[f'{column}'] == '32'), df[f'{int(column)+1}'], df['32'])

    elif (df[f'{column}'] == 33.0).any():
        df['33'] = np.where((df[f'{column}'].astype(int) == 33.0), df[f'{int(column)+1}'], 0)

    elif (df[f'{column}'] == 34.0).any():
        df['34'] = np.where((df[f'{column}'].astype(int) == 34.0), df[f'{int(column)+1}'], 0)

    elif (df[f'{column}'] == 35.0).any():
        df['35'] = np.where((df[f'{column}'].astype(int) == 35.0), df[f'{int(column)+1}'], df['35'])

    elif (df[f'{column}'] == 36.0).any():
        df['36'] = np.where((df[f'{column}'].astype(int) == 36.0), df[f'{int(column)+1}'], 0)


df.drop(['37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52'], axis=1, inplace=True)
df.drop(0, axis=0, inplace=True)

df.rename(columns={'24': 'Timestamp', '25': 'Int_Temperature', '26': 'Int_Humidity', '27': 'Int_Coin_cell_voltage',
                   '28': 'Temperature', '29': 'Battery_Voltage', '30': 'Ultra_Depth', '31': 'Velocity',
                   '32': 'RSSI', '33': 'Signal_Speed', '34': 'Unnamed', '35': 'Depth_Pressure', '36': 'Barometric_Reference',
                   '37': 'Signal_Strength', '38': 'Provider', '39': 'Cellular_technology', '40': 'Roaming'}, inplace=True)

df.to_csv('new_data.csv', sep=";")

#SQL Server initation
conn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=MIC-BCEN-K05\SQLEXPRESS,54342;"
            "Database=datalogger;"
            "UID=user2;"
            "PWD=Premtazmo1234;")
conn = pyodbc.connect(conn_str)

cursor = conn.cursor()

#Sending data to the local database
"""cursor.execute('''
		CREATE TABLE data_method_2 (
		    Timestamp nvarchar(50),
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
               ''')"""

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO data_method_2 (Timestamp, Int_Temperature, Int_Humidity, Int_Coin_cell_voltage, Temperature, Battery_Voltage,
                Ultra_Depth, Velocity, RSSI, Signal_Speed, Unnamed, Depth_Pressure, Barometric_Reference)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                row.Timestamp,
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
                )
conn.commit()


