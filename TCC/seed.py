#-----------------------------------------------------------------------------#

### APP IMPORTS ###

from app.database import Database

#-----------------------------------------------------------------------------#

### SEED CLASS ###

class Seed():

    def __init__(self, *args, **kwargs):

        self.db = Database('tcc')


        #self.build_staff()
        #self.build_breaks()

    def build_staff(self):

        command = ''' CREATE TABLE staff (          
            id INT NOT NULL PRIMARY KEY,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            role TEXT)'''

        self.db.cursor.execute(command)
        self.db.connection.commit()

        supervisor = ['Michael Atheros', 
            'Adele Wood', 'Amanda Curtis', 'Daniel Joyce', 'Janice Wilcock', 'Lynette Glover',
            'Michelle Archer', 'Moana Kuma', 'Rory Sheehan', 'Samuel Patterson'            
            ]

        advanced = ['Alex Ingram', 'Callum Hornblow', 'Jack Duncan', 'Jewell Vole', 'Liam Reeve',
            'Lynne Fraser', 'Nikki Hibbert', 'Sean Baker'
            ]

        intermediate = [
            
            ]

        beginner = [
            'Adam Cooper', 'Mike Saunders', 'Piper Zimmerman'
            ]

        trainee = [
            'James Thompson'
            ]

        graveyard = [
            'Chris Baran'
            ]

        owner = [
            'John Sheehan', 'Julie Sheehan'
            ]

        id_count = 1
        for pair in [('supervisor', supervisor), ('advanced', advanced), ('beginner', beginner),
                     ('trainee', trainee), ('graveyard', graveyard), ('owner', owner)]:

            role = pair[0]
            for staff in pair[1]:
                firstname = staff.split()[0]
                lastname = staff.split()[1]
                command = '''INSERT INTO staff
                            VALUES ("%s", "%s", "%s", "%s");''' % (id_count, firstname, lastname, role)
                self.db.cursor.execute(command)
                id_count += 1

            self.db.connection.commit()

    def build_breaks(self):

        command = ''' CREATE TABLE breaks (          
            
            id INT NOT NULL PRIMARY KEY,
            staff_id INT,
            
            coffee1 INT,
            meal INT,
            coffee2 INT,
            
            taxi INT,

            supervisor INT DEFAULT 0,
            interim INT DEFAULT 0,
            dishes INT DEFAULT 0,
            cactus INT DEFAULT 0,
            training TEXT,

            FOREIGN KEY(staff_id) REFERENCES staff(id)

            )'''

        self.db.cursor.execute(command)
        self.db.connection.commit()
            
#-----------------------------------------------------------------------------#

### ENGINE ###

Seed()

#-----------------------------------------------------------------------------#