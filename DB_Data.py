import mysql.connector
from mysql.connector import Error

def retrieve(username_in):
    try:
        # perform mysql connection
        connection = mysql.connector.connect(host='localhost',
                                             database='fyp',
                                             user='root',
                                             password='')
        # prepare mysql query
        mySql_select_query = "SELECT * FROM wm_index WHERE username='"+username_in+"'"

        cursor = connection.cursor()
        cursor.execute(mySql_select_query)
        data = cursor.fetchall()

        return data
    except mysql.connector.Error as error:
        print("Failed to select record from WMI table {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def fetch(id_in):
    try:
        # perform mysql connection
        connection = mysql.connector.connect(host='localhost',
                                             database='fyp',
                                             user='root',
                                             password='')
        # prepare mysql query
        mySql_select_query = "SELECT * FROM wm_index WHERE id='"+id_in+"'"

        cursor = connection.cursor()
        cursor.execute(mySql_select_query)
        data = cursor.fetchall()

        return data
    except mysql.connector.Error as error:
        print("Failed to select record from WMI table {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def insert(username_in, auditory_score_in, auditory_duration_in, auditory_index_in, visual_score_in, visual_duration_in, visual_index_in, wmi_in):
    try:
        # perform mysql connection
        connection = mysql.connector.connect(host='localhost',
                                             database='fyp',
                                             user='root',
                                             password='')

        # prepare mysql query
        mySql_insert_query = "INSERT INTO wm_index" \
                             "(username, visual_score, visual_duration, auditory_score, auditory_duration, visual_result, auditory_result, wmi_result )" \
                             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        # prepare statement
        recordTuple = (username_in, visual_score_in, visual_duration_in, auditory_score_in, auditory_duration_in, visual_index_in, auditory_index_in, wmi_in)
        cursor = connection.cursor()

        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into WMI table")

    except mysql.connector.Error as error:
        print("Failed to insert record into WMI table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
