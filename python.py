import datetime

now = datetime.datetime.now()

print
print "Current date and time using str method of datetime object:"
print str(now)

print
print "Current date and time using instance attributes:"
print "Current year: %d" % now.year
print "Current month: %d" % now.month
print "Current day: %d" % now.day
print "Current hour: %d" % now.hour
print "Current minute: %d" % now.minute
print "Current second: %d" % now.second
print "Current microsecond: %d" % now.microsecond

print
print "Current date and time using strftime:"
print now.strftime("%Y-%m-%d %H:%M")

print
print "Current date and time using isoformat:"
print now.isoformat()


# Python Program - Get IP Address

import socket;
print("Want to get IP Address ? (y/n): ");
check = input();
if check == 'n':
    exit();
else:
    print("\nYour IP Address is: ",end="");
    print(socket.gethostbyname(socket.gethostname()));
