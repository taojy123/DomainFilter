
import urllib2
import time
import datetime

t = 0
timeout = 15
try:
    lines = open("2.txt").readlines()
    t = float(lines[0])
    timeout = float(lines[1])
except:
    pass
print t
print timeout

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
        p = urllib2.urlopen(url, timeout=timeout).read()
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

print "------------------------"
print "Finish!"
time.sleep(3)
