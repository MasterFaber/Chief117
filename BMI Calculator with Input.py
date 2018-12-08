# BMI CALCULATOR USING FUNCTIONS

name = input('Please enter your name -> ')
weight = input('Enter your weight in kgs -> ')
height = input('Enter your height in feet -> ')

def bmi_function_alpha(x, y, z):
    absolute_height = float(z) * 0.3048
    bmi = int(y) / float((float(absolute_height) ** 2))
    print(str(x))
    print('YOUR BMI IS -> ')
    print(bmi)
    if bmi > 25:
        return print('You are overweight!')
    elif bmi < 18:
        return print('You are underweight!')
    else:
        return print('You are good to go.')

bmi_function_alpha(name, weight, height)

end_game = input('Press enter key to exit')
