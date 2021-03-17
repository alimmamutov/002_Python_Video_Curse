
computerNumber = 50
step = 50
userAnswer = ""

while userAnswer != "=":
    userAnswer = input(f'Ваше число - {computerNumber}?')
    step = step // 2
    if userAnswer == '>':

        computerNumber += step

    elif userAnswer == '<':

        computerNumber -= step

else:
    print('WIN')