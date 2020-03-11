
class Staff():    

    def __init__(self, id, firstname, lastname, role, **kwargs):

        self.id = id

        self.firstname = firstname
        self.lastname = lastname
        self.name = self.firstname + ' ' + self.lastname

        self.roles = self.determine_roles(role)


    def determine_roles(self, role):

        roles = ['supervisor', 'advanced', 'intermediate', 'beginner']

        if role not in roles:
            return [role]

        return roles[roles.index(role):]

