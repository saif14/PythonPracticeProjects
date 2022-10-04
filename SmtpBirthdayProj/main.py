import smtplib

my_email = "parvezsaifmahmud@gmail.com"
password = ""

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="mahmud.saif@ymail.com", msg="Hola! Test Message!")
connection.close()