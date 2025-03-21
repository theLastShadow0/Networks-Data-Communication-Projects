# Networks-Data-Communication-Projects
# Project 1: Problem Analysis, Problem Solving, and Programming – Socket Programming Using TCP/IP

Problem Statement: 

Socket programming can be used to allow two nodes on a network to communicate with each other.
While the first socket (node) listens on a particular port at an IP, the second socket reaches out to the first one to form a connection.
While the server forms the listener socket, the client constitutes the requesting socket that reaches out to the server.
As can be seen, socket programs are used to create a client-server environment.
Consider an input string TAM of letters ‘T’, ‘A’, and ‘M’. This string, which is given by the user, ends with ‘#’.
The client stores this string TAM in a table (or array), called TAM_TAB_Client.
Then, the client sends this string to the server, which saves it in a table, called TAM_TAB_Server.
The number of each of these letters is unknown. 
We have a function at the server side, called SWAP_Server(TAM_TAB_Server, i, j), which places the ith letter in the jth entry and the jth letter in the ith entry of TAM_TAB_Server.
Note that SWAP_Server(TAM_TAB_Server, i, j) is defined for all integers i and j between 0 and length(TAM_TAB_Server) – 1, where length(TAM_TAB_Server) is the number of letters of the input string TAM.
The server has a function, called Sort_TAM_Server, which sorts the letters in the array TAM_TAB_Server in a way that all T’sappear first, followed by all A’s, and followed by all M’s.
Once the array TAM_TAB_Server is sorted, the server sends back the result to the client, which prints it out on the screen.

1. Using our algorithmic language, write the algorithm, Sort_TAM_Server, which should have one parameter: The array TAM_TAB_Server.
Also, your algorithm Sort_TAM_Server is correct only if the four constraints below are satisfied:

        Constraint 1: Each letter (‘A’, ‘M’, or ‘T’) is evaluated only once.
        Constraint 2: The function SWAP_Server(TAM_TAB_Server, i, j) is used only when it is necessary.
        Constraint 3: No extra space can be used by the algorithm Sort_TAM_Server. In other words, only the array TAM_TAB_Server can be used to sort the ‘A’, ‘M’, or ‘T’.
        Constraint 4: The algorithm, Sort_TAM_Server, cannot count the number of each letter ‘A’, ‘M’, or ‘T’ in TAM_TAB_Server.
2. Show that Sort_TAM_Server is correct using an informal proof (i.e., discussion).
3. Give a full program corresponding to the client and server using your favorite programming
language.

# Project 2: Encoding Strategies

Problem Statement:

The first step in turning nodes and physical links into usable building blocks is to understand how to connect them in such a way that bits can be transmitted from one node to the other.
Therefore, the task is to encode the binary data that the source node wants to send into the signals that the physical links can carry and then to decode the signal back into the corresponding binary data at the receiving node.
Assume that we are working with two discrete signals: high and low.
In practice, these signals might correspond to two different voltages on a copper-based link, two different power levels on an optical link, or two different amplitudes on a radio transmission.


![image](https://github.com/user-attachments/assets/75fc4c81-b5c3-488f-89be-45188f81b5f9)
Fig. 1: Signals traveling between signaling components – Bits flowing between adaptors

The network adaptor – a piece of hardware that connects a node to a link – contains a signaling component that encodes bits into signals at the sending node and decodes signals into bits at the receiving node (Fig. 1).
There are three encoding strategies (Fig. 2), called Non-Return to Zero (NRZ), Non-Return to Zero Inverted (NRZI), and Manchester Encoding, respectively.


![image](https://github.com/user-attachments/assets/5cb2d525-b8d0-49e6-9df0-faed39849cc4)
Fig. 2: NRZ, NRZI, and Manchester Encoding strategies


        Encoding Strategy 1 (Non-Return to Zero “NRZ”): NRZ maps the data value 1 onto the high signal and the data value 0 onto the low signal.
        Encoding Strategy 2 (Non-Return to Zero Inverted “NRZI”): NRZI has the sender make a transition from the current signal to encode a 1 and stay at the current signal to encode a 0.
        Encoding Strategy 3 (Manchester Encoding): Manchester encoding does a more explicit job of merging the clock with the signal by transmitting the exclusive OR of the NRZ-encoded data and the clock. 
        You can think of the local clock as an internal signal that alternates from low to high; a low/high pair is considered one clock cycle.

Observe that the Manchester encoding results in 0 being encoded as a low-to-high transition and 1 being encoded as a high-to-low transition.

        Discuss each of those three encoding strategies.
        Give an implementation of the three above-mentioned encoding strategies using your favorite programming language.
        Your program should accept as input a binary string and encode it using those three encoding strategies.
        The output of your program should be like the one shown on Fig. 2

# Project 3: Special Encoding Scheme

Problem Statement:

We assume that the sending node sends integer values to the receiving node.
First, the sender encodes the integer it wants to send using a special encoding scheme, which can be described as follows:

An integer value, denoted by N, is a non-zero integer between –121 and 121.
The sender produces a decomposition of an integer value using powers of 3, namely 1 (or 3^0 ), 3 (or 3^1 ), 9 (or 3^2), 27 (or 3^3), and 81 (or 3^4).
The sender sends a sequence of –1, 0, and/or 1, each of which is associated with a power of 3.
The receiver decodes the received sequence of –1, 0, and/or 1 to obtain the same value sent by the sender.
Constraint: Each power of 3 (i.e., 1, 3, 9, 27, and 81) should appear exactly once in the decomposition and is preceded by a coefficient, which can be –1, 0, or 1.

1. Propose an algorithm for this special encoding scheme using socket.

        The client receives the input (i.e., integer value between –121 and 121) from the user and sends it to the server.
        The server generates the code (i.e., sequence of –1, 0, and/or 1) and sends it back to the client.
        The client receives the code from the server and visualizes it.
2. Prove that your proposed algorithm is correct using informal proof (i.e., discussion).
3. Provide an implementation of your algorithm using the client/server model (i.e., socket). Feel free to use your favorite programming language
Observation: The intervals [-121,-41], [-40,-14], [-13,-5], [-4,-2], [-1,-1], [1,1], [2,4], [5,13], [14,40], and [41,121] play a particular role.
