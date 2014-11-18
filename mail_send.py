#!/usr/bin/env python
# coding:utf-8

import smtplib 
from email.MIMEMultipart import MIMEMultipart 
from email.MIMEBase import MIMEBase 
from email.MIMEText import MIMEText 
from email import Encoders 
import os

from setting import FROM_EMAIL, PASSWORD, TO_EMAIL

def mail(to, subject, text, attach): 
	gmail_user = FROM_EMAIL
	gmail_pwd = PASSWORD
	msg = MIMEMultipart()

	msg['From'] = gmail_user 
	msg['To'] = to 
	msg['Subject'] = subject

	msg.attach(MIMEText(text))

	if os.path.exists(attach): 
		part = MIMEBase('application', 'octet-stream') 
		part.set_payload(open(attach, 'rb').read()) 
 		Encoders.encode_base64(part) 
		part.add_header('Content-Disposition', 
			'attachment; filename="%s"' % os.path.basename(attach)) 
		msg.attach(part)

	mailServer = smtplib.SMTP('smtp.163.com') 
	mailServer.ehlo() 
	mailServer.starttls() 
	mailServer.ehlo() 
	mailServer.login(gmail_user, gmail_pwd) 
	mailServer.sendmail(gmail_user, to, msg.as_string()) 
	# Should be mailServer.quit(), but that crashes... 
	mailServer.close()

mail(TO_EMAIL, 
	"Hello XR", 
	"Hello XR , i'm guyou !",
	"",)
