'''
TO DO's
-download PGA data into data strcture

-allow a user to create their fantasy team
-allow an admin to approve a user
-show the best fantasy line up
-allow user to view any team
-show the pool standings
-show the open standings
'''

class User(object):
    '''
    the User class takes the name of the user and the picks for their golfers
    '''
    def __init__(self, name=None, golferPicks=None):
        self.name = name
        self.golferPicks = golferPicks

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getGolferPicks(self):
        return self.golferPicks

    def setGolferPicks(self, golferPicks):
        self.golferPicks = golferPicks

class Admin(User):
    '''
    the Admin class does everything the User class does AND accepts/declines Users
    '''
    def __init__(self, adminPriv=True):
        self.adminPriv = adminPriv

    def getAdminPriv(self):
        return self.adminPriv

    def setAdminPriv(self, adminPriv):
        self.adminPriv = adminPriv
