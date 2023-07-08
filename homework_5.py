from collections import UserDict

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
        self.phone_list = []
        if phone: 
            self.phone_list.append(phone)

    def add_phone(self, phone: Phone):
        self.phone_list.append(phone)
        pass

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
        return f'{self.name.value} {self.phone_list}'

    def __repr__(self) -> str:
        return str(self)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def search_user(self, name_str: str):
        name = Name(name_str)
        if self.data.get(name.value):
            return self.data[name.value]

        # the same:
        #if self.data.get(name_str):
        #    return self.data[name_str]
        return None

def main():
    
    ab = AddressBook()
    name = Name("Bill")
    phone1 = Phone("12345")
    rec1 = Record(name, phone1)

    rec2 = Record(name, Phone("111"))
    rec2.add_phone(Phone("222"))
    rec2.add_phone(Phone("333"))
    
    ab.add_record(rec1)
    
    ab.add_record(Record(Name("Jill")))

    ab.add_record(rec2)
    
 
    phone2 = Phone("56784")
    #print(ab)

    rec = ab["Jill"]
    
    rec.add_phone(phone2)
    print(rec)


    rec.change_phone(Phone("56784"), Phone("99345"))
    print(rec)
    
    for rec in ab.values():
        assert isinstance(rec1, Record)
        print(rec)


if __name__ == "__main__":
    main()
