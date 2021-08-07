from datetime import datetime
from playsound import playsound 
alarm_time = input("Hi Satyam,\nEnter the time of alarm to be set in this 12hr format :HH:MM:SS AM/PM\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11]
alarm_message = input("What is the alarm set for: ")
print("Great Master Satyam, Alarm set for: ",alarm_time)

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if (alarm_period == current_period):
        if (alarm_hour == current_hour):
            if (alarm_minute == current_minute):
                if (alarm_seconds == current_seconds):
                    print("Sir You have to \n",alarm_message)
                    playsound('audio.mp3')
                    break