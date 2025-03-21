# Networks-Data-Communication-Projects
#Project 1: 

Problem Analysis, Problem Solving, and Programming – Socket Programming Using TCP/IP

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
