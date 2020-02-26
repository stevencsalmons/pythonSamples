import random
# leverage list of options
msgs = [
    'Absolutely certain',
    'Fairly positive',
    'Likely',
    'Ask again',
    'Unlikely',
    'Doubtful',
    'Not happening'
]
# from msgs, use random method for random integer between 0 and the length of the list
print(msgs[random.randint(0, len(msgs) - 1)])