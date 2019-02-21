import fileinput
import math

#11000100

def des(t,key):

    sbox0 = [
    ['1','0','3','2'],
    ['3','2','1','0'],
    ['0','2','1','3'],
    ['3','1','3','2']]

    sbox1 = [
    ['0','1','2','3'],
    ['2','0','1','3'],
    ['3','0','1','0'],
    ['2','1','0','3']]

    #Split the text
    head_text, tail_text = split_list(t)

    #Expanded keys
    exp1 = tail_text[3] + tail_text[0] + tail_text[1] + tail_text[2] + tail_text[1] + tail_text[2] + tail_text[3] + tail_text[0]

    #XOR with subkeys
    temp = xor(list(exp1),list(key))

    #Divide on 2 the XOR array
    head, tail = split_list(temp)

    #Convert binary to integer
    h_row = int(head[0] + head[3], 2)
    h_column = int(head[1] + head[2], 2)

    t_row = int(tail[0] + tail[3], 2)
    t_column = int(tail[1] + tail[2], 2)

    #Use S-BOX
    h_value = sbox0[h_row][h_column]
    t_value = sbox1[t_row][t_column]

    #Convert from integer to binary
    str1 = "{0:b}".format(int(h_value))
    str2 = "{0:b}".format(int(t_value))

    if str1 == "1" or str1 == "0":
        str1 = "0" + str1

    if str2 == "1" or str2 == "0":
        str2 = "0" + str2

    #Join 2 strings
    final = str1 + str2

    #Permutate final string
    final = list(final)
    final_perm = final[1] + final[3] + final[2] + final[0]

    #XOR the output with the initial tail
    output = xor(list(final_perm),head_text)

    #Concatenate initial head with output
    concatenated =  output + list(tail_text)
    return concatenated

def xor(x,y):
    n = len(x)
    res = [None] * n
    for i in range(n):
        if x[i] == "0" and y[i] == "0":
            res[i] = "0"
        elif x[i] == "0" and y[i] == "1":
            res[i] = "1"
        elif x[i] == "1" and y[i] == "0":
            res[i] = "1"
        else:
            res[i] = "0"
    return res

def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]

def main():
    instructions = []
    mode = key = text = ""

    # parse input file
    for line in fileinput.input():
        try:
            # add line after removing the newline character
            instructions.append(line[:-1])
        except:
            break

    mode = instructions[0]

    key = list(instructions[1])
    text = list(instructions[2])

    #Initial permutation for text
    t = text[1] + text[5] + text[2] + text[0] + text[3] + text[7] + text[4] + text[6]

    #Obtaining first 2 keys
    k1 = key[0] + key[6] + key[8] + key[3] + key[7] + key[2] + key[9] + key[5]
    k2 = key[7] + key[2] + key[5] + key[4] + key[9] + key[1] + key[8] + key[0]

    if mode == "E":

        #Call of function simplified des
        result1 = des(t,k1)

        #Change halves
        head, tail = split_list(result1)
        result1 = tail + head

        #Call again using the result1
        result1 = ''.join(result1)
        result2 = des(result1,k2)

    elif mode == "D":

        #Call of function simplified des
        result1 = des(t,k2)

        #Change halves
        head, tail = split_list(result1)
        result1 = tail + head

        #Call again using the result1
        result1 = ''.join(result1)
        result2 = des(result1,k1)

    #Final permutation
    final_result = result2[3] + result2[0] + result2[2] + result2[4] + result2[6] + result2[1] + result2[7] + result2[5]
    print(str(final_result))

if __name__ == '__main__':
    main()
