import os
from mailerpy import Mailer


student_info = [
    {"name": "sukreet", "email": "sukreet138@gmail.com", "course": "data science"},
    {"name": "dinesh", "email": "bajagaindinesh21@gmail.com", "course": "python"},
]


mail_content = """
Hello {name},

Welcome to class {course}. This is automated mail.

Thanks
"""

mail_passwod = os.environ.get("EMAIL_PASSWORD")
my_mailer = Mailer("smtp.gmail.com", 587, "rabindrasapkota2@gmail.com", mail_passwod)
attachment_list = ["", ""]

for student in student_info:
    mail_content_for_std = mail_content.format(name=student["name"], course=student["course"])
    print(f"Sending mail to {student.get("email")}")
    my_mailer.send_mail([student.get("email")], "From Python", mail_content_for_std)
