
import urllib2
import time
import datetime

try:
    t = float(open("2.txt").read())
except:
    t = 0
print t

output = datetime.datetime.now().strftime("%Y%m%d") + ".txt"
print output

print "------------------------"

open(output, "w").write("")
lines = open("1.txt").readlines()
for line in lines:
    line = line.strip()
    if not line:
        continue
    print line

    url = line
    if "http" not in url:
        url = "http://" + url

    flag = True
    try:
        p = urllib2.urlopen(url, timeout=5).read()
        if len(p) < 10:
            flag = False
    except:
        flag = False

    if flag:
        print "ok"
    else:
        print "null"
        open(output, "a").write(line + "\n")

    time.sleep(t)
