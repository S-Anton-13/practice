import string
import random
from dataclasses import asdict
from practice3_dataclass import Product
import datetime as data



class Print_tiket:
    def __init__(self):
        self.__get_product()

    # генерируем рандомный список "типо продуктов" чтобы не делать его каждый раз руками
    def __init_product_dict(self) -> dict[str, int]:
        product_dict = {}
        for i in range(1, 30):
            key_lenght = random.randint(2, 6)
            key = ''.join(random.choice(string.ascii_letters) for i in range(key_lenght))
            value = random.randint(1, 30)

            product_dict[key] = value
        return product_dict

    def __input_product(self) -> str:
        input_product = input('введите продукт: ')
        return input_product

    def __input_coast(self) -> float:
        input_coast = float(input('введите колличество: '))
        return input_coast

    def __get_product(self) -> None:
        # получаем сгенерированый список
        product_dict = self.__init_product_dict()
        print(product_dict)
        input_product = self.__input_product()
        coast = self.__input_coast()
        # проверяем наличие продукта в сгененрированом списке, возвращаем True или False в зависимости от значение
        if input_product in product_dict:
            if coast <= product_dict.get(input_product):
                print('Имеется',
                      product_dict.get(input_product), ' ', input_product,
                      ' на складе', '\n',
                      'желаете ' 'купить ',
                      coast, 'шт?'
                      )
                if self.__chek_y_or_n():
                    tiket = Product(name=input_product, coast=coast)
                    self.__print_tiket_shablon(tiket)
                else:
                    print('чек не напечатан')


            else:
                print('Нет на складе в таком количестве')
        else:
            print('Нет на складе такого продукта')

    def __chek_y_or_n(self) -> bool:
        result = input('Введите y или n для подтверждения/отмены: ')
        y_n = False
        y = 'yY'
        n = 'nN'
        if result in y:
            y_n = True
            print('ОК')
        elif result in n:
            y_n = False
            print('Отмена')
        return y_n



    def __print_tiket_shablon(self, tiket: Product) -> None:
        tiket_ = asdict(tiket)
        print("--------------------", "\n",
              tiket_['name'], "  ", tiket_['coast'],"  ",'\n',
              "---------------------", '\n',
              'Спасибо за покупку'
              )
