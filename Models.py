import hashlib
from datetime import date

class Token:
    def __init__(self):
        self.Number = None
        self.User = None
        self.Contest = None
        
    def createToken(self, contest, user):
        self.Contest = contest
        self.User = user
        self.Number = self.getHash()

    def getHash(self):
        str = f"{self.Contest}-{self.User}-{date.today()}"
        result = hashlib.sha256(str.encode())
        return result.hexdigest()

    # def markDB(self):
      

class Contest:
    def __init__(self,number,name,reward,deadline):
        self.Number = number
        self.Name = name
        self.Reward = reward
        self.Deadline = deadline

class Error:
    def __init__(self):
        self.errorCode = None
        self.error = None
    
    def userExists(self):
        self.errorCode = 24
        self.error = f"User has already participated in the contest"

    def tokenNotAvailable(self):
        self.erroCode = 25
        self.error = f"Token has been alotted to another user"