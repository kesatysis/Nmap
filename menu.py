import os

os.chdir("bin")

def menu():

	print("""
1. Start Nmap default
2. Start Nmap full
""")
loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "1":
        os.system("python nmap-default.py")
        print("====================================")
        print("[+] Start Nmap default :)")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break
    elif what == "2":
        os.system("python nmap-full.py")
        print("====================================")
        print("[+] Start Nmap full :)")
        print("====================================")
        rmenu = input("[?] Back to Menu? (y/n): ")
        if rmenu == "y":
            menu()
        else:
            break