"""Практическая работа №2."""

# Вводная часть
# -------------

intro = """
Представим, что мы хотим сделать сервис, связанный с рецептами и ресторанами.
И пока согласуем доступ по API к хранилищу рецептов (пишет и наполняет другая команда),
мы пишем свой код для рассчёта расходов на закупку ингредиентов.
Нам передали данные как бы мы получили их по проектируемому API.
"""

# Задание
# ----------

task = """
Нужно создать два класса. Один Ингредиент, а другой Рецепт.

Подберите блюдо, которое название которого начинается с тойже буквы, что и Ваша фамилия.
Укажите в комментарии в начале файла:
# (И)шутин -> (И)тальянская пицца
Подобрать блюдо поможет ссылка https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%91%D0%BB%D1%8E%D0%B4%D0%B0_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83


Если в рецепте мало ингредиентов, их можно добавить... По Вашему вкусу. Пусть их будет 5+.
Можно придумать ("приготовить") собственный рецепт. 

Следует написать python-код так, чтобы выполнялись следующие минимальные условия:

- создать класс Ингредиент, описывающий ингредиент (название, вес, и т.д.). Значения характеристик ингредиента определите "на глаз".

- создать класс Рецепт, отвечающий на вопросы: "Вес сырого продукта?", "Вес готового продукта?", "Себестоимость?". В классах добавить/реализовать необходимые методы рассчёта.

Исходный Рецепт должен быть записан в виде словаря (Как в шаблоне).

Написать unittest в отдельном файле с использованием setUp() и SetUpClass() методов. (TearDown(), TearDownClass())

По аналогии, подберите и второе блюдо, но начинающееся с буквы имени. Протестируйте свои классы и на нём.

Проведите замер покрытия тестами.

Ожидается, что все задания практики делаются в git-репозитории. Не забывайте коммитить готовые фичи по ходу выполнения задания.

"""

# Шаблон-пример
# ----------

class Ingredient:
    """Ингредиент."""

    def __init__(self, name, raw_weight, weight, cost) -> None:
        self._name = name 
        self._raw_weight = raw_weight 
        self._weight = weight 
        self._cost = cost 

    @property
    def name(self):
        return self._name
    @property
    def raw_weight(self):
        return self._raw_weight
    @property
    def weight(self):
        return self._weight
    @property
    def cost(self):
        return self._cost
    

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Название должно являться строкой")
        self._name = value

    @raw_weight.setter
    def raw_weight(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Чистый вес должен быть указан в числовом значении")
        self._raw_weight = value
    @weight.setter
    def weight(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Вес должен быть указан в числовом значении")
        self._weight = value
    @cost.setter
    def cost(self, value):
        if not isinstance(value, int):
            raise ValueError("Стоимость должна быть типом int")
        self._cost = value



    
    # защитите его от неверных входных данных
    # есть два пути: использовать @property и допонительные методы или библиотеку pydantic
    # можно пойти и так и так - для сравнения


class Receipt:

    def __init__(self, name:str, ingredient_list:list[tuple[str, int, int, int]]) -> None:
        self.name = name
        self.ingredients = ... # подумайте об эффективном способе завести ингредиенты в классе Рецепта


    def calc_cost(self, portions=1):
        ...

    def calc_weight(self, portions=1, raw=True):
        ...

    def __str__(self) -> str:
        pass


if __name__ == '__main__':
    a = Ingredient("1", 1, 1.1, 1)
    a.weight = "fg"
# if __name__ == '__main__':
#     # Добавьте ещё один (или более) параметр к кортежу, описывающий Ингредиент
#     # (Представьте что вы готовите. Возможно чего-то не хвататет для этого?)

#     receipt_from_api = {
#         "title": "Яичница с беконом и помидорами.",
#         "ingredients_list": [
#             ('Яйцо', 80, 70, 20),
#             ('Бекон', 200, 100, 300),
#             ('Помидор', 100, 80, 200),
#         ],
#     }

#     receipt = Receipt(receipt_from_api['title'], receipt_from_api['ingredients_list'])

#     # напишите самопроверку, что вызовы отрабатывают без ошибок на Вашем Рецепте
#     receipt.calc_cost()

#     # ...
