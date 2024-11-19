from AAA import Bookstore


while True:
 
    print("Welcome to my bookstore")
    print("1.Add books\n2.Sell books\n3.Increase the price\n4.Reduce the price\n5.Show all books\n6.Quit")

    choice = input("Enter your choice:")
    if choice =="1":
      add = Bookstore.Add_books()
    elif choice == "2":
      sell = Bookstore.Sell_books()
    elif choice == "3":
      increase_price= Bookstore.Increase_price()
    elif choice =="4":
      reduce_price = Bookstore.Reduce_price()
    elif choice =="5":
      show = Bookstore.Show_all_books()
    elif choice =="6":
      print("Exit the Bookstore")
    else:
      print("An invalid choice, please try again")
      break




