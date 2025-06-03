import time
import datetime
import os
#hides the pygame prompt without going in and editing the pygame files.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
#allows for the use of sound files
import pygame

#defining our function
def set_alarm(alarm_time):
    #initial print that grabs the input
    print(f"Alarm set for {alarm_time}")
    #set the location sound file in our library to a variable. Used a local path since its in the same folder
    sound_file = "Clock_Ring.mp3"
    #we want to loop through and print each second until the alarm hits, so we will use a while loop
    #I went with a boolean version as I find them more readable
    is_running = True
    while is_running:
        #grabbing the current time from the datetime module. It is a method of the datetime class. I used the strtime method to convert the output to a string with the same format as our input.
        curr_time = datetime.datetime.now().strftime("%H:%M:%S")
        #prints the current time each second. Will always run at least once.
        print(curr_time)
        #checks to see if the current time equals our alarm time
        if curr_time == alarm_time:
            #print a wake up message
            print("Wake Up! 🛌")
            #calling the initialize method of the mixer class in pygame.
            pygame.mixer.init()
            #loading the sound file
            pygame.mixer.music.load(sound_file)
            #play the sound file
            pygame.mixer.music.play()
            #in order to make sure the sound file plays in full, I am using the get_busy() function in a while loop
            #otherwise the condition becoming false would end the loop prematurley
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        #if not we sleep for 1s and check the comparitor again.
        time.sleep(1)

#standard dunder main block. Don't want the main being run if this file is being imported
if __name__ == "__main__":
    alarm_time = input("Enter the alamr time (HH:MM:SS): ")
    set_alarm(alarm_time)