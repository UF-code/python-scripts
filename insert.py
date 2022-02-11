import mysql.connector



cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='job_task')

if cnx:
    print('Well Done!')


cursor = cnx.cursor()

query = "SELECT * FROM customers"

cursor.execute(query)

for customer in cursor:
    print(customer)






cnx.close()