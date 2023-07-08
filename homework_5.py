from collections import UserDict

def input_error(func):
    def wrapper(*args, **kwargs):
        argc = len(args)
        result = None
        try:
            result = func(*args, **kwargs)
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me name and phone please")
        except IndexError:
            print("You entered incorrect data")
        except TypeError:
            print("Wrong input type")
        return result
    return wrapper     
####################################################

class Field:
    pass

class Name:

    def __init__(self, name):
        self.value = name

class Phone:

    def __init__(self, number):
        self.number = number

    def __str__(self) -> str:
        return f'phone: {self.number}'

    def __repr__(self) -> str:
        return str(self)

class Record:

    def __init__(self, name : Name, phone = None):
        self.name = name
        self.phone_list = []    #list[Phone()]
        if phone: 
            self.phone_list.append(phone)

    def add_phone(self, phone: Phone):
        self.phone_list.append(phone)

    def change_phone(self, phone_from: Phone, phone_to: Phone):
        for idx, item in enumerate(self.phone_list):
            if phone_from.number == item.number:
                self.phone_list[idx] = phone_to

    def delete_phone(self, number: str):
        # iterate from end to begin (reverse iteration)
        for item in reversed(self.phone_list):
            if item.number == number:
                self.phone_list.remove(item)

    def __str__(self) -> str:
        return f'{self.phone_list}'

    def __repr__(self) -> str:
        return str(self)

class AddressBook(UserDict):

    def add_record(self, record: Record):
        if self.data.get(record.name.value):
            rec = self.data[record.name.value]
            rec.phone_list.extend(record.phone_list)
        else:
            self.data[record.name.value] = record

    # -> return Record(name)
    def search_user(self, name_str: str):
        name = Name(name_str)
        if self.data.get(name.value):
            return self.data[name.value]

        # the same:
        #if self.data.get(name_str):
        #    return self.data[name_str]
        return None

########################################################

address_book = AddressBook()

@input_error
def hello(*args):
    return f"How can I help you?"

@input_error
def add(*args):
    name = args[0]
    number = args[1]
    address_book.add_record(Record(Name(name), Phone(number)))
    return f"Add success {name} {number}"

@input_error
def change(*args):
    name = args[0]
    number_from = int(args[1])  #check if number, else generate exception
    number_to = int(args[2])    #check if number, else generate exception
    phone_from = args[1]
    phone_to = args[2]

    record = address_book.search_user(name)
    if record:
        record.change_phone(Phone(phone_from), Phone(phone_to))
        return f"Change success {name} {number_from}->{number_to}"
    return f"Change error {name} {number_from}->{number_to}"

@input_error
def phone(*args):
    name = args[0]
    phone = ""
    record = address_book.search_user(name)
    if record:
        return " ".join([phone.number for phone in record.phone_list])
    return "ERROR empty"

@input_error
def show_all():
    return address_book

@input_error
def good_bye(*args):
    print("Good bye!")
    exit(0)
    return None

@input_error
def no_command(*args):
    return "Unknown command"

###############################################
def parser(text: str): #-> tuple([callable, tuple([str]|None)]):
    if text.lower().startswith("add"):
        return add, text.lower().replace("add", "").strip().split()
    if text.lower().startswith("hello"):
        return hello, None
    if text.lower().startswith("change"):
        cmd = text.lower().replace("change", "")
        return change, cmd.strip().split()
    if text.lower().startswith("phone"):
        cmd = text.lower().replace("phone", "")
        return phone, cmd.strip().split()
    if text.lower().startswith("show all"):
        return show_all, None
    if text.lower().startswith("good bye") or text.lower().startswith("exit") or text.lower().startswith("close"):
        return good_bye, None 

    return no_command, None

###############################################
def main():
    while True:
        user_input = input(">>>")
        command, args = parser(user_input)
        if args != None:
            result = command(*args)
        else:
            result = command()
        print(result)

###############################################
if __name__ == "__main__":
    main()
