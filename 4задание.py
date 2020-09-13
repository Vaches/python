#задание  Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
# и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера
# на реальных данных (создать экземпляры
# класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    class Position(worker):
        def __init__(self, name, surname, position, wage , bonus):
        super()__init__(name, surname,position, wage, bonus)

        def get_total_income(self):
            return self.name + ' ' +self.surname

        def get_total_income(self):
            return self.income.get('wage') + self.income.get("'bonus")
    a = Position('Vyacheslav, Reshetin, manager, 50000, 15000')
    print(a.get_full_name())
    print(a.position)