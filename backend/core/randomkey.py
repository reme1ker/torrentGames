import random


def randomkey():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    alphavite = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    random_index = ""
    randomAlphs = random.randint(8, 13)
    randomNums = 15 - randomAlphs
    for i in range(0, randomNums):
        random_index += str(random.randint(0, len(numbers) - 1))
    for i in range(0, randomAlphs):
        random_index += str(random.choice(alphavite))
    random_index = str(random_index)
    randomStr = random.sample(random_index, len(random_index))
    randomStr = (''.join(randomStr))
    inde = 0
    resultkey = ""
    for i in randomStr:
        inde += 1
        resultkey += i
        if inde == 5 or inde == 10:
            resultkey += "-"
    return resultkey
