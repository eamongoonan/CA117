class Student:
    def __init__(self, sname, fname, id, modules=None):
        self.surname = sname
        self.forename = fname
        self.sid = id
        self.modlist = [] if modules is None else modules

    def add_module(self, mod):
        if mod not in self.modlist:
            self.modlist.append(mod)

    def del_module(self, mod):
        if mod in self.modlist:
            self.modlist.remove(mod)

    def print_details(self):
        print("ID:", self.sid)
        print("Surname:", self.surname)
        print("Forename:", self.forename)
        print("Modules:", " ".join(self.modlist))
