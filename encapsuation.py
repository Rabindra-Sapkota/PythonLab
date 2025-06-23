class Book:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        self.__price = new_price


class Book2(Book):
    def __init__(self, obj_1):
        super.__init__

b_1 = Book("Harry potter", 100)
print(b_1.name)
# print(b_1.__price)  # This will raise an AttributeError because __price is private
b_1.set_price(200)
print(b_1.get_price())


print(b_1._Book__price)
