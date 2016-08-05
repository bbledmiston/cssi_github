import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
i = 1


while True:
    print "Rolled: " + str(dice1) + " " + str(dice2)
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
    i += 1

    if dice==1 and dice2==1:
        print  "Rolled: " + str(dice1) + " " + str(dice2)
        print "Snake Eyes"
    if dice1==6 and dice2==6:
        print  "Rolled: " + str(dice1) + " " + str(dice2)
        print "Double Six"
        print "It took you %d times" %i
        break
            
