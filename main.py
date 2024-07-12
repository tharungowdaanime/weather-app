from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import random as me 




root = Tk() #window
root.title("Weather App")
root.geometry("1030x600") #dimensions
root.config(bg="#4682B4") #baground colour
root.resizable(False, False)


# Function to get weather data




    
def getWeather():
    city = text_feild.get() #gets the name of the city inputed

    geolocator = Nominatim(user_agent="geoapiExercise") 
    location = geolocator.geocode(city)  # Geocode the city name
    obj = TimezoneFinder() 

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"latitude: {round(location.latitude, 4)}°N")
    long_lon.config(text=f"longitude: {round(location.longitude, 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    api_key = "you_api_key"  # Replace with your actual WeatherAPI key
    api = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location.latitude},{location.longitude}"

    response = requests.get(api)
    json_data = response.json() #gets data in json format


    #Below line gets Temperature , hunidity , pressure , wind speed , description
    temp1 = json_data["current"]["temp_c"]
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure_mb']
    wind = json_data['current']['wind_kph']
    description = json_data['current']['condition']['text']

    temp2.config(text=(temp1,"°C"))
    hum.config(text=(humidity,"%"))
    pre.config(text=(pressure,"hPa"))
    wind3.config(text=(wind,"m/s"))
    des2.config(text=(description))




    #uses datetime module to get day
    first = datetime.now()
    day1.config(text=first.strftime("%A"))
    
    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))
    
    third = second+timedelta(days=2)
    day3.config(text=third.strftime("%A"))
    
    fourth= third+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))
    
    fifth = fourth+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))
    
    sixth = fifth+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))
    
    seventh = sixth+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


    #forecast 
    forecast_api = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location.latitude},{location.longitude}&days=7"
    forecast_response = requests.get(forecast_api)
    forecast_data = forecast_response.json()["forecast"]["forecastday"]

    # Below lines get the forecast data and put this into bottom 7 boxes
    tdays1.config(text=f"{forecast_data[0]['date']}\nDay: {forecast_data[0]['day']['maxtemp_c']}°C\nNight: {forecast_data[0]['day']['mintemp_c']}°C\n{forecast_data[0]['day']['condition']['text']}")
    tdays2.config(text=f"{forecast_data[1]['date']}\nDay: {forecast_data[1]['day']['maxtemp_c']}°C\nNight: {forecast_data[1]['day']['mintemp_c']}°C\n{forecast_data[1]['day']['condition']['text']}")
    tdays3.config(text=f"{forecast_data[2]['date']}\nDay: {forecast_data[2]['day']['maxtemp_c']}°C\nNight: {forecast_data[2]['day']['mintemp_c']}°C\n{forecast_data[2]['day']['condition']['text']}")
    tdays4.config(text=f"{forecast_data[3]['date']}\nDay: {forecast_data[3]['day']['maxtemp_c']}°C\nNight: {forecast_data[3]['day']['mintemp_c']}°C\n{forecast_data[3]['day']['condition']['text']}")
    tdays5.config(text=f"{forecast_data[4]['date']}\nDay: {forecast_data[4]['day']['maxtemp_c']}°C\nNight: {forecast_data[4]['day']['mintemp_c']}°C\n{forecast_data[4]['day']['condition']['text']}")
    tdays6.config(text=f"{forecast_data[5]['date']}\nDay: {forecast_data[5]['day']['maxtemp_c']}°C\nNight: {forecast_data[5]['day']['mintemp_c']}°C\n{forecast_data[5]['day']['condition']['text']}")
    tdays7.config(text=f"{forecast_data[6]['date']}\nDay: {forecast_data[6]['day']['maxtemp_c']}°C\nNight: {forecast_data[6]['day']['mintemp_c']}°C\n{forecast_data[6]['day']['condition']['text']}")



    

    

# UI setup
app_icon = PhotoImage(file="imeages/logo2.png") #app icon
root.iconphoto(False, app_icon)

Round_box = PhotoImage(file="imeages/rectanglr_box2.png") #box where temp,hmidity,pressure,windspeed and description is shwm
Label(root, image=Round_box, bg="#4682B4").place(x=70, y=90)

label1 = Label(root, text="Temperature", font=('Helvetica', 15), fg="white", bg="#000000")  #temp in upper box
label1.place(x=95, y=125)

label2 = Label(root, text="Pressure", font=('Helvetica', 15), fg="white", bg="#000000")  #pressure in upper box
label2.place(x=95, y=155)

label3 = Label(root, text="Humidity", font=('Helvetica', 15), fg="white", bg="#000000")  #humidity in upper box
label3.place(x=95, y=185)

label4 = Label(root, text="Wind Speed", font=('Helvetica', 15), fg="white", bg="#000000") #wind speed in upper box
label4.place(x=95, y=215)

label5 = Label(root, text="Description", font=('Helvetica', 15), fg="white", bg="#000000")  #description in uppper box
label5.place(x=95, y=245)

search_image = PhotoImage(file="imeages/round_black_box2.png")
search_feild = Label(image=search_image, bg="#4682B4").place(x=400, y=110) #search or entry field

search_icon = PhotoImage(file="imeages/icons8-search-48.png")
search_icon_image = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#000000", command=getWeather).place(x=690, y=130) #seach icon image button

weather_image = PhotoImage(file="imeages/weather_image2.png")
weather_icon = Label(search_feild, image=weather_image, bg="#000000").place(x=435, y=125) #weather icon in text field taken from openweatherimage

text_feild = tk.Entry(root, justify="center", width=15, font=('Poppins', 18, 'bold'), bg="#000000", border=0, fg="white")
text_feild.place(x=490, y=135) #entry field

Bottom_box = Frame(root, width=1100, height=230, bg="#212120").pack(side=BOTTOM) #big bottom box

#two bottom boxes one square and other 6 inverted rectangle
firstbox = PhotoImage(file="imeages/rectanglr_box2.png")
secondbox = PhotoImage(file="imeages/bootom_boxs8.png")

#frames
firstframe = Label(Bottom_box, image=firstbox, bg="#212120")
firstframe.place(x=5, y=370)

secondframe = Label(Bottom_box, image=secondbox, bg="#212120")
secondframe.place(x=255, y=400)

thirdframe = Label(Bottom_box, image=secondbox, bg="#212120")
thirdframe.place(x=380, y=400)

fourthframe = Label(Bottom_box, image=secondbox, bg="#212120")
fourthframe.place(x=505, y=400)

fifthframe = Label(Bottom_box, image=secondbox, bg="#212120")
fifthframe.place(x=630, y=400)

sixthframe = Label(Bottom_box, image=secondbox, bg="#212120")
sixthframe.place(x=755, y=400)

seventhframe = Label(Bottom_box, image=secondbox, bg="#212120")
seventhframe.place(x=880, y=400)

#labels for the day of the week
day1 = Label(firstframe, font="Helvetica 20", bg="#000000", fg="white")
day1.place(x=40, y=10)

day2 = Label(secondframe,font="Helvetica 10", bg="#000000", fg="white")
day2.place(x=10, y=10)

day3 = Label(thirdframe, font="Helvetica 10", bg="#000000", fg="white")
day3.place(x=10, y=10)

day4 = Label(fourthframe, font="Helvetica 10", bg="#000000", fg="white")
day4.place(x=10, y=10)

day5 = Label(fifthframe, font="Helvetica 10", bg="#000000", fg="white")
day5.place(x=10, y=10)

day6 = Label(sixthframe, font="Helvetica 10", bg="#000000", fg="white")
day6.place(x=10, y=10)

day7 = Label(seventhframe, font="Helvetical 10", bg="#000000", fg="white")
day7.place(x=10, y=10)


#Labels for forecast data
tdays1 = Label(firstframe,font=("Verdana",14),bg="#000000",fg="#4682B4")
tdays1.place(x=15,y=80)

tdays2 = Label(secondframe,font=("Verdana",8),bg="#000000",fg="#4682B4")
tdays2.place(x=10,y=40)

tdays3 = Label(thirdframe,font=("Verdana",8),bg="#000000",fg="#4682B4")
tdays3.place(x=10,y=40)

tdays4 = Label(fourthframe,font=("Verdana",8),bg="#000000",fg="#4682B4")
tdays4.place(x=7,y=40)

tdays5 = Label(fifthframe,font=("Verdana",8),bg="#000000",fg="#4682B4")
tdays5.place(x=10,y=40)

tdays6 = Label(sixthframe,font=("Verdana",8),bg="#000000",fg="#4682B4")
tdays6.place(x=10,y=40)

tdays7 = Label(seventhframe,font=("Verdana",8),bg="#000000",fg="#4682B4")
tdays7.place(x=10,y=40)


#clock
clock = Label(root, font=("Verdana", 30, 'bold'), fg="white", bg="#4682B4")
clock.place(x=490, y=40)

#timezone
timezone = Label(root, font=("Helvetica", 30), fg="white", bg="#4682B4")
timezone.place(x=780, y=110)

#longitude and latitude of the location
long_lat = Label(root, font=("Courier", 10), fg="white", bg="#4682B4")
long_lat.place(x=800, y=170)

long_lon = Label(root, font=("Courier", 10), fg="white", bg="#4682B4")
long_lon.place(x=800, y=195)


# Labels for temperature, pressure, humidity, wind speed, and description
temp2 = Label(root,font=("Helvetica",11),fg="white",bg="#000000")
temp2.place(x=215,y=130)
hum = Label(root,font=("Helvetica",11),fg="white",bg="#000000")
hum.place(x=215,y=190)
pre = Label(root,font=("Helvetica",11),fg="white",bg="#000000")
pre.place(x=185,y=160)
wind3 = Label(root,font=("Helvetica",11),fg="white",bg="#000000")
wind3.place(x=215,y=220)
des2 = Label(root,font=("Helvetica",11),fg="white",bg="#000000")
des2.place(x=215,y=250)

# generates random numbers from random module and places anime imag accordingly . It looks fu :)
random_anime = me.randint(1,3)

if random_anime == 1:
    anime = PhotoImage(file="imeages/goku_image2.png")
    goku = Label(root, image=anime, bg="#4682B4")
    goku.place(x=440,y=210)

    goku2 = Label(root, text="Don't tell anyone but i am the most powerfull character", font=('Montserrat', 17,'bold'), fg="white", bg="#4682B4")
    goku2.place(x=550, y=250)

elif random_anime == 2:
    anime2 = PhotoImage(file="imeages/luffy2.png")
    luffy = Label(root, image=anime2, bg="#4682B4")
    luffy.place(x=440,y=210)

    luffy2 = Label(root, text="Don't tell anyone but i am the pirate king", font=('Montserrat', 17,'bold'), fg="white", bg="#4682B4")
    luffy2.place(x=550, y=250)

else :
    anime3 = PhotoImage(file="imeages/naruto3.png")
    naruto = Label(root, image=anime3, bg="#4682B4")
    naruto.place(x=440,y=210)

    naruto2 = Label(root, text="Don't tell anyone but i am the Hokage", font=('Montserrat', 17,'bold'), fg="white", bg="#4682B4")
    naruto2.place(x=550, y=250)

myname = Label(root, text="Created By I.P THARUN GOWDA", font=('Courier', 15), fg="white", bg="#4682B4")  #temp in upper box
myname.place(x=35, y=340)

root.mainloop() #Don't change this line


# don't tell anyone but i am the honered one , and soon i concured autonomus ultra instinct and became a hokage then i went on to concuer the sea and became a pirate king , soon i acuired bankai and defeathed ywach and saved soul society and killed muzand , i am the greatest (this was just for fun don't take it seriously , i like watching anime so i simply icluded it here)
