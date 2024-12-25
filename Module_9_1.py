# Задача "Вызов разом":

int_list = [52, 16, 31, 97, 17]

def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        fname = function.__name__
        for i in int_list:
            results[fname] = function(int_list)
    return results

print(apply_all_func(int_list, min, max))
print(apply_all_func(int_list, len, sum, sorted))