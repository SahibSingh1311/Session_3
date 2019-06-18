# Inheritance Class missing
class Login:
    def LoginUSer(self):
        print(">>Login ")
class GoogleLogin(Login):
    def LoginUSer(self, email, password):
        print("Google Login Done")

class FacebookLogin(Login):
    def LoginUSer(self, Phone):
        print("OTP Login Done")

class cab:
    def bookCab(self, source, destination):
        print("Cab Booked from {} to {}". format(source, destination) )
class micro(cab):
    def bookCab(self, source, destination):
        print("Micro Cab Booked from {} to {}". format(source, destination) )
class mini(cab):
    def bookCab(self, source, destination):
        print("Mini Cab Booked from {} to {}" .format(source, destination) )
login = Login()
login.LoginUSer()

print()

login = GoogleLogin()
login.LoginUSer("john@example.com","pass123")
# Run time is dynamic memory management(PYTHON USES THIS)
# compile time is pre information
Cab = cab()
Cab.bookCab("Silver Arc", "MBD")
