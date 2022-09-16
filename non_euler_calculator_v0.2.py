first_input = float(input('First Number: '))
second_input = float(input('Second Number: '))
interaction = input('What do you want to do with these numbers? ')
if interaction == '+':
    answer = first_input + second_input
elif interaction == '-':
    answer = first_input - second_input
elif interaction == 'x':
    answer = first_input * second_input
elif interaction == '*':
    answer = first_input * second_input
elif interaction == '/':
    answer = first_input / second_input
elif interaction == '^':
    answer = first_input ** second_input
else:
    answer = print("There is no such arithmetic interaction!")
print("Answer:",f"{answer:g}")

while not answer == 0:
    first_input = float(input('First Number: '))
    second_input = float(input('Second Number: '))
    interaction = input('What do you want to do with these numbers? ')
    if interaction == '+':
        answer = first_input + second_input
    elif interaction == '-':
        answer = first_input - second_input
    elif interaction == 'x':
        answer = first_input * second_input
    elif interaction == '*':
        answer = first_input * second_input
    elif interaction == '/':
        answer = first_input / second_input
    elif interaction == '^':
        answer = first_input ** second_input
    else:
        answer = print("There is no such arithmetic interaction!")
    print("Answer:", f"{answer:g}")
