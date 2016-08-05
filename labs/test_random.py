import random

int1 = random.randint(1,6)
print int1
int2 = random.randint(1,6)
print int2
holdnumber = int1 + int2

if int1 == int2:
    print "Doubles! Move %d spaces and roll again" %(holdnumber)
else:
    print " Move %d spaces. Next players turn!" %(holdnumber)
