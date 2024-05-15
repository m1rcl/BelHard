# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError

class Category():
    categories = list({})

    def add(cls, category: str):
        try:
            if not len(cls.categories):
                cls.categories.append({"name": category, "is_published": None})
                return 0
            for index in range(len(cls.categories)):
                if category not in cls.categories[index].values():
                    cls.categories.append(
                        {"name": category, "is_published": None})
                    return cls.categories[index]
            else:
                raise ValueError
        except ValueError:
            print(f"category: {category} exist in categories!")

    def get(cls, index: int):
        try:
            if cls.categories[index]:
                return cls.categories[index]
            else:
                raise IndexError
        except IndexError:
            print(f"index: {index} not exist in categories!")


# def delete(cls, index: int):
# if cls.categories[index]:
# del cls.categories[index]
##
##
# def update(cls, index: int, category: str):
# try:
# if cls.categories[index]:
# category_uniq = set(cls.categories)
# if category not in category_uniq:
# cls.categories[index] = category
# else:
# raise ValueError
# else:
# raise IndexError
# except IndexError:
# print(f"index: {index} not exist in categories!")
# except ValueError:
# print(f"new category: {category} not uniq!")


my_category = Category()

my_category.add("user")
print(my_category.categories)
my_category.add("user")
my_category.add("admin")
print(my_category.categories)

print(my_category.get(index=0))
print(my_category.get(index=100))

# my_category.add("superadmin")
# print(my_category.categories)
# my_category.delete(index=1)
# print(my_category.categories)
##
# my_category.update(index=1, category="developer")
# print(my_category.categories)
# my_category.update(index=0, category="developer")
# print(my_category.categories)
