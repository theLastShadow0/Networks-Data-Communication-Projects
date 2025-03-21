def SWAP_Server(TAM_TAB_Server, i, j):
    if i != j:
        temp = TAM_TAB_Server[i]
        TAM_TAB_Server[i] = TAM_TAB_Server[j]
        TAM_TAB_Server[j] = temp

def Sort_TAM_Server(TAM_TAB_Server):
    TAM_TAB_Server = list(TAM_TAB_Server)
    low = 0
    mid = 0
    high = len(TAM_TAB_Server) - 2
    while mid <= high:
        if TAM_TAB_Server[mid] == 'T':
            SWAP_Server(TAM_TAB_Server, low, mid)
            low += 1
            mid += 1
        elif TAM_TAB_Server[mid] == 'A':
            mid += 1
        elif TAM_TAB_Server[mid] == 'M':
            SWAP_Server(TAM_TAB_Server, mid, high)
            high -= 1
    TAM_TAB_Server = "".join(TAM_TAB_Server)
    TAM_TAB_Server = TAM_TAB_Server.rstrip("#")
    return TAM_TAB_Server

TAM = input("Please enter a sequence of only T, A, or M characters ending with a #: ")

if TAM == '#':
    print("The input is empty try again.")
else:
    print(Sort_TAM_Server(TAM))