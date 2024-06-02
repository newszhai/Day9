from datetime import datetime,date
a =datetime.today()
print(a)
print(a.year)
print(a.month)
print(a.day)
a=date(2017,3,1)
b=date(2017,3,15)
print(a.__eq__(b))
print(a.__ge__(b))
print(a.__gt__(b))
print(a.__le__(b))
print(a.__lt__(b))
print(a.__ne__(b))


print(a.__sub__(b))
print(a.__rsub__(b))
print(a.__format__('%y-%m-%d'))
print(a.__format__('%y/%m/%d'))


from datetime import time
t =time(12,20,55,520)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
print((t.__format__('%H:%M:%S')))
print(t)

b=datetime.now()
print(b)
print(b.date())
print(b.time())

from datetime import timedelta
b1=b+timedelta(days=1)
print(b1)
b2=b+timedelta(days=-10)
print(b2)