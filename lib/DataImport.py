# Import dependencies
import mysql.connector
import json
import sqlalchemy

# read database config file
with open("parameters/config.json") as config:
    param = json.load(config)

# settting up the function with parameters
def dataupdate(RecordDate, Temperature, Pressure, CreatedBy):
    # Connecting to data warehouse
    try:
        engine = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                          format(param['Teletron'][0]['user'],
                                                 param['Teletron'][0]['password'],
                                                 param['Teletron'][0]['host'],
                                                 param['Teletron'][0]['database']), echo=False)

        # Cleaning the data from existing tables MetricValues and Metrics
        Teletron_con = engine.connect()
        # If connection is established, push the data into datawarehouse
        if Teletron_con.connect():
            try:
                sql = """INSERT INTO crudexample (RecordDate, Temperature, Pressure, CreatedBy)
                            VALUES (%s, %s, %s, %s) """
                # Establish the record with set of data to be taken form variables
                record = (RecordDate, Temperature, Pressure, CreatedBy)
                # Execute sql with collected records
                Teletron_con.execute(sql, record)
                # Close connection
                Teletron_con.close()
                # Dispose the engine
                engine.dispose()
            except OSError as e:
                print(e)
    except OSError as e:
        print(e)