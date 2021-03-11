#Main program for 5G system
import satscr as user1
import satscr2 as user2
import math


class Ran:
    ipt1 = int(input('enter no usr1- 1:call/text 2:InternetUse 3:Network OS'))
    ipt2 = int(input('enter no usr2- 1:Call/text 2:InternetUse 3:Network OS'))
    txuser1 = user1.Transmitter.txfn(ipt1)
    txuser2 = user2.Transmitter.txfn(ipt2)
    rxuser1 = user1.Receiver.rxfn(txuser2)
    rxuser2 = user2.Receiver.rxfn(txuser1)


class CoreNet:

    @staticmethod
    def cnbackendu1():
        rn = Ran()
        x = range(360)
        out1 = 0
        for i in x:
            if rn.txuser1[i] == math.sin(math.radians(i)):
                out1 = 1
            elif rn.txuser1[i] == math.cos(math.radians(i)):
                out1 = 2
            elif rn.txuser1[i] == math.tan(math.radians(i)):
                out1 = 3
        return out1

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


class AppLayer:
    op1 = CoreNet.cnbackendu1()
    op2 = CoreNet.cnbackendu2()
    check1 = 0
    check2 = 0
    sendu1 = ''
    sendu2 = ''
    paswd1 = 0
    paswd2 = 0
    paswdchk1 = 1234
    paswdchk2 = 5678

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
