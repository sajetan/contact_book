from project import *

class UserAuth(object):
    def __init__(self,username,password):

        self.username = username
        self.password = password

    def do_authentication(self):
        if self.username == "tej" and self.password == "123":
            #starting user session
            session['logged_in'] = True
        else:
            return False
        return True


