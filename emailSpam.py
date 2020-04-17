import os, smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# get number of emails to send and user details from file
def get_user(file):
    user = []
    with open(file, 'r') as f:
        next(f)
        n = f.readline()
        for l in f:
            user.append(l.rstrip('\n'))
    return n, user

# get list of emails to send to
def get_emails(file):
    emails = []
    with open(file, mode='r') as emails_file:
        for email in emails_file:
            emails.append(email.split()[0])
    return emails

# get message from file
def get_message(file):
    with open(file, 'r') as message_file:
        message_file_content = message_file.read()
    return message_file_content


def main():

    # set correct path of files
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

    n, user = get_user(os.path.join(THIS_FOLDER, 'your_details.txt')) # read user details from file
    emails = get_emails(os.path.join(THIS_FOLDER, 'email_list.txt')) # read emails from file
    msg = get_message(os.path.join(THIS_FOLDER, 'message.txt')) # read message from file

    # set up the SMTP server
    service = user[0].split("@", 1)[1].lower()
    
    if service == 'gmail.com':
        s = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    elif service == 'mail.ru':
        s = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    elif service == 'yahoo.com':
        s = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
    else:
        print('Unsupported email provider')
        quit()

    # login with provided user details
    s.login(user[0], user[1])

    # send the emails
    for i in range(len(emails)):
        for j in range(int(n)):
            s.sendmail(user[0], emails[i], msg)

    # close the connection
    s.quit()


if __name__ == '__main__':
    main()



