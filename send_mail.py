from mailerpy import Mailer
import os

PASSWORD = os.environ.get("EMAIL_PASSWORD")

my_mailer = Mailer("smtp.gmail.com", 587, "rabindrasapkota2@gmail.com", PASSWORD)


student_info = {
    "1": {"Name": "Bishal", "email": "bishal.freshway@gmail.com"}
  , "2": {"Name": "Rachita", "email": "rachyta2105@gmail.com"}
}

mail_content = """
Hello {name},

I am sending mail from Python

Thanks
"""
attachment_list = [os.path.join("C:\\Users\\rabin\\Desktop", "lab.csv")]

for roll_no, std in student_info.items():
    name = std["Name"]
    email = std["email"]
    my_mailer.send_mail([email], "From Python", mail_content.format(name=name), attachmets=attachment_list, mail_cc=[], mail_bcc=[])
