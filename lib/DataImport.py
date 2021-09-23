# Import dependencies
import mysql.connector
import json
import sqlalchemy

# read database config file
with open("parameters/config.json") as config:
    param = json.load(config)

# settting up the function with parameters
def dataupdate(MetricId, DataPoint, EffectiveBeginDate, EffectiveEndDate, CreatedDate,CreatedBy):
    # Connecting to data warehouse
    try:
        engine = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                          format(param['EpiProd'][0]['user'],
                                                 param['EpiProd'][0]['password'],
                                                 param['EpiProd'][0]['host'],
                                                 param['EpiProd'][0]['database']), echo=False)

        # Cleaning the data from existing tables MetricValues and Metrics
        Epi_con = engine.connect()
        # If connection is established, push the data into datawarehouse
        if Epi_con.connect():
            try:
                sql = """INSERT INTO SlavsTest (MetricId, DataPoint, EffectiveBeginDate, EffectiveEndDate, CreatedDate,CreatedBy)
                            VALUES (%s, %s, %s, %s,%s,%s) """
                # Establish the record with set of data to be taken form variables
                record = (MetricId, DataPoint, EffectiveBeginDate, EffectiveEndDate, CreatedDate,CreatedBy)
                # Execute sql with collected records
                Epi_con.execute(sql, record)
                # Close connection
                Epi_con.close()
                # Dispose the engine
                engine.dispose()
            except OSError as e:
                print(e)
    except OSError as e:
        print(e)