from tkinter import *
from tkinter.messagebox import showerror
from tkinter.ttk import Combobox
import pandas as pd
import joblib
main_window = Tk()
main_window.geometry ('670x400')
main_window.title("House Price Prediction")


def convert_MsZoning(a):
    if a == 'Low Density area':
        return 0
    elif a == 'Medium Density Area':
        return 1
    elif a == 'Village Area':
        return 3
    elif a == 'High Density Area':
        return 4
    else:
        return 2


def convert_Utilities(b):
    if b == 'All utilities included':
        return 0
    else:
        return 1

def convert_LotConfig(c):
    if c == 'Inside lot':
        return 0
    elif c == 'Corner lot':
        return 2
    elif c == 'CulDSac':
        return 3
    elif c == 'Frontage of 2 sides':
        return 1
    else:
        return 4

def convert_LandSlope(d):
    if d == 'Gentle slope':
        return 0
    elif d == 'Moderate Slope':
        return 1
    else:
        return 2

def convert_ExterCond(e):
    if e == 'Average':
        return 0
    elif e == 'Good':
        return 1
    elif e == 'Fair':
        return 2
    elif e == 'Excellent':
        return 4
    else:
        return 3

def convert_Heating(f):
    if f == 'Gas warm air furnace':
        return 0
    elif f == 'Gas/hot/water/steam':
        return 1
    elif f == 'Gravity furnace':
        return 2
    elif f == 'Wall furnace':
        return 3
    elif f == 'Hot/water/steam/heat':
        return 4
    else:
        return 5


def convert_PoolQC(g):
    if g == 'No Pool':
        return 0
    elif g == 'Good':
        return 3
    elif g == 'Excellent':
        return 1
    else:
        return 2


def convert_MiscFeature(msf):
    if msf == 'None':
        return 0
    elif msf == 'Shed (over 100 SF)':
        return 1
    elif msf == '2nd Garage':
        return 2
    elif msf == 'Other':
        return 3
    else:
        return 4


def convert_OverallCond(i):
    if i == 'Very Poor':
        return 1
    elif i == 'Poor':
        return 2
    elif i == 'Fair':
        return 3
    elif i == 'Below Average':
        return 4
    if i == 'Average':
        return 5
    elif i == 'Above Average':
        return 6
    elif i == 'Good':
        return 7
    elif i == 'Very Good':
        return 8
    else:
        return 9


def convert_OverallQual(g):
    if g == 'Very Poor':
        return 1
    elif g == 'Poor':
        return 2
    elif g == 'Fair':
        return 3
    elif g == 'Below Average':
        return 4
    if g == 'Average':
        return 5
    elif g == 'Above Average':
        return 6
    elif g == 'Good':
        return 7
    elif g == 'Very Good':
        return 8
    elif g == 'Excellent':
        return 9
    else:
        return 10



def calculate():
    Ms_Zo = convert_MsZoning(Mszoning.get())
    Util = convert_Utilities(Utilities.get())
    Ltcf = convert_LotConfig(LotConfig.get())
    Lnds = convert_LandSlope(LandSlope.get())
    extcond = convert_ExterCond(ExterCond.get())
    heat = convert_Heating(Heating.get())
    PQ = convert_PoolQC(PoolQC.get())
    Misc = convert_MiscFeature(MiscFeature.get())
    ovcnd = convert_OverallCond(OverallCond.get())
    ovc = convert_OverallQual(OverallQual.get())

    tlsa = TotalBsmtSF.get("1.0",END)
    #if TotalBsmtSF.get("1.0", END)=="\n":

    try:
        tbsa = int(tlsa)
    except ValueError:
        print("The value is not numerical")
        showerror(title="value Error", message="total basement surface Area should be a numerical value")
        return

    frstsurface = first_FlrSF.get("1.0", END)
    try:
        frst_surface = int(frstsurface)
    except ValueError:
        showerror(title="value Error" , message = "First floor surface Area should be a numerical value")
        return

    GrLa = GrLivArea.get("1.0", END)
    try:
        Grnd_lA = int(GrLa)
    except ValueError:
        showerror(title="value Error", message="Ground Living Area should be a numerical value")
        return

    Flb = FullBath.get("1.0", END)
    try:
        Full_Bath = int(Flb)
    except ValueError:
        showerror(title="value Error", message=" Number of Bathrooms field  should have a numerical value")
        return

    TotRms = TotRmsAbvGrd.get("1.0", END)
    try:
        Total_rooms = int(TotRms)
    except ValueError:
        showerror(title="value Error", message=" Number of rooms should be a numerical value")
        return

    FireP = Fireplaces.get("1.0", END)
    try:
        Fire_place = int(FireP)
    except ValueError:
        showerror(title="value Error", message=" Number of Fireplaces should be a numerical value")
        return

    Grgcars = GarageCars.get("1.0", END)
    try:
        cars_in_garage = int(Grgcars)
    except ValueError:
        showerror(title="value Error", message=" Garage Capacity should be a numerical value")
        return

    Grgarea = GarageArea.get("1.0", END)
    try:
        garage_Area = int(Grgarea)
    except ValueError:
        showerror(title="value Error", message=" Garage Area should be a numerical value")
        return


    inputs = [ 'MSZoning' ,'Utilities', 'LotConfig', 'LandSlope','ExterCond', 'Heating', 'PoolQC',
               'MiscFeature', 'TotalBsmtSF', '1stFlrSF' ,'GrLivArea', 'FullBath','TotRmsAbvGrd',
               'Fireplaces','GarageCars','GarageArea', 'OverallCond' ,'OverallQual'
            ]

    df = pd.DataFrame([[Ms_Zo,Util,Ltcf,Lnds,extcond,heat,PQ,Misc,tbsa,frst_surface,Grnd_lA,
                        Full_Bath,Total_rooms,Fire_place,cars_in_garage,garage_Area,
                        ovcnd,ovc]], columns=inputs)
    model = joblib.load('trained_model.pkl')
    price = model.predict(df.loc[:, inputs])
    Predicted_price.insert("end-1c",int(price))



# Creating ComboBoxes
l1 = Label(main_window, text= 'Select Zoning of the Property')
Mszoning = StringVar()
cbox_1 = Combobox(main_window, textvariable= Mszoning,values =['Low Density area',
                                                               'Medium Density Area','Village Area',
                                                               'High Density Area','Commercial Area'])
l1.grid(row = 0, column= 0)
cbox_1.grid(row = 0, column= 5)
cbox_1.current(0)

l2 = Label(main_window, text= 'Select Included Utilities')
Utilities = StringVar()
cbox_2 = Combobox(main_window, textvariable= Utilities,values =['All utilities included','Electricity and Gas Only'])
l2.grid(row = 0, column= 10)
cbox_2.grid(row = 0, column= 15)
cbox_2.current(0)

l3 = Label(main_window, text= 'Select Lot Configurataion')
LotConfig = StringVar()
cbox_3 = Combobox(main_window, textvariable= LotConfig,values =['Inside lot','Corner lot','CulDSac','Frontage of 2 sides','Frontage of 3 sides'])
l3.grid(row = 1, column= 0)
cbox_3.grid(row = 1, column= 5)
cbox_3.current(0)

l4 = Label(main_window, text= 'Select LandSlop')
LandSlope = StringVar()
cbox_4 = Combobox(main_window, textvariable= LandSlope,values =['Gentle slope','Moderate Slope','Severe Slope'])
l4.grid(row = 1, column= 10)
cbox_4.grid(row = 1, column= 15)
cbox_4.current(0)

l5 = Label(main_window, text= 'Select External Condition')
ExterCond = StringVar()
cbox_5 = Combobox(main_window, textvariable= ExterCond,values =['Average','Good','Fair','Excellent','Poor'])
l5.grid(row = 2, column= 0)
cbox_5.grid(row = 2, column= 5)
cbox_5.current(0)

l6 = Label(main_window, text= 'Select Heating Type')
Heating = StringVar()
cbox_6 = Combobox(main_window, textvariable= Heating,values =['Gas warm air furnace','Gas/hot/water/steam','Gravity furnace','Wall furnace',
                                                              'Hot/water/steam/heat','Floor Furnace'])
l6.grid(row = 2, column= 10)
cbox_6.grid(row = 2, column= 15)
cbox_6.current(0)

l7 = Label(main_window, text= 'Select Pool Quality')
PoolQC = StringVar()
cbox_7 = Combobox(main_window, textvariable= PoolQC,values =['No Pool','Good','Excellent','Fair'])
l7.grid(row = 3, column= 0)
cbox_7.grid(row = 3, column= 5)
cbox_7.current(0)

l8 = Label(main_window, text= 'Select Misc Features')
MiscFeature = StringVar()
cbox_8 = Combobox(main_window, textvariable= MiscFeature,values =['None','Shed (over 100 SF)','2nd Garage','Other','Tennis Court'])
l8.grid(row = 3, column= 10)
cbox_8.grid(row = 3, column= 15)
cbox_8.current(0)

l9 = Label(main_window, text= 'Select Overall Condition')
OverallCond = StringVar()
cbox_9 = Combobox(main_window, textvariable= OverallCond,values =['Very Poor','Poor','Fair','Below Average','Average','Above Average','Good','Very Good','Excellent'])
l9.grid(row = 4, column= 0)
cbox_9.grid(row = 4, column= 5)
cbox_9.current(0)

l10 = Label(main_window, text= 'Select Overall Quality')
OverallQual = StringVar()
cbox_10 = Combobox(main_window, textvariable= OverallQual,values =['Very Poor','Poor','Fair','Below Average','Average','Above Average','Good','Very Good','Excellent','Very Excellent'])
l10.grid(row = 4, column= 10)
cbox_10.grid(row = 4, column= 15)
cbox_10.current(0)

l11 = Label(main_window, text= 'Enter total basement square feet')
l11.grid(row = 8, column = 0)
TotalBsmtSF = Text(main_window,width=15, height = 0.3)
TotalBsmtSF.grid(row = 8 , column = 5)

l12 = Label(main_window, text= 'Enter 1st floor square feet')
first_FlrSF = Text(main_window,width=15, height = 0.3)
l12.grid(row = 8, column = 10)
first_FlrSF.grid(row = 8 , column = 15)

l13 = Label(main_window, text= 'Enter GrLivArea square feet')
l13.grid(row = 9, column = 0)
GrLivArea = Text(main_window,width=15, height = 0.3)
GrLivArea.grid(row = 9 , column = 5)

l14 = Label(main_window, text= 'Enter # of bathrooms')
FullBath = Text(main_window,width=15, height = 0.3)
l14.grid(row = 9, column = 10)
FullBath.grid(row = 9 , column = 15)

l15 = Label(main_window, text= 'Enter # of rooms')
l15.grid(row = 10, column = 0)
TotRmsAbvGrd = Text(main_window,width=15, height = 0.3)
TotRmsAbvGrd.grid(row = 10 , column = 5)

l16 = Label(main_window, text= 'Enter # of Fireplaces')
Fireplaces = Text(main_window,width=15, height = 0.3)
l16.grid(row = 10, column = 10)
Fireplaces.grid(row = 10 , column = 15)

l17 = Label(main_window, text= 'Enter garage capacity (#cars)')
l17.grid(row = 11, column = 0)
GarageCars = Text(main_window,width=15, height = 0.3)
GarageCars.grid(row = 11 , column = 5)

l18 = Label(main_window, text= 'Enter Size of garage in square feet')
GarageArea = Text(main_window,width=15, height = 0.3)
l18.grid(row = 11, column = 10)
GarageArea.grid(row = 11 , column = 15)

l18 = Label(main_window, text= 'Estimated House Price')
l18.place(x= 360, y =220)
#l18.config(width=150)
l18.config(font=("Courier", 15))

Predicted_price = Text(main_window,width=20, height = 2)
Predicted_price.place(x = 385, y = 250)
b = Button(main_window, text = 'Calculate Price', command = calculate)
b.place(x =390, y = 300 , width=150, height = 65)
main_window.mainloop()