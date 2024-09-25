import test
# 1. Пользователь подаёт на ввод список из чисел, необходимо вывести список, состоящий только из чётных чисел (append)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def _chet_nums(nums: list) -> list:
    chet = []
    for i in nums:
        if not i % 2:
            chet.append(i)
    return chet


# _chet_nums(nums)

# 2. Пользователь вводит слово, необходимо проверить, является ли слово палиндромом шалаш | шалаш

word = str(input('Введите слово: '))


def _palidrom(word: str) -> str:
    wordReverse = ""
    if word == wordReverse.join(reversed(word)):
        return 'палиндром'
    else:
        return 'НЕ палиндром'


# _palidrom(word)


# 3. Необходимо написать функцию, принимающую на вход список чисел. Она обрабатывает его и возвращает суммы пар чисел:
# << [1,2,3,4,5,6]
# >> [3,7,11]
# Если передано не чётное количество чисел для составления пар, последнее число не учитывается

def _sum_nums(nums: list) -> list:
    chet = nums[1::2]
    nechet = nums[::2]
    sum_nums = []
    print(nums)
    for i in range(len(nums[::2])):
        sum_nums.append(chet[i]+nechet[i])

    return sum_nums
# _sum_nums([i for i in range(0,100)])

