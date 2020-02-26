import random

def eightBall(intNumber):
    if intNumber == 1:
        return 'Certainly'
    elif intNumber == 2:
        return 'Fairly positive'
    elif intNumber == 3:
        return 'Likely'
    elif intNumber == 4:
        return 'Possibly'
    elif intNumber == 5:
        return 'Try again'
    elif intNumber == 6:
        return 'Not likely'
    elif intNumber == 7:
        return 'Nope'

intRandom = random.randint(1, 7)
fortune = eightBall(intRandom)
print(fortune)