# Import dependencies
from tkinter import *
from tkinter import ttk
import mysql.connector
import sqlalchemy
import json
import datetime as dt
import getpass
import mysql

with open("parameters/config.json") as config:
    param = json.load(config)

# Establishing engine
engine = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                          format(param['Teletron'][0]['user'],
                                                 param['Teletron'][0]['password'],
                                                 param['Teletron'][0]['host'],
                                                 param['Teletron'][0]['database']), echo=False)
# Defining entry form
def entry():
    # getting form data
    temperature = Temperature.get()
    pressure = Pressure.get()
    recorddate = (dt.date.today()).strftime('%Y-%m-%d')
    CreatedBy = getpass.getuser()
    # applying empty validation
    if temperature == ''  or pressure =='' or recorddate == '' or CreatedBy == '':  message.set("fill the empty field!!!")
    else:
        # Create connection object to Epi
        Epi_con = engine.connect()
        # Preparing SQL query to INSERT a record into the database.
        sql = """INSERT INTO crudexample (RecordDate, Temperature, Pressure,CreatedBy)
                                    VALUES (%s, %s, %s, %s) """

        data = (recorddate, temperature, pressure , CreatedBy)

        try:
            # executing the sql command
            Epi_con.execute(sql, data)
            # commit changes in database
            Epi_con.commit()
        except:
            message.set("Data Stored successfully")


#def read():

#def update():

#def delete():

#def dbsetup():



# defining Registration form function
def Entryform():
    global entry_screen
    entry_screen = Tk()
    # Setting title of screen
    entry_screen.title("Data Entry Form")
    # setting height and width of screen
    entry_screen.geometry("400x270")
    # declaring variable
    global message
    global RecordDate
    global Temperature
    global Pressure
    global CreatedBy

    Temperature = IntVar()
    Pressure = IntVar()
    RecordDate = StringVar()
    CreatedBy = StringVar()
    message = StringVar()
    # Creating layout of Data Entry Form
    Label(entry_screen, width="300", text="Please enter details below", bg="blue", fg="white").pack()

    # Temperature Label
    Label(entry_screen, text= "Temperature * ").place(x=20, y=80)
    # Temperature textbox
    Entry(entry_screen, textvariable= Temperature).place(x=140, y=82)

    # Pressure Label
    Label(entry_screen, text = "Pressure * ").place(x=20, y=120)
    # Pressure textbox
    Entry(entry_screen, textvariable = Pressure).place(x=140, y=122)

    # Label for displaying entry status[success/failed]
    Label(entry_screen, text = "", textvariable=message).place(x=95, y=240)

    # Submit Button
    Button(entry_screen, text="Submit", width=10, height=1, bg="gray", command=entry).place(x=105, y=210)
    Button(entry_screen, text="Update", width=10, height=1, bg="gray", command=entry).place(x=205, y=210)
    Button(entry_screen, text="Delete", width=10, height=1, bg="gray", command=entry).place(x=305, y=210)
    entry_screen.mainloop()

# calling function entry form
Entryform()