from playsound import playsound
import time

CLEAR_AND_RETURN="\033[H" #we clear the entire terminal,cleared and returned to that home position,printed over what we had before
def alarm(seconds):
  time_gone=0

  while time_gone< seconds:
    time.sleep(1) #wait for one seconds
    time_gone+=1
    time_left=seconds-time_gone
    minutes_left=time_left//60
    seconds_left=time_left%60
    print(f"{CLEAR_AND_RETURN}Alarm will sound in:   {minutes_left:02d}:{seconds_left:02d}")# 02d means make this 2 digit and padded with 0
  playsound("alarm.mp3")
minutes=int(input("How many minutes to wait:  "))
seconds=int(input("How many seconds to wait:  ")) 
total_seconds=minutes*60+seconds 
alarm(total_seconds)    


        

