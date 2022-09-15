# Go to your Google account and enable two-factor authentication
# Then set up an app specific password for Python, This password will be used by python for logging in to your email.

from email.message import EmailMessage
# from secret import password
import ssl
import smtplib
from getpass import getpass
# This package can be used to secure password, but it will only work in Terminal or Command line interface.


""" What is SSL library in Python?
SSL stands for Secure Sockets Layer and is designed to create secure connection between client and server. Secure 
means that connection is encrypted and therefore protected from eavesdropping. It also validate server identity"""

""" What is smtplib library in Python?
The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine 
with an SMTP or ESMTP listener daemon. """

""" What is a daemon?
In multitasking computer operating systems, a daemon is a computer program that runs as a background process, 
rather than being under the direct control of an interactive user.    
"""
# This is your mail id
sender_email = input("Enter your email id: ")
# App password set by you for python.
password = input("Enter your password: ")
# password = getpass()
# This function requires a proper terminal to turn off echoing of typed characters
# What is keyboard echo?
# the appearance of letters on the screen as someone types. While echoing what people
# type is the norm, in some situations it's not used
# GetPassWarning

# here you can input a single mail id or a list of mail ids separated by ,
receiver_email = input("Enter the email ids of the people you want to send this mail: ").split(",")
subject = input("Enter the subject of your email: ")

# Spanning strings over multiple lines can be done using triple quotes, It can also be used for long comments in code.
# What is EOF Error ?
# when reading a line. The acronym EOF stands for End Of File. This message literally means that the program called
# input() but failed to have any available input to read.

# To Trigger EOF error and save the email content enter Ctrl+Z in terminal and Ctrl+D in IDE.
print("Enter the content for your email. Press Ctrl+Z to save it.")
lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

body = '\n'.join(lines)

email = EmailMessage()
email['From'] = sender_email
email['To'] = receiver_email
email['subject'] = subject
# email['body'] = body
email.set_content(body)

""" create_default_context() . The default SSL context is good for a client connecting to a server. 
It does certificate verification, including hostname verification, and has officially reasonable defaults, 
some of which you can see in ctx. """

# SMTP_PORT = 25
# SMTP_SSL_PORT = 465
# If port is omitted, the standard SMTP-over-SSL port (465) is used, port specifies the port to which to connect.
# host = Name of the remote host to which to connect
# if no host specified then local host is used

# try passing a list in receiver_email
# as smtp refers to a server
"""What is a context?
ssl is built upon using certificates to encrypt and decrypt data between two machines. Those certificates are held 
in a temporary context, so the encryption and decryption can take place. No context = no ssl.
"""
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    try:
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, receiver_email, email.as_string())
    except smtplib.SMTPAuthenticationError:
        print("Login Credentials are incorrect please try again...")
    except smtplib.SMTPRecipientsRefused:
        print("Email Address for recipient is incorrect please try again...")
