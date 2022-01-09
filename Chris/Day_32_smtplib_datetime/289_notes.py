import smtplib

# make a burner email account:
my_email = "mistwire.test01@gmail.com"
password = "xxxxxxxx"

# connect to email provider's server (use with to avoid open/close issue):
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
with smtplib.SMTP ("smtp.gmail.com", port=587) as connection:
    # start and secure connection to email server:
    connection.starttls()
    # login
    connection.login(user=my_email, password=password)
    # send!
    connection.sendmail(
        from_addr=my_email,
        to_addrs="lupusthemonk@yahoo.com",
        msg="Subject:Hello World2\n\nThis is the body of the email!")
# close connection (not needed if you use 'with' keyword):
# connection.close()

