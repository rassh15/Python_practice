# Healthy Progammer

'''
Create a program which reminds to do the following in an interval of time and 
An audio file will played to remind about the task to do 
audio only stop when person type appropriate keyword.

Water :  water.mp3 (3.5 litre) - Drank - log
Eyes :   eye.mp3 - ev 30min - EyDone - log
Exercise : physical.mp3 - every 45 min = ExDone - log

Use Pygame module to play audio file
'''
import time
from datetime import date, datetime
from pygame import mixer
import threading

def water_reminder():

    print("Water Reminder")
    audio_file('water')
    log_file('water')

def eye_reminder():
    print("Eye Reminder")
    audio_file('eye')
    log_file('eye')

def exercise_reminder():
    print("Exercise Reminder")
    audio_file('physical')
    log_file('exercise')

def log_file(name):
    print("Log File")
    with open("C:\\Users\\Ars\\Documents\\python\\Git\\Python Practice\\07_Exercise_Data\\log.txt",'a') as f:
        f.write(f"{name} at {datetime.now()}\n")

def audio_file(name):
    #Starting the mixer

    mixer.init()

    #Loading the song
    mixer.music.load("C:\\Users\\Ars\\Documents\\python\\Git\\Python Practice\\07_Exercise_Data\\"+name+".mp3")

    #Playing the song
    mixer.music.play()

    while True:
        choice = ''
        if name == 'water':
            print("Please Drink Water and type Drank : ")
            choice = input()
        elif name == 'eye':
            print("Please do an exercise and type EyDone : ")
            choice = input()

        elif name == 'physical':
            print("Please do the exercise and type ExDone : ")
            choice = input()

        
        if choice == 'Drank' or choice == 'EyDone' or choice == 'ExDone':

            mixer.music.stop()
            break






if __name__ == '__main__':
    
    #audio_file("physical")
    #water_reminder()

    
    tmp1 = datetime.now().timestamp()
    tmp2 = datetime.now().timestamp()
    tmp3 = datetime.now().timestamp()
    start_time = time.time()
    second = 59


    print("Healthy Reminder")
    while True:

        curr_time = time.time()
        elapsed_time = curr_time - start_time

        #cr_dt = datetime.now().timestamp()
        # print('siff  ',int(elapsed_time))
        

        if elapsed_time > second:
            break

        elif int(datetime.now().timestamp() - tmp1) == 20:
            water_reminder()
            tmp1 = datetime.now().timestamp()
            
        elif int(datetime.now().timestamp() - tmp2) == 38:
            eye_reminder()
            tmp2 = datetime.now().timestamp()
            
        elif int(datetime.now().timestamp() - tmp3) == 48:
            exercise_reminder()
            tmp3 = datetime.now().timestamp()



'''
        elif int(elapsed_time) == 20:
            water_reminder()

        elif int(elapsed_time) == 38:
            eye_reminder()

        elif int(elapsed_time) == 48:
            exercise_reminder()        '''

        