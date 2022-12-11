# Using readlines()
file1 = open('input.txt', 'r')
lines = file1.readlines()
lines = [l.strip() for l in lines]

max_calories = -1
current_calories_counter = 0
for food in lines:
    if food == '':
        max_calories = max(max_calories, current_calories_counter)
        current_calories_counter = 0        
        continue
    
    current_calories_counter += int(food)

print('max_calories:', max_calories)


