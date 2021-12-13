#creatinga alark clock program 
#sound will ring at specified time


import time
from playsound import playsound

alarm_time = input('Enter time hour and minute: ').split()


# time_data = time.localtime()
# hour = time_data.tm_hour
# minn = time_data.tm_min

# print(time.strftime("%H:%M",times))

# print(time.strptime('10:09',"%H:%M"))
flag = True
while flag:
    time_data = time.localtime()
    hour = time_data.tm_hour
    minn = time_data.tm_min

        
    if hour==int(alarm_time[0]) and minn==int(alarm_time[1]):
        flag = False
        print(f'Your time is {time.strftime("%H:%M",time_data)}')
        print("Wake Up!")
        playsound("path to audio file")