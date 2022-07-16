import datetime
from random import randint


class Person:
    def __init__(self, full_name, age, phone_num):
        self._id = "P_" + str(randint(111, 999)),
        self._full_name = full_name,
        self._age = age,
        self._id_no = None,
        self._phone_num = phone_num,

    def set_id_no(self, id_no):
        self._id_no = id_no

    def get_id_no(self):
        return self._id_no

    def get_name(self):
        return self._full_name

    def display(self):
        return {
            "full_name": self._full_name,
            "age": self._age,
            "phone_num": self._phone_num,
            "library_id": self.get_id_no(),
        }


class Client(Person):
    def __init__(self, full_name, age, phone_num):
        super().__init__(full_name, age, phone_num)
        self.set_id_no("Cl_" + str(randint(111, 999)))


class Librarian(Person):
    def __init__(self, full_name, age, phone_num):
        super().__init__(full_name, age, phone_num)
        self._salary = 0
        self.set_id_no("Li_" + str(randint(111, 999)))

    def set_salary(self, salary1):
        self._salary = salary1

    def get_salary(self):
        return self._salary


class Book:
    def __init__(self, title, description, author):
        self.id = "B_" + str(randint(111, 999)),
        self._title = title,
        self._description = description,
        self._author = author,
        self._status = "Active",

    def borrow(self):
        self._status = "Inactive"
        return self._status

    def return_book(self):
        self._status = "Active"
        return self._status

    def get_id(self):
        return "".join(self.id)

    def get_name(self):
        return self._title

    def get_status(self):
        return self._status


class BorrowOrder:
    def __init__(self, end_date, book_id, client_id):
        self._id = "Or_" + str(randint(111, 999)),
        self._start_date = datetime.date.today().strftime("%b %d %Y")
        self._end_date = end_date,
        self._book_id = book_id,
        self._client_id = client_id,
        self._status = "Active",

    def display(self):
        return {
            "id": self._id,
            "start_date": self._start_date,
            "end_date": self._end_date,
            "book_id": self._book_id,
            "client_id": self._client_id,
            "status": self._status
        }

    def get_id(self):
        return self._id

    def check_status(self, ):
        if self._status == "Cancelled":
            return self._status
        else:
            if self._end_date[0] < datetime.date.today():
                self._status = "Expired"
                return self._status
            elif self._end_date[0] >= datetime.date.today():
                self._status = "Active"
                return self._status

    def cancel(self):
        self._status = "Cancelled"

    def get_status(self):
        return self._status

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def get_book_id(self):
        return "".join(self._book_id)


