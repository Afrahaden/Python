weight = float(input('Enter your weight: '))
unit = input('Enter (L)bs or (K)g: ').upper()
converted_weight = 0

if unit == 'L':
    converted_weight = weight * 0.45
    print(f'You are {converted_weight} kilos')
elif unit == 'K':
    converted_weight = weight / 0.45
    print(f'You are {converted_weight} pounds')



