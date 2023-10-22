#Body Mass Index
#formula: height in  meters squared(height*2) divided by weight in kgs = (1.74m*1.74m)/70. meters and kgs
import bmi_categories

def weight_conversion():
    weight_unit = str(input('Weight unit. kgs/lbs: '))
    weight = float(input('Enter your weight: ')) #conversion in the if statement. kgs= wieght/0.45 lbs=weight/*0.45. be specific eg 65 kgs

    if weight_unit == 'kgs':
        return weight
    elif weight_unit == 'lbs': #converting to kilograms
        return weight*0.45

def height_conversion():  
    height_unit = str(input('Height unit. m/cm: '))
    height = float(input('Enter your height: ')) #conversion in the if statement. be specific eg 174 cm

    if height_unit == 'cm': #converting centimeters to meters
        return height/100
    elif height_unit == 'm':
        return height 

bmi_range = weight_conversion() / (height_conversion()**2)

if bmi_range < 18.5:
    print('You\'re BMI is {}. You\'re in the underweight range.'.format(bmi_range))
    print(bmi_categories.bmi_weights[0])
elif bmi_range >= 18.5 and bmi_range <=24.9:
    print('You\'re BMI is {}. You\'re in the healthy weight range.'.format(bmi_range))
elif bmi_range >=25 and  bmi_range <=29.9:
    print('You\'re BMI is {}. You\'re in the overweight range.'.format(bmi_range))
    print(bmi_categories.bmi_weights[1])
elif bmi_range >=30:
    print('You\'re BMI is {}. You\'re in the obese range.'.format(bmi_range))
    print(bmi_categories.bmi_weights[2])
