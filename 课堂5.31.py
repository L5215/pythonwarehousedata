# from  datetime import datetime
# a=datetime.today()
# print(a)
# print(a.year)
# print(a.month)
# print(a.day)
import calendar
# from  datetime import date
# a=date.today()
# print(a)
# print(a.year)
# print(a.month)
# print(a.day)
# a=date(2017,3, 1)
# b=date(2017,3, 15)
# print(a.__eq__(b))
# print(a.__ge__(b))
# print(a.__gt__(b))
# print(a.__le__(b))
# print(a.__lt__(b))
# print(a.__ne__(b))
# print(a.__sub__(b))
# print(a.__rsub__(b))
# print(a.__format__('%Y-%m-%d'))
# print(a.__format__('%Y/%m/%d'))
# print(a.__format__('%y/%m/%d'))
# print(a.__format__('%D'))
# print(a.__format__('%d'))


# from datetime import *
# d=date(2012,12,12)
# print(d)
# #昨天
# d1=d+timedelta(days=-1)
# print(d1)
# #明天
# d2=d+timedelta(days=1)
# print(d2)
import time
# from datetime import *
# dt=datetime(2012,12,12,23,59,59)
# print(dt)

#昨天
# dt1=dt+timedelta(days=-1)
# print(dt1)
#明天
# dt2=dt+timedelta(days=1)
# print(dt2)
#上一个小时
# dt3=dt+timedelta(hours=-1)
# print(dt3)
#下一个小时
# dt4=dt+timedelta(hours=1)
# print(dt4)
#上一秒
# dt5=dt+timedelta(seconds=-1)
# print(dt5)
#下一秒
# dt6=dt+timedelta(seconds=1)

# a= time.time()
# for x in range(100000):
#     pass
# b=time.time()-a
# print(b)
# print(time.perf_counter())
# print(time.perf_counter())
# print(time.perf_counter())



# 如果没有给定时间戳，直接返回当前时间点的国际伦敦时间
# print(time.gmtime())
# 可以将时间戳转为本地时间
# print(time.localtime())
# a=time.time()
# 如果没有给定时间戳，直接返回当前时间点的本地时间jian
# time.localtime(a)
#
# print(time.time())
# print(time.ctime(time.time()))

# 将时间元组转化为format年月日格式
# a=time.strftime("%y-%m-%d %x",time.gtime())
# print(a)
# b=time.strftime("%y-%m-%d %x")
# print(b)
# # 返回当地的时间和日期
# c=time.strftime("%x %x")
# print(c)

month(theyear.themonth,w=0,l=0)
prmonth(thryear,themonth,w=0,l=0)
calendar.prmonth(2021,11)
thismonth = calendar.month(2021,11,0)
print(thismonth)

calendar.prmonth(2021,11,0)
calendar.prmonth(2021,11,1)
calendar.prmonth(2021,11,2)
calendar.prmonth(2021,11,3)
1.3setfirstweekday(firstweekday):
calendar.setfirstweekday(1)
calendar.prmonth(2021,11)
1.4isleap(year):
import calendar
print(calendar.isleap((2018)))