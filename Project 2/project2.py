def NRZI_encoding(binary_seq):
    binary_seq = list(binary_seq)  
    count = 0  

    def skip_bit(count):
        if count < len(binary_seq) and binary_seq[count] == '1':  #if it starts at 1 increment count and go to while loop
            count += 1
            switch_bit(count)

        elif count < len(binary_seq) and binary_seq[count] =='0': #if it starts at 0 increment count and repeat skip_bit function
            count += 1
            skip_bit(count)

    def switch_bit(count):
        while count < len(binary_seq):

            if binary_seq[count] == '0':
                binary_seq[count] = '1'  

            elif binary_seq[count] == '1':
                binary_seq[count] = '0'
                count += 1
                skip_bit(count)
                break

            count += 1

    skip_bit(count)
    return "".join(binary_seq)
     
def manchester_encoding(bin_seq):
    man = ""
    clock_seq = ""
    clock = 0
    
    for i in bin_seq:
        clock_seq += str(clock)
        en_bit = clock ^ int(i)
        man += str(en_bit)
        clock = (clock + 1) % 2
    return man,clock_seq

binary_input = input("Please enter a binary sequence: ")
NRZ = binary_input
NRZI = NRZI_encoding(binary_input)
manchester, clock_sequence = manchester_encoding(binary_input)

print("\nNRZ:       ", NRZ)
print("Clock:     ", clock_sequence) 
print("Manchester:", manchester)
print("NRZI:      ", NRZI)

