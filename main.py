import datetime
from functions import add_client, add_librarian, add_book, status_color
from models import Client, Book, Librarian, BorrowOrder
from termcolor import cprint, colored

print("Welcome to our Library system")
# The Star
orders = []
librarians = []
clients = [
    Client("ADEL OKLA", 32, "0599123456"),
    Client("AWAD AL BATAL", 36, "0599654321"),
    Client("SHAFEAK GARMA", 28, "0598765432"),
]
books = [
    Book("THE STAR WARS", "Expand your knowledge of a galaxy far, far away", "DAN ZEHR "),
    Book("TO KILL A MOCKINGBIRD", "To Kill a Mockingbird has become a classic of modern American literature",
         "HARPER LEE"),
    Book("NINETEEN EIGHTY-FOUR", "Is a dystopian social science fiction novel and cautionary tale", "GEORGE ORWELL"),
    Book("THE CALL OF THE WILD", "is a short adventure novel", "JACK LONDON"),
]
while True:
    cprint("Main:", "magenta")
    cprint("""    1- Add new client
    2- Add new librarian
    3- Add new book
    4- Borrow a book
    5- Return a book
    6- Services(available books-orders-clients..etc)
    7- Exit""", "blue")
    choice = input(colored("Your choice:", "grey", "on_white") + " ")
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
            cprint("Main/Borrow_Order", "magenta")

            cprint("""    a- Make a borrow order
    b- Display all clients
    c- Display available books
    m- Return to Main""", "blue")
            choice = input(colored("Your choice:", "grey", "on_white") + " ")
            if choice == "a":
                b_id = input(colored("Enter the book's id please: ", "cyan"))
                b_exist = [i for i in books if b_id == "".join(i.get_id()) and "".join(i.get_status()) == "Active"]
                order_id = [i for i in orders if b_id == "".join(i.get_book_id())]
                if len(b_exist) == 0:
                    if len(order_id) > 0:
                        cprint(
                            "Sorry this book is not available now...!!!", "red")
                        cprint("It will be available after ", "white", "on_grey", end="")
                        cprint(f"{''.join(order_id[0].get_end_date())}", "yellow", "on_grey")
                        cprint("Returned to Borrow_Order", "yellow")
                        continue
                    else:
                        cprint("Enter a valid book id please", "red")
                        cprint("Returned to Borrow_Order", "yellow")
                        continue
                else:
                    id1 = input(colored("Enter the client's library id please: ", "cyan"))
                    c_exist = [i for i in clients if id1 == "".join(i.get_id_no())]
                    if len(c_exist) != 0:
                        client = c_exist[0]
                        pass
                    else:
                        cprint("The user that you entered id for is not exist ", "red")
                        cprint("Add new user:", "green")
                        client = add_client(Client, clients)
                        pass

                    bro_book = [i for i in books if b_id == "".join(i.get_id())]
                    bro_book[0].borrow()
                    while True:
                        end_days = input(colored("How many days the client want to borrow the book: ", "cyan"))
                        if not end_days.isdigit():
                            cprint("Enter digit numbers only please", "red")
                            continue
                        else:
                            end_dates = datetime.date.today() + datetime.timedelta(days=int(end_days))
                            a = end_dates.strftime("%b %d %Y")
                        order = BorrowOrder(
                            end_date=a,
                            book_id=bro_book[0].get_id(),
                            client_id=client.get_id_no())

                        orders.append(order)

                        cprint(
                            "The book reserved successfully with order id ", "white", "on_grey", end="")
                        cprint(f"{''.join(order.get_id())}, ", "yellow", "on_grey", end="")
                        cprint(f"and will be returned on ", "white", "on_grey", end="")
                        cprint(f"{a}", "yellow", "on_grey")
                        cprint("Returned to Borrow_Order", "yellow")
                        break
                    continue
            if choice == "b":
                cprint(f"available clients list:", "magenta")
                for i in clients:
                    print(f"Name : {''.join(i.get_name())}    Id: {''.join(i.get_id_no())} ")
                cprint("Returned to Borrow_Order", "yellow")
                continue
            if choice == "c":
                cprint("List of available books:", "magenta")
                available_books = [i for i in books if "".join(i.get_status()) == "Active"]
                for i in available_books:
                    print(
                        f"title : {''.join(i.get_name())}  author: {''.join(i.get_author())}  id: {''.join(i.get_id())}")
                cprint(f"Returned to Borrow_Order", "yellow")
                continue
            if choice == "m":
                choice = "**"
                break
            else:
                cprint("invalid input..!!!", "red")
                continue
    if choice == "5":
        while True:
            or_id = input(colored("Enter the order id please: ", "cyan"))
            or_exist = [i for i in orders if or_id == "".join(i.get_id())]
            if len(or_exist) != 0:
                if "".join(or_exist[0].get_status()) == "Active":
                    or_exist[0].cancel()
                    book = [i for i in books if or_exist[0].get_book_id() == "".join(i.get_id())]
                    book[0].return_book()
                    cprint(f"The book with title ", "white", "on_grey", end="")
                    cprint(f"{''.join(book[0].get_name())} ", "yellow", "on_grey", end="")
                    cprint("successfully returned ", "white", "on_grey")
                    choice = "**"
                    break
                else:
                    if "".join(or_exist[0].get_status()) == "Cancel":
                        cprint("The order already canceled", "red")
                        choice = "**"
                        break
                    if "".join(or_exist[0].get_status()) == "Expire":
                        cprint("The order already expired", "red")
                        choice = "**"
                        break
            else:
                cprint("The borrow order id that you entered is not exist , try to enter valid id.", "red")
                menu_return = input(colored("If you want to return to the main menu press 'm':  ", "cyan"))
                if menu_return == "m":
                    choice = "**"
                    break
                else:
                    continue
    if choice == "6":
        while True:
            cprint("Main/Services:", "magenta")
            cprint("""    a-Clients
    b-Books
    c-Orders
    d-Librarians
    m-Return to Main""", "blue")
            choice = input(colored("Your choice:", "grey", "on_white") + " ")
            if choice == "a":
                cprint("List of clients:", "magenta")
                if len(clients) == 0:
                    cprint("The list is empty", "white", "on_grey")
                else:
                    cprint(f"number of clients: ", "white", "on_grey", end="")
                    cprint(f"{len(clients)} ", "yellow", "on_grey")
                    for i in clients:
                        print(f"Full.Name: {colored(i.display()['full_name'][0], 'red')}", end="|  |")
                        print(f"Age: {colored(i.display()['age'][0], 'red')}", end="|  |")
                        print(f"Phone no: {colored(i.display()['phone_num'][0], 'red')}", end="|  |")
                        print(f"Library-Id: {colored(i.display()['library_id'], 'red')}")
                choice = "**"
            if choice == "b":
                while True:
                    cprint("Main/Services/Books:", "magenta")
                    cprint("""    a- All books
    b- Available books
    c- Borrowed books
    s- Return to Services
    m- Return to Main""", "blue")
                    choice = input(colored("Your choice:", "grey", "on_white") + " ")
                    if choice == "a":
                        if len(books) == 0:
                            cprint("The list is empty", "white", "on_grey")
                        else:
                            cprint(f"number of books: ", "white", "on_grey", end="")
                            cprint(f"{len(books)} ", "yellow", "on_grey")
                            for i in books:
                                print(f"Id: {''.join(i.display()['id'])}", end="|  |")
                                print(f"Title: {i.display()['title'][0]}", end="|  |")
                                print(f"Description: {i.display()['description'][0]}", end="|  |")
                                print(f"Author: {i.display()['author'][0]}", end="|  |")
                                print(f"Status: {status_color(''.join(i.display()['status']))}")
                        cprint("Returned to Books", "yellow")
                    if choice == "b":

                        available_books = [i for i in books if "".join(i.get_status()) == "Active"]
                        if len(available_books) == 0:
                            cprint("The list is empty", "white", "on_grey")
                        else:
                            cprint("Number of available books is: ", "white", "on_grey", end="")
                            cprint(f"{len(available_books)} ", "yellow", "on_grey")
                            for i in available_books:
                                print(f"Id: {i.display()['id'][0]}", end="|  |")
                                print(f"Title: {i.display()['title'][0]}", end="|  |")
                                print(f"Description: {i.display()['description'][0]}", end="|  |")
                                print(f"Author: {i.display()['author'][0]}")
                        cprint("Returned to Books", "yellow")
                    if choice == "c":
                        borrowed_books = [i for i in books if "".join(i.get_status()) == "Inactive"]
                        if len(borrowed_books) == 0:
                            cprint("The list is empty", "white", "on_grey")
                        else:
                            cprint("Number of borrowed books is: ", "white", "on_grey", end="")
                            cprint(f"{len(borrowed_books)} ", "yellow", "on_grey")
                            for i in borrowed_books:
                                print(f"Id: {i.display()['id'][0]}", end="|  |")
                                print(f"Title: {i.display()['title'][0]}", end="|  |")
                                print(f"Description: {i.display()['description'][0]}", end="|  |")
                                print(f"Author: {i.display()['author'][0]}")
                        cprint("Returned to Books", "yellow")
                    if choice == "s":
                        choice = "**"
                        break
                    if choice == "m":
                        break
            if choice == "c":
                while True:
                    cprint("Main/Services/Orders:", "magenta")

                    cprint("""    a- All orders list
    b- Active orders list
    c- Expired orders list
    d- Cancelled orders list
    e- Check single order status
    s- Return to Services
    m- Return to Main""", "blue")
                    choice = input(colored("Your choice:", "grey", "on_white") + " ")
                    if choice == "a":
                        cprint(f"All orders list", "magenta")
                        if len(orders) == 0:
                            cprint("The list is empty", "white", "on_grey")
                        else:
                            cprint(f"The number of all orders: ", "white", "on_grey", end="")
                            cprint(f"{len(orders)} ", "yellow", "on_grey")
                            for i in orders:
                                print(f"Id: {i.display()['id'][0]}", end="|  |")
                                print(f"S.date: {''.join(i.display()['start_date'])}", end="|  |")
                                print(f"E.date: {i.display()['end_date'][0]}", end="|  |")
                                print(f"Book-Id: {i.display()['book_id'][0]}", end="|  |")
                                print(f"Client-Id: {i.display()['client_id'][0]}", end="|  |")
                                print(f"Status: {status_color(''.join(i.display()['status']))}")
                        cprint("Returned to Orders", "yellow")
                    if choice == "b":
                        active_orders = [i for i in orders if "".join(i.get_status()) == "Active"]
                        cprint(f"Active orders list", "magenta")
                        if len(active_orders) == 0:
                            cprint("The list is empty", "white", "on_grey")
                        else:
                            cprint(f"The number of active orders: ", "white", "on_grey", end="")
                            cprint(f"{len(active_orders)} ", "yellow", "on_grey")
                            for i in active_orders:
                                print(f"Id: {i.display()['id'][0]}", end="|  |")
                                print(f"S.date: {''.join(i.display()['start_date'])}", end="|  |")
                                print(f"E.date: {i.display()['end_date'][0]}", end="|  |")
                                print(f"Book-Id: {i.display()['book_id'][0]}", end="|  |")
                                print(f"Client-Id: {i.display()['client_id'][0]}")
                        cprint("Returned to Orders", "yellow")
                    if choice == "c":
                        expired_orders = [i for i in orders if "".join(i.get_status()) == "Expired"]
                        cprint(f"Expired orders list", "magenta")
                        if len(expired_orders) == 0:
                            cprint("The list is empty", "white", "on_grey")
                        else:
                            cprint(f"The number of expired orders: ", "white", "on_grey", end="")
                            cprint(f"{len(expired_orders)} ", "yellow", "on_grey")
                            for i in expired_orders:
                                print(f"Id: {i.display()['id'][0]}", end="|  |")
                                print(f"S.date: {''.join(i.display()['start_date'])}", end="|  |")
                                print(f"E.date: {i.display()['end_date'][0]}", end="|  |")
                                print(f"Book-Id: {i.display()['book_id'][0]}", end="|  |")
                                print(f"Client-Id: {i.display()['client_id'][0]}")
                        cprint("Returned to Orders", "yellow")
                    if choice == "d":
                        cancelled_orders = [i for i in orders if "".join(i.get_status()) == "Cancelled"]
                        cprint("Cancelled orders list", "magenta")
                        if len(cancelled_orders) == 0:
                            cprint("The list is empty", "white", "on_grey")
                        else:
                            cprint(f"The number of cancelled orders: ", "white", "on_grey", end="")
                            cprint(f"{len(cancelled_orders)} ", "yellow", "on_grey")
                            for i in cancelled_orders:
                                print(f"Id: {i.display()['id'][0]}", end="|  |")
                                print(f"S.date: {''.join(i.display()['start_date'])}", end="|  |")
                                print(f"E.date: {i.display()['end_date'][0]}", end="|  |")
                                print(f"Book-Id: {i.display()['book_id'][0]}", end="|  |")
                                print(f"Client-Id: {i.display()['client_id'][0]}")
                        cprint("Returned to Orders", "yellow")
                    if choice == "e":
                        or_id = input(colored("Enter the order id please: ", "cyan"))
                        or_exist = [i for i in orders if or_id == "".join(i.get_id())]
                        if len(or_exist) != 0:
                            bo_exist = [i for i in books if
                                        "".join(i.get_id()) == "".join(or_exist[0].get_book_id())]
                            cprint(
                                f"The status of the borrow order for the book with title ", "white", "on_grey", end="")
                            cprint(''.join(bo_exist[0].get_name()), "yellow", "on_grey", end="")
                            cprint(" is ", "white", "on_grey", end="")
                            cprint(''.join(or_exist[0].check_status()), "yellow", "on_grey")
                        else:
                            cprint("The borrow order id that you entered is not exist , try to enter a valid id.",
                                   "red")
                        cprint("Returned to Orders", "yellow")
                    if choice == "s":
                        choice = "**"
                        break
                    if choice == "m":
                        break
            if choice == "d":
                cprint("List of librarians:", "magenta")
                if len(librarians) == 0:
                    cprint("The list is empty", "white", "on_grey")
                else:
                    cprint(f"number of librarians: ", "white", "on_grey", end="")
                    cprint(f"{len(librarians)} ", "yellow", "on_grey")
                    for i in librarians:
                        print(f"Full.Name: {colored(i.display()['full_name'][0], 'green')}", end="|  |")
                        print(f"Age: {colored(i.display()['age'][0], 'green')}", end="|  |")
                        print(f"Phone no: {colored(i.display()['phone_num'][0], 'green')}", end="|  |")
                        print(f"Library-Id: {colored(i.display()['library_id'], 'green')}", end="|  |")
                        print(f"Salary: {colored(i.get_salary(), 'green')} USD$")
                choice = "**"
            if choice == "m":
                choice = "**"
                break
            else:
                if choice == "**":
                    cprint(f"Returned to Services", "yellow")
                else:
                    cprint("invalid input..!!!", "red")
                continue
    if choice == "7":
        cprint("                                              ", "red", "on_grey")
        cprint("_____________________Exit_____________________", "red", "on_grey")
        cprint("                                              ", "red", "on_grey")
        break
    else:
        if choice == "**":
            cprint(f"Returned to Main", "yellow")
        else:
            cprint("invalid input..!!!", "red")
        continue
