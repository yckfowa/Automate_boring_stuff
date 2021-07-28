# consults stakeoverflow -https://stackoverflow.com/questions/60658830/automate-the-boring-stuff-coin-flip-streaks

import random
number_of_streaks = 0
res = []
streak = 0

for experiment_number in range(10000):

    for i in range(100):
        res.append(random.randint(0, 1))
    
    for i in range(len(res)):
        if i == 0:
            pass
        elif res[i] == res[i-1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            number_of_streaks += 1
    
    res = []

print(f'Chance of streak: {number_of_streaks / 100}')

