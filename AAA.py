class Bookstore():
    def __init__(self):
        self._Books = {}
        self._Name = "x"
        self._Author = "x"
        self._Price = float(0)
       

    def Add_books(self):
        self._Name=input("Enter the name of the book:")
        self._Author=input("Enter the author of the book:")
        self._Price=input("Enter the price of the book:")
        self._Books[self._Name] = {self._Author,self._Price}
            


    def Sell_books(self):
        Name=input("Enter the name of the book:")
        Author=input("Enter the author of the book:")
        Price=input("Enter the price of the book:")

 