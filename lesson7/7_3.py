# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории нарушает
# уникальность в списке категорий, вызвать исключение ValueError

class Category():
    categories = list()

    def add(cls, category: str):
        try:
            if category not in cls.categories:
                cls.categories.append(category)
                return cls.categories.index(category)
            else:
                raise ValueError
        except ValueError:
            print(f"category: {category} exist in categories by index {
                cls.categories.index(category)}!")


    def get(cls, index: int):
        try:
            if cls.categories[index]:
                return cls.categories[index]
            else:
                raise IndexError
        except IndexError:
            print(f"index: {index} not exist in categories!")


    def delete(cls, index: int):
        try:
            if cls.categories[index]:
                del cls.categories[index]
            else:
                raise IndexError
        except IndexError:
            print(f"index: {index} not exist in categories!")


    def update(cls, index: int, category: str):
        try:
            if cls.categories[index]:
                if category not in cls.categories:
                    cls.categories[index] = category
                else:
                    raise ValueError
            else:
                raise IndexError
        except IndexError:
            print(f"index: {index} not exist in categories!")
        except ValueError:
            print(f"new category: {category} not uniq!")


my_category = Category()

my_category.add("user")
print(my_category.categories)
my_category.add("user")
my_category.add("admin")
print(my_category.categories)

print(my_category.get(index=0))
print(my_category.get(index=100))

my_category.add("superadmin")
print(my_category.categories)
my_category.delete(index=1)
print(my_category.categories)

my_category.update(index=1, category="developer")
print(my_category.categories)
my_category.update(index=0, category="developer")
print(my_category.categories)
