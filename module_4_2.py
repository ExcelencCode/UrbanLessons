def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
# Программа не может вызвать внутреннюю функцию inner_function,
# т.к. она существует только внутри функции test_function, а пространство видимости
# распространяется изнутри наружу, а не наоборот
inner_function()