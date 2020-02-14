from time import *
from pygame import mixer
#import time
print(asctime())
print("welcome")
#function to init 
def play(file, stopit):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while(True):
        x = input()
        if x == stopit:
            mixer.music.stop()
            break

def wlog(text):
    with open('log.txt', 'a') as f:
        f.write(f"{asctime()} - {text}")

if __name__ == "__main__":
    # intiating time for activities
    init_eyesecs = time()
    init_watersecs = time()
    init_exsecs = time()
    eyesecs = 30*60
    watersecs = 40*60
    exsecs = 60*60

    #starting infinte loop
    while True:
        if time() - init_watersecs > watersecs:
            print("water drinking time\ntype 'drank' when finish")
            play('water.mp3', 'drank')
            wlog('Drank water')
        if time() - init_eyesecs > eyesecs:
            print("Eye exercise time\ntype 'done' when finish")
            play('eye.mp3', 'done')
            wlog('eyes exercise done')
        if time() - init_exsecs > exsecs:
            print("Exercise time\ntype 'done' when finish")
            play('workout.mp3', 'done')
            wlog('workout done')

