
"""
Created on Sun Apr 29 15:53:34 2018

@author: prerna.prakash
"""

import win32com.client as win32

def send_Mail(to:str,subject:str,attachment:str,html:str)->bool:
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    #tolist = ['prerna.prakash@accenture.com','kunal.mistry@accenture.com','punam.s.kumbhar@accenture.com']
    mail.To = to
    mail.Subject = subject
    #mail.Body = 'Hello Shashank. Java is lame'
    with open('C:\\Users\\prerna.prakash\\Flask\\templates\\hello.html', 'r') as myfile:
        data=myfile.read().replace('\n', '')
        mail.HTMLBody = data #this field is optional
    
    # To attach a file to the email (optional):
    #attachment  = "Path to the attachment"
    mail.Attachments.Add(attachment)
    
    mail.Send()
    print('your mail has been sent')




