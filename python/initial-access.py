import os

os.system("clear")

print()

print(" __8888888888888888888888888888888888888888")
print(" _88______________________________________88")
print(" 88_____8888_______________________________88")
print(" 88____88888_______________________________88")
print(" 88____88__88______________________________88")
print(" 88___88___88______________________________88")
print(" 88___88888888_____________________________88")
print(" 88__888___8888____________________________88")
print(" 88__88______88____________________________88")
print(" 88_________________888____________________88")
print(" 88________________88888___________________88")
print(" 88______________888888888_________________88")
print(" 88_____________88888888888________________88")
print(" 88____________8888888888888_______________88")
print(" 88___________888888888888888______________88")
print(" 88_________8888888888888888888____________88")
print(" 88_________8888888888888888888____________88")
print(" 88__________88888888888888888_____________88")
print(" 88_________________8888___________________88")
print(" 88_______________8888888__________________88")
print(" 88____________________________88______88__88")
print(" 88_____________________________88____888__88")
print(" 88_____________________________88888888___88")
print(" 88______________________________88__888___88")
print(" 88______________________________888_88____88")
print(" 88________________________________888_____88")
print(" _88______________________________________88")
print(" __8888888888888888888888888888888888888888")
print()
print("Welcome to the Rayla Initial Access Framework")
print()
print("Select an option below:")
print()
print("[1]: Create a MsfVenom Payload")
print("[2]: Search for a MsfVenom Payload")
print("[3]: Exit the Rayla Initial Access Framework")
print()


#venomsearch function

def venomsearch():
	os.system("clear")
	print()
	print("Please enter the keyword you want to search for:")
	print()
	keyword = input("Keyword: ")
	print()
	print("Searching MsfVenom for payloads...")
	print()
	os.system("msfvenom -l payloads | grep " + keyword)
	print()
	input("Press any button to return to the Rayla Initial Access Framework")
	os.system("python3 /rayla/python/initial-access.py")




#selection function

def selection():
	choice = input("Option: ")

	if choice == "1":
		input("This is a work in progress... Press enter.")
		os.system("python3 /rayla/python/initial-access.py")

	elif choice == "2":
		venomsearch()
		#input("This is a work in progress... Press enter.")
		#os.system("python3 /rayla/python/initial-access.py")

	elif choice == "3":
		os.system("clear")
		os.system("python3 /rayla/python/rayla.py")

	else:
		input("Please enter valid option... Press enter.")
		os.system("python3 /rayla/python/inital-access.py")


selection()
