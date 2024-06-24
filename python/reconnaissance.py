import os
import nmap
import webbrowser

os.system("clear")

print()

print("Welcome to the Rayla Reconnaissance Framework")

print()
print("──▀▀▀▀▀▀▀▀▀▀▀▄▄▀▀▀▀▀▀▀▀▀▀▀")
print("────────────█▀▀█")
print("───────────█▓▓▓▓█")
print("───────══▄▀█▓▓▓▓█▀▄══")
print("──▄▄▄▄▄▄▄█▒█▓▓▓▓█▒█▄▄▄▄▄▄▄")
print("──█▀▀▀▀█▀███▄▓▓▄███▀█▀▀▀▀█")
print("─▄█▄──▄█▄───▀██▀───▄█▄──▄█▄")
print("─█▒█──█▒█──────────█▒█──█▒█")
print("─▀▀▀──▀▀▀──────────▀▀▀──▀▀▀")

print()


def selection():

	print("Please select an option below:")
	print()
	print("[1]: Scan network for open ports")
	print("[2]: View reports")
	print("[3]: OSINT Framework")
	print("[4]: Exit the Rayla Reconnaissance Framework")

	print()

	choice = input("Option: ")

	#choice 1
	if choice == "1":
		os.system("clear")
		print()
		address = input("Please enter IP address or domain name you want to scan: ")
		os.system("clear")
		print()
		print("Starting Nmap scan on: " + address + ".")
		print()
		print("──────██")
		print("─────████")
		print("────▄███")
		print("────▀▀████")
		print("──────▀▀████───────██")
		print("────────▀▀████───────██")
		print("──────────▀▀████───────██")
		print("────────────▀▀████───────██")
		print("──────────────▀▀████████───██")
		print("────────────────▀█████████───██")
		print("─────────────────████████████──██")
		print("──────────────────████████████───██")
		print("───────────────────███████████▄────██")
		print("────────────────█──█████████───█─────██")
		print("──────────────────█─▀██████────█───────██")
		print("────────────────────█─▀█████───█")
		print("──────────────────────█─▀████▄▀")
		print("────────────────────────█ ")
		print("──────────────────────────█")
		print()
		os.system("nmap -A " + address + " > /rayla/reconnassiance/nmap-reports/open-ports.txt")
		
		os.system("clear")
		os.system("cat /rayla/reconnassiance/nmap-reports/open-ports.txt")
		print()
		print("Nmap scan report saved to /rayla/reconnassiance/nmap-reports/open-ports.txt")
		print()
		input("Press enter when you are done viewing the report.")
		os.system("python3 /rayla/python/reconnaissance.py")



	#choice 2
	elif choice == "2":
		os.system("clear")
		print()
		print("Which report do you want to view?")
		print()
		print("[1]: Open ports report")
		print("[2]: Go back")

		print()
		choice_report = input("Option: ")

		if choice_report == "1":
			os.system("clear")
			os.system("cat /rayla/reconnassiance/nmap-reports/open-ports.txt")
			print()
			input("Press enter when you are done viewing the report.")
			os.system("python3 /rayla/python/reconnaissance.py")

		elif choice_report == "2":
			os.system("python3 /rayla/python/reconnaissance.py")

		else:
			print("Invalid entry... Hit enter")
			input()
			os.system("python3 /rayla/python/reconnaissance.py")



	#choice 3
	elif choice == "3":
		print("Opening OSINT Framework")
		webbrowser.open_new_tab('https://osintframework.com/')
		print()
		input("Press any button to return to the Rayla Reconnaissance Framework")
		os.system("python3 /rayla/python/reconnaissance.py")


	#choice 4
	elif choice == "4":
		os.system("clear")
		os.system("python3 /rayla/python/rayla.py")




	#other choice
	else:
		print("Invalid entry... Hit enter")
		input()
		os.system("python3 /rayla/python/reconnaissance.py")



selection()


