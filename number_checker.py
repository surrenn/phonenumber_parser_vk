import re

with open('new_numbers.txt') as file:
    numbers = [item.strip() for item in file]


filter_numbers = []
for number in numbers:
    number = re.sub('\D', '', number)

    if len(number) >= 10 and len(number) < 12 and number.isnumeric():
        filter_numbers.append(number)

print(filter_numbers)
print(len(filter_numbers))

ready_numbers = []
for item in filter_numbers:
    if len(item) == 10:
        new_item = '7' + item
        ready_numbers.append(new_item)
        continue
    if len(item) == 11 and item[0] != '7':
        new_item = '7' + item[1:]
        ready_numbers.append(new_item)
        continue
    else:
        ready_numbers.append(item)

print(ready_numbers)
print(len(ready_numbers))

#write filtered numbers
with open ("ready_numbers.txt", "a") as f:
    for filter_number in ready_numbers:
        f.write(filter_number + '\n')