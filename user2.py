# User 2- Same as user 1. Look at the user1.py program
# This program is written symmetrically to show the interaction between two users through the 5G network.
import math
import numpy as np
import csv
import webbrowser
import sounddevice as sd
import matplotlib.pyplot as plt


class Transmitter:

    @staticmethod
    def txfn(ipvar):
        sig = np.zeros(360)
        x = range(360)
        if ipvar == 1:
            for i in x:
                sig[i] = math.sqrt(x[i])
        elif ipvar == 2:
            for j in x:
                sig[j] = x[j] * x[j]
        else:
            for k in x:
                sig[k] = x[k] / 2
        return sig


class Receiver:

    @staticmethod
    def rxfn(lstvar):
        print('Connection established with user1')
        return lstvar

    @staticmethod
    def texting(lstvar2):
        print('Hello User2, you have a new message from user1')
        print(lstvar2)
        return lstvar2

    @staticmethod
    def u2internet(lstvar3):
        new = 2
        webbrowser.open(lstvar3, new=new)
        return lstvar3

    @staticmethod
    def netos(lstvar4):
        if lstvar4 == 1:
            print('Enter or change your details')
            name = input('Enter first name')
            area = input('Enter your location')
            phno = int(input('Enter 10 digit phone no'))
            monthdata = int(input('Enter your monthly data requirements'))
            with open('csvtest.csv', mode='a') as csv_file:
                fieldnames = ['Name', 'area', 'Phone No', 'Monthly Data']
                newdata = csv.DictWriter(csv_file, fieldnames=fieldnames)
                newdata.writeheader()
                newdata.writerow({'Name': name, 'area': area, 'Phone No': phno, 'Monthly Data': monthdata})

        elif lstvar4 == 2:
            print('Your plan details')
            with open('csvtest.csv') as csv_file:
                details = csv.DictReader(csv_file)
                for i in details:
                    print(i)

        return lstvar4

    @staticmethod
    def u2call(d, fs):
        print('Talk to user1')
        voice = sd.rec(int(d * fs), fs, 1)
        sd.wait()
        sd.play(voice, fs)
        plt.plot(voice)
        plt.show()
        return d, fs
