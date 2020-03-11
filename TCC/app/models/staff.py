
class Staff():    

    def __init__(self, id, firstname, lastname, role, **kwargs):

        self.id = id

        self.firstname = firstname
        self.lastname = lastname
        self.name = self.firstname + ' ' + self.lastname

        self.role = role

