import random

numbers_of_rotation = int(input("Моля въведете броя на тегленията на числата: "))
# Статистика за познатите числа
keys_list = [num for num in range(1, 6)]
value_list = [0 for num in range(1, 6)]

my_dictionary = dict(zip(keys_list, value_list))
my_list = []

# Статистика за числата от 1 до 35, които да се падали, от страна на тото сървъра

toto_keys_list = [num for num in range(1, 36)]
toto_value_list = [0 for num in range(1, 36)]

toto_dictionary = dict(zip(keys_list, value_list))
toto_list = []

for _ in range(numbers_of_rotation):
    result = 0
    toto_server_numbers = []
    user_numbers = []
    for _ in range(25):
        pc_number = random.randint(1, 35)
        if pc_number not in toto_server_numbers:
            toto_server_numbers.append(pc_number)
        if len(toto_server_numbers) == 5:
            break
    for _ in range(25):
        pc_number = random.randint(1, 35)
        if pc_number not in user_numbers:
            user_numbers.append(pc_number)
        if len(user_numbers) == 5:
            break

    for num1 in toto_server_numbers:
        toto_list.append(num1)
        for num2 in user_numbers:
            if num1 == num2:
                result += 1
    if result == 5:
        print(f"Поздравления, вие познахте и 5те числа!!!, а именно: {toto_server_numbers}")
    my_list.append(result)

for element in my_list:
    if element not in my_dictionary:
        my_dictionary[element] = 1
    else:
        my_dictionary[element] += 1

sorted_dict = dict(sorted(my_dictionary.items(), key=lambda x: (-x[1], x[0])))

# _____________________________________
for element in toto_list:
    if element not in toto_dictionary:
        toto_dictionary[element] = 1
    else:
        toto_dictionary[element] += 1

toto_sorted_dict = dict(sorted(toto_dictionary.items(), key=lambda x: (-x[1], x[0])))

print(f"{'-' * 113}")
total_number_of_combination = (35 * 34 * 33 * 32 * 31) / (5 * 4 * 3 * 2 * 1)
total_number_of_combination = "{:,}".format(total_number_of_combination).replace(",", "_")
print(f"Общият брой на всички комбинации: {total_number_of_combination}")
print()
for number, value in sorted_dict.items():
    value = "{:,}".format(value).replace(",", "_")
    print(f"Познати числа: {number:02d} -> Честота на случване: {value}")

print(f"{'-' * 113}")
print()

for number, value in toto_sorted_dict.items():
    value = "{:,}".format(value).replace(",", "_")
    print(f"Числото: {number:02d} -> Честота на случване: {value}")

print(f"{'-' * 113}")