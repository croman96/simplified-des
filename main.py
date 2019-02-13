import fileinput
import math

def main():
    instructions = []

    # parse input file
    for line in fileinput.input():
        try:
            # add line after removing the newline character
            instructions.append(line[:-1])
        except:
            break

if __name__ == '__main__':
    main()
