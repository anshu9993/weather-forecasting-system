# Design and implement weather forecasting system.

# importing the libraries
import requests as r
from tkinter import *
from tkinter import ttk
import datetime
from PIL import ImageTk, Image


root = Tk()
root.title("Forecast")
root.geometry("400x370")
root['background'] = "LightSky Blue"

# CITYNAMES
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur""Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
city_name=StringVar()
com=ttk.Combobox(root,text="MITS Weather App",values=list_name,font=("bold", 11),textvariable=city_name)
com.place(x=170,y=30)



#note
w_lable=Label(root,text="Current weather",bg= "LightSky Blue" , font=("bold", 12))   
w_lable.place(x=10,y=30)

# Time
dt = datetime.datetime.now()
hour = Label(root, text=dt.strftime('%H: %M '), bg= "LightSky Blue",font=("bold", 9))
hour.place(x=10, y=52)

# Theme for the respective time the application is used
if int((dt.strftime('%H'))) >=6 & int((dt.strftime('%H'))) <=18:
	img = ImageTk.PhotoImage(Image.open('sunn.png'))
	panel = Label(root, image=img)
	panel.place(height=80, width=80,x=10, y=90)
else:
	img = ImageTk.PhotoImage(Image.open('moon.png'))
	panel = Label(root, image=img)
	panel.place(height=70, width=70, x=10, y=90)

# Current Temperature
lable_temp = Label(root, text="...", width=0, bg='LightSky Blue',font=("bold", 25))
lable_temp.place(x=142, y=90)
lable_tempc = Label(root, text="°C", width=0, bg='LightSky Blue',font=("bold", 13))
lable_tempc.place(x=179, y=90)

# weather description
lable_w_description = Label(root, text="...", width=0,bg='LightSky Blue', font=("bold", 17))
lable_w_description.place(x=142, y=125)

# wind
w_lable = Label(root, text="Wind", width=0,
bg='LightSky Blue', font=("bold", 12))
w_lable.place(x=10, y=210)
wi_lable = Label(root, text="...", width=0,bg='LightSky Blue', font=("bold", 12))
wi_lable.place(x=10, y=230)
wik_lable = Label(root, text="Km/h", width=0,bg='LightSky Blue', font=("bold", 12))
wik_lable.place(x=43, y=230)

# feels like
f_lable = Label(root, text="feels like", width=0,
bg='LightSky Blue', font=("bold", 12))
f_lable.place(x=100, y=210)
fl_lable = Label(root, text="...", width=0,bg='LightSky Blue', font=("bold", 12))
fl_lable.place(x=100, y=230)

# humidity
humi = Label(root, text="Humidity",width=0,
bg='LightSky Blue', font=("bold", 12))
humi.place(x=200, y=210)
lable_humidity = Label(root, text="...", width=0,bg='LightSky Blue', font=("bold", 12))
lable_humidity.place(x=200, y=230)
lablep_humidity = Label(root, text="%", width=0,bg='LightSky Blue', font=("bold", 12))
lablep_humidity.place(x=230, y=230)


# Other temperature details
maxi = Label(root, text="Max Temp", width=0,bg='LightSky Blue', font=("bold", 12))
maxi.place(x=10, y=300)
max_temp = Label(root, text="...", width=0,bg='LightSky Blue', font=("bold", 12))
max_temp.place(x=10, y=320)
maxp_temp = Label(root, text="°C", width=0,bg='LightSky Blue', font=("bold", 8))
maxp_temp.place(x=40, y=320)

mini = Label(root, text="Min. Temp. ", width=0,bg='LightSky Blue', font=("bold", 12))
mini.place(x=310, y=210)
min_temp = Label(root, text=" ...", width=0,bg='LightSky Blue', font=("bold", 12))
min_temp.place(x=310, y=230)
minp_temp = Label(root, text="°C", width=0,bg='LightSky Blue', font=("bold", 8))
minp_temp.place(x=340, y=230)


# pressure
prs = Label(root, text="Pressure", width=0,bg='LightSky Blue', font=("bold", 12))
prs.place(x=100, y=300)
prs_l = Label(root, text="...", width=0,bg='LightSky Blue', font=("bold", 12))
prs_l.place(x=100, y=320)
prsp_l = Label(root, text="mb", width=0,bg='LightSky Blue', font=("bold", 12))
prsp_l.place(x=130, y=320)

# visibility
dp = Label(root, text="Visibility ", width=0,bg='LightSky Blue', font=("bold", 12))
dp.place(x=200, y=300)
dp_l = Label(root, text="...", width=0,bg='LightSky Blue', font=("bold", 12))
dp_l.place(x=200, y=320)
dpp_l = Label(root, text="km", width=0,bg='LightSky Blue', font=("bold", 12))
dpp_l.place(x=230, y=320)

def get_data():
    city = city_name.get()
    try:
        response = r.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6df5771e86fcd7302e7024df221ac938")
        response.raise_for_status() 
        data = response.json()
        lable_temp.config(text=int(data["main"]["temp"] - 273.15))
        lable_w_description.config(text=data["weather"][0]["description"])
        lable_humidity.config(text=data["main"]["humidity"])
        fl_lable.config(text=int(data["main"]["feels_like"] - 273.15))
        min_temp.config(text=int(data["main"]["temp_min"] - 273.15))
        max_temp.config(text=int(data["main"]["temp_max"] - 273.15))
        dp_l.config(text=data["visibility"])
        prs_l.config(text=data["main"]["pressure"])
        wi_lable.config(text=data["wind"]["speed"])
      

        
    except r.exceptions.RequestException as e:
        # Handle network or API request errors
        print(f"Error: {e}")
    except KeyError as e:
        # Handle missing keys in the API response
        print(f"KeyError: {e}")

default_city = "Gwalior"  
# Function to fetch weather data for the default city
def set_default_city_data():
    city_name.set(default_city)
    get_data()
set_default_city_data()

# Button
done_button=Button(root,text="search",font=("bold", 7),command=get_data)
done_button.place(x=360,y=30)


root.mainloop()

