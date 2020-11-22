import psycopg2


'''
Method used to establish an inital connection to determine if database exists
'''
def testDatabaseConnection():
    connection = False
    try:
        connection = psycopg2.connect(user = "russell", password="n0passw0rd", host = "127.0.0.1", port = "5432", database = "postgres")
        cursor = connection.cursor()
        
    except:
        print("Testing: Can not connect to database")

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("Could connect to database")
            return True
        else:
            return False
