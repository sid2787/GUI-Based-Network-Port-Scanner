# 18BCE7038

# Modules
import sys
import os
import socket,threading,time
import smtplib
from email.message import EmailMessage
from datetime import datetime
from tkinter import *
 
# Default Port Range
start = 1
end = 1024
log = []
ports = []
target = 'localhost'

# Program Functionality 
def scanPort(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        c = s.connect_ex((target, port))
        if c == 0:
            m = '> Port %d \tis open!' % (port,)
            log.append(m)
            ports.append(port)
            listbox.insert("end", str(m))
            updateResult()
        s.close()
    except OSError: print('> Too many open sockets. Port ' + str(port))
    except:
        c.close()
        s.close()
        sys.exit()
    sys.exit()
     
def updateResult():
    rtext = " [ " + str(len(ports)) + " / " + str(end) + " ] ports open for " + str(target)
    L27.configure(text = rtext)
 
def startScan():
    global ports, log, target, end
    clearScan()
    log = []
    ports = []
    start = int(L24.get())
    end = int(L25.get())
    # Log file contents
    log.append('> Port Scanner')
    log.append('='*14)
    log.append(' Target:\t' + str(target))
    log.append(' Time Started:  ' + str(datetime.now()))
    log.append('='*14 + '\n') 
    try:
        target = socket.gethostbyname(str(L22.get()))
        log.append(' Target IP: \t' + str(target))
        log.append(' Port Range : \t[ ' + str(start) + ' / ' + str(end) + ' ]')
        log.append('\n')
        # Driver Code
        while start <= end:
            try:
                scan = threading.Thread(target=scanPort, args=(target, start))
                scan.setDaemon(True)
                scan.start()
            except: time.sleep(0.01)
            start += 1
    except:
        m = '> Target ' + str(L22.get()) + ' not found.'
        log.append(m)
        listbox.insert(0, str(m))
         
def saveScan():
    global log, target, ports, end
    log[5] = " Open Ports:\t[ " + str(len(ports)) + " / " + str(end) + " ]\n"
    with open('portscan-'+str(target)+'.txt', mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(log))

def mailScan():
    # Enter E-mail credentials here
    User = 'email@gmail.com' # E-mail ID
    Passwd = 'password' # Email Password
    msg = EmailMessage()
    msg['Subject'] = 'Scan Results For '+str(target)
    msg['From'] = User
    msg['To'] = User
    # Modify message content
    msg.set_content('Greetings! Results of the scan performed on target : '+str(target)+' conducted on ' +str(datetime.now())+' has been attached.')

    with open('portscan-'+str(target)+'.txt', 'rb') as f:
        file_data = f.read()
        file_name = f.name
    
    msg.add_attachment(file_data, maintype='text', subtype='txt', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(User,Passwd)
        smtp.send_message(msg)

 
def clearScan():
    listbox.delete(0, 'end')
 
# GUI Code 
gui = Tk()
gui.title('Port Scanner')
gui.geometry("400x600+20+20")
 

m1c = '#00ccff'
bgc = '#000000'
fgc = '#111111'
 
gui.tk_setPalette(background=bgc, foreground=m1c, activeBackground=fgc,activeForeground=bgc, highlightColor=m1c, highlightBackground=m1c)
 

L11 = Label(gui, text = "Port Scanner",  font=("Helvetica", 16, 'underline'))
L11.place(x = 16, y = 10)
 
L21 = Label(gui, text = "Target: ")
L21.place(x = 16, y = 90)
 
L22 = Entry(gui, text = "localhost")
L22.place(x = 180, y = 90)
L22.insert(0, "localhost")
 
L23 = Label(gui, text = "Ports: ")
L23.place(x = 16, y = 158)
 
L24 = Entry(gui, text = "1")
L24.place(x = 180, y = 158, width = 95)
L24.insert(0, "1")
 
L25 = Entry(gui, text = "1024")
L25.place(x = 290, y = 158, width = 95)
L25.insert(0, "1024")
 
L26 = Label(gui, text = "Results: ")
L26.place(x = 16, y = 220)
L27 = Label(gui, text = "[ ... ]")
L27.place(x = 180, y = 220)
 

frame = Frame(gui)
frame.place(x = 16, y = 275, width = 370, height = 215)
listbox = Listbox(frame, width = 59, height = 6)
listbox.place(x = 0, y = 0)
listbox.bind('<<ListboxSelect>>')
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
 

B11 = Button(gui, text = "Start Scan", command=startScan)
B11.place(x = 16, y = 500, width = 170)
B21 = Button(gui, text = "Save Result", command=saveScan)
B21.place(x = 210, y = 500, width = 170)
B31 = Button(gui, text = "Send Mail", command=mailScan)
B31.place(x = 115, y = 540, width = 170)
 
# Enable GUI
gui.mainloop()
