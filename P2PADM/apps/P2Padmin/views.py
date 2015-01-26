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
                return render_to_response('monitor.html', RequestContext(request))  
            else:  
                return render_to_response('login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))  
        else:  
            return render_to_response('login.html', RequestContext(request, {'form': form,}))

#@csrf_protect
def index(request):
    form = LoginForm()
    return render_to_response('login.html',{'form':form})


#def getP2PInfo(request):
#    return render_to_response('monitor.html')
def p2pInfoMon(request):
    def getInfoByDay(m_date):
        ins_list = P2PServerInfo.objects.filter(project='easy4ip',col_date__range = (m_date - datetime.timedelta(days=2),m_date))
        if len(ins_list) == 3:
            m_p2p_onlinenum = int(ins_list[2].p2p_onlinenum) - int(ins_list[1].p2p_onlinenum)
            m_rel_onlinenum = int(ins_list[2].rel_onlinenum) - int(ins_list[1].rel_onlinenum)
            m_relay_accnum = int(ins_list[2].relay_accnum) - int(ins_list[1].relay_accnum)
            m_p2p_accnum = int(ins_list[2].p2p_accnum) - int(ins_list[1].p2p_accnum)
        else:
            m_p2p_onlinenum = int(ins_list[1].p2p_onlinenum) - int(ins_list[0].p2p_onlinenum)
            m_rel_onlinenum = int(ins_list[1].rel_onlinenum) - int(ins_list[0].rel_onlinenum)
            m_relay_accnum = int(ins_list[1].relay_accnum) - int(ins_list[0].relay_accnum)
            m_p2p_accnum = int(ins_list[1].p2p_accnum) - int(ins_list[0].p2p_accnum)
        return m_p2p_onlinenum,m_rel_onlinenum,m_relay_accnum,m_p2p_accnum
    m_Infosets = []
    m_p2p_onlinenum_list = []
    m_rel_onlinenum_list = []
    m_relay_accnum_list = []
    m_p2p_accnum_list = []
    for i in range(0,6):
        m_Infosets.append(getInfoByDay(datetime.datetime.today()))
    for i in range(0,6):
        m_p2p_onlinenum_list.append(m_Infosets[i][0])
        m_rel_onlinenum_list.append(m_Infosets[i][1])
        m_relay_accnum_list.append(m_Infosets[i][2])
        m_p2p_accnum_list.append(m_Infosets[i][3])
    return render_to_response('monitor.html',RequestContext(request,{'m_p2p_onlinenum_list':m_p2p_onlinenum_list,}))#'m_rel_onlinenum_list':m_rel_onlinenum_list,'m_relay_accnum_list':m_relay_accnum_list, 'm_p2p_accnum_list':m_p2p_accnum_list,}))


