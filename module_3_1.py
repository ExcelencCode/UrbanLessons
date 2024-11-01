calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string_):
    count_calls()
    return (len(string_), string_.upper(), string_.lower())


def is_contains(string, list_to_search):
    count_calls()
    for i in range (len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            return True
            break
    return False
    # return any(string.lower() == item.lower() for item in list_to_search)


print(string_info('Chillout'))
print(string_info('Anybody home?'))
print(is_contains('Fellow', ['feLLow', 'cause', 'symbol']))
print(is_contains('Cheese', ['Bread', 'BUTTER', '  ']))

print(calls)
