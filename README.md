# 5G-SmartphoneSimulation
A small project in which I've simulated the working of a cellular network as seen from our smartphones.
# Introduction
- Based on my simple understanding of 5G networks and with the help of standard python libraries, I've created a Python project which shows the working of 5G networks &
  how this is seen on our smartphones, tablets & other devices.
- To show this working, I've written 3 separate programs, with the main program being the 5G system. The other 2 programs represent the users of the network. Based on the context
  of the situation, the user can either be a person, the internet or the network service provider. I've done this based on an idea of our real world usage of smartphones. We can     call or text other people, connect to the internet through mobile data services, or view and change our data plans and other customer details through an app.
# The main program - 5G system:
- My 5G system consists of three layers, similar to the real network: The RAN(Radio Access Network), the CoreNet(Core Network) and the application layer, which interacts with       users. I have highly simplified the functioning of each of these components. The RAN in real life is responsible for sending physical RF signals, and establishing connections     between routers and users in the network.
- In my program, the RAN is responsible for connecting user 1 and user 2 by transmitting specific waveforms (simple sinusoidal waveforms, square waveforms, etc) to each other.
- These waveforms represent the 3 basic functions Call/Text, Mobile Internet usage & network service options.
- In the real 5G network, the core network acts as the medium of communication between the RAN and the application layer. It performs all the background work required to run our     applications, connect to the internet and other closed networks (Student emails and login for universities, employee accounts for organizations, bank accounts, etc), and passes   control to the application layer through the network operating system.
- The network OS splits the system into different instances of itself to quickly serve multiple users and IOT machines at once. I'm trying to construct a simplified version of the   network OS which fits in with my current system. For now, the network OS duties are also performed by the core network, and I'm only considering one instance of the network's     operation at any point of time.
- My core network identifies the signal sent to each user through the RAN and instructs the application layer to send messages accordingly to the user.
- The application layer is the medium of interaction between the users and the system. I have made a very simple version on Python without any graphical user interface. Any ideas
  or improvements on this aspect will be gratefully welcomed and accepted.
# The Users:
- The other two programs are symmetrical to each other. They simply represent our smartphone with a basic transmitter and receiver antenna which is used to connect and interact     with the network. My program for the user involves two classes Transmitter and Receiver. The transmitter sends the basic signals which is passed to the other user's receiver       class through the RAN. The receiver class shows the output of the 5G system through the application layer, based on the interaction between the users.
# On to the programs>>>
I'll move on to the code and explain my intentions through comments.
