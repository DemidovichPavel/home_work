class Book:


    def __init__(self, title, auther):
        self.title = title
        self.auther = auther


    def get_full_name(self):
        return f'{self.title} - {self.auther}'

my_book = Book('Anna Korenina', 'Lev Tolstoy')
print(my_book.get_full_name())
print(my_book.title)
print(my_book.auther)
my_book = Book('Skotniy Dvor', 'Oruel')
print(my_book.get_full_name())



