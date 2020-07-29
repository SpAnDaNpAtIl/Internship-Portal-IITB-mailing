import requests
import json
from bs4 import BeautifulSoup as bs
import smtplib
from email.message import EmailMessage
from data_for_instiapp import *
import datetime



blog = requests.get('https://www.insti.app/api/training-blog', headers = header)
today_info_with_time = str(datetime.datetime.now())


#print(blog.status_code)
if(str(blog.status_code)=='200'):
    raw_json_data = blog.json()
    
    def content_organise(content_to_be_organised):
        #creating a html script to beautify it
        html_full = '<!DOCTYPE HTML><html><head></head><body>'+ content_to_be_organised+'</body></html>'
        message_content = bs(html_full, features="lxml").get_text()
        return message_content
        
    
    def send_email(hexa, deca):
        #hexa is content of the mail and deca is title
        msg = EmailMessage()
        msg.set_content(content_organise(hexa))

        msg['Subject'] ='Internship Blog:'+deca
        msg['From'] = email_ID_used_for_sending_mails
        msg['To'] = email_ID_to_send
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_ID_used_for_sending_mails, password)
        server.send_message(msg)
        server.close()
        
    for eagt in raw_json_data:
        current_hour = int(today_info_with_time[11:13])
        eagt_date = eagt.get('published')[:10]
        eagt_hour_of_post = int(eagt.get('published')[11:13])
        if(eagt_date==today_info_with_time[:10]):
            if(current_hour==10 and eagt_hour_of_post<current_hour):
                send_email(eagt.get(content), eagt.get(title))
            elif(current_hour==14 and eagt_hour_of_post>=10 and eagt_hour_of_post<14):
                send_email(eagt.get(content), eagt.get(title))
            elif(current_hour==18 and eagt_hour_of_post>=14 and eagt_hour_of_post<18):
                send_email(eagt.get(content), eagt.get(title))
            elif(current_hour==23 and eagt_hour_of_post>=18):
                send_email(eagt.get(content), eagt.get(title))
            else:
                pass
        else:
            pass
    

    
else:
    print("Hey Maybe there is some problem in the headers which you have added in data_for_instiapp.py")