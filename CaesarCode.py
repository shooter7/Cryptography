def planToCypher(text):
    cypher = ""
    for i in text:
        if i==" ":continue
        c = ord(i) + 3
        if c>ord("z") :
            c-=26
        cypher += chr(c)
    print "cypher text is " +cypher

def cypherToPlan(text):
    plan = ""
    for i in text:
        c = (ord(i) - 3)
        if c<ord("a") :
            c+=26
        plan += chr(c)
    print "plan text is " + plan

text = raw_input("enter text:")


def runprogram(text):
    print ("choose number:")
    print ("1-plane text")
    print ("2-cypher text")
    n = input(">")
    if n == 1:
        planToCypher(text)
    elif n == 2:
        cypherToPlan(text)
    else:
        runprogram()


runprogram(text)


