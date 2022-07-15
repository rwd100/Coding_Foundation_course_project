import datetime

from functions import add_client, add_librarian
from models import Client, Book, Librarian, BorrowOrder

print("Welcome to our Library system")

orders = []
librarians = []
clients = [
    Client("Hasan Okla", 32, "0596665866"),
    Client("Awad Mansea", 36, "05966658"),
    Client("Shafek Adal", 20, "05966658"),
]
books = [
    Book("Star Wars1", "it is about sci-fi stories", "Aydal"),
    Book("Star Wars2", "it is about sci-fi stories", "Aydal"),
    Book("Star Wars3", "it is about sci-fi stories", "Aydal"),
    Book("Star Wars4", "it is about sci-fi stories", "Aydal"),
]

while True:
    print("""press
        1- add new client
        2- add new librarian
        3- borrow a book
        4- return a book
        5-services(available books-orders-clients..etc)
        6- Exit""")
    choice = int(input("Your choice: "))
    if choice == 1:
        while True:
            add_client(Client, clients)
            break
    if choice == 2:
        while True:
            add_librarian(Librarian, librarians)
            break
    if choice == 3:
        while True:
            print("Making a borrow order")
            print("""press
                    a-make a borrow order
                    b-display all clients
                    c-display available books
                    r-return""")
            choice = input("Your choice: ")
            if choice == "a":
                b_id = input("Enter the book's id please: ")
                b_exist = [i for i in books if b_id == "".join(i.get_id()) and "".join(i.get_status()) == "Active"]
                if len(b_exist) == 0:
                    print("Sorry this book id is not available  ...!!!")
                    continue
                else:
                    id1 = input("Enter the client's library id please :")
                    c_exist = [i for i in clients if id1 == "".join(i.get_id_no())]
                    if len(c_exist) != 0:
                        client = c_exist[0]
                        pass
                    else:
                        print("The user that you entered id for  is not exist ")
                        print("Add new user:")
                        client = add_client(Client, clients)
                        pass

                    bro_book = [i for i in books if b_id == "".join(i.get_id())]
                    bro_book[0].borrow()
                    end_days = int(input("How many days the client want to borrow the book: "))
                    end_dates = datetime.date.today() + datetime.timedelta(days=end_days)
                    a = end_dates.strftime("%b %d %Y")
                    order = BorrowOrder(
                        end_date=a,
                        book_id=bro_book[0].get_id(),
                        client_id=client.get_id_no())
                    orders.append(order)
                    print(
                        f"The book reserved successfully with order id '{''.join(order.get_id())}', and will be returned on {a} ")
                    continue
            if choice == "b":
                print(f"available clients list:")
                for i in clients:
                    print(f"Name : {''.join(i.get_name())}    Id: {''.join(i.get_id_no())} ")
                continue
            if choice == "c":
                print("List of available books:")
                available_books = [i for i in books if "".join(i.get_status()) == "Active"]
                for i in available_books:
                    print(f"title : {''.join(i.get_name())}  id: {''.join(i.get_id())}")
                continue
            if choice == "r":
                break
            else:
                print("invalid input")
                continue
    if choice == 4:
        while True:
            or_id = input("Enter the order id please: ")
            or_exist = [i for i in orders if or_id == "".join(i.get_id())]
            if len(or_exist) != 0:
                if "".join(or_exist[0].get_status()) == "Active":
                    or_exist[0].cancel()
                    book = [i for i in books if or_exist[0].get_book_id() == "".join(i.get_id())]
                    book[0].return_book()
                    print(f"The book with title {''.join(book[0].get_name())} successfully returned ")
                    break
                elif "".join(or_exist[0].get_status()) == "Cancel":
                    print("the ordr already canceled")
                    break
                elif or_exist[0].get_end_date()[0] < datetime.date.today():
                    print("the ordr already expired")
                    break
            else:
                print("The borrow order id that you entered is not exist , try to enter valid id.")
                menu_return = input("If you want to return to the main menu press 'm':  ")
                if menu_return == "m":
                    break
                else:
                    continue
    if choice == 5:
        while True:
            print("""Services:
                    a-clients
                    b-books
                    c-orders
                    d-librarians
                    r-return to main""")
            choice = (input("Your choice: "))
            if choice == "r":
                break
            if choice == "b":
                while True:
                    print("""Services:
                            a-available books
                            b-borrowed books
                            r- return""")
                    choice = input("Your choice: ")
                    if choice == "a":
                        available_books = [i for i in books if "".join(i.get_status()) == "Active"]
                        print(f"Number of available books is : {len(available_books)}")
                        for i in available_books:
                            print(f"title : {''.join(i.get_name())}  id: {''.join(i.get_id())}")

                    if choice == "b":
                        borrowed_books = [i for i in books if "".join(i.get_status()) == "Inactive"]
                        print(f"Number of borrowed books is : {len(borrowed_books)}")
                        for i in borrowed_books:
                            print(f"title2 : {''.join(i.get_name())}  id2: {''.join(i.get_id())}")

                    if choice == "r":
                        break
            if choice == "c":
                while True:
                    print("""Services:
                            a-active orders list
                            b-expired orders list
                            c- cancelled orders list
                            d-check order status
                            r-return""")
                    choice = input("Your choice: ")
                    if choice == "a":
                        active_orders = [i for i in orders if "".join(i.get_status()) == "Active"]
                        print(f"{len(active_orders)}")
                        print(f"Active orders list")
                        for i in active_orders:
                            print(f"Id {''.join(i.get_id())}")






    if choice == 6:
        break
