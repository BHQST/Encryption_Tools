#! usr/bin/env python3
# encrypts based on which rule is chosen

def main():
    Menu = ['1:RULE 1', '2:RULE 2', '3:RULE 3', '4:RULE 4', '5:RULE 5', '6:RULE 6', '7:RULE 7', '8:RULE 8', '9:DNA COMPLEMENT']
    print('## Select option for encoding ##')
    for c in Menu:
        print(c)

    inp = input('Enter Choice: ')

    if int(inp) == 1:
        rule1()
    elif int(inp) == 2:
        rule2()
    elif int(inp) == 3:
        rule3()
    elif int(inp) == 4:
        rule4()
    elif int(inp) == 5:
        rule5()
    elif int(inp) == 6:
        rule6()
    elif int (inp) == 7:
        rule7()
    elif int(inp) == 8:
        rule8()
    elif int(inp) == 9:
        dna_complement()
    else:
        print('Invalid Input!')

def rule1():
    mapping = {
        '00': 'A',
        '01': 'C',
        '10': 'G',
        '11': 'T',
        ' ': ' ',   
    }
    
    c = input('Enter binary to encode to DNA: ').strip()

    cipher = []
    for x in range(0,len(c), 2):
        piece = c[x:x+2]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule2():
    mapping = {
        '00': 'A',
        '01': 'G',
        '10': 'C',
        '11': 'T',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 2):
        piece = c[x:x+2]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule3():
    mapping = {
        '00': 'G',
        '01': 'A',
        '10': 'T',
        '11': 'C',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 2):
        piece = c[x:x+2]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule4():
    mapping = {
        '00': 'G',
        '01': 'T',
        '10': 'A',
        '11': 'C',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 2):
        piece = c[x:x+2]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule5():
    mapping = {
        '00': 'T',
        '01': 'C',
        '10': 'G',
        '11': 'A',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 2):
        piece = c[x:x+2]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule6():
    mapping = {
        '00': 'T',
        '01': 'G',
        '10': 'C',
        '11': 'A',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 2):
        piece = c[x:x+2]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule7():
    mapping = {
        '00': 'C',
        '01': 'A',
        '10': 'T',
        '11': 'G',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 2):
        piece = c[x:x+2]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule8():
    mapping = {
        '00': 'C',
        '01': 'T',
        '10': 'A',
        '11': 'G',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 2):
        piece = c[x:x+2]
        cipher.append(mapping[piece])

    print (''.join(cipher))



# dna complement conversion
def dna_complement():
    mapping = {
        'G': 'C',
        'A': 'T',
        'T': 'A',
        'C': 'G',
        ' ': ' ',
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 2):
        piece = c[x:x+2]
        cipher.append(mapping[piece])

    print (''.join(cipher))
# runs the script
main()






	
	
	
	
