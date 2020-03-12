
class Staff():    

    def __init__(self, staff, **kwargs):

        self.id = staff[0]

        self.firstname = staff[1]
        self.lastname = staff[2]
        self.name = self.firstname + ' ' + self.lastname

        self.roles = self.determine_roles(staff[3])


    def determine_roles(self, role):

        roles = ['supervisor', 'advanced', 'intermediate', 'beginner']

        if role not in roles:
            return [role]

        return roles[roles.index(role):]

