import datetime
from functions import add_client, add_librarian, add_book
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
    print("""Main:
        1- Add new client
        2- Add new librarian
        3- Add new book
        4- Borrow a book
        5- Return a book
        6- Services(available books-orders-clients..etc)
        7- Exit""")
    choice = input("Your choice: ")
    if choice == "1":
        while True:
            add_client(Client, clients)
            choice = "**"
            break
    if choice == "2":
        while True:
            add_librarian(Librarian, librarians)
            choice = "**"
            break
    if choice == "3":
        while True:
            add_book(Book, books)
            choice = "**"
            break
    if choice == "4":
        while True:
            print("""Main/Borrow_Order
            a- Make a borrow order
            b- Display all clients
            c- Display available books
            m- Return to Main""")
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
                        print("The user that you entered id for is not exist ")
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
                    print("Returned to Borrow_Order")
                    continue
            if choice == "b":
                print(f"available clients list:")
                for i in clients:
                    print(f"Name : {''.join(i.get_name())}    Id: {''.join(i.get_id_no())} ")
                print("Returned to Borrow_Order")
                continue
            if choice == "c":
                print("List of available books:")
                available_books = [i for i in books if "".join(i.get_status()) == "Active"]
                for i in available_books:
                    print(f"title : {''.join(i.get_name())}  author: {''.join(i.get_author())}  id: {''.join(i.get_id())}")
                print(f"Returned to Borrow_Order")
                continue
            if choice == "m":
                choice = "**"
                break
            else:
                print("invalid input..!!!")
                continue
    if choice == "5":
        while True:
            or_id = input("Enter the order id please: ")
            or_exist = [i for i in orders if or_id == "".join(i.get_id())]
            if len(or_exist) != 0:
                if "".join(or_exist[0].get_status()) == "Active":
                    or_exist[0].cancel()
                    book = [i for i in books if or_exist[0].get_book_id() == "".join(i.get_id())]
                    book[0].return_book()
                    print(f"The book with title {''.join(book[0].get_name())} successfully returned ")
                    choice = "**"
                    break
                elif "".join(or_exist[0].get_status()) == "Cancel":
                    print("the ordr already canceled")
                    choice = "**"
                    break
                elif "".join(or_exist[0].get_status()) == "Expire":
                    print("the ordr already expired")
                    choice = "**"
                    break
            else:
                print("The borrow order id that you entered is not exist , try to enter valid id.")
                menu_return = input("If you want to return to the main menu press 'm':  ")
                if menu_return == "m":
                    choice = "**"
                    break
                else:
                    continue
    if choice == "6":
        while True:
            print("""Main/Services:
            a-Clients
            b-Books
            c-Orders
            d-Librarians
            m-Return to Main""")
            choice = (input("Your choice: "))
            if choice == "a":
                print("List of clients:")
                if len(clients) == 0:
                    print("The list is empty")
                else:
                    print(f"number of clients : {len(clients)}")
                    for i in clients:
                        print(f"Full.Name: {i.display()['full_name'][0]}", end="|  |")
                        print(f"Age: {i.display()['age'][0]}", end="|  |")
                        print(f"Phone no: {i.display()['phone_num'][0]}", end="|  |")
                        print(f"Library-Id: {i.display()['library_id']}")
                choice = "**"
            if choice == "b":
                while True:
                    print("""Main/Services/Books:
            a- All books
            b- Available books
            c- Borrowed books
            s- Return to Services
            m- Return to Main""")
                    choice = input("Your choice: ")
                    if choice == "a":
                        if len(books) == 0:
                            print("The list is empty")
                        else:
                            print(f"Number of books is : {len(books)}")
                            for i in books:
                                print(f"Id: {''.join(i.display()['id'])}", end="|  |")
                                print(f"Title: {i.display()['title'][0]}", end="|  |")
                                print(f"Description: {i.display()['description'][0]}", end="|  |")
                                print(f"Author: {i.display()['author'][0]}", end="|  |")
                                print(f"Status: {''.join(i.display()['status'])}")
                        print("Returned to Books")
                    if choice == "b":
                        available_books = [i for i in books if "".join(i.get_status()) == "Active"]
                        if len(available_books) == 0:
                            print("The list is empty")
                        else:
                            print(f"Number of available books is : {len(available_books)}")
                            for i in available_books:
                                print(f"Id: {i.display()['id'][0]}", end="|  |")
                                print(f"Title: {i.display()['title'][0]}", end="|  |")
                                print(f"Description: {i.display()['description'][0]}", end="|  |")
                                print(f"Author: {i.display()['author'][0]}")
                        print("Returned to Books")
                    if choice == "c":
                        borrowed_books = [i for i in books if "".join(i.get_status()) == "Inactive"]
                        if len(borrowed_books) == 0:
                            print("The list is empty")
                        else:
                            print(f"Number of borrowed books is : {len(borrowed_books)}")
                            for i in borrowed_books:
                                print(f"Id: {i.display()['id'][0]}", end="|  |")
                                print(f"Title: {i.display()['title'][0]}", end="|  |")
                                print(f"Description: {i.display()['description'][0]}", end="|  |")
                                print(f"Author: {i.display()['author'][0]}")
                        print("Returned to Books")
                    if choice == "s":
                        choice = "**"
                        break
                    if choice == "m":
                        break
            if choice == "c":
                while True:
                    print("""Main/Services/Orders:
            a- All orders list
            b- Active orders list
            c- Expired orders list
            d- Cancelled orders list
            e- Check single order status
            s- Return to Services
            m- Return to Main""")
                    choice = input("Your choice: ")
                    if choice == "a":
                        print(f"All orders list")
                        if len(orders) == 0:
                            print("The list is empty")
                        else:
                            print(f"The number of active orders : {len(orders)}")
                            for i in orders:
                                print(f"Id: {i.display()['id'][0]}", end="|  |")
                                print(f"S.date: {''.join(i.display()['start_date'])}", end="|  |")
                                print(f"E.date: {i.display()['end_date'][0]}", end="|  |")
                                print(f"Book-Id: {i.display()['book_id'][0]}", end="|  |")
                                print(f"Client-Id: {i.display()['client_id'][0]}", end="|  |")
                                print(f"Status: {''.join(i.display()['status'])}")
                        print("Returned to Orders")
                    if choice == "b":
                        active_orders = [i for i in orders if "".join(i.get_status()) == "Active"]
                        print(f"Active orders list")
                        if len(active_orders) == 0:
                            print("The list is empty")
                        else:
                            print(f"The number of active orders : {len(active_orders)}")
                            for i in active_orders:
                                print(f"Id: {i.display()['id'][0]}", end="|  |")
                                print(f"S.date: {''.join(i.display()['start_date'])}", end="|  |")
                                print(f"E.date: {i.display()['end_date'][0]}", end="|  |")
                                print(f"Book-Id: {i.display()['book_id'][0]}", end="|  |")
                                print(f"Client-Id: {i.display()['client_id'][0]}")
                        print("Returned to Orders")
                    if choice == "c":
                        expired_orders = [i for i in orders if "".join(i.get_status()) == "Expired"]
                        print(f"Expired orders list")
                        if len(expired_orders) == 0:
                            print("The list is empty")
                        else:
                            print(f"The number of expired orders : {len(expired_orders)}")
                            for i in expired_orders:
                                print(f"Id: {i.display()['id'][0]}", end="|  |")
                                print(f"S.date: {''.join(i.display()['start_date'])}", end="|  |")
                                print(f"E.date: {i.display()['end_date'][0]}", end="|  |")
                                print(f"Book-Id: {i.display()['book_id'][0]}", end="|  |")
                                print(f"Client-Id: {i.display()['client_id'][0]}")
                        print("Returned to Orders")
                    if choice == "d":
                        cancelled_orders = [i for i in orders if "".join(i.get_status()) == "Cancelled"]
                        print(f"Cancelled orders list")
                        if len(cancelled_orders) == 0:
                            print("The list is empty")
                        else:
                            print(f"The number of expired orders : {len(cancelled_orders)}")
                            for i in cancelled_orders:
                                print(f"Id: {i.display()['id'][0]}", end="|  |")
                                print(f"S.date: {''.join(i.display()['start_date'])}", end="|  |")
                                print(f"E.date: {i.display()['end_date'][0]}", end="|  |")
                                print(f"Book-Id: {i.display()['book_id'][0]}", end="|  |")
                                print(f"Client-Id: {i.display()['client_id'][0]}")
                        print("Returned to Orders")
                    if choice == "e":
                        or_id = input("Enter the order id please: ")
                        or_exist = [i for i in orders if or_id == "".join(i.get_id())]
                        if len(or_exist) != 0:
                            bo_exist = [i for i in books if
                                        "".join(i.get_id()) == "".join(or_exist[0].get_book_id())]
                            print(
                                f"The status of the borrow order for the book with title {''.join(bo_exist[0].get_name())} is {''.join(or_exist[0].get_status())}")
                        else:
                            print("The borrow order id that you entered is not exist , try to enter valid id.")
                        print("Returned to Orders")
                    if choice == "s":
                        choice = "**"
                        break
                    if choice == "m":
                        break
            if choice == "d":
                print("List of librarians:")
                if len(librarians) == 0:
                    print("The list is empty")
                else:
                    print(f"number of librarians : {len(librarians)}")
                    for i in librarians:
                        print(f"Full.Name: {i.display()['full_name'][0]}", end="|  |")
                        print(f"Age: {i.display()['age'][0]}", end="|  |")
                        print(f"Phone no: {i.display()['phone_num'][0]}", end="|  |")
                        print(f"Library-Id: {i.display()['library_id']}", end="|  |")
                        print(f"Salary: {i.get_salary()}$")
                choice = "**"
            if choice == "m":
                choice = "**"
                break
            else:
                if choice == "**":
                    print(f"Returned to Services")
                else:
                    print("invalid input..!!!")
                continue
    if choice == "7":
        break
    else:
        if choice == "**":
            print(f"Returned to Main")
        else:
            print("invalid input..!!!")
        continue
