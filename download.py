import os
import csv
import mysql.connector

    
def download_file_csv():
    # connect to database connection
    cnx = mysql.connector.connect(user='root', host='localhost', database='raw')
    cursor = cnx.cursor()

    # write query

    query = "SELECT * FROM data"
    cursor.execute(query)

# check output folder exit or not
    if not os.path.exists(r'C:\\Upload_System\\output'):
        os.mkdir(r'C:\\Upload_System\\output')
    
    # write data to the output file
    with open(r'C:\\Upload_System\\output\\output.csv', 'w', newline='') as csvfile:
        csvwriter= csv.writer(csvfile)
        csvwriter.writerow([i[0] for i in cursor.description])
        csvwriter.writerows(cursor)

        # show download successfully message
    print("File download successfully!")

    # Close database connection
    cursor.close()
    cnx.close()

    # call the function
download_file_csv()
