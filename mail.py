import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

email = config.email
password = config.password

def send_mail(text='Email Body', subject='Hello World',from_email='Rdxmax<email>', to_emails=None):
	assert isinstance(to_emails, list)
	msg = MIMEMultipart('alternative')
	msg['From'] = from_email
	msg['To'] = ", ".join(to_emails)
	msg["Subject"] = subject
	
	txt_part = MIMEText(text, 'plain')
	msg.attach(txt_part)

	# txt_part = MIMEText('<h1>This is a html message</h1>', 'html')
	# msg.attach(txt_part)

	msg_str = msg.as_string()
	# login
	server = smtplib.SMTP(host='smtp.gmail.com', port=587)
	server.ehlo()
	server.starttls()
	server.login(email, password)
	server.sendmail(from_email, to_emails, msg_str)

	server.quit()


receiver = list(map(str, input("Receivers: ").split(",")))
send_mail(to_emails=receiver)
