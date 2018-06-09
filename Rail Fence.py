import math

def encrypt(plian, step=2):
    cipher = ""
    for i in range(0, step):  # int(round((len(plian)/step)+.4))
        for j in range(i, len(plian), step):
            if (plian[j].isalpha()):
                cipher += plian[j]
    print cipher


def decrypt(cipher, step=2):
    plian = ""
    print int(math.ceil(float(len(cipher))/step))
    for i in range(0, int(math.ceil(float(len(cipher))/step))):  # int(round((len(plian)/step)+.4))
        for j in range(i, len(cipher),int(math.ceil(float(len(cipher))/step))):
            if (cipher[j].isalpha()):
                plian += cipher[j]
    print plian


def runprogram():
    print ("choose number:")
    print ("1-plaine text")
    print ("2-cipher text")
    n = input(">")
    print
    text = raw_input("enter text:")

    if n == 1:
        encrypt(text)
    elif n == 2:
        decrypt(text)
    else:
        runprogram()


runprogram()
