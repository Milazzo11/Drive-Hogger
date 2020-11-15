import sys
import time
import threading
import random


fr = open("data.txt", "r")
f_lines = fr.readlines()
fr.close()
# reads from data file

mb_counter = input("Enter amount of data (MB) to write > ")

try:  # if the user doesn't enter an integer, the program will stop
    mb_counter = int(mb_counter)
except:
    print("Entry Error")
    time.sleep(2)
    sys.exit()

counter = 0
# defines a counter to represent the number of files written

up_counter = mb_counter * 18
# multiplies by 18 to correctly represent the amount of data written
# the data.txt file is currently ~55 kb, and 55 x 18 ~ 1000 kb = 1 MB
# change this multiplier if the file data is changed


print("Loading...")


def slow_func():  # writes files
    global counter
    global f_lines

    if counter < up_counter:
        scounter = str(counter)
        randval = str(random.random())

        f = open(f"slowfiles\\data{scounter}{randval}.txt", "w")
        f.writelines(f_lines)
        f.close()
    else:
        sys.exit()


while True:
    for y in range(10):
        if counter < up_counter:  # if the target isn't reached the program will keep running
            counter += 1
            x = threading.Thread(target=slow_func)
            x.start()
        else:  # if the target is reached the program will stop
            print("Complete")
            time.sleep(2)
            sys.exit()