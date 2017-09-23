# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.items = items
        self.ignore_case = False
        if 'ignore_case' in kwargs:
            self.ignore_case = kwargs['ignore_case']
        self.returned = []

    def __next__(self):
        # Нужно реализовать __next__
        for item in self.items:
            if item not in self.returned:
                if self.ignore_case is True and type(item) == str:
                    self.returned.append(item.lower())
                    self.returned.append(item.upper())
                else:
                    self.returned.append(item)
                return item
        raise StopIteration()

    def __iter__(self):
        return self
