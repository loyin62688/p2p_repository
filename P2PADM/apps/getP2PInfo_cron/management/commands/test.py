#!/usr/bin/env python
#coding=utf-8
import requests


def getInfo():
    r = requests.get("http://121.199.3.195:8801")
    print r.content
    
if __name__ == '__main__':
    getInfo()
