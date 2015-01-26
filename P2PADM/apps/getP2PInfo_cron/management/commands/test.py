#!/usr/bin/env python
#coding=utf-8
import requests
import StringIO
import re


def getP2PSerInfo():
    p_devnum = re.compile(r'Devices num = \d{1,}$')
    p_p2pcount = re.compile(r'P2P count = -*\d{1,}$')
    p_num = re.compile(r'\d{1,}$')
    r = requests.get("http://121.199.3.195:8801")
    f = StringIO.StringIO(r.content)
    for i in f.readlines():
        m_devnum = p_devnum.search(i)
        m_p2pcount = p_p2pcount.search(i)
        if m_devnum:
            n_devnum = p_num.search(m_devnum.group())
            if n_devnum:
                tmp_devnum = n_devnum.group()
        if m_p2pcount:
            n_p2pcount = p_num.search(m_p2pcount.group())
            if n_p2pcount:
                tmp_p2pcount = n_p2pcount.group()
    return tmp_devnum,tmp_p2pcount

def getP2PRelayInfo():
    p_relaycount = re.compile(r'Bind count = \d{1,}$')
    p_agentsnum = re.compile(r'Agents num = \d{1,}$')
    p_num = re.compile(r'\d{1,}$')
    r = requests.get("http://121.40.175.128:8901")
    f = StringIO.StringIO(r.content)
    for i in f.readlines():
        m_relaycounts = p_relaycount.search(i)
        m_devnumOnline = p_agentsnum.search(i)
        if m_relaycounts:
            n_relaycounts = p_num.search(m_relaycounts.group())
            if n_relaycounts:
                tmp_relaycounts = n_relaycounts.group()
        if m_devnumOnline:
            n_devnumOnline = p_num.search(m_devnumOnline.group())
            if n_devnumOnline:
                tmp_devnumOnline = n_devnumOnline.group()
    return tmp_relaycounts,tmp_devnumOnline
    
if __name__ == '__main__':
    a,b = getP2PSerInfo()
    print a,b
    c,d = getP2PRelayInfo()
    print '===========' + '\n' + c,d
