from tkinter import *
import os
import smtplib
from email.message import EmailMessage  # its a class to send messages in a better way. We no need to creater everything seperately
import tkinter 
from tkinter import filedialog
#import schedule
import time
#import datetime as dt

root = Tk()

win_icon = PhotoImage(file='D:\Codes\C Prog\Wizard\win_icon.png')
root.iconphoto(False, win_icon)

send_btn = PhotoImage(file='D:\Codes\C Prog\Wizard\send_button.png')
files_btn = PhotoImage(file='D:\Codes\C Prog\Wizard\\file.png')

root.maxsize(800, 600)
root.minsize(800, 600)

root.title('Python Mail Sender')

to = tkinter.StringVar()
cc = tkinter.StringVar()
bcc = tkinter.StringVar()
message = tkinter.StringVar()
sub = tkinter.StringVar()

EMAIL_ADDRESS = os.environ.get('acc')
EMAIL_PASSWORD =  os.environ.get('pass')

msg = EmailMessage()  # created an object of 'EmailMessage' class
#msg.set_content('Sending some images...')
mg = EmailMessage() # for automated

# attach files
files = []  # an empty list
#files = ['P:\Docs\VS code\Python\mini_project\\result.pdf']

def select_file():
    root.filename = filedialog.askopenfile(initialdir="/c", title="Select a file")
    files.append(str(root.filename.name))


def send():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        msg['Subject'] = sub.get()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to.get()
        if(cc.get()):
            msg['Cc'] = cc.get()
        if(bcc.get()):
            msg['Bcc'] = bcc.get()
        
        mssg = message.get()
        msg.set_content(mssg)

        for file in files:
            with open(file, 'rb') as f:  # 'rb' = read bytes
                file_data = f.read()  # getting access
                #file_type = imghdr.what(f.name)  # 'f.name' will give the excat file type in which it got into it. We can change it in any like '.png'
                file_name = f.name
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)  # for pdf : maintype = 'application', subtype = 'octet-stream' and for images : maintyp='image', subtype=f.name

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        smtp.quit()

    #
    time.sleep(10) # time selay for 60 seconds
    sbj = "Images you may like"
    msge = "Greetings Sir\n\nThis is an automated mail.\nYou bought some images from us, we do have some more images according to your interest which you can check out.\nHere are some of our top rated images you may like."
    img_files = ['D:\Codes\C Prog\Wizard\\1.jpg', 'D:\Codes\C Prog\Wizard\\2.jpg']

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        mg['Subject'] = sbj
        mg['From'] = EMAIL_ADDRESS
        mg['To'] = to.get()
        
        mg.set_content(msge)

        
        for file in img_files:
            with open(file, 'rb') as f:
                file_data = f.read()
                file_name = f.name
            mg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)  # for pdf : maintype = 'application', subtype = 'octet-stream' and for images : maintyp='image', subtype=f.name


        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(mg)
        smtp.quit()
    #


label_email = Label(root, text='To', font=('calibre', 13), pady=10, padx=40)
email_entry = Entry(root, textvariable=to, font=('calibre', 8, 'normal'), width=40, fg='grey')

label_message = Label(root, text='Type your message', font=('calibre', 13), pady=10)
message_entry = Entry(root, textvariable=message, font=('calibre', 8, 'normal'), width=40, fg='grey')

label_sub = Label(root, text='Subject', font=('calibre', 13), pady=10)
sub_entry = Entry(root, textvariable=sub, font=('calibre', 8, 'normal'), width=40, fg='grey')

label_cc = Label(root, text='Cc', font=('calibre', 13), pady=10)
cc_entry = Entry(root, textvariable=cc, font=('calibre', 8, 'normal'), width=40, fg='grey')

label_bcc = Label(root, text='Bcc', font=('calibre', 13), pady=10)
bcc_entry = Entry(root, textvariable=bcc, font=('calibre', 8, 'normal'), width=40, fg='grey')

btn = Button(root, image=send_btn, padx=15, command=send, relief=FLAT)

label_email.place(relx=0.25, rely=0.02)
email_entry.place(relx=0.4, rely=0.04)

label_sub.place(relx=0.25, rely=0.078)
sub_entry.place(relx=0.4, rely=0.1)


label_cc.place(relx=0.29, rely=0.14)
cc_entry.place(relx=0.4, rely=0.16)

label_bcc.place(relx=0.28, rely=0.195)
bcc_entry.place(relx=0.4, rely=0.218)

label_message.place(relx=0.5, rely=0.45, anchor=CENTER)
message_entry.place(relx=0.5, rely=0.52, anchor=CENTER, width=600, height=20)  # height=80

btn_files = Button(root, image=files_btn, pady=5, padx=40, command=select_file, relief=FLAT)
btn_files.place(relx=0.5, rely=0.35, anchor=CENTER)

# btn.grid(row=5)
btn.place(relx=0.5, rely=0.8, anchor=CENTER)



root.mainloop()

# to make it a '.exe' file
# 1) install pyinstaller 'pip install pyinstaller'
# 2) then type 'pyinstaller --onefile -w projectmini.py'
#    -w to disable the window when we open the .exe file
#    projectmini.py is the name of the file(code)