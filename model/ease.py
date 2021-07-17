from .db import check_user_email
from passlib.hash import sha256_crypt
from datetime import datetime

class UserValidator:
    def __init__(self,name,email,password):
        self.name = name.strip()
        self.email = email.strip()
        self.password = password.strip()

        # We are going to validate the class 

        try:
            self.valid = False
            if self.name != "":
                if self.email != "":
                    if check_user_email(self.email): #checking if the email is duplicated
                        if self.password != "":
                            self.password = sha256_crypt.hash(self.password, )
                            self.valid = True
                            self.msg = "User registered"
                        else:
                            self.msg = "Invalid Password"
                    else:
                        self.msg = "Email is not valid"
                else:
                    self.msg = "Name cannot be empty"
        except:
            self.valid = False
            self.msg="error occured, if you keep on showing contact developers"


    def data(self):
        return self.name, self.email, self.password, datetime.now()