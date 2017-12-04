arabic_digits = int(input('Please enter the number which do you want to convert: \n'))
dict_out = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
            900: 'CM', 1000: 'M'}
roman_digits = ''
for counter in [1000, 100, 10, 1]:
    number = arabic_digits % (counter * 10) - arabic_digits % counter
    if number in dict_out.keys():
        roman_digits += dict_out[number]
    else:
        if (1 * counter) < number < (4 * counter):
            roman_digits += dict_out[1 * counter] * int(number / counter)
        elif (5 * counter) < number < (9 * counter):
            roman_digits += dict_out[5 * counter] + dict_out[1 * counter] * int(number / counter - 5)
print(roman_digits)
