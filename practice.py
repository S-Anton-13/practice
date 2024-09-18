# 1. На ввод подаётся произвольный символ. Необходимо вывести его 5 раз,
# но начиная с новой строки,
# к предыдущей строке прибавляется ещё 1 такой же символ.
# Пример:

# *
# **
# ***
# ****
# *****
char = str(input('Введите символ: '))

def _typedata(char):
    for n in range(1,6):
        print(char*n)


_typedata(char)
# 2. На ввод подаётся число от 1 до 12. Необходимо вывести название месяца по его номеру.
# >> 3
# Март
month_number = int(input('Введите месяц: '))
def _serachmonth(month_number: int):
    month = {1: 'January', 2: 'Febryary', 3: 'Marth', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
             9: 'Semptember', 10: 'October', 11: 'Novemder', 12: 'Decemder'}
    if month_number in month:
        print(month[month_number])
    else:
        print('Введите целое число от 1 до 12')

_serachmonth(month_number)
