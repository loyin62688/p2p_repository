from django.core.management.base import BaseCommand, CommandError
from django.db import models
from P2PADM.apps.P2Padmin.models import *
#from placeholders import *
import os
import requests
import StringIO
import re
import datetime
    
class Command(BaseCommand):
    def getP2pSerAddr():
        pass        
    def getRelaySerAddr():
        pass
    def getP2PSerInfo(self):
        p_devnum = re.compile(r'Devices num = \d{1,}$')
        p_p2pcount = re.compile(r'P2P count = -*\d{1,}$')
        p_num = re.compile(r'\d{1,}$')
        r = requests.get("http://www.easy4ipcloud.com:8801/")
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

    def getP2PRelayInfo(self):
        p_relaycount = re.compile(r'Bind count = \d{1,}$')
        p_agentsnum = re.compile(r'Agents num = \d{1,}$')
        p_num = re.compile(r'\d{1,}$')
        r = requests.get("http://www.easy4ipcloud.com:8901/")
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
    
    def handle(self, *args, **options):
        m_p2pdevnum,m_p2pcounts = self.getP2PSerInfo()
        m_relaycounts,m_relaydevnum = self.getP2PRelayInfo()
        p2pInfo_mod = P2PServerInfo(project = 'easy4ip', col_date = datetime.datetime.now()-datetime.timedelta(days=7-i), p2p_onlinenum = m_p2pdevnum, rel_onlinenum = m_relaydevnum, relay_accnum = m_relaycounts, p2p_accnum = m_p2pcounts)
        p2pInfo_mod.save()
