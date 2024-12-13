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
            print(f"Book: {s}\nAuthor: {self._Books[s]['Author']}\nPrice: ${self._Books[s]['Price']:.2f}")
            print("\n")
            
    def Increase_price(self):
        self._book_Name = input("Enter the name of the book that you want to increase the price:")
        if self._book_Name in self._Books:
            print 


    def Save_books_to_file(self, filename="booklist.txt"):
         with open(filename, "w") as file:
            count = 1
            for name, info in self._Books.items():
                file.write(f"{count}\n")
                file.write(f"{name}\n")
                file.write(f"{info['Author']}\n")
                file.write(f"{info['Price']}\n")
                count += 1
         print(f"\nBooks have been saved to {filename} successfully!\n")

    def Load_books_from_file(self, filename="booklist.txt"):
        
            with open(filename,"r") as file:
                self._Books = {}    
                self.book_number = 1
                
                while True:    
                    countlines= file.readline().strip()
                    self.book_number += 1
                    if not countlines:
                        break
                    self._Name = file.readline().strip()
                    self._Author= file.readline().strip()
                    self._Price= file.readline().strip()
                    if self._Name and self._Author and self._Price:
                        self._Books[countlines]= {"Name":self._Name,"Author":self._Author,"Price":self._Price}
                        
                    else:
                        print("\nThere's an error. This file is incorrect.") 
                    continue
            print("Books have already loaded successfully!")
              # for W in self._Books:
        #     print(self._Books[s]["Author"])
        #     print(self._Books[s]["Price"])
        #     print("\n")
            for W, book in self._Books.items():
                print(f"{W}\n{book['Name']}\n{book['Author']}\n{book['Price']}\n")
       
        