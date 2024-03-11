#! usr/bin/env python3
# decrypts based on which rule is chosen

def main():
    Menu = ['1:RULE 1', '2:RULE 2', '3:RULE 3', '4:RULE 4', '5:RULE 5', '6:RULE 6', '7:RULE 7', '8:RULE 8', '9:DNA COMPLEMENT']
    print('## Select options for decoding ##')
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
        'A': '00',
        'C': '01',
        'G': '10',
        'T': '11',
        ' ': ' ',   
    }

    c = input('Enter DNA to decode to binary: ').strip()

    cipher = []
    for x in range(0,len(c), 1):
        piece = c[x:x+1]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule2():
    mapping = {
        'A': '00',
        'G': '01',
        'C': '10',
        'T': '11',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 1):
        piece = c[x:x+1]
        cipher.append(mapping[piece])

    print (''.join(cipher))
    
def rule3():
    mapping = {
        'G': '00',
        'A': '01',
        'T': '10',
        'C': '11',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 1):
        piece = c[x:x+1]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule4():
    mapping = {
        'G': '00',
        'T': '01',
        'A': '10',
        'C': '11',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 1):
        piece = c[x:x+1]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule5():
    mapping = {
        'T': '00',
        'C': '01',
        'G': '10',
        'A': '11',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 1):
        piece = c[x:x+1]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule6():
    mapping = {
        'T': '00',
        'G': '01',
        'C': '10',
        'A': '11',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 1):
        piece = c[x:x+1]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule7():    
    mapping = {
        'C': '00',
        'A': '01',
        'T': '10',
        'G': '11',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 1):
        piece = c[x:x+1]
        cipher.append(mapping[piece])

    print (''.join(cipher))

def rule8():
    mapping = {
        'C': '00',
        'T': '01',
        'A': '10',
        'G': '11',
        ' ': ' ',   
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 1):
        piece = c[x:x+1]
        cipher.append(mapping[piece])

    print (''.join(cipher))

# dna complement conversion
def dna_complement():
    mapping = {
        'C': 'G',
        'T': 'A',
        'A': 'T',
        'G': 'C',
        ' ': ' ',
    }

    c = input('Enter message to decode: ').strip()

    cipher = []
    for x in range(0,len(c), 1):
        piece = c[x:x+1]
        cipher.append(mapping[piece])

    print (''.join(cipher))
    

# runs the script
main()
	
	
	
	
