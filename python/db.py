import sqlite3
from datetime import datetime, date, time

try:
    sqlite_connection = sqlite3.connect('alabama.db')
    #sqlite_create_table_query = '''CREATE TABLE accounts (
     #                           name TEXT NOT NULL,
      #                          money INTEGER,
		#						skin INTEGER,
		#						admin INTEGER,
		#						joining_date TIMESTAMP);'''
    cursor = sqlite_connection.cursor()
    #print("Database connect to SQLITE")
    #cursor.execute(sqlite_create_table_query)
    #sqlite_connection.commit()
    #print("Table Create")

    cursor.close()

except sqlite3.Error as error:
    print("Failed connect to sqlite", error)
finally:
		if (sqlite_connection):
			sqlite_connection.close()
			print("Connection to Sqlite closed.")

def UpdateAccount(pInfolist):
	try:
		sqlite_connection = sqlite3.connect('alabama.db')
		cursor = sqlite_connection.cursor()
		sqlite_update_account_query = ''' UPDATE accounts 
											SET admin = {1}, 
											money = {2}, 
											skin = {3}
											WHERE name = {4}'''.format(
												pInfolist['Admin'], 
												pInfolist['Money'],
												pInfolist['Skin'],
												pInfolist['Name']
											)
		cursor.execute(sqlite_update_account_query)
		sqlite_connection.commit()
		cursor.close()
	except sqlite3.Error as error:
		print("Failed connect to sqlite", error)
	finally:
		if (sqlite_connection):
			sqlite_connection.close()
			print("Connection to Sqlite closed.")
	return True

def AddAccount(pInfolist):
	try:
		sqlite_connection = sqlite3.connect('alabama.db')
		cursor = sqlite_connection.cursor()
		sqlite_insert_account_query = ''' INSERT INTO accounts
										(name, money, skin, admin, joining_date)
										VALUES ( ?, ?, ?, ?, ?)'''
		cursor.execute(sqlite_insert_account_query, ( str(pInfolist['Name']), int(pInfolist['Money']), int(pInfolist['Skin']), int(pInfolist['Admin']), datetime.now() ))
		cursor.close()
	except sqlite3.Error as error:
		print("Failed connect to sqlite")
	finally:
		if (sqlite_connection):
			sqlite_connection.close()
			print("Connection to Sqlite closed")
	return True