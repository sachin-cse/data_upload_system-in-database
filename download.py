import os
import csv
import sqlite3
import pdfkit

    
def download_file_csv():
    # connect to database connection
    cnx = sqlite3.connect("./database/mydata.db")
    cursor = cnx.cursor()

    # write query

    query = "SELECT * FROM data"
    cursor.execute(query)

# check output folder exit or not
    if not os.path.exists(r'D:\\Upload_System\\output'):
        os.mkdir(r'D:\\Upload_System\\output')
    
    # write data to the output file
    with open(r'D:\\Upload_System\\output\\csv\\output.csv', 'w', newline='') as csvfile:
        csvwriter= csv.writer(csvfile)
        csvwriter.writerow([i[0] for i in cursor.description])
        csvwriter.writerows(cursor)

        # show download successfully message
    print("File download successfully!")

    # Close database connection
    cursor.close()
    cnx.close()


# download file in pdf format
def download_file_pdf():
    cnx = sqlite3.connect("./database/mydata.db")
    cursor = cnx.cursor()


    query = "SELECT * FROM data"
    cursor.execute(query)

    
    # get data as HTML table
    html_table = "<table style='border-collapse:collapse; border:1px solid black; width:60%; margin:auto;'><caption style='font-weight:bold; font-size:20px; color:blue;'>Student Data</caption><tr>{}</tr>{}</table>".format(
        "".join("<th style='padding:10px; border:1px solid black; background-color:lightblue;'>{}</th>".format(column[0]) for column in cursor.description),
        "".join("<tr style='background-color: lightgray;'>{}</tr>".format(
            "".join("<td style='padding: 10px; border: 1px solid black;'>{}</td>".format(cell) for cell in row)
        ) for row in cursor.fetchall())
    )

    if not os.path.exists(r'D:\\Upload_System\\output'):
        os.mkdir(r'D:\\Upload_System\\output')

    with open(r'D:\\Upload_System\\output\\html\\output.html', 'w') as html_file:
        html_file.write(html_table)

    # convert HTML to PDF
    pdfkit.from_file(r'D:\\Upload_System\\output\\html\\output.html', r'D:\\Upload_System\\output\\pdf\\output.pdf')

    # show download successfully message
    print("File download successfully!")

    # Close database connection
    cursor.close()
    cnx.close()

# prompt message
print("Choose file format you want to download..")
print("1.csv format\n2.pdf format")
format_choice = input()
if format_choice == "1":
    # Call the function to download the file in CSV format
    download_file_csv()
    print("File downloaded in CSV format.")
    
elif format_choice == "2":
    # Call the function to download the file in PDF format
    download_file_pdf()
    print("File downloaded in PDF format.")
    
else:
    print("Invalid choice. Please enter either 1 or 2.")


