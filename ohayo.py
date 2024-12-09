from AAA import Bookstore
Variable = Bookstore()
while True:
 
    print("Welcome to my bookstore")
    print("1.Add books\n2.Sell books\n3.Increase the price\n4.Reduce the price\n5.Show all books\n6.Save books to the file\n7.Quit\n")

    choice = input("Enter your choice:")
    if choice =="1":
      add = Variable.Add_books()
    elif choice == "2":
      sell = Variable.Sell_books()
    elif choice == "3":
      increase_price= Variable.Increase_price()
    elif choice =="4":
      reduce_price = Variable.Reduce_price()
    elif choice =="5":
      show = Variable.Show_all_books()
    elif choice =="6":
      save = Variable.Save_books_to_file()
    elif choice =="7":
      print("Exit the Bookstore")
    else:
      print("An invalid choice, please try again")
      break
    

