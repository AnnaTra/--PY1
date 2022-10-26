main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
""".lower()

main_str = "".join(c for c in main_str if c.isalpha())

dictionary_of_symbols = {symbol: main_str.count(symbol) for symbol in main_str}
print(dictionary_of_symbols)

def get_count_char(main_str):
    symbols_dict = {}
    for symbol in main_str:
        if symbol in symbols_dict:
            symbols_dict[symbol] += 1
        else:
            symbols_dict[symbol] = 1
    return symbols_dict
print(get_count_char(main_str))

def calculate_the_percentages(dictionary_of_symbols):
    len_ = len(main_str)
    for symbol in dictionary_of_symbols:
        dictionary_of_symbols[symbol] = round(dictionary_of_symbols.get(symbol) / len_ * 100, 3)
    return dictionary_of_symbols
print("Словарь с процентным соотношением каждой буквы к общему числу букв в строке", calculate_the_percentages(dictionary_of_symbols))





