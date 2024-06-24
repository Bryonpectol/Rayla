import os

user = os.getlogin()

os.system("clear")

print()

print("Starting Rayla 1.0...")

print()
print("───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───")
print("───█▒▒░░░░░░░░░▒▒█───")
print("────█░░█░░░░░█░░█────")
print("─▄▄──█░░░▀█▀░░░█──▄▄─")
print("█░░█─▀▄░░░░░░░▄▀─█░░█")
print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
print("█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█")
print("█░░║║║╠─║─║─║║║║║╠─░░█")
print("█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

print()

print("██████╗░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░	░░███╗░░░░░░█████╗░")
print("██╔══██╗██╔══██╗╚██╗░██╔╝██║░░░░░██╔══██╗	░████║░░░░░██╔══██╗")
print("██████╔╝███████║░╚████╔╝░██║░░░░░███████║	██╔██║░░░░░██║░░██║")
print("██╔══██╗██╔══██║░░╚██╔╝░░██║░░░░░██╔══██║	╚═╝██║░░░░░██║░░██║")
print("██║░░██║██║░░██║░░░██║░░░███████╗██║░░██║	███████╗██╗╚█████╔╝")
print("╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝	╚══════╝╚═╝░╚════╝░")

print()

print("Welcome to the Rayla Framework, " + user + ".")

print()

input("Press enter to view Rayla's options")

os.system("clear")

print("Please familiarize yourself with https://attack.mitre.org/ before using Rayla.")
print()
print("Rayla Framework 1.0 options:")
print()
print("[1]: Reconnaissance")
print("[2]: Resource Development")
print("[3]: Initial Access")
print("[4]: Execution")
print("[5]: Persistence")
print("[6]: Privilege Escalation")
print("[7]: Defense Evasion")
print("[8]: Credential Access")
print("[9]: Discovery")
print("[10]: Lateral Movement")
print("[11]: Collection")
print("[12]: Command and Control")
print("[13]: Exfiltration")
print("[14]: Impact")
print("[0]: Exit")
print()

def selection():

	choice = input("Enter a number from above to choose an option: ")


	if choice == "0":
		os.system("clear")

	elif choice == "1":
		os.system("python3 /rayla/python/reconnaissance.py")

	elif choice == "2":
		os.system("python3 /rayla/python/resource-development.py")

	elif choice == "3":
		os.system("python3 /rayla/python/initial-access.py")

	elif choice == "4":
		os.system("python3 /rayla/python/execution.py")

	elif choice == "5":
		os.system("python3 /rayla/python/persistence.py")

	elif choice == "6":
		os.system("python3 /rayla/python/privilege-escalation.py")

	elif choice == "7":
		os.system("python3 /rayla/python/defense-evasion.py")

	elif choice == "8":
		os.system("python3 /rayla/python/credential-access.py")

	elif choice == "9":
		os.system("python3 /rayla/python/discovery.py")

	elif choice =="10":
		os.system("python3 /rayla/python/lateral-movement.py")

	elif choice =="11":
		os.system("python3 /rayla/python/collection.py")

	elif choice =="12":
		os.system("python3 /rayla/python/command-control.py")

	elif choice =="13":
		os.system("python3 /rayla/python/exfiltration.py")

	elif choice =="14":
		os.system("python3 /rayla/python/impact.py")

	else:
		selection()

selection()


