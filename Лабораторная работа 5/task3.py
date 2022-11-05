from random import randint

def get_unique_list_numbers() -> list[int]:
    unique_list_numbers = list(set([randint(-10, 10) for _ in range(15)]))
    while len(unique_list_numbers) < 15:
        number = randint(-10, 10)
        if number not in unique_list_numbers:
            unique_list_numbers.append(number)
    return unique_list_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
