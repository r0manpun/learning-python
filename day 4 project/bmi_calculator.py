weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in m: '))

bmi = weight/ height **2

# bmi = weigth(lb)/ height(in) ** 2 *703
print('Your BMI is: ', format(bmi,'.2f'))