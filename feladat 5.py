with open("szamok5.txt") as f:
    numbers = f.read()


numbers = numbers.replace(" ", "")
numbers = numbers.split("\n")

lista = []

for i in numbers:
    lista.append(i.split(";"))

big_list = []
x = 0
y = 0

for item in lista:
    small_list = []
    for num in item:
        small_list.append(int(num))
        y += 1
    big_list.append(small_list)
    x += 1

my_list = big_list

x = 0
y = 0

for item in my_list:
    my_sum = 0
    for num in item:
        my_sum += num
        y += 1
    print(f"The sum of the {x+1}. line is {my_sum}.")
    x += 1

print('')

x = 0
y = 0

for item in my_list:
    my_sum = 0
    my_avg = 0
    my_length = len(item)
    for num in item:
        my_sum += num
        y += 1
    my_avg = my_sum / my_length
    print(f"The average of the {x+1}. line is {my_avg}.")
    x += 1

print('')

x = 0
y = 0

for item in my_list:
    my_items = []
    for num in item:
        my_items.append(num)
        y += 1
    print(f"The max of the {x+1}. line is {max(my_items)}.")
    x += 1

print('')

x = 0
y = 0

for item in my_list:
    my_items = []
    for num in item:
        my_items.append(num)
        y += 1
    print(f"The min of the {x+1}. line is {min(my_items)}.")
    x += 1

print('')

for item in my_list:
    print(f"There are {len(item)} numbers in this line.")

print('')

x = 0
y = 0
my_sum = 0

for item in my_list:
    for num in item:
        my_sum += num
        y += 1
    x += 1

print(f"SUM = {my_sum}")

x = 0
y = 0
my_sum = 0
my_avg = 0
my_length = len(item)

for item in my_list:
    for num in item:
        my_sum += num
        y += 1
    x += 1
my_avg = my_sum / my_length
print(f"AVG = {my_avg}")

x = 0
y = 0
my_items = []

for item in my_list:
    for num in item:
        my_items.append(num)
        y += 1
    x += 1

print(f"MAX = {max(my_items)}")


x = 0
y = 0
my_items = []

for item in my_list:
    for num in item:
        my_items.append(num)
        y += 1
    x += 1

print(f"MIN = {min(my_items)}")

pieces = 0

for item in my_list:
    pieces += len(item)

print(f"There are {pieces} numbers in the list.")

print('')

my_sum = 0

for item in my_list:
    for num in item:
        my_sum += num
        break

print(f"The sum of the first column: {my_sum}")

my_sum = 0
my_avg = 0
my_length = len(item)

for item in my_list:
    for num in item:
        my_sum += num
        break

my_avg = my_sum / my_length
print(f"The average of the first column is {my_avg}")

x = 0
y = 0
my_items = []

for item in my_list:
    for num in item:
        my_items.append(num)
        break

print(f"The max of the first column is {max(my_items)}.")

x = 0
y = 0
my_items = []

for item in my_list:
    for num in item:
        my_items.append(num)
        break

print(f"The min of the first column is {min(my_items)}.")

my_items = []

for item in my_list:
    for num in item:
        my_items.append(num)
        break

print(f"There are {len(my_items)} numbers in this line.")

print(big_list[1][3])


