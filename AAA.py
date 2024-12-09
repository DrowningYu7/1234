class Bookstore():
    def __init__(self):
        self._Books = {}
        self._Name = "x"
        self._Author = "x"
        self._Price = float(0)
        self._book_Name ="x"
       

    def Add_books(self):
        self._Name = input("Enter the name of the book:")
        self._Author = input("Enter the author of the book:")
        self._Price = float(input("Enter the price of the book:"))
        self._Books[self._Name] = {"Author":self._Author,"Price":self._Price}
        print("\nYou added this book successfully!")
        print("Now you have these books")
        print(self._Books)
        print("\n")
        
        
    def Sell_books(self):
        self._Name=input("Enter the name of the book:")

        if self._Name in self._Books:
            print(self._Books)
            del self._Books[self._Name]
            print("\nYou sold this book successfully!")
        else:
            print("\nSorry TvT Book not found in the Bookstore.")    
        print("Now you have these books:")
        print(self._Books)
        print("\n")
        

    def Show_all_books(self):
        # for s in self._Books:
        #     print(self._Books[s]["Author"])
        #     print(self._Books[s]["Price"])
        #     print("\n")
        for s in self._Books:
            print(f"Book: {s}, Author: {self._Books[s]['Author']}, Price: ${self._Books[s]['Price']:.2f}")
            print("\n")
            
    def Increase_price(self):
        self._book_Name = input("Enter the name of the book that you want to increase the price:")
        if self._book_Name in self._Books:
            print 


    def Save_books_to_file(self, filename="booklist.txt"):
         with open(filename, "w") as file:
             for name, info in self._Books.items():
                    file.write(f"Book: {name}, Author: {info['Author']}, Price: ${info['Price']:.2f}\n")
             print(f"\nBooks have been saved to {filename} successfully!\n")