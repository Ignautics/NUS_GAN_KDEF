from glob import glob
import os
import numpy as np

f = open("label.txt", "w")

image = glob((os.path.join("", '*.JPG')))
image.sort()

def print_exp(exp):
    a = np.zeros(7)
    a[exp] = 1
    for v in a:
        f.write("%d" % v)

def print_ag(ag):
    a = np.zeros(5)
    a[ag] = 1
    for v in a:
        f.write("%d" % v)


for im in image:
    if (im[1] == 'F'):
        gender = 0
    elif (im[1] == 'M'):
        gender = 1
    else:
        print("Error gender:%s" % im[1])
    
    s = im[4:6]
    if (s == "AF"):
        exp = 0
    elif (s == "AN"):
        exp = 1
    elif (s == "DI"):
        exp = 2
    elif (s == "HA"):
        exp = 3
    elif (s == "NE"):
        exp = 4
    elif (s == "SA"):
        exp = 5
    elif (s == "SU"):
        exp = 6
    else:
        print("ERROR expression: %s" % im)


    s = im[6:8]
    if (s == "FL"):
        ag = 0
    elif (s == "HL"):
        ag = 1
    elif (s == "HR"):
        ag = 2
    elif (s == "FR"):
        ag = 3
    elif (im[6] == "S"):
        ag = 4
    else:
        print("ERROR Angle:%s " % im)

    f.write("%d" % gender)

    print_exp(exp)

    print_ag(ag)
    f.write("\n")


