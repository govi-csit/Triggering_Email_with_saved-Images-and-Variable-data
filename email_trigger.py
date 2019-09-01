#import bunch of libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from jinja2 import Template

# create message object instance
msg = MIMEMultipart()
message = "Thank you"

# setup the parameters of the message
#From email address
msg['From'] = "xxxxx.csit@gmail.com"
#From email password
password = "xxxxx"
#To email address
msg['To'] = "xxxxxx@gmail.com"
#Email subject
msg['Subject'] = "Triggering Email with saved Images and Varialble data"


#fetch the images from current directory
from glob import glob
list_of_images = glob('*.JPG')

#variable data
name = "Govinda"

#building email body template
main = Template('''
    <html><body><p>Adding varialbe data - <font color="red">Name : </font>{{name}}</p><br>
    </p>Adding Images : </p><br>
    {% for image in pictures %}<img src="cid:{{image}}">&nbsp;{% endfor %}
    <br></p>This is a sample email</p></body></html>''')
html = main.render(name = name, pictures=list_of_images)
msgHtml = MIMEText(html, 'html')
msg.attach(msgHtml)

#attaching images
for filename in list_of_images:
    fp = open(filename, 'rb')
    msg_img = MIMEImage(fp.read())
    fp.close()
    msg_img.add_header('Content-ID', '<{}>'.format(filename))
    msg_img.add_header('Content-Disposition', 'inline', filename=filename)
    msg.attach(msg_img)

#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
# Login Credentials for sending the mail
server.login(msg['From'], password)
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print ("successfully sent email to %s:" % (msg['To']))

    