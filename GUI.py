from tkinter import *
from  tkinter import  ttk
#importing connection
import  mysql.connector
import sqlalchemy
import json
import datetime as dt
import getpass
import mysql.connector
import json
import sqlalchemy

with open("parameters/config.json") as config:
    param = json.load(config)

# Establishing engine
engine = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                          format(param['EpiProd'][0]['user'],
                                                 param['EpiProd'][0]['password'],
                                                 param['EpiProd'][0]['host'],
                                                 param['EpiProd'][0]['database']), echo=False)
# Defining entry form
def entry():
    # getting form data
    MetricId1 = MetricId.get()
    DataPoint1 = DataPoint.get()
    EffectiveBeginDate1 = EffectiveBeginDate.get()
    EffectiveEndDate1 = EffectiveEndDate.get()
    CreatedDate1 = (dt.date.today()).strftime('%Y-%m-%d')
    CreatedBy1 = getpass.getuser()
    # applying empty validation
    if MetricId1 == '' or DataPoint1== '' or EffectiveBeginDate1 == '' or EffectiveEndDate1 =='' or CreatedDate1 == '' or CreatedBy1 == '':  message.set("fill the empty field!!!")
    else:
        # Create connection object to Epi
        Epi_con = engine.connect()
        # Preparing SQL query to INSERT a record into the database.
        sql = """INSERT INTO SlavsTest (MetricId, DataPoint, EffectiveBeginDate, EffectiveEndDate, CreatedDate,CreatedBy)
                                    VALUES (%s, %s, %s, %s,%s,%s) """

        data = (MetricId1, DataPoint1, EffectiveBeginDate1, EffectiveEndDate1 , CreatedDate1, CreatedBy1)

        try:
            # executing the sql command
            Epi_con.execute(sql, data)
            # commit changes in database
            Epi_con.commit()
        except:
            message.set("Data Stored successfully")

# defining Registration form function
def Entryform():
    global entry_screen
    entry_screen = Tk()
    # Setting title of screen
    entry_screen.title("Data Entry Form")
    # setting height and width of screen
    entry_screen.geometry("300x270")
    # declaring variable
    global message;
    global MetricId
    global DataPoint
    global EffectiveBeginDate
    global EffectiveEndDate
    global CreatedDate
    global CreatedBy
    MetricId = IntVar()
    DataPoint = IntVar()
    EffectiveBeginDate = StringVar()
    EffectiveEndDate= StringVar()
    CreatedDate = StringVar()
    CreatedBy = StringVar()
    message = StringVar()
    # Creating layout of Data Entry Form
    Label(entry_screen, width="300", text="Please enter details below", bg="green", fg="white").pack()
    # MetricId Label
    Label(entry_screen, text = "MetricId * ").place(x=20, y=40)
    # MetricId textbox
    Entry(entry_screen, textvariable = MetricId).place(x=140, y=42)
    # DataPoint Label
    Label(entry_screen, text= "DataPoint * ").place(x=20, y=80)
    # DataPoint textbox
    Entry(entry_screen, textvariable= DataPoint).place(x=140, y=82)
    # EffectiveBeginDate Label
    Label(entry_screen, text = "EffectiveBeginDate * ").place(x=20, y=120)
    # EffectiveBeginDate textbox
    Entry(entry_screen, textvariable = EffectiveBeginDate).place(x=140, y=122)
    # EffectiveEndDateLabel
    Label(entry_screen, text = "EffectiveEndDate * ").place(x=20, y=160)
    # EffectiveEndDate textbox
    Entry(entry_screen, textvariable = EffectiveEndDate).place(x=140, y=162)
    # Label for displaying entry status[success/failed]
    Label(entry_screen, text = "", textvariable=message).place(x=95, y=240)
    # Submit Button
    Button(entry_screen, text="Submit", width=10, height=1, bg="gray", command=entry).place(x=105, y=210)
    entry_screen.mainloop()

# calling function entry form
Entryform()