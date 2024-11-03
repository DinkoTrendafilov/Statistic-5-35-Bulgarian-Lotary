import random

numbers_of_rotation = int(input("Моля въведете броя на тегленията на числата: "))

keys_list = [num for num in range(1, 6)]
value_list = [0 for num in range(1, 6)]

my_dictionary = dict(zip(keys_list, value_list))
my_list = []
total_number_of_combination = (35 * 34 * 33 * 32 * 31) / (5 * 4 * 3 * 2 * 1)

toto_keys_list = [num for num in range(1, 36)]
toto_value_list = [0 for num in range(1, 36)]

toto_dictionary = dict(zip(keys_list, value_list))
toto_list = []
counter = 0

for _ in range(numbers_of_rotation):
    result = 0
    toto_server_numbers = [num for num in range(1, 36)]
    user_numbers = [num for num in range(1, 36)]

    random.shuffle(toto_server_numbers)
    random.shuffle(user_numbers)

    toto_server_numbers = toto_server_numbers[:5]
    user_numbers = user_numbers[:5]

    for num1 in toto_server_numbers:
        toto_list.append(num1)
        for num2 in user_numbers:
            if num1 == num2:
                result += 1
    if result == 5:
        counter += 1
        print(f"#{counter:_} Поздравления, вие познахте и 5те числа!!!, а именно: {toto_server_numbers}")

    my_list.append(result)
print()
print(f"Вашият брой 5-ци: [{counter:_}] | от {numbers_of_rotation:_} броя тегления се очаква "
      f"[{(numbers_of_rotation / total_number_of_combination):.2f}] броя 5-ци")
print()
for element in my_list:
    if element not in my_dictionary:
        my_dictionary[element] = 1
    else:
        my_dictionary[element] += 1

sorted_dict = dict(sorted(my_dictionary.items(), key=lambda x: (-x[1], x[0])))

for element in toto_list:
    if element not in toto_dictionary:
        toto_dictionary[element] = 1
    else:
        toto_dictionary[element] += 1

toto_sorted_dict = dict(sorted(toto_dictionary.items(), key=lambda x: (-x[1], x[0])))

print(f"{'-' * 113}")
print(f"Общият брой на всички комбинации: {total_number_of_combination:_}")
print()
for number, value in sorted_dict.items():
    print(f"Познати числа: {number:02} -> Честота на случване: {value:_}")

print(f"{'-' * 113}")
print()
for number, value in toto_sorted_dict.items():
    print(f"Числото: {number:02} -> Честота на случване: {value:_}")
print(f"{'-' * 113}")
