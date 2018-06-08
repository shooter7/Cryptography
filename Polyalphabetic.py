#encripe function
def plainToCypher(text,rule):
    cypher = ""
    for i in range(0,len(text)):
        if text[i].isalpha():
            c = ord(text[i]) + 3+(i%rule)*2
            if c>ord("z") :
                c-=26
            cypher += chr(c)
    print "cypher text is " +cypher


#decripe function
def cypherToplain(text,rule):
    plain = ""
    for i in range(0, len(text)):
        if text[i].isalpha():
            c = ord(text[i]) -(3+(i%rule)*2)
            if c<ord("a") :
                c+=26
            plain += chr(c)
    print "plain text is " + plain


def runprogram():
    print ("choose number:")
    print ("1-plaine text")
    print ("2-cypher text")
    n = input(">")
    text = raw_input("enter text:")
    if n == 1:
        plainToCypher(text,3)
    elif n == 2:
        cypherToplain(text,3)
    else:
        runprogram()


runprogram()
