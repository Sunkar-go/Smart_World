import smtplib
from email.message import EmailMessage
email=EmailMessage()
email['from'] = 'kuanyshev.s@kcn.kz'
email['to'] = 'sunkarsokol1995@gmail.com'
email['subject'] = 'Just test first mail message'

email.set_content('я надеюсь это сообщение дойдет до адресата.')

with smtplib.SMTP(host='smtp.mail.ru',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('kuanyshev.s@kcn.kz','6ZbH79B2w37m0zyJGEKV')
    smtp.send_message(email)