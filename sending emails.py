# I did the knowledge assessment at the start, got every question right and it told me to start here
# But I would like to return later to check the parts about game development

import smtplib #simple mail transfer protocol --> knows how to handle email 
import datetime as dt
import random

# lower security boundaries on gmail
# settings > security > disable two steps identification > allow less secure apps

now = dt.datetime.now() # generates a string with current date and time
year = now.year
month = now.month
weekday = now.weekday()

date_of_birth = dt.datetime(year = 1997, month = 5, day = 27, hour = 20, minute = 33) # create my own datetime variable with my date of birth and now iI have attributes that I can access and comprare before sending email

myBirthday = str(date_of_birth.day) + "/" + str(date_of_birth.month)

if year > 2020:
    print("Is the pandemic over yet?")
    print(myBirthday)
    print(str(year) + "\n" + str(month) + "\n" + str(weekday))

quote_list = []

with open("quotes.txt") as q_file:
    q_list = q_file.readlines()
    quote = random.choice(q_list)
    print(quote)
    
my_email = "test@gmail.com"
with smtplib.SMTP("smtp.gmail.com") as connection: #smtp.live.com (for outlook) amd smtp.mail.yahoo.com (yahoo)

    my_msg = f"Subject:A good day\n\n{quote}"

    connection.starttls() #starts TLS - Transport Layer Security, to ensure the security of our email, encrypts messages

    connection.login("test@gmail.com", "my_password")
    connection.sendmail(
        from_addr = "test@gmail.com",
        to_addrs = "othertest@gmail.com",
        msg = my_msg
        )

# connection.close()  not needed because we are using 'with'
