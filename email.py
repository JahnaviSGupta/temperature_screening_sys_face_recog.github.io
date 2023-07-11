import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("raspberryodj@gmail.com" , "raspberryodj@1234")
server.sendmail("admin@gmail.com",
                "XYZ's Temperature too High")

server.quit()
