'''
#import module as a
#from module import add as a, sub as b
from module import *

print(add(10,2))
print(sub(10,2))
#print(a.mult(10,2))
#print(a.div(10,2))
'''

from datetime import datetime, timedelta, timezone, date
import time, math, random

'''
# time-zonme이 없다 > 그럼 뭘 기준으로 출력하는거지?
now = datetime.today()
print(now)
print(now.day)

# time-zone이 있음 > 한국 시간으로 맞춰져있다는 뜻?
now2 = datetime.now()
print(now2)
print(now2.day)

next_week = now + timedelta(days=1)
print(next_week)
'''
'''
print(timezone.utc)
print(datetime.now(timezone.utc))
'''
'''
open_day = date(year = 2024, month = 11, day = 18)
print(date.today())
print(date.today().weekday())
'''
'''
print(time.time())
print(time.localtime())
print("====================")
time.sleep(2)
print("====================")
print(time.time())
print(time.localtime())
'''
'''
print(math.pi)
print(math.sqrt(4))
print(math.factorial(4))
print(math.ceil(3.2))
print(math.floor(3.2))
print(round(2.6))
'''
'''
set = set()

while len(set) < 6 :
    set.add(random.randint(1,45))

l = sorted(set)
print(l)
'''
'''
import sys

#print(sys.argv)
#print(sys.argv[1:])

if "-h" in sys.argv or "--help" in sys.argv :
    print("사용법 : python main.py [옵션]")
    print("-h,--help        도움말 표시 ")
    print("-v, --version    버전정보표시")
    sys.exit(0)

if "-v" in sys.argv or "--version" in sys.argv :
    print("버전 : 1.0.0")
    sys.exit(0)
'''
'''
import os

dir_current = os.getcwd()
print(dir_current)
file_path = os.chdir(dir_current)
dir = os.popen("ls")
print(dir.read())
#os.rmdir("test")
print(os.environ.get("PATH"))
'''
import json

data = {
    "name" : "홍길동",
    "age" : 20,
    "city" : "서울"
}

json_str = json.dumps(data)
print(json_str)

json_obj = json.loads(json_str)
print(json_obj)