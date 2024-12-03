class Bookstore():
    def __init__(self):
        self._Books = {}
        self._Name = "x"
        self._Author = "x"
        self._Price = float(0)
       

    def Add_books(self):
        self._Name = input("Enter the name of the book:")
        self._Author = input("Enter the author of the book:")
        self._Price = input("Enter the price of the book:")

        self._Books[self._Name] = {self._Author,self._Price}
        print("\nYou added this book successfully!")
        print(self._Books)
        print("\n")
        
        
        

    def Sell_books(self):
        self._Name=input("Enter the name of the book:")
        

        if self._Name in self._Books:
            print(self._Books)
            del self.Books[variable]
            print("\nYou sold this book successfully!")
        else:
            print("\nSorry.Book not found in the Bookstore.")    
        print("\n") 
        