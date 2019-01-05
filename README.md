# tcp-udp-client-servers
Implementations of TCP and UDP client and servers that can be run in conjunction. Also contains implementations of servers and clients with artificial packet loss.


IMPORTANT INFORMATION ABOUT HOW THIS ALL WORKS!!!!
An important aspect in this project is the String format of the OC and numbers. The
format required for input of the client is as follows: operatorNum1,Num2. For example:
+1,2
Is a valid input, which translates to 1+2
/5,3
Is another valid input, which translates to 5/3
Any form that does not conform to this style cannot be parsed correctly. Please make
sure you put your input in with that format when you are using.

I separated this project into 6 python files. client_udp.py and server_udp.py simulate a
UDP client server process when run in tandem. client_udp.py contains a method called
client_udp(), that starts the client process when run. The main method in the client.udp.py file
just runs the method, so client can be run via main, or via a python command line call with the
file.


server_udp.py simulates the server processes in the process. It contains the method
server_udp() that runs the process when it is executed. The main method contains a call to this
method, so you can run it by calling the method itself, or running main.


client_tcp.py and server_tcp.py simulate a TCP client server process when both are run
in tandem. They are written in the same vein as the udp equivalents, except these methods are
implemented via TCP instead. client_tcp.py contains the client_tcp() method which starts the
client process. This can be either run with the method call in the python terminal, or by running
the main method in the py file itself.


server_tcp.py simulates the server process. This one contains the method server_tcp()
which can be run either by a method call in the file itself, or just by running the main method of
the py file.


The last two files are client_udp_loss.py and server_udp_loss.py. These files were made
for part 2 of the project. client_udp_loss.py works similarly to how I’d implemented it previously,
but this one has the potential of timing out if it takes too long for the response. This is handled in
the method client_udp() or just by running the main method of it.


server_udp_loss.py is used to handle the server side. In this side, the fixed drop
probability is specified as an argument in the method server_probability(probability) where
probability is the probability of the packet not being dropped (must be between 0 and 1 or else
exception is thrown). You can run this my running the method in the python terminal and
specifying the probability you want. You can also run the method method, which defaults
probability to .5.


In terms of tradeoffs, I focused more on making sure my program was easily readable instead of
fastest running. I could have possibly implemented aspects such as the valid_message method
I wrote cleaner and more efficiently. But again, I was more focused on understanding how these
protocols both worked.


I could improve my project by adding in an exit feature to the server that can be sent from the
client. As it stands right now, both client and server run indefinetly until a Ctrl+C command is
received. I could have also made the application’s main methods implement some sort of user
interface. Right now, running the main methods runs everything through the Python Terminal
itself. The last improvement comes at the extra credit portion. I implemented it via the parameter
list of the method call in server_udp_loss.py. So, while the developer can specify the loss rate,
the user of the program cannot via the client_udp_loss.py main method. I wish I could have
found a way to do this.


The pieces of code each work in pairs(server_tcp.py works with client_tcp.py for example).
Ideally, the user would run both main methods in the client and server python files, input their
OC and message in the client side, and receive results. This works with the TCP and UDP ones.
This also works for server_udp_loss and client_udp_loss, but the loss rate of the server is
defaulted to .5. This can be changed within the actual code of server_udp_loss, as the
probability is passed via a parameter list in the method. Thus, if running the actual method
through the Python terminal(called server_udp(probability)), all that is needed is the probability
passed in.


As for programming languages, the entire project was written in Python3 with the socket.py library.
