with open("adatok.txt") as f:
    data = f.read()

data = data.replace(",", ".")
data = data.split('\n')

while data.count("") > 0:
    data.remove("")

my_list = []

for item in data:
    new_list = item.split(";")
    my_list.append(new_list)

for item in my_list:
    item[2] = float(item[2])
    item[3] = float(item[3])
    item[4] = float(item[4])

for item in my_list:
    print(item[0] + ":")
    my_sum = item[2] + item[3] + item[4]
    print("\tAVG = " + str(my_sum/3))
    masses = []
    masses.append(item[2])
    masses.append(item[3])
    masses.append(item[4])
    print("\tMIN: " + str(min(masses)))
    print("\tMIN: " + str(max(masses)))

counter = 0
my_sum = 0
for item in my_list:
    my_sum += item[2]
    my_sum += item[3]
    my_sum += item[4]
    counter += 1

print(f"\nAVG of all: {my_sum / (counter * 3)}")
print("Dr. Ken Hurt's second measurement: " + str(my_list[3][2]))
print("Ben Dover's average weight: " + str((my_list[2][2] + my_list[2][3] + my_list[2][4])/3))

third_measurement = 0

for item in my_list:
    third_measurement += item[4]

avg_third_measurement = third_measurement/len(my_list)

print("The name of the people who's first measurement is higher than the average of the third column of measurements:")

for item in my_list:
    if item[2] > avg_third_measurement:
        print("\t" + str(item[0]))


first_measurement = 0

for item in my_list:
    first_measurement += item[2]

avg_first_measurement = first_measurement/len(my_list)

counter_first = 0
for item in my_list:
    if item[2] > avg_first_measurement:
        counter_first += 1

print(f"There are {counter_first} people who's first measurement is more than the average of the first row of "
      f"measurements.")

avg_ben_ken_first = (my_list[2][2] + my_list[3][2])/2

print(f"The average of Ben Dover's and Dr Ken Hurt's first measurement: {(my_list[2][2] + my_list[3][2])/2}")
