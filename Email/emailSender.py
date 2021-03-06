'''
Code for sending emails
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
Date: 21.03.2015
----------------------
Requirements : Postfix, Mail
Configure Deb Postfix https://rtcamp.com/tutorials/linux/ubuntu-postfix-gmail-smtp/
Configure RPM Postfix http://freelinuxtutorials.com/quick-tips-and-tricks/configure-postfix-to-use-gmail-in-rhelcentos/
Setup Email id http://www.cyberciti.biz/tips/linux-use-gmail-as-a-smarthost.html
Make the file executable
Cron Setup : http://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/
Sample Cron  : * * * * * /usr/bin/python /home/tusharmakkar08/Query_Optimizer/emailSender.py >/dev/null 2>&1
'''
#!/usr/bin/env python

import os

def readEmail(filename):
    '''
    filename : This file contains list of Email ID's (one per line)
    '''
    subject = "Welcome to ConCat !"
    with open ("/home/tusharmakkar08/Query_Optimizer/demoEmail.txt", "r") as myFile:
        text=myFile.readlines()
    #~ print text
    with open (filename, "r") as myFile:
        for line in myFile:
            #~ print "hi",line
            emailSend(line, subject, text)
    
def emailSend(emailId, subject, text):
    '''
    emailId : Email Id to which we want to send email
    subject : Subject of the email
    text : Content of email in a list
    
    Sends Email via mail command linux
    '''
    content = "".join(text)
    command = "echo "+ "\"" + content + "\"" + "|mail -s " + "\"" +  subject + "\"" + " " + emailId
    #~ print command
    return os.system(command)
    
    
if __name__ == '__main__':
    readEmail("/home/tusharmakkar08/Query_Optimizer/demoEmailId.txt")
