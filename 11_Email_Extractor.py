# Extract mail from string

#using reegular expressions

import re

email_str = '''Today rass12@gmail.in is the day when i think my babe is angry rass22@gmail.org with me and I think because rass33@yahoo.com i sleep early may rass44@yahoo.in be that's why she is upset rass55@rediffmail.com with. Till now she didn't reply to my messages rass66@gmail.com on whatsapp. I need to call rass77@ibm.com her to know about the rass88@sky.com condition or whats going on with. It is rass99@gmail.com the same thing that is happening of rass10@gmail.com something elese is happen rass11@gmail.com to her for not reply on whatsapp rass12@gmail.com'''

patt = re.compile(r'[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+[a-zA-Z]')
matches = patt.finditer(email_str)

for i in matches:
    print(i.group())

