from termcolor import cprint, colored


def add_client(Client, clients):
    full_name = ""
    age_num = ""
    valid_phone = ""

    while True:
        name = input(colored("Enter the client's full name please: ", "cyan"))
        if not "".join(name.split()).isalpha():
            cprint("enter a a valid name please", "red")
            continue
        if len(name.split(" ")) < 2:
            cprint("enter the full name please", "red")
            continue
        else:
            full_name = name.upper()
            break
    while True:
        age = input(colored("Enter the client's age please: ", "cyan"))
        if not age.isdigit():
            cprint("enter only digit numbers please", "red")
            continue
        if not int(age) in range(18, 66):
            cprint("Sorry only ages from 18 to 65 are allowed", "red")
            continue
        else:
            age_num = age
            break
    while True:
        phone = input(colored("Enter the client's phone number please: ", "cyan"))
        if not phone.isdigit():
            cprint("enter only digit numbers please", "red")
            continue
        if not phone.startswith("059") or len(phone) != 10:
            cprint("Enter a valid phone number which starts with '059' and has 10 nums ", "red")
            continue
        else:
            valid_phone = phone
            break

    new_client = Client(
        full_name=full_name,
        age=age_num,
        phone_num=valid_phone
    )
    clients.append(new_client)
    cprint("A new client had been added successfully ,his id is ", "white", "on_grey", end="")
    cprint(f"{new_client.get_id_no()}", "yellow", "on_grey")
    return new_client


def add_librarian(Librarian, librarians):
    full_name = ""
    age_num = ""
    valid_phone = ""
    valid_salary = ""
    while True:
        name = input(colored("Enter the librarian's full name please: ", "cyan"))
        if not "".join(name.split()).isalpha():
            cprint("enter a a valid name please", "red")
            continue
        if len(name.split(" ")) < 2:
            cprint("enter the full name please", "red")
            continue
        else:
            full_name = name.upper()
            break
    while True:
        age = input(colored("Enter the librarian's age please: ", "cyan"))
        if not age.isdigit():
            cprint("enter only digit numbers please", "red")
            continue
        if not int(age) in range(18, 100):
            cprint("Sorry only ages from 18 to 99 are allowed", "red")
            continue
        else:
            age_num = age
            break
    while True:
        phone = input(colored("Enter the librarian's phone number please: ", "cyan"))
        if not phone.isdigit():
            cprint("enter only digit numbers please", "red")
            continue
        if not phone.startswith("059") or len(phone) != 10:
            cprint("Enter a valid phone number which starts with '059' and has 10 nums ", "red")
            continue
        else:
            valid_phone = phone
            break
    while True:
        salary = input(colored("Enter the librarian's salary please: ", "cyan"))
        if "".join(salary.split(".")).isdigit():
            valid_salary = salary
            break
        else:
            cprint("enter only digit numbers please", "red")
            continue

    new_librarian = Librarian(
        full_name=full_name,
        age=age_num,
        phone_num=valid_phone,
    )
    salary = valid_salary
    new_librarian.set_salary(salary)
    librarians.append(new_librarian)
    cprint("A new librarian had been added successfully ,his id is ", "white", "on_grey", end="")
    cprint(f"{new_librarian.get_id_no()}", "yellow", "on_grey")
    return new_librarian


def add_book(Book, books):
    title = ""
    author = ""
    while True:
        t = input(colored("Enter the book's title please: ", "cyan"))
        if not "".join(t.split()).isalpha():
            cprint("enter a a valid name please", "red")
            continue
        else:
            title = t.upper()
            break
    description = input(colored("Enter the book's description please: ", "cyan"))
    while True:
        a = input(colored("Enter the book's author name please: ", "cyan"))
        if not a.isalpha():
            cprint("enter a a valid name please", "red")
            continue
        else:
            author = a.upper()
            break

    new_book = Book(
        title=title,
        description=description,
        author=author, )

    books.append(new_book)
    cprint("A new book had been added successfully ,his id is ", "white", "on_grey", end="")
    cprint(f"{new_book.get_id()}", "yellow", "on_grey")
    return new_book


def status_color(status):
    if status == "Active":
        return colored(status, "green")
    if status == "Inactive":
        return colored(status, "red")
    if status == "Expired":
        return colored(status, "blue")
    if status == "Cancelled":
        return colored(status, "red")
