import random

def main():
    encoded_string = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽"
    for i in range(len(encoded_string)):
        print(chr(ord(encoded_string[i])>>8))
        print(chr((ord(encoded_string[i]))-((ord(encoded_string[i])>>8)<<8)))
        print (i)


main()

picoCTF{16_bits_inst34d_of_8_e703b486}