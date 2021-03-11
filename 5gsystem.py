#Main program for 5G system

#Import statements:
#These statements arer used to interact with the tx and rx class of users 1 and 2.

import satscr as user1
import satscr2 as user2

#math library imported for using basic trigonometric functions to be seen below:
import math

#Radio Access Network- Transmits signal from user 1 to user 2 and vice versa
#Txuser1, txuser2, rxuser1 & rxuser2 represent the transmitted and received signals of user 1 and 2, which will be 
#used by the CoreNet for further analysis
class Ran:
    ipt1 = int(input('enter no usr1- 1:call/text 2:InternetUse 3:Network OS'))
    ipt2 = int(input('enter no usr2- 1:Call/text 2:InternetUse 3:Network OS'))
    txuser1 = user1.Transmitter.txfn(ipt1)
    txuser2 = user2.Transmitter.txfn(ipt2)
    rxuser1 = user1.Receiver.rxfn(txuser2)
    rxuser2 = user2.Receiver.rxfn(txuser1)

#Core Network- Interprets signals sent to the users through the RAN, instructs Applayer accordingly
#Two static methods have been declared to interpret signals for user1 and user2 separately.
class CoreNet:
#cnbackendu1- corenetwork's backend for user1. (performs background operations)
    @staticmethod
    def cnbackendu1():
        # Calling class RAN to use tx and rx variables mentioned earlier in lines 16-21
        rn = Ran()
        x = range(360)
        out1 = 0
        #Iteratively compare each point of the waveform with a standard sin, cos and tan wave, and return op variable
        #for user1 to applayer, which then displays a message to user1 accordingly
        for i in x:
            if rn.txuser1[i] == math.sin(math.radians(i)):
                out1 = 1
            elif rn.txuser1[i] == math.cos(math.radians(i)):
                out1 = 2
            elif rn.txuser1[i] == math.tan(math.radians(i)):
                out1 = 3
        return out1
#Corenetwork backend for user2- same functions as in the case of user1. out2 is the op variable for user2, which helps applayer act accordingly
    @staticmethod
    def cnbackendu2():
        rn = Ran()
        x = range(360)
        out2 = 0
        for i in x:
            if rn.txuser2[i] == math.sqrt(i):
                out2 = 1
            elif rn.txuser2[i] == x[i] * x[i]:
                out2 = 2
            elif rn.txuser2[i] == x[i] / 2:
                out2 = 3
        return out2

#Application Layer- Accesses the output variables of corenet to decide what to do
class AppLayer:
    #Accessing corenet functions mentioned above lines 27-56
    op1 = CoreNet.cnbackendu1()
    op2 = CoreNet.cnbackendu2()
    #Variables which define user interaction with the system.
    check1 = 0
    check2 = 0
    sendu1 = ''
    sendu2 = ''
    paswd1 = 0
    paswd2 = 0
    #Screen lock or PIN for smartphones of users 1 and 2. Ideas for better security measures are greatly appreciated 
    paswdchk1 = 1234
    paswdchk2 = 5678

    #Decision mechanism of Applayer, based on corenet inputs for user 1 and 2. Output directly displayed on common screen
    if op1 == 1:
        print('sin wave- call and text user1')
        check1 = int(input('Enter 1 for call and 2 for text'))
        if check1 == 1:
            u1voice = user2.Receiver.u2call(10, 16000)
        elif check1 == 2:
            sendu1 = input('Write something to user2')
            u1txtmsg = user2.Receiver.texting(sendu1)

    elif op1 == 2:
        print('cos wave- Internet user1')
        url = input('Enter your url')
        u1net = user1.Receiver.u1internet(url)

    elif op1 == 3:
        print('tan wave- netos user1')
        paswd1 = int(input('Enter your pin'))
        if paswd1 == paswdchk1:
            print('Hello valued customer')
            ask1 = int(input('1- Enter details, 2- Read details'))
            out1 = user1.Receiver.netos(ask1)
        else:
            print('Incorrect password, please try again')

    if op2 == 1:
        print('square root- call and text user2')
        check2 = int(input('Enter 1 for call and 2 for text'))
        if check2 == 1:
            u2voice = user1.Receiver.u1call(10, 16000)
        elif check2 == 2:
            sendu2 = input('Write something to user1')
            u2txtmsg = user2.Receiver.texting(sendu2)

    elif op2 == 2:
        print('sq no- Internet user2')
        url2 = input('Enter your url')
        u2net = user2.Receiver.u2internet(url2)
    elif op2 == 3:
        print(' divide by 2- netos user2')
        paswd2 = int(input('Enter your pin'))
        if paswd2 == paswdchk2:
            print('Hello valued customer')
            ask2 = int(input('1-Enter info, 2- Read details'))
            out2 = user2.Receiver.netos(ask2)
        else:
            print('Incorrect password, please try again')
