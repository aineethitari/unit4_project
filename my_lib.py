import sqlite3
from passlib.context import CryptContext #cyptographic algorithm
pwd_config = CryptContext(schemes = ["pbkdf2_sha256"],
                          default = "pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds=30000
                          )

class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall() #gets a list
        return result

    def get(self,query):
        result = self.cursor.execute(query).fetchone() #gets only one result(the first)
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


def encrypt_password(user_password):
    #this function receives plain text password from the user and returns the hash salted
    return pwd_config.encrypt(user_password)

def check_password(user_password, hashed): #this is to check that the password entered is the same one as the hash
    return pwd_config.verify(user_password, hashed)
