# Task 1
number = int(input('Please input the number of a day in a week: \n'))
week_days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
if (0 < number < 8):
    print(week_days[number])
else:
    print('Any week has not less than 0 and no more than 7 days. Your input is incorrect.')

# ******************************************************************************
# Task 2
cat = {"name": "Vasya", "color": "Grey with dark lines", "age": 3, "weight": 7, "food": "fish"}
print(cat.get("name"))
print(cat.get("food"))

# ******************************************************************************
# Task 3
string = input('Please input the string for analysis: \n')
result = {}
my_list = list(string)

for i in my_list:
    count = result.get(i)
    if count:
        result[i] = count + 1
    else:
        result[i] = 1

print(result)
