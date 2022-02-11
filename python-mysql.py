from datetime import date, datetime
import mysql.connector

 
def read_everything(table_name):
    query = f"SELECT * FROM {table_name}"

    cursor.execute(query)

    for item in cursor:
        print(item)


def insert_data(first_name, last_name, email):
    query = f"INSERT INTO customers (first_name, last_name, email, birthdate, createdAt, updatedAt) VALUES('{first_name}', '{last_name}', '{email}', '{date.today()}', '{datetime.now()}', '{datetime.now()}')"

    cursor.execute(query)



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

    else:
        read_everything('customers')

        # Adding 1 Million Dummy Data
        # for i in range(1000000):
        #     insert_data('fname', 'lname', f"fname@lname{i}.com")

        cnx.commit()

    finally:
        cursor.close()
        cnx.close()