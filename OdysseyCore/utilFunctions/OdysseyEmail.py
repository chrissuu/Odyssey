import smtplib
import email


# The email endpoint may now be useless due to gmail's software
class OdysseyEmail:
    def __init__(self, strEMAIL, strPASSWORD):
        self.EMAIL = strEMAIL
        self.PASSWORD = strPASSWORD

    def send_email(self, receiver_address, cc_address, bcc_address, subject, message):
        try:
            emails = email.message.EmailMessage()
            emails['To'] = receiver_address
            emails["Subject"] = subject
            emails['From'] = self.EMAIL
            if len(cc_address) > 0:
                emails['Cc'] = cc_address
            if len(bcc_address) > 0:
                emails['Bcc'] = bcc_address

            emails.set_content(message)
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            s.login(self.EMAIL, self.PASSWORD)
            s.send_message(emails)
            s.close()
            return True
        except Exception as e:
            print(e)
            return False


OdysseyEmail = OdysseyEmail('aodysseya@gmail.com','Chrissunjinsu0153!@#$%^&*()')
OdysseyEmail.send_email('chrisssu19@gmail.com',"","","test","test")
