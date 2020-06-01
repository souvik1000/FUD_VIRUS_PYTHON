import os
import Colors
import Generate_File

print("[+] shell.py is compiling")
pwd = os.getcwd()
path = os.path.join('C:\\Users\\ghosh\\Desktop\\My_Virus\\Icon','virus.ico')
os.system("pyinstaller -F -i "+ path +" shell.py 2>nul")
print ("\n[+]Output generated at dist\shell.exe")