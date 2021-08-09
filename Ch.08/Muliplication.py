import random, time

number_of_questions = 10
limit = 3
start_time = 0
correct_answers = 0
i = 0

for question_number in range(number_of_questions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    result = num1 * num2

    while limit > 0:

        if start_time == 0:
            start_time = time.time()

        while True:
            answer = input(f'{question_number + 1}: {num1} * {num2} = ')
            try:
                answer = int(answer)
                break
            except ValueError:
                print('Please enter a number not character or symbols')

        if answer == result:
            print('Correct!')
            correct_answers += 1
            time.sleep(1)
            break
        elif (time.time() - start_time) >= 8:
            print('Time\'s up.')
            break
        else:
            print('Incorrect, try again!')
            limit -= 1
    question_number += 1

time.sleep(1)
print (f'Score: {correct_answers} / {number_of_questions}')

