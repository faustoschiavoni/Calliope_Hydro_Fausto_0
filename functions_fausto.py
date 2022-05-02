import datetime
import smtplib


def notify_via_email(mex):

    gmail_user = 'tesiFaustonotify@gmail.com'
    gmail_pwd = 'tesifausto'
    FROM = 'tesiFaustonotify@gmail.com'
    TO = 'fausto.schiavoni@mail.polimi.it'
    SUBJECT = 'Last Execution Tesi update(Calliope Hyrdo)'
    dataora = datetime.datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    TEXT = f'data: {dataora} \n\n{mex}'

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_pwd)
    server.sendmail(FROM, TO, message)
    server.close()
