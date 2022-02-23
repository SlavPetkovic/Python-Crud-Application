# Import Dependencies
from lib.DataImport import dataupdate
import datetime as dt
import getpass

# Define final function
def dataload(name):
    try:
        RecordDate = (dt.date.today()).strftime('%Y-%m-%d')
        Temperature = input("Please Insert Temperature Data Point: ")
        Pressure = input("Please Insert Pressure Data Point: ")
        CreatedBy = getpass.getuser()

        dataupdate(RecordDate, Temperature, Pressure, CreatedBy)
        print("Data has been inserted successfully")
    except:
        print("Data load was not successful")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataload('PyCharm')
