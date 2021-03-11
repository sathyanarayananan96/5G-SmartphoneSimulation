# Program for user 1

#Import statements
import math
import numpy as np
import csv
import webbrowser
import sounddevice as sd
import matplotlib.pyplot as plt

#Transmitter class- contains transmit function, with input ipvar representing user1's connection to the 5G network
#txfn generates the sinusoidal waveforms to be sent to user2 through the 5G network
class Transmitter:

    @staticmethod
    def txfn(ipvar):
        sig = np.zeros(360)
        x = range(360)
        if ipvar == 1:
            for i in x:
                sig[i] = math.sin(math.radians(x[i]))
        elif ipvar == 2:
            for j in x:
                sig[j] = math.cos(math.radians(x[j]))
        else:
            for k in x:
                sig[k] = math.tan(math.radians(x[k]))
        return sig

#Receiver class- Contains 5 functions, to be described with inputs from the 5G system through user2
class Receiver:

    #Represents a steady connection- the function of the RAN is shown to the user
    @staticmethod
    def rxfn(lstvar1):
        print('Connection established with user2')
        return lstvar1

    #Responsible for receiving text message from user 2 through 5G system and displaying to user1
    @staticmethod
    def texting(lstvar2):
        print('Hello User1, you have a new message from user2')
        print(lstvar2)
        return lstvar2

    #This function represents mobile data usage: I've used the simple webbrowser library to open a browser page like google chrome from python, on the command
    #of the users through the 5G system.
    @staticmethod
    def u1internet(lstvar3):
        new = 2
        webbrowser.open(lstvar3, new=new)
        return lstvar3

    #Network Operating system- my version of it. It provides the services of the network service provider in my case
    #Allows us to modify our address and contact info, and other plan information, and updates a csv file. Shows o/p to user
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
    def u1call(d, fs):
        print('Talk to user2')
        voice = sd.rec(int(d*fs), fs, 1)
        sd.wait()
        sd.play(voice, fs)
        plt.plot(voice)
        plt.show()
        return d, fs
