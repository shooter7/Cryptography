def plainToCypher(text):
    cypher = ""
    for i in text:
        if i.isalpha():
            c = ord(i) + 3
            if c>ord("z") :
                c-=26
            cypher += chr(c)
    print "cypher text is " +cypher

def cypherToplain(text):
    plain = ""
    for i in text:
        if i.isalpha():
            c = (ord(i) - 3)
            if c<ord("a") :
                c+=26
            plain += chr(c)
    print "plain text is " + plain

text = raw_input("enter text:")


def runprogram(text):
    print ("choose number:")
    print ("1-plaine text")
    print ("2-cypher text")
    n = input(">")
    if n == 1:
        plainToCypher(text)
    elif n == 2:
        cypherToplain(text)
    else:
        runprogram()


runprogram(text)


