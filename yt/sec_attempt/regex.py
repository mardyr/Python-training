import  re

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[AEIOUM]+',x)
print(y)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)


data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

z = re.findall('\S+@\S+',data) # jeden lub wiecej znakow nie bedacych white-spacem i pozniej malpka i pozniej znowu jeden lub wiecej
print(z)

z = re.findall('^From (\S+@\S+)', data) # () operator wyluskania
print(z)

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
x = re.findall('^From .*@([^ ]*)',line)
print(x)