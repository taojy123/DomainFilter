# -*- coding: cp936 -*-

import urllib2
import time

try:
    t = float(raw_input("请设置扫描间隔(秒):"))
except:
    t = 0

raw_input("请将输入的网址列表存放于 1.txt 文档中, 然后按下回车键开始..")

open("output.txt", "w").write("")
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
        open("output.txt", "a").write(line + "\n")

    time.sleep(t)

raw_input("完成! 请按下回车键退出...")
