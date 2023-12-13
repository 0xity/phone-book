class ContactBook:
    def __init__(self):
        self.contactlist = {
            "Luca": "4206980085",
            "Kate": "4822911413",
            "Oxity": "0817708177"
        }

    def add_contact(self):
        name = input("Input a name: ")
        if name in self.contactlist:
            print(f"{name} already exists! Please pick a different name.")
            del name
            self.add_contact()
        else:
            number = input("Input the phone number: ")
            self.contactlist[name] = number
            print(f"{name} with the phone number {number} has been added")

    def update_contact(self):
        name = input("Input a name: ")
        if name not in self.contactlist:
            print(f"Cannot find {name} in contact list! Please pick a valid name.")
            del name
            self.update_contact()
        else:
            number = input("Input the phone number: ")
            self.contactlist[name] = number
            print(f"{name} with the phone number {number} has been updated")

    def remove_contact(self):
        name = input("Input a name: ")
        if name not in self.contactlist:
            print(f"Cannot find {name} in contact list! Please pick a valid name.")
            del name
            self.remove_contact()
        else:
            self.contactlist.pop(name)
            print(f"{name} has been removed")

    def view_contact(self):
        name = input("Input a name: ")
        if name not in self.contactlist:
            print(f"Cannot find {name} in contact list! Please pick a valid name.")
            del name
            self.view_contact()
        else:
            print(f"{name}: {self.contactlist[name]}")

    def show_list(self):
        print(self.contactlist)


if __name__ == "__main__":
    pb = ContactBook()
    pb.show_list()
    pb.add_contact()
    pb.update_contact()
    pb.remove_contact()
    pb.show_list()
