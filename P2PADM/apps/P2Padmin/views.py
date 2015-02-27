# Create your views here.

from django.shortcuts import render_to_response,render,get_object_or_404    
from django.http import HttpResponse, HttpResponseRedirect    
from django.contrib.auth.models import User    
from django.contrib import auth  
from django.contrib import messages  
from django.template.context import RequestContext
from django.forms.formsets import formset_factory  
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  
from django.contrib.auth.decorators import login_required 
from .forms import LoginForm
import datetime
#from django.db import models
from P2PADM.apps.P2Padmin.models import *
import csv

def requires_login(view):
    def new_view(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
        return view(request, *args, **kwargs)
    return new_view

#@csrf_protect 
def login(request):  
    if request.method == 'GET':  
        form = LoginForm()  
        return render_to_response('login.html', RequestContext(request, {'form': form,}))  
    else:  
        form = LoginForm(request.POST)  
        if form.is_valid():  
            username = request.POST.get('username', '')  
            password = request.POST.get('password', '')  
            user = auth.authenticate(username=username, password=password)  
            if user is not None and user.is_active:  
                auth.login(request, user)  
                print 'login sucess!!!!!!!!'
                return render_to_response('monitor.html', RequestContext(request))  
            else:  
                print 'login failed!!!!'
                return render_to_response('login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))  
        else:  
            return render_to_response('login.html', RequestContext(request, {'form': form,}))

#@csrf_protect
def index(request):
    form = LoginForm()
    return render_to_response('login.html',{'form':form})

def getInfoByDay(m_date,m_project):
    ins_list = P2PServerInfo.objects.filter(project=m_project,col_date__range = (m_date - datetime.timedelta(days=2),m_date))
    print 'len ins_list ======='
    print len(ins_list)
    if len(ins_list) == 3:
#            m_p2p_onlinenum = int(ins_list[2].p2p_onlinenum) - int(ins_list[1].p2p_onlinenum)
#            m_rel_onlinenum = int(ins_list[2].rel_onlinenum) - int(ins_list[1].rel_onlinenum)
        m_p2p_onlinenum = int(ins_list[2].p2p_onlinenum)
        m_rel_onlinenum = int(ins_list[2].rel_onlinenum)
        m_relay_accnum = int(ins_list[2].relay_accnum) - int(ins_list[1].relay_accnum)
        m_p2p_accnum = int(ins_list[2].p2p_accnum) - int(ins_list[1].p2p_accnum)
    elif len(ins_list) == 2:
#            m_p2p_onlinenum = int(ins_list[1].p2p_onlinenum) - int(ins_list[0].p2p_onlinenum)
#            m_rel_onlinenum = int(ins_list[1].rel_onlinenum) - int(ins_list[0].rel_onlinenum)
        m_p2p_onlinenum = int(ins_list[1].p2p_onlinenum)
        m_rel_onlinenum = int(ins_list[1].rel_onlinenum)
        m_relay_accnum = int(ins_list[1].relay_accnum) - int(ins_list[0].relay_accnum)
        m_p2p_accnum = int(ins_list[1].p2p_accnum) - int(ins_list[0].p2p_accnum)
    else:
        m_p2p_onlinenum=0
        m_rel_onlinenum=0
        m_relay_accnum=0
        m_p2p_accnum=0
    return [m_p2p_onlinenum,m_rel_onlinenum,m_relay_accnum,m_p2p_accnum]

#def getP2PInfo(request):
#    return render_to_response('monitor.html')
def p2pInfoMon(request,m_p2pwebsite):
    print 'm_p2pwebsite =' + m_p2pwebsite
    m_Infosets = []
    m_Infosets_ins = []
    m_p2p_onlinenum_list = []
    m_rel_onlinenum_list = []
    m_relay_accnum_list = []
    m_p2p_accnum_list = []
    def initSerInfoDir(i):
        x = {}
        x['m_p2p_onlinenum'] = i[0]
        x['m_rel_onlinenum'] = i[1]
        x['m_relay_accnum'] = i[2]
        x['m_p2p_accnum'] = i[3]
        return x
    for i in range(0,7):
        x =datetime.datetime.today()-datetime.timedelta(days=i)
        print 'x ======'
        print x
        m_Infosets.append(getInfoByDay(x,m_p2pwebsite))
        m_Infosets_ins.append(initSerInfoDir(getInfoByDay(x,m_p2pwebsite)))        
    for i in range(0,7):
        print 'B'
        m_p2p_onlinenum_list.append(m_Infosets[i][0])
        m_rel_onlinenum_list.append(m_Infosets[i][1])
        m_relay_accnum_list.append(m_Infosets[i][2])
        m_p2p_accnum_list.append(m_Infosets[i][3])
    return render_to_response('monitor.html',RequestContext(request,{'m_relay_accnum_list':m_relay_accnum_list,'m_p2p_accnum_list':m_p2p_accnum_list,'m_Infosets_ins':m_Infosets_ins,}))#'m_rel_onlinenum_list':m_rel_onlinenum_list,'m_relay_accnum_list':m_relay_accnum_list, 'm_p2p_accnum_list':m_p2p_accnum_list,}))


def downloadP2PCSV(request):
    # Create the HttpResponse object with the appropriate CSV header.
    p2pdate = ('6daysago','5daysago','4daysago','3daysago','2daysago','yestday','today')
    title = (' ','P2PONLINE_NUM','RELAYONLINE_NUM','RELAYACCUSS_NUM','P2PACCUESS_NUM')
    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=p2pInfo.csv'

    # Create the CSV writer using the HttpResponse as the "file."
    writer = csv.writer(response)
    writer.writerow(title)
    for i in range(0,7):
        print 'C'
        x = []
        x.append(p2pdate[i])
        x.extend(getInfoByDay(datetime.datetime.today()-datetime.timedelta(days=i)))
        writer.writerow(x)
    return response
