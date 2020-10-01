#healthy programmer
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylog.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__' :
    # musiconloop("water.mp3", "stop")

    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watertime = 2100
    eyestime =  2400
    exercisetime = 3000

    while True:
        if time() - init_water > watertime:
            print("water time,type 'drank' to stop the alarm")
            musiconloop("water.mp3" , "drank")
            init_water = time()

            log_now("water drank at ")

        if time() - init_eyes > eyestime:
            print("eye exercise time,type 'done' to stop the alarm")
            musiconloop("eyes.mp3", "done")
            init_eyes = time()

            log_now("eye exercise done at ")

        if time() - init_exercise > exercisetime:
            print("physical exercise time, type 'done' to stop the alarm")
            musiconloop("physicalex.mp3", "done")
            init_exercise = time()

            log_now("exercise done at ")


