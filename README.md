# Triggering_Email_with_Python
Instructions:
1. Kkeep both input images(input_image1, input_image2) and python file(email_trigger.py) in same directory
2. add 'From Email' address in line no:14 and the corresponding passowrd in line no:16
3. add 'To Email address' in line no:18 
3. after running the code, will be expected to receive an email to 'sender email' which contains the same output as shown in ouput.JPG

Expected Issues
Gmail will not allow to login into gmail account via smtplib due to security purpose, so we will be expected to see the below error

raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepte
d. Learn more at\n5.7.8 http://support.google.com/mail/bin/answer.py?answer=1425
7\n5.7.8 {BADCREDENTIALS} s10sm9426107qam.7 - gsmtp')

To resolve this error, enable a flag : "Allow less secure apps: ON"  in security settings. Please refer https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp for further information.
    You migh see an error as shown below due to Gmail 
