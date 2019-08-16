# Program takes in a Centigrade value and returns it in Fahrenheit
# Hina Sekine 

centigrade = int(input('C: '))
while centigrade <= -274:
    centigrade = int(input('C: '))

fahrenheit = ((centigrade * 9) / 5) + 32

print('F:', "%.1f"%fahrenheit)
