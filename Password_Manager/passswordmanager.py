from cryptography.fernet import Fernet
"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
    key_file.write(key) """

def load_key():
	file = open("key.key",'rb')
	key= file.read()
	file.close()
	return key

key = load_key()

# using fr as to store Fernet(key)
fr = Fernet(key)

def view():
	with open('passwords.txt',"r") as f:
		for line in f.readlines():
			d = line.rstrip()
			user,pd = d.split("|")
			print("User: ",user,", Password: ",fr.decrypt(pd.encode()).decode())


def add():
	name = input("Account Name: ")
	pwd = input("Password: ")
	with open('passwords.txt',"a") as f:
		f.write(name + "[" + fr.encrypt(pwd.encode()).decode()+']' + "\n")


option = input("Do you want to change ur password?: ")


while option.lower() == "yes":
	mode = input("Would you like to set new password(add) or view the password or quit?: ")

	if mode.lower() == "q":
		break

	if mode.lower() == "view":
		view()

	elif mode.lower() == "add":
		add()
		
	else:
		print("Invalid option!")
