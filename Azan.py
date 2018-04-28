import winsound
import time
from datetime import datetime


while True:
    hello = str(datetime.now().time())
    hi = hello[0:8]
    print(hi)
    
    if hi == "03:56:00":
        print("Fajr Time")
        winsound.Beep(1500,60000)



    if hi == "13:02:00" :
        print("Zuhr Time")
        winsound.Beep(1500,60000)
        


    if hi == "18:02:00":
        print("Zuhr Time")
        winsound.Beep(1500,60000)



    if hi == "20:23:00":
        print("Maghrib Time")
        winsound.Beep(1500,60000)
        
        
    if hi == "21:34:00":
        print("Isha Time")
        winsound.Beep(1500,60000)

    else:
        continue



