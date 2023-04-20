from random import randint


def gen_ascii(filename, size):

    txt =''

    for i in range(size):
        roll = randint(0,256)

        txt += chr(roll)
    
    with open(filename, 'w' ,  encoding="utf-8") as file:
        file.write(txt)

    


gen_ascii("10_kb_file_random.txt" , 8*1024)                                                    
