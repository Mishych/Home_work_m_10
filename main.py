from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone_number):
        if self.check_number(phone_number):
            super().__init__(phone_number)
        else: 
            raise ValueError("Not correct")
            
    @staticmethod
    def check_number(phone_number):
        return len(phone_number) == 10 and phone_number.isdigit()
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number: Phone):
        phone = phone_number
        self.phones.append(phone)
    
    def printt(self):
        return self.phones
       
    def remove_phone(self, phone):
        for el in self.phones:
            if el == phone:
                self.phones.remove(phone)
                return f"Phone {phone} has been deleted"
        return f"Phone {phone} is not found"
    
    def edit_phone(self, old_phone, new_phone):
        for ind, phone in enumerate(self.phones):          
            if phone == old_phone:
                self.phones[ind] = new_phone
                return f"Phone number has been updated for {self.name.value}"
        return f"{old_phone} is not founded"
    
    def find_phone(self, phone_to_find):
        for phone in self.phones:
            if phone == phone_to_find:
                return phone_to_find
        return f"This phone number {phone_to_find} is not found"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p for p in self.phones)}"
    
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
         
    def find(self, name):
        if name in self.data:
            return self.data[name]
        return f"This name {name} is not in the record"
    
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
            print(f"{name} has been deleted from the AddressBook")
        return f"{name} is not in the AddressBook"
           
if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    # print(john_record)

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    # print(john)
    john.edit_phone("1234567890", "1112223333")

    # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555556")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    
    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)
