from django.core.management.base import BaseCommand, CommandError
from django.db import models
from P2PADM.apps.P2Padmin.models import *
#from placeholders import *
import os
import requests
import StringIO
import re
import datetime

CONFIG_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
class Command(BaseCommand):
    def getP2pSerAddr():
        pass        
    def getRelaySerAddr():
        pass
    def getP2PSerInfo(self,ip):
        p_devnum = re.compile(r'Devices num = \d{1,}$')
        p_p2pcount = re.compile(r'P2P count = -*\d{1,}$')
        p_num = re.compile(r'\d{1,}$')
        r = requests.get("http://{0}:8801/".format(ip))
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

    def getP2PRelayInfo(self,ip):
        p_relaycount = re.compile(r'Bind count = \d{1,}$')
        p_agentsnum = re.compile(r'Agents num = \d{1,}$')
        p_num = re.compile(r'\d{1,}$')
        r = requests.get("http://{0}:8901/".format(ip))
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
        config_file = os.path.join(CONFIG_ROOT+'config.yaml')
        f = open(config_file)
        m_yaml = yaml.load(f)
        for m in m_yaml:
            for i in m_yaml[m]['p2pser_ip']:
                tmp_m_p2pdevnum,tmp_m_p2pcounts = self.getP2PSerInfo(i)
                m_p2pdevnum = m_p2pdevnum + tmp_m_p2pdevnum
                m_p2pcounts = m_p2pcounts + tmp_m_p2pcounts
                tmp_m_p2pdevnum=tmp_m_p2pcounts=0
            for i in m_yaml[m]['p2prel_ip']:
                m_relaycounts,m_relaydevnum = self.getP2PRelayInfo(i)
                m_relaycounts = m_relaycounts + tmp_m_relaycounts
                m_relaydevnum = m_relaydevnum + tmp_m_relaydevnum
                tmp_m_relaycounts=tmp_m_relaydevnum=0
            p2pInfo_mod = P2PServerInfo(project = m, col_date = datetime.datetime.now(), p2p_onlinenum = m_p2pdevnum, rel_onlinenum = m_relaydevnum, relay_accnum = m_relaycounts, p2p_accnum = m_p2pcounts)
                p2pInfo_mod.save()    
#        m_p2pdevnum,m_p2pcounts = self.getP2PSerInfo()
#        m_relaycounts,m_relaydevnum = self.getP2PRelayInfo()
#        p2pInfo_mod = P2PServerInfo(project = 'easy4ip', col_date = datetime.datetime.now(), p2p_onlinenum = m_p2pdevnum, rel_onlinenum = m_relaydevnum, relay_accnum = m_relaycounts, p2p_accnum = m_p2pcounts)
#        p2pInfo_mod.save()
