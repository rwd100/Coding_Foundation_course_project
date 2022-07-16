from models import Book


def add_client(Client, clients):
    full_name = ""
    age_num = ""
    valid_phone = ""

    while True:
        name = input("Enter the client's full name please: ")
        if not "".join(name.split()).isalpha():
            print("enter a a valid name please")
            continue
        if len(name.split(" ")) < 2:
            print("enter the full name please")
            continue
        else:
            full_name = name.upper()
            break
    while True:
        age = input("Enter the client's age please: ")
        if not age.isdigit():
            print("enter only digit numbers please")
            continue
        if not int(age) in range(18, 66):
            print("Sorry only ages from 18 to 65 are allowed")
            continue
        else:
            age_num = age
            break
    while True:
        phone = input("Enter the client's phone number please: ")
        if not phone.isdigit():
            print("enter only digit numbers please")
            continue
        if not phone.startswith("059") or len(phone) != 10:
            print("Enter a valid phone number which starts with '059' and has 10 nums ")
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
    print(f"A new client had been added successfully ,his id is '{new_client.get_id_no()}'")
    return new_client


# title, description, author

def add_librarian(Librarian, librarians):
    full_name = ""
    age_num = ""
    valid_phone = ""
    valid_salary = ""
    while True:
        name = input("Enter the librarian's full name please: ")
        if not "".join(name.split()).isalpha():
            print("enter a a valid name please")
            continue
        if len(name.split(" ")) < 2:
            print("enter the full name please")
            continue
        else:
            full_name = name.upper()
            break
    while True:
        age = input("Enter the librarian's age please: ")
        if not age.isdigit():
            print("enter only digit numbers please")
            continue
        if not int(age) in range(18, 100):
            print("Sorry only ages from 18 to 99 are allowed")
            continue
        else:
            age_num = age
            break
    while True:
        phone = input("Enter the librarian's phone number please: ")
        if not phone.isdigit():
            print("enter only digit numbers please")
            continue
        if not phone.startswith("059") or len(phone) != 10:
            print("Enter a valid phone number which starts with '059' and has 10 nums ")
            continue
        else:
            valid_phone = phone
            break
    while True:
        salary = input("Enter the librarian's salary please: ")
        if "".join(salary.split(".")).isdigit():
            valid_salary = salary
            break
        else:
            print("enter only digit numbers please")
            continue

    new_librarian = Librarian(
        full_name=full_name,
        age=age_num,
        phone_num=valid_phone,
    )
    salary = valid_salary
    new_librarian.set_salary(salary)
    librarians.append(new_librarian)
    print(f"A new librarian had been added successfully ,his id is '{new_librarian.get_id_no()}'")
    return new_librarian


def add_book(Book, books):
    title = ""
    author = ""
    while True:
        t = input("Enter the book's title please: ")
        if not "".join(t.split()).isalpha():
            print("enter a a valid name please")
            continue
        else:
            title = t.upper()
            break
    description = input("Enter the book's description please: ")
    while True:
        a = input("Enter the book's author name please: ")
        if not t.isalpha():
            print("enter a a valid name please")
            continue
        else:
            author = a.upper()
            break

    new_book = Book(
        title=title,
        description=description,
        author=author,)

    books.append(new_book)
    print(f"A new book had been added successfully ,his id is '{new_book.get_id()}'")
    return new_book
