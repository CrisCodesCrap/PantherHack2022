from datetime import datetime
from database import User, session as db
from passlib.context import CryptContext

hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")

class LoginHandler:
    
    def getUser(username:str):
        user = db.execute('SELECT * FROM users WHERE username = :username', {'username': username}).first()
        if user:
            return user
        return False
    
    def VerifyPassword(hashedPassword:str, password:str):
        return hasher.verify(password, hashedPassword)

    def CheckExistingUserDataForRegister(this,username:str, email:str):
        UserByName = this.getUser(username)
        UserByEmail = db.execute('SELECT * FROM users WHERE email = :email', {'email': email}).first()
        if not UserByName and not UserByEmail:
            return True
        return False

    def CheckExistingUserDataForLogin(this,username:str, password:str):
        user = this.getUser(username)
        if user:
            if this.VerifyPassword(user.password, password):
                return user
        return False
    
    def NewUserAssignment(username:str, password:str, email:str):
        user = User(username=username, password=hasher.hash(password), email=email, timeJoined=datetime.now(),messagesSent=0,lastSeen=datetime.now(),online=True)
        try:
            db.add(user)
        except Exception as e:
            print(e)
            return False
        return True