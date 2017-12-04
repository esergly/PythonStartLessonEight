money = float(input('How much money do you have?: \n'))
digits = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
          10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
          17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
          60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 1000000: 'million',
          1000000000: 'billion'}
temp = 0
result = ""
temp_money = (money * 100) / 100
cents = int((money * 100) % 100)
if len(str(temp_money)) == 0:
    result = result + ' '
if len(str(temp_money)) > 12:
    result = result + 'You have a lot of money. That is all what you have to know, Bill Gates.'
else:
    i = 12
    n = 1000000000
    count = 1
    while i > 3:
        temp = int(temp_money / (n / count))
        if 0 < temp <= 20 or temp == 30 or temp == 40 or temp == 50 or temp == 60 or temp == 70 or temp == 80 or temp == 90 or temp == 100:
            result = result + str(digits.get(temp)) + ' ' + str(digits[(n / count)]) + ' '
        elif 20 < temp < 100:
            result = result + str(digits.get(temp - (temp % 10))) + ' ' + str(
                digits.get(temp - (temp - (temp % 10)))) + ' ' + str(digits[(n / count)]) + ' '
        elif temp > 100:
            result = result + str(digits.get(((temp - (temp % 100)) / 100))) + ' ' + str(
                digits.get((temp - (temp % 100)) / ((temp - (temp % 100)) / 100))) + ' ' + str(
                digits.get(temp - (temp - (temp % 100)) - (temp - (temp - (temp % 10))))) + ' ' + str(
                digits.get(temp - (temp - (temp % 10)))) + ' ' + str(digits[(n / count)]) + ' '
        elif temp == 0:
            result = ""
        temp_money = int(temp_money % (n / count))
        count = count * 1000
        i -= 3

    if len(str(temp_money)) > 0:
        temp = int(temp_money / 1)
        if 0 < temp <= 20 or temp == 30 or temp == 40 or temp == 50 or temp == 60 or temp == 70 or temp == 80 or temp == 90 or temp == 100:
            result = result + str(digits.get(temp)) + ' '
        elif 20 < temp < 100:
            result = result + str(digits.get(temp - (temp % 10))) + ' ' + str(
                digits.get(temp - (temp - (temp % 10)))) + ' '
        elif temp > 100:
            result = result + str(digits.get(((temp - (temp % 100)) / 100))) + ' ' + str(
                digits.get((temp - (temp % 100)) / ((temp - (temp % 100)) / 100))) + ' ' + str(
                digits.get(temp - (temp - (temp % 100)) - (temp - (temp - (temp % 10))))) + ' ' + str(
                digits.get(temp - (temp - (temp % 10)))) + ' '
        elif temp == 0:
            result = ""

    if 0 < cents <= 20 or cents == 30 or cents == 40 or cents == 50 or cents == 60 or cents == 70 or cents == 80 or cents == 90:
        result = result + 'dollars and ' + str(digits.get(cents)) + ' cents'
    elif cents > 20:
        result = result + 'dollars and ' + str(digits.get(cents - (cents % 10))) + ' ' + str(
            digits.get(cents - (cents - (cents % 10)))) + ' cents'
    elif cents == 0:
        result = result + 'dollars and zero cents'
print(result)
