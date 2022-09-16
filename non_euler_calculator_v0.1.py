first_input = input('First Number: ')
second_input = input('Second Number: ')
interaction = input('What do you want to do to these numbers? ')
if interaction == '/': answer = float(first_input) / float(second_input)
else:
    if interaction == 'x': answer = float(first_input) * float(second_input)
    else:
        if interaction == '-': answer = float(first_input) - float(second_input)
        else:
            if interaction == '+': answer = float(first_input) + float(second_input)
print("Answer:",answer)
while not answer == 0:
    first_input = input('First Number: ')
    second_input = input('Second Number: ')
    interaction = input('What do you want to do to these numbers? ')
    if interaction == '/':
        answer = float(first_input) / float(second_input)
    else:
        if interaction == 'x':
            answer = float(first_input) * float(second_input)
        else:
            if interaction == '-':
                answer = float(first_input) - float(second_input)
            else:
                if interaction == '+': answer = float(first_input) + float(second_input)
    print("Answer:", answer)