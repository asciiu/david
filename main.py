import httplib2
import os
import psycopg2

from googleapiclient import discovery
from google.oauth2 import service_account

try:
    connection = psycopg2.connect(user="...",
                                password="...",
                                host="...",
                                port="5432",
                                database="...")

    cursor = connection.cursor()
    available_inventory = "select * from available_inventory"
    cursor.execute(available_inventory)
    inventory = cursor.fetchall() 
     
    values = [
        ['Category', 'market_name', 'market_and_category', 'today_avail', 'tomorrow_avail', 'avg_r7_avail', 'avg_r14_avail', 'avg_r21_avail', 'avg_r28_avail'],
        #['Box_Truck', 'Dallas', 'Dallas_Box_Truck', '9', '9', '9', '9', '9', '10'],
        #['Box_Truck', 'Denver', 'Denver_Box_Truck', '9', '9', '9', '9', '9', '10'],
        #['Box_Truck', 'Los Angeles', 'Los Angeles_Box_Truck', '9', '9', '9', '9', '9', '10'],
        #['Cargo_Van', 'Atlanta', 'Atlanta_Cargo_Van', '9', '9', '9', '9', '9', '10'],
        #['Cargo_Van', 'Bay Area', 'Bay Area_Cargo_Van', '9', '9', '9', '9', '9', '10'],
        #['Cargo_Van', 'Dallas', 'Dallas_Cargo_Van', '9', '9', '9', '9', '9', '10'],
        #['Cargo_Van', 'Denver', 'Denver_Cargo_Van', '9', '9', '9', '9', '9', '10'],
        #['Cargo_Van', 'Houston', 'Houston_Cargo_Van', '9', '9', '9', '9', '9', '10'],
        #['Cargo_Van', 'Los Angeles', 'Los Angeles_Cargo_Van', '9', '9', '9', '9', '9', '10'],
        #['Cargo_Van', 'Miami', 'Dallas_Cargo_Van', '9', '9', '9', '9', '9', '10'],
        #['Cargo_Van', 'San Antonio', 'Dallas_Cargo_Van', '9', '9', '9', '9', '9', '10'],
        #['Cargo_Van', 'San Diego', 'Dallas_Cargo_Van', '9', '9', '9', '9', '9', '10'],
        #['Cargo_Van', 'Seattle', 'Dallas_Cargo_Van', '9', '9', '9', '9', '9', '10'],
    ]

    for row in inventory:
        values.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])

    for row in values:
        print(row)

    # All that follows here is the google sheet specific stuffs that updates 
    # the sheets values 
    #scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
    #secret_file = os.path.join(os.getcwd(), 'client_secret.json')

    #spreadsheet_id = '1O2prMvyR0anLt-rSlWpeTXpv8iGHQ2VA8XQ2w6QLXV0'
    #range_name = 'Inventory!A1'

    #credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
    #service = discovery.build('sheets', 'v4', credentials=credentials)

    #data = {
    #  'values' : values 
    #}

    #service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, body=data, range=range_name, valueInputOption='USER_ENTERED').execute()


except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

except OSError as error:
    print("Error encountered doing the thing", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")