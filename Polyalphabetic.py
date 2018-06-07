#encripe function
def planToCypher(text,rule):
    cypher = ""
    for i in range(0,len(text)):
        if text[i].isalpha():
            c = ord(text[i]) + 3+(i%rule)*2
            if c>ord("z") :
                c-=26
            cypher += chr(c)
    print "cypher text is " +cypher


#decripe function
def cypherToPlan(text,rule):
    plan = ""
    for i in range(0, len(text)):
        if text[i].isalpha():
            c = ord(text[i]) -(3+(i%rule)*2)
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
        planToCypher(text,3)
    elif n == 2:
        cypherToPlan(text,3)
    else:
        runprogram()


runprogram(text)
