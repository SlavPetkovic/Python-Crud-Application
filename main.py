# Import Dependencies
from lib.DataImport import dataupdate
import datetime as dt
import getpass

# Define final function
def dataload(name):
    try:
        MetricId = input("Please Insert MetricId: ")
        DataPoint = input("Please Insert Data Point: ")
        EffectiveBeginDate = input("Please Insert Effective begin date: ")
        EffectiveEndDate = input("Please Insert Effective begin date: ")
        CreatedDate = (dt.date.today()).strftime('%Y-%m-%d')
        CreatedBy = getpass.getuser()

        dataupdate(MetricId, DataPoint, EffectiveBeginDate, EffectiveEndDate, CreatedDate, CreatedBy)
        print("Data has been inserted successfully")
    except:
        print("Data load was not successful")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataload('PyCharm')
