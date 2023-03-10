import csv
import sqlite3
import time
import os
import openpyxl

def insert_data(file_path):
    try:
        # validate file extension
        if file_path.lower().endswith('.csv'):
            with open(file_path, newline='') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)
                data = [tuple(row) for row in reader]
        elif file_path.lower().endswith('.xlsx'):
            wb = openpyxl.load_workbook(file_path)
            ws = wb.active
            data = [tuple(cell.value for cell in row) for row in ws.iter_rows(min_row=2)]
        else:
            raise ValueError("Unsupported file format. Only .csv and .xlsx files are allowed.")

        conn = sqlite3.connect("./database/mydata.db")
        cursor = conn.cursor()

        # CREATE TABLE IF NOT EXISTS
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, email TEXT)
        ''')

        start_time = time.time()
        # data insert into the table
        cursor.executemany('INSERT INTO data (name, age, email) VALUES (?, ?, ?)', data)

        conn.commit()
        conn.close()
        end_time = time.time()
        execution_time = end_time - start_time
        print('Data added to the database successfully!')
        print(f"Execution time: {execution_time:.2f} seconds")
    except Exception as e:
        print(f"An error occurred: {e}") 
