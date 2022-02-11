from datetime import date, datetime
import mysql.connector

 
def read_everything(table_name):
    query = f"SELECT * FROM {table_name}"

    cursor.execute(query)

    for item in cursor:
        print(item)

    


# query = f"INSERT INTO customers (first_name, last_name, email, birthdate, createdAt, updatedAt) VALUES('UGUR', 'FIRAT', 'ugur@firat123.com', '1111-11-11', '{datetime.now()}', '{datetime.now()}')"

# cursor.execute(query)


# query = "SELECT * FROM customers"
# cursor.execute(query)

# for customer in cursor:
#     print(customer)






# print(datetime.now())
# 2022-02-11 23:43:01.113319


if __name__ == "__main__":    
    try:
        cnx = mysql.connector.connect(user='root', password='password',
                                host='localhost',
                                database='job_task')

        if cnx:
            print('Python MySQL Connection Established!')

        cursor = cnx.cursor()

    except Exception as err:
        print(err)


    read_everything('customers')

    cnx.commit()
    cursor.close()
    cnx.close()