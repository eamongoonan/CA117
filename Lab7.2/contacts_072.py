class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return " ".join([self.name, self.phone, self.email])

class ContactList:
    def __init__(self):
        self.d = {}

    def add_contact(self, contact):
        self.d[contact.name] = contact

    def del_contact(self, contact):
        if contact in self.d:
            del self.d[contact]

    def get_contact(self, contact):
        if contact in self.d:
            return self.d[contact]
        else:
            return None

    def __str__(self):
        return (
            "Contact list\n" +
            "------------\n" +
            "\n".join([str(self.d[k]) for k in sorted(self.d)])
        )
