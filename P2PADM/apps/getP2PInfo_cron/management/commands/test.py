
import requests
import StringIO
import re

def test(t_ip): 
    def getP2PRelayInfo(ip):
        p_relaycount = re.compile(r'Bind count = \d{1,}$')
        p_agentsnum = re.compile(r'Agents num = \d{1,}$')
        p_num = re.compile(r'\d{1,}$')
        print 'begin to get!!!!!!!!!!!!!!!!!!!!!!1'
        r=None
        while(r==None):
            try:
                r = requests.get("http://{0}:8901/".format(ip), timeout=5)
            except :
                print 'end to get!!!!!!!!!!!!!!!!!!!!!!!!!'
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
        f.close()
        return tmp_relaycounts,tmp_devnumOnline
    a,b = getP2PRelayInfo(t_ip)
    return a,b

if __name__ == '__main__':
    print test('54.186.94.170')
    
