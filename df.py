# -*- coding: cp936 -*-

import urllib2
import time

try:
    t = float(raw_input("������ɨ����(��):"))
except:
    t = 0

raw_input("�뽫�������ַ�б����� 1.txt �ĵ���, Ȼ���»س�����ʼ..")

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

raw_input("���! �밴�»س����˳�...")
